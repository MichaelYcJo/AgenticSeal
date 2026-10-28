"""The gate and CI ran the same five checks over one branch and asked them
about different ranges (#423).

`broad_gate.py` built every child check's argument out of `--base` as the
caller typed it, so a plain branch name resolved to the LOCAL ref.
`.github/workflows/hygiene.yml` spells the same thing `origin/<base>`, which
is not a choice it made — a runner's checkout has no local branch, so that is
the only spelling that resolves there. On 2026-09-16 the local ref was one
commit behind its remote: the gate reported two survivors, all excused, exit 0
and drew the stamp, and CI reported seven places and exit 1 on the same
branch, the same check and the same commit.

What stays here are the cases that read a shipped document: the workflow's
spellings held against the gate's, and the documents that say which base the
gate asks about. #923 places them. The resolver, the line it prints and the
consumers it hands the commit to are `tests/skills/test_broad_gate.py` since #942.
"""

import ast
import os
import re

import pytest
from conftest import code_lines, load_module, read

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GATE = os.path.join(ROOT, "skills", "verify", "scripts", "broad_gate.py")
HYGIENE = os.path.join(ROOT, ".github", "workflows", "hygiene.yml")


def gate_module():
    return load_module(GATE, "agentic_broad_gate_for_range_tests")


# --- the two readers, held against each other --------------------------------
#
# The defect was not a bug inside either file. It was two files answering one
# question differently, each correct on its own, with nothing in the tree
# comparing them. `tests/test_the_lenient_run_says_what_the_broad_gate_will_
# say.py` was written for #354's identical shape — three readers grading one
# tree — and its structural half is the precedent this follows.

# Every place the workflow names a base, not only the ones spelled as a
# quoted argument at the start of a line. The value may be quoted or bare,
# and a bare one can carry a `${{ … }}` expression with spaces inside it, so
# the unquoted alternative treats such an expression as part of one token.
# An `env:` assignment counts: `.github/workflows/hygiene.yml` already names
# a base that way at its milestone step, and a `run:` block reading `$BASE`
# is as much a reader of the base as one spelling it on a command line.
BASE_ARGUMENT = re.compile(
    r"(?:--baseline|--range)\s+(?:\"([^\"]*)\"|((?:\$\{\{[^}]*\}\}|\S)+))"
)
BASE_ENVIRONMENT = re.compile(r"^\s*BASE:\s*(\S.*?)\s*$")
# A step that passes the base through a shell variable names the `env:`
# assignment, which this reader checks on its own — requiring the
# remote-tracking spelling here as well would turn the case red for a
# refactor that left the workflow correct.
SHELL_VARIABLE = re.compile(r'^"?\$\{?BASE\}?"?$')
REMOTE_TRACKING = "origin/${{ github.base_ref }}"


def base_spellings(text):
    """Every revision `text` names as a base, as it spells it.

    Takes text rather than reading the file, so the reader itself can be
    driven over shapes the workflow does not happen to use today — round 1's
    finding 4 was that a reader nothing drives is a reader nobody can tell is
    partial.

    **Code lines only** (#462), through `tests/conftest.py#code_lines`, so a
    flag in a whole-line or a trailing comment is not a base. **A `BASE:`
    counts only as a key of an `env:` mapping**: the nearest shallower code
    line above it is `env:`, so one under `with:` or inside a `run: |` block
    is not a base. **An empty quoted value is `""`, never `None`** (#463), so
    the spelling check fails on it by name the way it fails on every other
    malformed spelling, rather than raising `TypeError`.
    """
    found = []
    lines = code_lines(text)
    for n, line in enumerate(lines):
        for match in BASE_ARGUMENT.finditer(line):
            quoted, bare = match.group(1), match.group(2)
            found.append(quoted if quoted is not None else bare)
        environment = BASE_ENVIRONMENT.match(line)
        if environment and keyed_under_env(lines, n):
            found.append(environment.group(1))
    return found


def keyed_under_env(lines, n):
    """Whether the nearest code line above `lines[n]` that is shallower than
    it is `env:`, which makes `lines[n]` a key of that mapping."""
    depth = len(lines[n]) - len(lines[n].lstrip())
    for above in reversed(lines[:n]):
        if above.strip() and len(above) - len(above.lstrip()) < depth:
            return above.strip() == "env:"
    return False


def assert_every_base_is_remote_tracking(spellings):
    """The check the workflow's spellings are held to, over a list, so it can
    be driven with a malformed one (#463). A shell variable names the `env:`
    assignment, which this list carries on its own."""
    for argument in spellings:
        if SHELL_VARIABLE.match(argument):
            continue
        assert argument.startswith(REMOTE_TRACKING), (
            f"the workflow no longer asks about the remote-tracking ref: "
            f"{argument!r}. A runner's checkout has no local branch, so this "
            "is the only spelling that resolves there — if it moved, the gate "
            "has to move with it"
        )


def workflow_base_arguments():
    """Every revision the hygiene workflow names as a base.

    A substring search for the remote-tracking spelling stays green while a
    fourth base-taking step is added without it, because the earlier three
    still carry the string — so each occurrence is read on its own.
    """
    found = base_spellings(read(HYGIENE))
    assert found, "the hygiene workflow names no base at all"
    return found


def test_the_gate_reaches_for_the_spelling_the_workflow_uses(tmp_path):
    """A11. The gate and CI are two readers of one question, and this is what
    keeps them from drifting apart in silence again.

    Red from either side: edit the workflow to drop `origin/` and the first
    half fails; edit the resolver to stop naming the remote-tracking ref, or
    to stop being called at all, and the rest does."""
    assert_every_base_is_remote_tracking(workflow_base_arguments())

    mod = gate_module()
    assert mod.REMOTE_LABEL == "origin/{ref}", mod.REMOTE_LABEL
    assert mod.REMOTE_BASE.endswith(mod.REMOTE_LABEL), (
        f"the gate's fallback {mod.REMOTE_BASE!r} is not the workflow's "
        f"{mod.REMOTE_LABEL!r} under a full ref path"
    )
    assert REMOTE_TRACKING.startswith(mod.REMOTE_LABEL.format(ref="")), (
        f"the workflow spells the base {REMOTE_TRACKING!r} and the gate "
        f"reaches for {mod.REMOTE_BASE!r}"
    )
    # Formatted, not as written: the template doubles its braces to survive
    # `str.format`, so the literal it holds is `{ref}@{{upstream}}` and only
    # the filled value is the revision git is actually asked for.
    assert mod.UPSTREAM_BASE.format(ref="base") == "base@{upstream}", mod.UPSTREAM_BASE

    called = [
        node
        for node in ast.walk(ast.parse(read(GATE)))
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "resolve_base"
    ]
    assert len(called) == 1, (
        f"`resolve_base` is called {len(called)} times in broad_gate.py; the "
        "spelling above is only the workflow's while the gate still reaches "
        "for it"
    )


# --- the documents say which base, and go red if they stop ---------------------

# #969 moved the base rule with the run, from the sealer's step 1 to the
# orchestration that now runs the gate before the sealer is spawned.
REVIEW_ORCH = os.path.join(ROOT, "skills", "code-review", "orchestration.md")
VERIFY = os.path.join(ROOT, "skills", "verify", "orchestration.md")

# Each document needs ONE block carrying both halves — that the base is
# resolved, and what it is resolved TO. A mention of `origin/` in a table
# three hundred lines from the sentence about the base is not the fact stated;
# `tests/test_the_lenient_run_says_what_the_broad_gate_will_say.py`'s
# *no document describes the lenient reader alone* is the precedent.
#
# `broad_gate.py` is NOT in this list and is checked below instead. Its
# `REMOTE_BASE` and `UPSTREAM_BASE` constants sit in one block and carry both
# words between them, so a whole-file block walk passes on the code whatever
# the docstring says — a check that cannot fail, which is the counterfeit
# `skills/verify/SKILL.md` *The Seal Test* is about. Measured: deleting the
# docstring's paragraph left this case green.
DESCRIBES_THE_BASE = (REVIEW_ORCH, VERIFY)


def says_what_the_base_resolves_to(text):
    """True where one block of `text` carries both halves of the fact."""
    return any("origin/" in b and "upstream" in b for b in text.split("\n\n"))


def test_the_block_reader_can_fail():
    """The reader above, driven both ways, so the cases that use it are not
    asserting something nothing can break."""
    assert says_what_the_base_resolves_to("resolved to origin/<base>, its upstream")
    assert not says_what_the_base_resolves_to("the base is the ref you typed")
    assert not says_what_the_base_resolves_to("origin/<base>\n\nits upstream")


def test_no_document_leaves_the_base_reading_as_the_ref_you_typed():
    """Contract rule 14. The resolution is a change to what a person reads — the sealer
    passes the base, and the panel and the printed line are read by whoever
    doubts a seal. A document that still describes the base as the ref as
    typed is a false sentence, and this is what makes that red rather than
    quiet."""
    missing = [
        os.path.relpath(path, ROOT)
        for path in DESCRIBES_THE_BASE
        if not says_what_the_base_resolves_to(read(path))
    ]
    assert not missing, (
        f"these describe the gate's base without saying what it resolves to: {missing}"
    )


def test_the_gates_own_docstring_says_the_base_is_resolved():
    """The interface a reader meets before the code. Read as the module's
    docstring rather than as the file, because the file also holds the
    constants that name the same refs and would answer for it."""
    doc = ast.get_docstring(ast.parse(read(GATE)))
    assert doc, "broad_gate.py has no module docstring"
    assert says_what_the_base_resolves_to(doc), (
        "the gate's docstring describes the base without saying what it "
        f"resolves to:\n{doc}"
    )


def test_the_documents_name_the_panel_row_the_gate_actually_prints():
    """The ref beside the base commit is the half of the stamp a reader uses
    to tell a fresh base from a stale one. From #666 it was the row under
    `base`, and since #832's S5a it is the `base` row itself, beside the
    commit; `from` is not a row the panel has. The orchestrator quotes the
    gate's lines and describes no panel row, so only a stale name is refused."""
    said = " ".join(read(REVIEW_ORCH).split())
    assert "the row under `base` carries the ref" not in said
    assert "`from`" not in said, (
        "skills/code-review/orchestration.md names a row the panel lost"
    )
    mod = gate_module()
    base = mod.Base("base", "aaaaaaa", "origin/base", "bbbbbbb")
    checks = {
        name: mod.Check(name, 0, "1 passed in 0.1s", "out.txt")
        for name in (mod.SUITE, mod.CHAIN_NAME)
    }
    rows = mod.panel("ccccccc", base, checks, None)
    labels = [row[0] for row in rows if row]
    assert "from" not in labels, f"the panel still has a `from` row: {labels}"
    assert ("base", "bbbbbbb  origin/base") in rows, rows


# --- the workflow reader, driven over every shape a base is spelled in ---------

# The six spellings round 1 drove the old pattern over. Three were invisible
# to it, and one of those three — the `BASE:` assignment — is not
# hypothetical: `.github/workflows/hygiene.yml` already spells a base that
# way, and `plan.md` *Technical context* counts that line among the four
# base-taking steps. So the pin covered three of the four the plan enumerates
# while `trail/phases/phase-4.md` and the changelog claimed all of them.
WORKFLOW_SHAPES = [
    (
        '            --baseline "origin/${{ github.base_ref }}" seal/threads/',
        "origin/${{ github.base_ref }}",
    ),
    (
        '          python3 x.py --baseline "origin/${{ github.base_ref }}" specs/',
        "origin/${{ github.base_ref }}",
    ),
    (
        "            --baseline origin/${{ github.base_ref }}",
        "origin/${{ github.base_ref }}",
    ),
    ('            --baseline "$BASE"', "$BASE"),
    # A `BASE:` is a base only as a key of `env:` (#462), so the shape
    # carries the mapping it stands in.
    (
        "        env:\n          BASE: origin/${{ github.base_ref }}",
        "origin/${{ github.base_ref }}",
    ),
    (
        '            --range "origin/${{ github.base_ref }}...HEAD" ${exempt[@]+"${exempt[@]}"}',
        "origin/${{ github.base_ref }}...HEAD",
    ),
]


def test_the_workflow_reader_sees_every_shape_a_base_is_spelled_in():
    """Finding 4. The flag on its own continuation line, the flag on the same
    line as its command, the value unquoted, a shell variable, an `env:`
    assignment, and a range. A reader that sees only the first shape passes
    while a step added in any of the others goes unread."""
    for line, expected in WORKFLOW_SHAPES:
        found = base_spellings(line)
        assert found == [expected], f"{line!r} was read as {found}"


def test_the_workflow_reader_finds_the_env_assignment_the_file_already_has():
    """The `BASE:` shape, over the real file rather than over a sample — it is
    the one the plan counts and the old pattern could not see. The count is
    held against an independent listing of the file's code lines naming a
    base, so it holds as steps come and go."""
    found = workflow_base_arguments()
    listed = [
        line
        for line in read(HYGIENE).split("\n")
        if not line.lstrip().startswith("#")
        and re.search(r"--baseline\b|\bBASE:", line)
    ]
    assert len(found) == len(listed), f"the workflow names {len(found)} bases: {found}"
    assert any(spelling == REMOTE_TRACKING for spelling in found), (
        f"no bare `{REMOTE_TRACKING}` among {found} — the `BASE:` assignment is unread"
    )


# --- #462, #463: what the reader counts, driven over one fixture ------------

# Every shape #462 names, in one workflow: a flag in a whole-line comment, a
# flag in a trailing comment, a `BASE:` under `with:` and one inside a
# `run: |` block beside the one `env:` carries, and an empty quoted value.
# Neutral values only (`CONTRIBUTING.md` *House rules*, *No real
# identifiers*).
MISLEADING_WORKFLOW = """\
jobs:
  release:
    steps:
      # --baseline origin/other
      - name: a flag in a trailing comment
        run: x --range foo  # --baseline bar
      - name: one base, and two lines spelled like one
        env:
          BASE: origin/${{ github.base_ref }}
        with:
          BASE: not-a-base-under-with
        run: |
          BASE: not-a-base-inside-run
          y --baseline "$BASE"
      - name: an empty base
        run: z --baseline ""
"""


def test_a_flag_in_a_comment_is_not_a_base():
    """B1, #462. Whole-line and trailing comments are not code, so neither
    `origin/other` nor `bar` is read; the flag before the trailing comment
    is."""
    found = base_spellings(MISLEADING_WORKFLOW)
    assert "origin/other" not in found, found
    assert "bar" not in found, found
    assert "foo" in found, found


def test_only_a_base_keyed_under_env_is_a_base():
    """B2, #462. The `BASE:` under `env:` counts; the one under `with:` and
    the one inside a `run: |` block do not. The whole reading, in order."""
    assert base_spellings(MISLEADING_WORKFLOW) == [
        "foo",
        REMOTE_TRACKING,
        "$BASE",
        "",
    ]


def test_an_empty_base_fails_the_spelling_check_by_name():
    """B3, #463. `--baseline ""` reads as `""`, not `None`, so the check the
    workflow's spellings are held to fails with `AssertionError` naming the
    value, the way every other malformed spelling fails, and never with
    `TypeError`."""
    found = base_spellings('        run: z --baseline ""')
    assert found == [""], found
    with pytest.raises(AssertionError, match="''"):
        assert_every_base_is_remote_tracking(found)
