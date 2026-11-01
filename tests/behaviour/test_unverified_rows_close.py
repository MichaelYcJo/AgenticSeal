"""What is left of `unverified_check.py`'s old file.

#942's phase 5 rebuilt `skills/verify/scripts/unverified_check.py`'s cases
into `tests/skills/test_unverified_check.py`, one class per function. Two kinds of
case stay here, byte for byte. The cases whose assertion reads a shipped
document's prose wait for #923. `test_the_fence_walks_agree_shape_by_shape`
holds `hooks/lib/blocks.py` and `hooks/lib/config.py#fence_map` to this module's
fence walk, a check across files, which stays where it is. The case that read
`skills/code-review/scripts/chain_check.py` and
`skills/settle/scripts/settle.py` for a call of this module's `settled` judged
one file per row, so each row is now a case of its module's file,
`tests/skills/test_chain_check.py` and `tests/skills/test_settle.py`.
"""

import importlib.util
import os

import pytest
from conftest import ROOT, posix_id

SCRIPT = os.path.join(ROOT, "skills", "verify", "scripts", "unverified_check.py")


def load():
    spec = importlib.util.spec_from_file_location("unverified_check", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


uc = load()


# Spelt by code point, so it stays legible in the source and no emoji stands
# in it.
OLD_MARK = chr(0x2705)

# Every shipped text that tells a session how a `## Not verified` row closes.
CLOSING_TEXTS = [
    ("templates", "setup", "config.md"),
    ("docs", "the-record-layout.md"),
    ("skills", "implement", "SKILL.md"),
    ("skills", "verify", "SKILL.md"),
    ("skills", "settle", "SKILL.md"),
    ("skills", "settle", "scripts", "settle.py"),
    ("skills", "verify", "scripts", "unverified_check.py"),
]


@pytest.mark.parametrize("parts", CLOSING_TEXTS, ids=lambda p: "/".join(p))
def test_no_text_that_states_the_closing_shows_the_old_mark(parts):
    """A text that still shows the emoji sends whoever follows it to a row
    the check refuses. Protects: one of these quietly keeping the old mark
    when the others moved, which is how a rule stated in five places drifts;
    no other case reads them for it."""
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        assert OLD_MARK not in f.read()


def test_the_skill_shows_the_word(tmp_path):
    """`skills/implement/SKILL.md` *4. The closing memo — only what the diff
    cannot show* is what the memo's writer reads for how a row closes, so its
    example row is one the check accepts as closed."""
    with open(
        os.path.join(ROOT, "skills", "implement", "SKILL.md"), encoding="utf-8"
    ) as f:
        text = f.read()
    example = next(ln for ln in text.splitlines() if ln.startswith("| closed "))
    p = tmp_path / "gaps.md"
    p.write_text(
        f"# memo\n\n## Not verified\n\n| Item | Who must answer |\n|---|---|\n{example}\n",
        encoding="utf-8",
    )
    op, closed, err = uc.check_file(str(p))
    assert not err and not op and len(closed) == 1, (op, closed, err)


def collapsed(*parts):
    """File text with newlines flattened, so a match is not asserting where
    the author happened to wrap a line."""
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return " ".join(f.read().split())


def test_the_template_is_the_shape_the_checker_reads(tmp_path):
    """Template and checker drift apart silently otherwise: every new work
    item would copy a section the release check then refuses."""
    with open(
        os.path.join(ROOT, "templates", "records", "sdd-gaps.md"), encoding="utf-8"
    ) as f:
        template = f.read()

    d = tmp_path / "specs" / "1780000000-work"
    d.mkdir(parents=True)
    p = d / "gaps.md"

    p.write_text(template, encoding="utf-8")
    _, _, err = uc.check_file(str(p))
    assert err and "placeholder" in err[0][1], (
        "a template copied and never filled in has to fail, or an empty record "
        "passes as a complete one"
    )

    filled = template.replace("<what was not verified>", "the TUI rendering").replace(
        "<who or what can answer it>", "user, on the next session"
    )
    p.write_text(filled, encoding="utf-8")
    op, _, err = uc.check_file(str(p))
    assert not err and len(op) == 1


def test_the_memo_holds_what_went_out_unproved_and_what_was_not_taken():
    """#1148. The purpose restated the changelog fragment, the divergence
    table copied the phase records, and nothing wrote the fed-back clauses,
    so the memo is the two sections it is the home of, and the scope line on
    the ladder's second rung. How the skill says so is the proofer's to
    read."""
    with open(
        os.path.join(ROOT, "templates", "records", "sdd-gaps.md"), encoding="utf-8"
    ) as f:
        headings = [line for line in f.read().splitlines() if line.startswith("## ")]
    # The template's three headings: `## Not verified` is the one
    # `unverified_check.py` reads, and the crafter writes under all three.
    assert headings == ["## Scope confirmation", "## Not verified", "## Not done"], (
        headings
    )


def test_the_skill_names_the_command_that_lists_a_deleted_row():
    """The writer of a row is the one who has to know how it closes. Since
    #945 a deleted row is the proofer's to read in the overview's diff, and
    no check at the pull request refuses it; how the skill states the
    closing convention is the proofer's to read too."""
    skill = collapsed("skills", "implement", "SKILL.md")
    # The command `seal unverified --baseline`, which a person runs to name
    # each row that left without the word `closed`.
    assert "seal unverified --baseline" in skill


# The phrase each language's files use for the base's tip, where CI's
# comparison lands (#612).
TIP_EN = "the base's tip"
TIP_KO = "base 브랜치의 끝"


@pytest.mark.parametrize(
    "doc, tip, false_sentence",
    [
        ("README.md", TIP_EN, None),
        ("README.ko.md", TIP_KO, None),
        (os.path.join("skills", "verify", "SKILL.md"), TIP_EN, None),
        # The module's docstrings (#612). The phrase stands here three times,
        # so this row cannot see the `--baseline` help alone go back to the
        # fork point; `tests/skills/test_unverified_check.py::Test_main::
        # test_accepts_the_baseline_help_naming_both_places` renders it.
        (
            os.path.join("skills", "verify", "scripts", "unverified_check.py"),
            TIP_EN,
            None,
        ),
    ],
    ids=posix_id,
)
def test_the_documents_state_the_merge_base_footing(doc, tip, false_sentence):
    """Eight files told a reader that `--baseline` compares against the base
    revision; #272 made it compare against `git merge-base REF HEAD`. A
    corrected behaviour whose old sentence survives somewhere else is #180's
    class, and these files are where this one could survive.

    That commit is the fork point on a branch checkout -- a local run, the
    broad gate's -- and the base's tip in CI, whose checkout of a pull request
    is the head already merged into the base. The files said only the first
    and placed it in CI (#612), and two of them said CI never compares at the
    tip, which is false. So each file that places the comparison names the
    base's tip too, in one phrase per language, and the false sentence is
    asserted gone where it stood.

    Positive assertions: the sentence has to be there, rather than one old
    wording having to be absent, because the old wording had several
    phrasings. Nothing else in these files had reason to name a merge base."""
    text = open(os.path.join(ROOT, doc), encoding="utf-8").read()
    assert "merge-base" in text or "merge base" in text, (
        f"{doc} describes `seal unverified --baseline` and does not say the "
        "comparison is against the merge base"
    )
    flat_text = " ".join(text.replace("#", " ").split())
    if tip:
        assert tip in flat_text, (
            f"{doc} does not say that in CI the merge base is the base's tip"
        )
    if false_sentence:
        assert false_sentence not in flat_text, (
            f"{doc} still says CI never compares at the base's tip"
        )


FENCE_SHAPES = [
    ["```", "x", "```"],
    ["~~~", "x", "~~~"],
    ["   ```", "x", "   ```"],
    ["    ```", "x", "    ```"],
    ["```", "x", "    ```", "y", "```"],
    ["```python", "x", "```"],
    ["```", "x", "```python", "y", "```"],
    ["```", "x", "```   ", "y"],
    ["````", "```", "x", "````"],
    ["```", "x", "``````", "y"],
    ["```", "x", "~~~", "y", "```"],
    ["~~~", "```", "x", "~~~"],
    ["```x`", "y", "```"],
    ["``` `x`", "y"],
    ["~~~ `x`", "y", "~~~", "z"],
    ["``", "x", "``"],
    ["```", "x", "y"],
    ["a", "```\r", "x\r", "```\r", "b\r"],
    ["| a |", "```", "| b |", "```", "| c |"],
]


@pytest.mark.parametrize("lines", FENCE_SHAPES, ids=range(len(FENCE_SHAPES)))
def test_the_fence_walks_agree_shape_by_shape(lines):
    """The delimiter rule is written once, in `hooks/lib/blocks.py`, and three
    walks still apply it, each with its own state: `uc.fence_spans`,
    `blocks.fence_only`, and the walk behind `hooks/lib/config.py#fence_map`.
    They agree on which lines are fenced and on where a block that never
    closes opened."""
    from conftest import load_hook_module

    spec = importlib.util.spec_from_file_location(
        "agentic_config_for_fence_walks",
        os.path.join(ROOT, "hooks", "lib", "config.py"),
    )
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    blocks = load_hook_module("lib/blocks.py", "agentic_blocks_for_fence_walks")
    fenced = set()
    for first, last in uc.fence_spans(lines):
        fenced.update(range(first, len(lines) if last is None else last + 1))
    unclosed = [first for first, last in uc.fence_spans(lines) if last is None]
    shown, opened_at = config.fence_map(lines)
    assert fenced == set(range(len(lines))) - {n for n, _ in shown}
    assert unclosed == ([] if opened_at is None else [opened_at])
    assert blocks.fence_only(lines) == (fenced, opened_at)
    walked = blocks.walk(lines)
    claimed = {n for n in range(len(lines)) if not walked.uncertain[n]}
    assert set(walked.hidden()) & claimed == fenced & claimed
