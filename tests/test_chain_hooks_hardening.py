"""Hardening cases: prose-mention false positives, cycle edges, lease isolation.

The commit gate's cases, the parity arm's among them, are in
`tests/test_commit_review_gate.py`'s `Test_main` (#942's phase 6), and the
parity arm's case of `hooks/commitgate.py#pre_commit` is in
`tests/test_commitgate.py`. The backstop's case below waits for
`hooks/gate.py`'s group.
"""

import json
import os
import re
import subprocess
import sys

import pytest
from conftest import a_git_whose_diff_fails, stage


def git(repo, *a):
    return subprocess.run(
        ["git", "-C", str(repo), *a],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )


# --- packaging sanity ------------------------------------------------------

ROOT = os.path.join(os.path.dirname(__file__), "..")


def _hook_commands():
    with open(os.path.join(ROOT, "hooks", "hooks.json"), encoding="utf-8") as f:
        cfg = json.load(f)
    return [
        h["command"]
        for groups in cfg["hooks"].values()
        for group in groups
        for h in group["hooks"]
    ]


def test_hooks_json_points_at_existing_python_scripts():
    # Every hook runs through an explicit interpreter -- shebang and exec bit
    # do not exist on Windows -- and every script it names must be in the
    # plugin, on either side of the fallback.
    for cmd in _hook_commands():
        for alt in cmd.split(" || "):
            rel = alt.split('"')[1].replace("${CLAUDE_PLUGIN_ROOT}/", "")
            assert rel.endswith(".py"), f"non-python hook: {rel}"
            assert os.path.isfile(os.path.join(ROOT, rel)), rel


def test_every_hook_names_a_windows_interpreter_after_the_posix_one():
    # `python3` is the documented requirement and stays first, so a POSIX
    # machine never pays for a second attempt. It is also the one name the
    # official Windows installer does not create -- that installer ships the
    # `py` launcher instead -- so a command knowing only `python3` leaves
    # every gate silent there, which is the failure direction that allows.
    #
    # The fallback runs only when the first alternative could not start:
    # dispatch exits 0 for every decision it makes, deny included, so `||`
    # is never a second run of a gate that already decided.
    for cmd in _hook_commands():
        alts = cmd.split(" || ")
        assert len(alts) == 2, f"expected exactly one fallback: {cmd}"
        assert alts[0].startswith('python3 "${CLAUDE_PLUGIN_ROOT}/'), cmd
        assert alts[1].startswith('py -3 "${CLAUDE_PLUGIN_ROOT}/'), cmd


def test_the_fallback_runs_the_same_script_with_the_same_arguments():
    # A fallback naming another group is worse than no fallback: the gates
    # that fired would be the wrong ones, and only on the platform nobody
    # runs by hand.
    for cmd in _hook_commands():
        first, second = cmd.split(" || ")
        assert first.split('"')[1:] == second.split('"')[1:], cmd


def test_plugin_version_is_in_changelog():
    # The changelog starts at the first public release, so commits before it
    # legitimately have no file — the claim under test is "if a changelog
    # exists, it must mention the version being shipped".
    changelog = os.path.join(ROOT, "CHANGELOG.md")
    if not os.path.isfile(changelog):
        pytest.skip("no CHANGELOG.md in this tree")
    with open(
        os.path.join(ROOT, ".claude-plugin", "plugin.json"), encoding="utf-8"
    ) as f:
        version = json.load(f)["version"]
    with open(changelog, encoding="utf-8") as f:
        assert version in f.read(), f"CHANGELOG missing {version}"


def test_bin_wrapper_resolves_the_checker_from_any_cwd():
    # bin/ lands on the Bash tool's PATH while the plugin is enabled, so the
    # wrapper must resolve the script relative to itself, never the caller's
    # working directory. Windows can't run a POSIX shebang script directly,
    # so a .cmd sibling ships alongside it -- PATHEXT resolves a bare
    # `fold-check` to whichever one the platform can execute.
    posix_wrapper = os.path.join(ROOT, "bin", "fold-check")
    windows_wrapper = os.path.join(ROOT, "bin", "fold-check.cmd")
    assert os.path.isfile(posix_wrapper), "bin/fold-check missing"
    assert os.path.isfile(windows_wrapper), "bin/fold-check.cmd missing"
    assert os.access(posix_wrapper, os.X_OK), "bin/fold-check not executable"
    target = os.path.join(ROOT, "skills", "settle", "scripts", "fold_check.py")
    assert os.path.isfile(target), "wrapper points at a missing script"
    wrapper = windows_wrapper if sys.platform == "win32" else posix_wrapper
    r = subprocess.run(
        [wrapper, "--help"],
        cwd="/",
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    assert r.returncode == 0, r.stderr
    assert "usage: fold-check" in r.stdout


def test_migrated_commands_stay_user_invoked():
    # These three shipped as commands/ (user-invoked). Moving them to skills/
    # must not silently turn them into auto-triggering skills.
    for name in ("preset-setup", "security-audit", "testing"):
        p = os.path.join(ROOT, "skills", name, "SKILL.md")
        assert os.path.isfile(p), f"{name} not migrated"
        head = open(p, encoding="utf-8").read().split("\n---\n", 1)[0]
        assert "disable-model-invocation: true" in head, name
    assert not os.path.isdir(os.path.join(ROOT, "commands")), (
        "commands/ should be gone — skills/ is the documented layout"
    )


def test_parity_declaration_is_bootstrappable_not_hand_written():
    # The migration config is the one declaration a user cannot derive, so the
    # blank-page problem is real: without a template and a place that asks,
    # migration mode is a feature nobody can reach.
    tpl = os.path.join(ROOT, "templates", "parity.md")
    assert os.path.isfile(tpl), "templates/parity.md missing"
    body = open(tpl, encoding="utf-8").read()
    for field in (
        "Original repo",
        "Baseline commit",
        "Policy root",
        "Coordinate-trust exceptions",
    ):
        assert field in body, f"template lost the {field!r} field"
    assert "parity-paths.md" in body, "template must say where the local path goes"

    # The bootstrap and the parity setup are the orchestrator's half of the
    # skill since #292, so the file that has to point at the template is
    # `orchestration.md`, not the `SKILL.md` every smith spawn opens.
    implement = open(
        os.path.join(ROOT, "skills", "implement", "orchestration.md"),
        encoding="utf-8",
    ).read()
    assert "templates/parity.md" in implement, "bootstrap never points at the template"
    assert "seal/README.md" in implement

    setup = os.path.join(ROOT, "skills", "parity-setup", "SKILL.md")
    assert os.path.isfile(setup), "no command for declaring parity later"
    head = open(setup, encoding="utf-8").read().split("\n---\n", 1)[0]
    assert "disable-model-invocation: true" in head, (
        "parity-setup writes a declaration; it must not fire on its own"
    )


def test_the_backstop_hands_the_parity_arm_none_where_git_could_not_list(
    repo, tmp_path, monkeypatch
):
    """S10 of work item 1791384157 (#868), the backstop's path reader:
    `reference-transaction` lists what a commit past `--no-verify` carries
    with `git diff` over its base, and a failure there is None, which
    `gate.touches_code` answers True. A break reading the failure as an empty
    list survived every case until this one."""
    if os.name == "nt":
        pytest.skip("the shim is a POSIX shell script")
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "hooks"))
    import commitgate
    import gate

    head = git(repo, "rev-parse", "HEAD").stdout.strip()
    stage(repo, "service.py")
    git(
        repo,
        "-c",
        "user.email=e@example.com",
        "-c",
        "user.name=e",
        "commit",
        "-qm",
        "c",
    )
    new = git(repo, "rev-parse", "HEAD").stdout.strip()
    assert commitgate._paths_between(str(repo), head, new)() == ["service.py"]
    monkeypatch.setenv("PATH", a_git_whose_diff_fails(tmp_path))
    listed = commitgate._paths_between(str(repo), head, new)()
    assert listed is None, listed
    assert gate.touches_code(listed)


def _folded(name):
    with open(os.path.join(ROOT, "docs", name), encoding="utf-8") as f:
        return " ".join(f.read().split())


def test_the_policy_says_one_reader_reads_a_token_and_a_failed_diff_asks():
    """Contract rule 14, for S7, S8 and S10 of work item 1791384157
    (#868): the consent-read paragraph of `docs/commit-review-gate-spec.md`
    says a command that does not split carries no token from where its split
    fails, `docs/the-commit-gate-inside-git.md` names the one reader, and
    *Parity arm* says a diff git could not take is asked about. Red against
    `5623d728`'s texts."""
    for name, sentence in (
        (
            "commit-review-gate-spec.md",
            "A command that does not split carries no token from where its split fails",
        ),
        (
            "the-commit-gate-inside-git.md",
            "through `hooks/tokens.py#given`, the one reader of a consent token",
        ),
        (
            "the-review-and-parity-arms.md",
            "A diff git could not take is not a change confined to the document roots",
        ),
    ):
        assert sentence in _folded(name), (name, sentence)


def test_the_review_arms_missing_path_line_is_written_where_it_is_met():
    """The case above and `tests/test_commit_review_gate.py`'s
    `test_the_review_arm_asks_on_a_document_only_commit` pin the code half;
    this pins the prose half.

    A reader who finds `touches_code` beside the review arm can take its
    absence for an oversight, as #518 did. The review arm's decision table and
    the wake/quiet table are where that reader looks, so each says the arm
    reads no paths, and the table says why beside the parity arm's row."""

    def flat(*parts):
        with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
            return re.sub(r"\s+", " ", f.read())

    spec = flat("docs", "the-review-and-parity-arms.md")
    review_arm = spec.split("### Review arm", 1)[1].split("####", 1)[0]
    assert (
        "| the change confined to `docs/`, `seal/` | no different from any "
        "other change — this arm reads no paths." in review_arm
    ), "the review arm's table lost its row for a docs-only change"
    assert "**Why this arm has no document-root line.**" in review_arm, (
        "the row points at a paragraph that is not there"
    )
    assert "it is never inferred from the paths it touches" in review_arm, (
        "the paragraph lost the rule it exists for: the lighter tier is a "
        "declaration made before the first edit, not a path line"
    )
    assert (
        "| a `routing.md` declaration names this branch, for either answer | "
        "silent" in review_arm
    ), "the review arm's table lost the declaration, one of its three quieters"

    wake = flat("skills", "implement", "orchestration.md")
    assert (
        "whatever the change touches; a commit confined to `docs/` and "
        "`seal/` wakes it too" in wake
    ), "the wake/quiet table no longer says the review arm reads no paths"


def test_user_invoked_skills_do_not_carry_trigger_scaffolding():
    """`Use when:` / `NOT for:` exist to route the model's own choice.

    A skill the model can never choose is picked by a person typing its name,
    and the routing paragraph does nothing there but take space."""
    import glob

    offenders = []
    for path in sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md"))):
        with open(path, encoding="utf-8") as f:
            head = f.read().split("\n---\n", 1)[0]
        if "disable-model-invocation: true" not in head:
            continue
        if "Use when:" in head or "NOT for:" in head:
            offenders.append(os.path.basename(os.path.dirname(path)))
    assert not offenders, (
        f"user-invoked skills carrying auto-trigger scaffolding: {offenders}"
    )


NUMBER_WORDS = {
    20: ("Twenty", "스무"),
    21: ("Twenty-one", "스물한"),
    22: ("Twenty-two", "스물두"),
    23: ("Twenty-three", "스물세"),
    24: ("Twenty-four", "스물네"),
}

# Where each edition states the count. Scoping to the row is not tidiness:
# `README.ko.md` says `스무 번` about something else entirely, and a
# whole-file search reads that as a stale skill count.
SKILL_ROW = {"README.md": "| Skills |", "README.ko.md": "| 스킬 |"}


def test_both_readmes_count_the_skills_that_are_actually_there():
    """The count is prose in two languages, and shipping a skill is a diff
    that never opens either file.

    Deriving it is the point. `CONTRIBUTING.md` requires the two editions to
    move together, so a check that read only the English one would license
    exactly half the drift.
    """
    import glob

    shipped = len(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md")))
    assert shipped in NUMBER_WORDS, (
        f"{shipped} skills ship and no spelling is recorded for that number "
        "-- add it to NUMBER_WORDS rather than loosening the check"
    )
    english, korean = NUMBER_WORDS[shipped]

    def says(text, word):
        # A bare `in` reads `Twenty` out of `Twenty-one`, which makes the
        # stale half fire on a correct document and the present half pass on
        # a wrong one. Both directions need the boundary.
        return re.search(re.escape(word) + r"(?![-\w])", text) is not None

    for edition, word in (("README.md", english), ("README.ko.md", korean)):
        with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
            rows = [ln for ln in f if ln.startswith(SKILL_ROW[edition])]
        assert len(rows) == 1, (
            f"{edition} has {len(rows)} rows starting `{SKILL_ROW[edition]}`; "
            "the check reads exactly one"
        )
        row = rows[0]
        assert says(row, word), (
            f"{edition}'s skills row does not say `{word}`, and {shipped} "
            f"skills ship: {row.strip()[:120]}"
        )
        for other, (wrong_en, wrong_ko) in NUMBER_WORDS.items():
            if other == shipped:
                continue
            stale = wrong_en if edition == "README.md" else wrong_ko
            assert not says(row, stale), (
                f"{edition}'s skills row still says `{stale}` while "
                f"{shipped} skills ship"
            )


def test_every_shipped_skill_is_named_in_both_readmes():
    """A count that matches while a name is missing is the quieter half.

    Round 1 found the first version of this useless in both directions. It
    searched the WHOLE file for a BARE name, so `audit` was satisfied by
    `/specseal:security-audit` in the cheat sheet and `verify` by two
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
                # Round 2: `\`code-review\` in text` was satisfied by the
                # hook table thirty rows below, so removing it from BOTH
                # editions' agents column stayed green -- which agent
                # preloads what is the whole content of that column.
                agent_rows = [ln for ln in text.splitlines() if ln.startswith("| **")]
                assert any(f"`{name}`" in ln for ln in agent_rows), (
                    f"{edition}'s agents table never names `{name}` as "
                    "preloaded by any agent"
                )
                continue
            if user_invoked:
                # A skill nobody can trigger is reachable only as a typed
                # command, so that is the form that has to be shown.
                assert f"/specseal:{name}" in text, (
                    f"{edition} never shows `{name}` in the form a person types"
                )
                continue
            rows = [ln for ln in text.splitlines() if ln.startswith(SKILL_ROW[edition])]
            assert f"`{name}`" in rows[0], (
                f"{edition}'s skills row does not list `{name}`, which no "
                "agent preloads and nobody can type"
            )


def test_the_readme_group_counts_are_derived_too():
    """22 = 1 + 15 + 6, and all four numbers were prose.

    Round 1: the total was pinned and the split was not, so a skill could
    move between groups, or the middle count could go stale against its own
    list, with nothing red. Each group has a machine-readable definition --
    preloaded by an agent, typed by a person, neither -- so each is spelled
    from that rather than from the sentence beside it."""
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

    # Round 2: the counts were derived correctly and then looked for
    # ANYWHERE in the one row that holds all three, so swapping the three
    # words between the groups stayed green -- `four more a session loads`
    # above a list of eleven. The word is anchored to its own group's
    # sentence, which also settles `열` being a prefix of `열한`.
    groups = {
        "preloaded": (len(preloaded), ("The %s the agents follow", "따르는 %s 개는")),
        "on demand": (len(on_demand), ("%s more a session loads", "%s 개는 작업이")),
        "user invoked": (len(user_invoked), ("%s you invoke by name", "나머지 %s은")),
    }
    spellings = {
        1: ("one", "한"),
        2: ("two", "두"),
        3: ("three", "세"),
        4: ("four", "네"),
        5: ("five", "다섯"),
        6: ("Six", "여섯"),
        7: ("Seven", "일곱"),
        10: ("Ten", "열"),
        11: ("Eleven", "열한"),
        12: ("Twelve", "열두"),
        13: ("Thirteen", "열세"),
        14: ("Fourteen", "열네"),
        15: ("Fifteen", "열다섯"),
    }
    for group, (count, phrases) in groups.items():
        assert count in spellings, (
            f"the `{group}` group holds {count} skills and no spelling is "
            "recorded -- add it rather than loosening the check"
        )
        english, korean = spellings[count]
        for edition, word, phrase in (
            ("README.md", english, phrases[0]),
            ("README.ko.md", korean, phrases[1]),
        ):
            with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
                rows = [ln for ln in f if ln.startswith(SKILL_ROW[edition])]
            assert phrase % word in rows[0], (
                f"{edition}'s skills row does not say `{phrase % word}`, and "
                f"the `{group}` group holds {count}"
            )
    assert sum(c for c, _ in groups.values()) == len(paths), (
        "the three groups do not partition the shipped skills"
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


# The stems that mark a person answering, and the window the sweep below
# reads them in. AT MODULE LEVEL so a case can assert what they do: the
# pattern IS the behaviour this repair changes, and a pattern nothing opens is
# the shape this whole release keeps finding
# (`seal/specs/1789455558-…/overview.md` — pin the thing the production path
# calls, never a copy beside it).
#
# Matched at a WORD BOUNDARY, and the first draft of this guard was not. A
# bare `"ask" in window` fires on `task`, so the probe that was supposed to
# show the contract's own wording passing — `open every coordinate a task
# names in one batch` — went red on the word `task`. That is the same defect
# as the one being guarded against, one layer down: a substring standing in
# for a word.
#
# #422, half one: that repair anchored the FRONT of each stem and left the
# back open, so a stem matched inside a longer word and the same defect stood
# one layer down again. Measured: contract rule 10's own wording — *open
# every coordinate a task names in one batch* — refused at exit 1 with
# `persona` one clause away, which `agents/smith.md` already writes. Both ends
# are anchored now, and the back anchor is what splits the stems into two
# groups.
#
# These carry their inflections, because an instruction is written in any of
# them: `asks`, `asked`, `asking`, `questions`, `answers`, `answered`.
ASKING_INFLECTED = ("question", "ask", "answer")
# These are anchored bare at both ends. The plural of each names a POPULATION
# rather than the party at the keyboard — `users` is whoever installs this
# plugin, `humans` is a category — where the singular is the party who
# answers, which is what this guard is looking for. `person's` still matches,
# because an apostrophe is a word boundary; `persona` does not, which is the
# half the issue measured.
#
# `user` stays, against the issue's own patch, which drops the stem to stop
# `users`. The back anchor added in the same breath already stops `users`, and
# dropping the stem would let *collect in one batch what the user answers*
# pass in silence — the user being precisely the party who answers
# (`questions.md` Q1, measured: no batch phrase in any definition is within
# the window of any occurrence of the word today, so keeping it refuses
# nothing that stands).
ASKING_BARE = ("person", "people", "human", "user")
ASKING = re.compile(
    r"\b(?:(?:{})(?:s|es|ed|ing|'s)?|(?:{}))\b".format(
        "|".join(ASKING_INFLECTED), "|".join(ASKING_BARE)
    ),
    re.IGNORECASE,
)
ASKING_WINDOW = 140

# #422, half two. The refusal became a claim in round 2 of #419; WHAT IT
# DECIDES ABOUT did not. The occurrence that opened a window was whatever
# contained the exact substring `in one batch`, so an instruction written any
# other way never reached the window that would have refused it. Three
# spellings were measured passing at exit 0:
#
#   *go in **one batch** before the first edit*  -- verbatim from the
#       sentence `CLAUDE.md`'s goal section carried until #730 left the rule
#       to `skills/implement/SKILL.md` *1. Read the spec before the code*;
#       the emphasis markers break the
#       literal;
#   *in a single batch* and *as a single batch* -- ordinary synonyms.
#
# So the preposition and the article are read as a small set, and emphasis
# comes out before the search. Widening the SET OF WORDS the window refuses is
# a different thing and is not done here: that direction makes a legitimate
# definition unwritable, which is round 2's finding pointing the other way.
BATCH_PHRASE = re.compile(r"\b(?:in|into|as) (?:one|a single|a) batch\b", re.IGNORECASE)
# All three markdown markers, which is what the normaliser of this same name
# in `skills/code-review/scripts/chain_check.py` already settled on. Round 1's 🟡 2: `*` alone left out the
# marker these files use MOST — code spans outnumber asterisks in four of the
# five definitions, `agents/warden.md` 250 to 159 and `agents/smith.md` 202 to
# 142 — so `` in `one batch` `` reached no window at all.
#
# The build kept `_` out on the grounds that stripping it mangles the window a
# person reads in the refusal, because every identifier these definitions name
# carries one. That cost is real and it is the ONLY cost: stripping `_` cannot
# change what is found, since no stem in `ASKING` and no word in
# `BATCH_PHRASE` carries one. A printed file name losing its underscores is
# worth less than a spelling the guard cannot see, which is the same trade
# `chain_check.py` makes under the same name — and two constants called
# `EMPHASIS` meaning two different things is what
# `tests/test_one_word_one_meaning.py` exists to stop.
EMPHASIS = re.compile(r"[*_`]+")


def batch_instructions(body):
    """Every batching instruction in BODY whose window names a person
    answering, as `(phrase, window, names)`.

    **The sweep below IS this function over `agents/*.md`, and the case beside
    it is this function over text the case writes.** Round 1's 🔴 1: nothing
    in the tree contains a batch phrase — measured, zero occurrences in all
    five definitions, before and after this branch — so the sweep's loop body
    never executed and the composition inside it was unreachable on anything
    committed. Five mutations of the finder, the emphasis strip, the window
    and the stem set each left the module at exit 0, 50 passed, while the two
    cases above went on pinning the constants.

    That is this work item's own subject one layer down, and the fifth
    instance of the class in this release: the cases pinned the pieces and the
    production path was a copy of them. `seal/specs/1789455558-…/overview.md`
    states the rule — pin the function the production path calls, never the
    helper beside it.
    """
    flat_body = EMPHASIS.sub("", " ".join(body.split()))
    for hit in BATCH_PHRASE.finditer(flat_body):
        at = hit.start()
        window = flat_body[max(0, at - ASKING_WINDOW) : at + ASKING_WINDOW]
        named = sorted({m.group(0).lower() for m in ASKING.finditer(window)})
        if named:
            yield hit.group(0), window, named


def test_the_sweep_refuses_a_planted_instruction_in_every_spelling():
    """The whole guard, run on text this case writes, because the corpus holds
    nothing for it to find.

    Red with the emphasis strip removed from `batch_instructions`, red with
    the finder back to the literal `in one batch`, red with the window at 5 or
    at 400, and red with the stems front-anchored only — the last on the
    negative at the end, which is the direction a wider stem set is wrong in.
    """
    for spelling in (
        "questions go in **one batch** before the first edit and the person "
        "answers them",
        "collect in a single batch everything a person has to answer",
        "collect as a single batch everything the user answers",
        "collect in one batch what a person answers",
        "collect into one batch what a person answers",
        "collect in `one batch` what a person answers",
        # Hard-wrapped prose, which is the shape of every file the sweep
        # reads: the phrase itself straddles a line break, and the whitespace
        # flattening inside `batch_instructions` is the only thing that finds
        # it. Round 2's 🟡 6 — no case wrote a newline at all, so dropping the
        # flattening left the module at exit 0, 51 passed while the guard went
        # silent on the commonest spelling a real definition can carry.
        "questions a person genuinely has to answer go in one\nbatch "
        "before the first edit",
    ):
        assert list(batch_instructions(spelling)), (
            f"the guard does not refuse {spelling!r}, so an instruction "
            "written that way reaches no window that would refuse it"
        )
    # The window bounds the distance. Prose that names a person two hundred
    # characters from a batch phrase is not this instruction.
    far = "collect them in one batch." + " filler" * 40 + " a person answers"
    assert not list(batch_instructions(far)), (
        "the window no longer bounds the distance, so ordinary prose far "
        "from a batch phrase is refused"
    )
    # contract rule 10's own legitimate wording, with the two words the
    # back anchor exists to stop one clause away.
    assert not list(
        batch_instructions(
            "open every coordinate a task names in one batch; the persona "
            "the smith writes for and the users who install this plugin are "
            "not parties to it"
        )
    ), "batching READS is refused, which is the false refusal round 2 bought off"


def test_the_asking_stems_are_anchored_at_both_ends():
    """#422 half one, pinned on the object the sweep below actually reads.

    The front anchor alone let a stem match inside a longer word, and the two
    words it reached are both ordinary in a definition: `persona`, which
    `agents/smith.md` writes, and `users`. Anchoring the back is not free —
    `\\bquestion\\b` would stop matching `questions` — so the stems are split,
    and this case is what says which group each is in.

    Red with the back anchor removed: `persona` and `users` start matching.
    Red with the inflection group removed: `questions` and `asked` stop.
    """
    for word in ("question", "questions", "ask", "asks", "asked", "asking"):
        assert ASKING.search(word), f"{word} no longer marks a person answering"
    for word in ("answer", "answers", "answered", "person", "person's"):
        assert ASKING.search(word), f"{word} no longer marks a person answering"
    for word in ("people", "human", "user", "user's"):
        assert ASKING.search(word), f"{word} no longer marks a person answering"
    # The back anchor, on the words the issue measured: a population, or a
    # word that merely contains a stem.
    for word in ("persona", "personas", "users", "humans", "humanity"):
        assert not ASKING.search(word), (
            f"{word} fires the guard, so a definition using an ordinary word "
            "has to be reworded for a question nobody is asking"
        )
    # WHAT THE BACK ANCHOR ALSO COST, pinned so the next reader meets it
    # rather than discovering it (round 1's 🟡 3). The agent nouns stopped
    # matching, and each of them NAMES the party this guard is looking for —
    # contract rule 4 writes `answerer` for exactly that party. This block
    # used to sit in the one above, whose message calls its words ordinary
    # *for a question nobody is asking*, which is false of these three.
    #
    # Widening the stem set is refused with grounds in
    # `seal/specs/1789540097-…/spec.md` *Out*, so this is residue and not a
    # defect. It is residue, not correctness.
    for word in ("asker", "answerer", "questioner"):
        assert not ASKING.search(word), (
            f"{word} is an agent noun the back anchor stops. If this line is "
            "ever reversed, it is a widening of what the guard refuses and "
            "needs the argument `spec.md` *Out* asks for"
        )
    # The front anchor, which round 2 of #419 bought and this must not undo.
    for word in ("task", "multitasking", "flask"):
        assert not ASKING.search(word), f"{word} is a substring, not the word"


def test_the_batch_phrase_is_found_by_its_claim_not_by_one_spelling():
    """#422 half two, pinned on the objects the sweep below actually reads.

    The refusal decided by the claim and the FINDER still decided by one exact
    substring, so an instruction written any other way never reached the
    window. All three spellings below were measured passing at exit 0 before
    this repair — the first is `CLAUDE.md:39` verbatim.

    This case holds the two PIECES and their reasons, and it is not the
    guard: `test_the_sweep_refuses_a_planted_instruction_in_every_spelling`
    holds the composition the sweep performs, which is what round 1's 🔴 1 was
    about. Both are kept, because a piece that goes red says which piece.

    Red with the emphasis strip removed: the first assertion fails.
    Red with the preposition or the article back to a literal: the synonyms
    stop being found.
    """
    for spelling in (
        "questions go in **one batch** before the first edit",
        "collect them in a single batch",
        "collect them as a single batch",
        "collect them in one batch",
        "collect them in a batch",
        "collect them as one batch",
        # Reached only after round 1's 🟡 2 widened the marker set and the
        # preposition set. Backticks are the marker these definitions use
        # most, and `into` was measured missed.
        "collect them in `one batch`",
        "collect them in _one batch_",
        "collect them into one batch",
    ):
        assert BATCH_PHRASE.search(EMPHASIS.sub("", spelling)), (
            f"an instruction written {spelling!r} never reaches the window "
            "that would refuse it, so the guard says nothing about it"
        )
    # Not every sentence with the word in it. The finder opens a window; the
    # window is what refuses. Widening the finder past the phrase would put
    # ordinary prose in front of the stem set for no gain.
    for innocent in (
        "batch independent reads and runs",
        "a batch of questions",
        "batching is what the contract asks for",
    ):
        assert not BATCH_PHRASE.search(innocent), (
            f"{innocent!r} is not a batching instruction and opens a window"
        )


def test_the_questions_are_collected_before_the_work_not_during_it():
    """A question's cost is when it arrives, not how hard it is.

    Asked before the first edit it costs a reply; asked at minute thirty it
    stops a session that may have nobody at the keyboard."""
    with open(
        os.path.join(ROOT, "skills", "implement", "SKILL.md"), encoding="utf-8"
    ) as f:
        implement = f.read()
    assert "in one batch" in implement, "implement lost the batching rule"
    assert "would not change what you build" in implement, (
        "without the assume-in-writing half, the batch becomes a list of "
        "everything and the work waits on all of it"
    )
    # The batch belongs to the SESSION that spawns the work, and that is a
    # property of the harness rather than a preference: no agent this plugin
    # spawns has `AskUserQuestion`, measured from two of them independently
    # (#419, round 1). It was pinned in `agents/smith.md` while the design
    # gate lived there, then briefly in `agents/framer.md` — and a definition
    # that carries the words of an act its agent has no tool for is an
    # instruction nothing can carry out. So the presence is asserted where the
    # tool is, and the absence over EVERY agent definition, by glob, so a
    # fourth one added tomorrow is checked on the day it lands.
    import glob

    with open(
        os.path.join(ROOT, "skills", "implement", "orchestration.md"),
        encoding="utf-8",
    ) as f:
        orchestration = f.read()
    # Since #911 question 1 goes in a call of its own and the boxes follow
    # only under `per axis`. The bare `in one call` this used to assert is
    # also satisfied by the routing.md-batching sentence, so it is pinned on
    # the sentence that carries the claim.
    assert "Question 1 goes in one call of its own" in " ".join(
        orchestration.split()
    ), (
        "the orchestrator's routing section no longer says question 1 is put "
        "in a call of its own before the first edit, with the boxes after it "
        "only under `per axis` (#911)"
    )
    # WHAT IS REFUSED IS A CLAIM, NOT A SPELLING, and the first version of
    # this assertion refused the spelling. It read `"in one batch" not in
    # body` over every definition — and contract rule 10, which every
    # agent receives at startup, gives that phrase a second and entirely
    # legitimate meaning: *Batch independent reads and runs*. A definition
    # writing `open every coordinate in one batch` would have been following
    # the contract and gone red under a message about a question nobody
    # asked. Round 2 found it; a check that refuses a phrase by spelling
    # rather than by what it claims is the shape this release keeps finding,
    # so it is repaired here rather than narrowed by one word.
    #
    # The claim is *this agent collects what a person must answer*. What marks
    # it is a question word beside the phrase, so the window around each
    # occurrence is what decides — flattened first, because these files wrap
    # prose at about 75 columns and a per-line test would miss every sentence
    # that spans two.
    #
    # WHAT IT STILL CANNOT TELL APART, written down rather than left to be
    # found: *you collect the batch* from *your caller collects the batch*.
    # The second is true and a definition may need to say it — `agents/
    # framer.md` does, in its rule that its caller *asks the routing batch*,
    # which stays clear of this. A definition that needs the other wording
    # will meet this assertion and should reword rather than widen it,
    # because one word is all that separates the true sentence from the
    # instruction.
    #
    # THE REST OF THE RESIDUE, for the same reason — these are what the window
    # cannot see, and each has a direction rather than a fix:
    #
    #   · It CROSSES HEADINGS. 140 characters over the flattened file is a
    #     span with no structural boundary in it, and #422 measured 42 % of
    #     `agents/framer.md` and 60 % of `agents/smith.md` as positions where
    #     a new occurrence would fire. Bounding it at a heading is a change
    #     with its own failure direction — an instruction whose sentence
    #     straddles a heading would pass — and it is ruled out with grounds in
    #     `seal/specs/1789540097-…/spec.md` *Out*.
    #   · It reads `*` and not `_`. See `EMPHASIS` above for why.
    #   · It refuses by the WORDS in the window, so a definition that names a
    #     person answering for some other reason within 140 characters of a
    #     legitimate batch phrase is refused and has to be reworded. That is
    #     the direction this guard is deliberately wrong in: a false refusal
    #     costs one sentence in a file somebody is already editing.
    #
    # The stems, the window, the phrase and the emphasis pattern are all
    # module-level, above, so `test_the_asking_stems_are_anchored_at_both_ends`
    # and `test_the_batch_phrase_is_found_by_its_claim_not_by_one_spelling`
    # read the same objects this sweep reads rather than copies of them.
    # ROUND 2's 🟡 7, in the part of it a fix pass may close. Extracting
    # `batch_instructions` held the composition and left the sweep's own read
    # and call unheld: with the function and the constants untouched, the read
    # could be truncated to ten bytes and the loop's iterable replaced by `()`
    # and the module stayed at exit 0, 51 passed — because `agents/*.md` holds
    # zero batch phrases, so nothing in the corpus ever reaches this walk. The
    # only guard over it was the glob assertion below, which pins how many
    # files were FOUND and nothing about what was done with them.
    #
    # So the walk reports what it read, and the report is asserted. `>= 3`
    # stays: it is about the glob, and these two are about the loop.
    #
    # WHAT THIS STILL CANNOT SEE, and it is an open item rather than residue:
    # the third mutation, `batch_instructions("")` — the function called on
    # something other than what was read. Catching that means observing the
    # call, which means a walk a case can drive with a file it plants; that is
    # mechanism a fix pass may not add on top of a unit an earlier fix pass
    # created, and a planted corpus is a change to what the suite guards that
    # `CONTRIBUTING.md` asks a separate argument for. It is in this work item's
    # `overview.md` *Not verified* with an answerer.
    definitions = sorted(glob.glob(os.path.join(ROOT, "agents", "*.md")))
    assert len(definitions) >= 3, f"agents/*.md matched {len(definitions)} files"
    read = []
    for path in definitions:
        with open(path, encoding="utf-8") as f:
            body = f.read()
        relative = os.path.relpath(path, ROOT)
        read.append((relative, len(body.encode("utf-8"))))
        for phrase, window, named in batch_instructions(body):
            raise AssertionError(
                f"{relative} tells an agent to collect {phrase} something a "
                f"person answers — the window names {named}. No agent this "
                "plugin spawns has `AskUserQuestion`, so collecting a batch "
                "of questions is an instruction nothing can carry out; the "
                "act belongs to the session that spawns the work. Batching "
                "READS is a different thing and is what contract rule 10 "
                f"asks for — that wording is not refused here.\n  …{window}…"
            )
    assert [name for name, _ in read] == [
        os.path.relpath(p, ROOT) for p in definitions
    ], f"the sweep did not walk every definition the glob found: {read}"
    # The file's OWN size, not a floor. A floor pins that the read was not
    # tiny, which is a different claim: #426 measured `f.read(2000)` green
    # while every one of the five definitions was truncated, because the
    # smallest -- `agents/scribe.md`, 3764 bytes -- is far above the floor.
    # A number below every real file's size is silent for every truncation
    # above it, and no bigger number closes that: it moves the silent range.
    # So the comparison has no number in it to be wrong. Byte length on both
    # sides, so it survives the emoji and em-dashes these files carry, and
    # nothing here asserts a size literal -- a case that reddens when somebody
    # rewords a definition is a case people delete.
    assert all(
        size == os.path.getsize(os.path.join(ROOT, name)) for name, size in read
    ), f"the sweep read a definition it did not read in full: {read}"


def test_the_cycle_is_bounded_and_ends_at_a_pull_request():
    """An unattended run needs a terminus, and two are wrong at that spot.

    Stopping at a report leaves finished work nobody will find; merging
    decides something the chain was never given."""
    with open(
        os.path.join(ROOT, "docs", "the-review-record.md"), encoding="utf-8"
    ) as f:
        record = " ".join(f.read().split())
    assert "three finding rounds by default" in record, "the review loop lost its bound"
    assert "follow-up.md" in record, "no home recorded for what is left"
    with open(os.path.join(ROOT, "agents", "smith.md"), encoding="utf-8") as f:
        smith = f.read()
    assert "The chain ends at a pull request, never a merge." in smith


# The two skills a definition calls rather than preloads. Neither is in any
# `skills:` list: a preloaded body is paid for on every spawn (#292), and a
# skill two frames in ten want is cheaper called than carried.
UTILITY_SKILLS = ("confidence-check", "feature-planner")


def definitions_naming(skill):
    """The `agents/*.md` files that name `skill`, read out of the glob.

    Which definition calls these is a fact about the tree, and a case that
    types the answer instead of reading it asserts an owner rather than
    checking one. That is what made the pair below go stale together when the
    gate moved: the name `smith` was in the case, so the tree could change
    under it and only the half that pinned a literal noticed.
    """
    import glob

    return [
        os.path.basename(path)
        for path in sorted(glob.glob(os.path.join(ROOT, "agents", "*.md")))
        if skill in open(path, encoding="utf-8").read()
    ]


def test_each_utility_skill_is_callable_from_exactly_one_definition():
    """S4 of #84. `confidence-check` and `feature-planner` were named in
    `agents/smith.md`'s design gate; 0.11.0 moves the judgment they serve to
    `agents/framer.md`, and a skill named in two definitions is two agents
    each believing the call is theirs.

    Counted from the glob rather than from a pair of filenames, so a sixth
    definition picking one of them up is red here on the day it lands."""
    for skill in UTILITY_SKILLS:
        homes = definitions_naming(skill)
        assert homes == ["framer.md"], (
            f"`{skill}` is named in {homes}. It belongs to exactly one "
            "definition -- the one whose phase decides what it answers -- and "
            "a second home is where the two agents start calling it over each "
            "other. If the home moved, `agents/framer.md`, the losing "
            "definition and the skill's own stand-down clause move together"
        )


def test_the_skills_stand_down_for_whichever_definition_calls_them():
    """Both skills used to fire on their own keywords while a design gate was
    deciding the same thing, so one request could open three scope
    conversations. The `NOT for` clause is what stopped that, and it names the
    agent it stands down for.

    This case used to read that name as the literal `smith`, which is why the
    clause and the gate could come apart: 0.11.0 moved the gate to the framer
    and the two SKILL.md files went on naming an agent that no longer calls
    them, with nothing red. The name is read out of the glob now, so the
    clause has to follow whichever definition actually holds the skill."""
    for skill in UTILITY_SKILLS:
        homes = definitions_naming(skill)
        assert len(homes) == 1, (
            f"`{skill}` is named in {homes}, so there is no single agent for "
            "its stand-down clause to name"
        )
        owner = os.path.splitext(homes[0])[0]
        head = (
            open(os.path.join(ROOT, "skills", skill, "SKILL.md"), encoding="utf-8")
            .read()
            .split("\n---\n", 1)[0]
        )
        assert f"{owner} is driving" in head, (
            f"`{skill}` stands down for somebody other than `{owner}`, which "
            f"is the definition that names it. The clause is what keeps it "
            "from firing on its own beside the phase that already calls it"
        )


def test_the_smith_says_whether_the_frame_holds_before_building_to_it():
    """S5 of #84. A `spec.md` and a `plan.md` are a drawing another party
    made, and a drawing can be wrong about the tree it describes. #107's
    phase 1 established that its own stated path could not work before a line
    was written; phase 1 of #84 did it again on a `skills:` list it was
    handed. Twice in two work items, unprompted, and written into no
    document -- which makes it a habit, and a habit is what the next spawn
    does not inherit.

    The home is pinned as well as the sentence, and it is the step after the
    requirements read. There the check runs on what was just read and a `no`
    costs the reading; after the build starts it arrives once the build has
    already been spent on a frame that does not hold.

    A `no` needs a destination or it becomes a second interruption. The one
    the sentence names is the phase record and the hand-back -- never a route
    back to the framer, which has no interactive phase to route back TO: the
    one moment of human contact belongs to the session that spawns the work,
    before the framer is spawned at all."""
    smith = " ".join(
        open(os.path.join(ROOT, "agents", "smith.md"), encoding="utf-8").read().split()
    )
    holds = "Say whether the frame holds before you build to it"
    assert holds in smith, (
        "`agents/smith.md` no longer tells the builder to judge the frame "
        "before building to it. It happened twice unprompted and was recorded "
        "nowhere, which is exactly what a written instruction is for"
    )
    # Since #967 the home is a step of `## Order of work`: after the step
    # that reads the work item, before the step that builds. Found by the
    # steps' own words rather than their numbers, so a step inserted above
    # them moves nothing here.
    read_at = smith.index("Read the work item:")
    build_at = smith.index("Build the phase as a vertical slice")
    assert read_at < smith.index(holds) < build_at, (
        "the drawing-holds check moved out from between the requirements read "
        "and the build. After the build starts, a frame that does not hold "
        "has already been spent on"
    )
    rule = smith[smith.index("**The frame is judged before it is built to.**") :]
    rule = rule[: rule.index(" check: ")]
    for named in ("phases/phase-N.md", "## What this phase found", "the hand-back"):
        assert named in rule, (
            f"the rule no longer names `{named}` as where a `no` goes. A "
            "`no` with no destination is a finding that reaches nobody"
        )
    assert "never back to the framer" in rule, (
        "the sentence stopped ruling out the route back to the framer, which "
        "is the second interruption that phase exists to spend once"
    )


def test_spec_directories_carry_the_timestamp_prefix():
    # implement/SKILL.md: "A work item's directory is
    # seal/specs/<unix-epoch-seconds>-<slug>/ ... keeps directories in
    # creation order and collision-free without a registry". Two were written
    # without
    # it and nothing noticed — the drift this plugin exists to catch, in its
    # own tree. The four that predate the convention were backfilled from the
    # commit that introduced each, so a plain listing now reads in order.
    import re

    specs = os.path.join(ROOT, "seal", "specs")
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
    `spec.md` or a `plan.md`, someone decided the work was worth describing,
    and the memo is the other half of that.
    """
    specs = os.path.join(ROOT, "seal", "specs")
    missing = []
    # Absent after a complete fold (#517), which is no directory missing a memo.
    for n in sorted(os.listdir(specs) if os.path.isdir(specs) else []):
        d = os.path.join(specs, n)
        if not os.path.isdir(d):
            continue
        on_the_ladder = any(
            os.path.isfile(os.path.join(d, f)) for f in ("spec.md", "plan.md")
        )
        if on_the_ladder and not os.path.isfile(os.path.join(d, "overview.md")):
            missing.append(n)
    assert not missing, f"work items with no closing overview: {missing}"


def test_installer_prints_commands_a_user_can_actually_type():
    # Plugin commands are namespaced. The installer printed /preset-setup,
    # which resolves to nothing — found by running the installer against a
    # real machine rather than by reading it.
    import re

    text = open(os.path.join(ROOT, "install.sh"), encoding="utf-8").read()
    bare = [
        m
        for m in re.findall(r"(?<!:)/([a-z][a-z-]+)\b", text)
        if m in {"preset-setup", "security-audit", "testing", "parity-setup"}
    ]
    assert not bare, f"un-namespaced plugin commands in install.sh: {bare}"
