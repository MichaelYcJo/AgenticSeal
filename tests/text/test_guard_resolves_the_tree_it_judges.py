"""The guard judged the session's cwd, not the tree the command acts on.

`git -C <repo> switch <branch>` names its own repository. The guard resolved
the repository from the session's cwd instead and, when that cwd was not a repo
at all, stood it in for the tree root. With the cwd at a home directory the
containment test in `sessions_in_tree` then matched every Claude session on the
machine, and a single-stream switch was denied by sessions in unrelated
repositories.

The guard's cases moved to `tests/hooks/test_worktree_guard.py`, the consent
writer's to `tests/hooks/test_worktree_consent.py`, and the commit gate's case that
says what declining does to `tests/test_commit_review_gate.py` (#942's phase
6). What stays reads the policy and the READMEs, which is #923's.
"""

import os

from conftest import ROOT


def test_the_guard_policy_says_the_record_is_filed_where_the_guard_judged():
    """Contract rule 14, for S1-S3 of work item 1791384157: *Creation
    consent*'s record says its clone is the one the guard judged, placed by
    one function. Red against `5623d728`'s text."""
    assert (
        "**The clone the guard judged.** The writer places a creation by the "
        "guard's own placement, `hooks/worktree_consent.py#place`"
    ) in _policy_text()


def test_the_guard_policy_names_the_shell_built_word_limit():
    """Contract rule 14, for S27 of work item 1791384157's second
    reframe: *Known limits* says in one sentence that a word the shell
    builds before git runs is not read and names #856's four forms as silent;
    *A. Branch switch* names no brace rule, cost or count, and no bullet names a brace-hidden
    `-C`. Red against `52c72bbe`'s text."""
    text = _policy_text()
    for sentence in (
        "A word the shell builds before git runs — a brace expansion, a "
        "substitution that spells `git`, a here-string or heredoc handed to a "
        'shell, a git spelled past the splitter (`g""it` in a line it cannot '
        "close) — is not read",
        "so `git rebase {main,feature/x}`, `git rebase --ro{,} feature/x`, `git "
        "stash {branch,} y` and `git worktree {add,} ../wt f` are listed and "
        "silent in every tree",
    ):
        assert sentence in text, sentence
    for gone in (
        "A brace expansion is unrecognised (#856)",
        "The brace shape adds",
        "Three costs are named.",
        "a `-C` a brace hides",
        "since #856 `git worktree {add,} ../wt f`, whose `add` only bash's brace "
        "expansion makes) is an unrecognised shape",
    ):
        assert gone not in text, gone


def _policy_text():
    """`docs/worktree-guard-spec.md`, whitespace folded so a wrapped sentence
    reads as one line."""
    path = os.path.join(ROOT, "docs", "worktree-guard-spec.md")
    with open(path, encoding="utf-8") as f:
        return " ".join(f.read().split())


def test_the_guard_policy_says_which_shapes_reach_the_rows_and_who_reads_the_stop():
    """S12 of work item 1791270162, contract rule 14: *A. Branch switch* names the
    three shapes, the stop's two readers and its failure direction, in the
    sentences a person reads to learn when the guard stops. Red against the
    policy as it stood at `9c03ae85`."""
    text = _policy_text()
    for sentence in (
        "The guard does not predict whether a command switches a branch.",
        "A listed shape is silent in every tree state and spawns no git.",
        "**a switch** — `git switch`, whatever its words.",
        "In a clean tree nobody else is in, row 5 says nothing of a switch, "
        "and nothing is said of a shape that might be one.",
        "it is a `deny` to the model, which rewrites in the plain spelling "
        "and meets the rows above on the retry, and no person is asked.",
        "so the stop is a `deny` whoever is at the keyboard.",
        "The consent record is never read for the stop",
        "**The failure direction.** The stop adds a stop for every "
        "unrecognised shape where the tree matters",
        # Round 1 of work item 1791270162: red 1 and red 3, absent at
        # `4de95fa7`.
        "A `git switch` on the same line makes the stop a `deny` whoever is "
        "at the keyboard",
        "Every tree on the line is read before the stop is taken",
        "A `rebase` is listed unless it has two words that are not options, "
        "or `--root` and one",
        # #854 (round 3 of work item 1791270162, yellow 1 and white 2),
        # absent at `3d78c220`.
        "and so is every word after a `--` or an `--end-of-options`",
        "git takes an unambiguous prefix of `--root` (`--ro`) as `--root`, "
        "and so does the guard.",
        'A reason that describes one tree calls it "this tree", whichever tree it is',
    ):
        assert sentence in text, sentence


def test_the_guard_policy_says_nothing_is_read_past_the_base():
    """S12 of work item 1791270162: *Which tree* keeps the frozen reading's
    paragraphs and says nothing is read past the base's words, and *Known
    limits* holds the new limits and none of the removed ones. Red against
    the policy as it stood at `9c03ae85`."""
    text = _policy_text()
    assert "**Nothing is read past the base's words**" in text
    for limit in (
        "A git subcommand this repository never ran",
        "A creation only a hidden spelling holds",
        "A `rebase` is listed, and detaches HEAD while it runs",
        "every unrecognised shape stops there, in every tree",
        # Round 1 of work item 1791270162, yellow 5 and yellow 4, absent at
        # `4de95fa7`.
        "A string handed to a shell (`sh -c`, `bash -c`, `eval`) is judged in "
        "the tree its segment names",
        "or either side of an `&` the splitter cut is the finding",
        # #854 (round 3 of work item 1791270162, white 3), absent at
        # `3d78c220`.
        "One is `cd w 2>&1` before the switch: the frozen splitter cuts it at its `&`",
        "a cut git inside an `if` body after `cd w`",
    ):
        assert limit in text, limit
    for gone in (
        "Two rules are read past the base.",
        "options are read from a static table",
        "name is looked up as git resolves it (*Which tree*)",
        "the guard asks wherever a view's words hold a switch",
    ):
        assert gone not in text, gone


def test_the_guard_policy_and_readmes_say_a_body_token_is_not_read():
    """Contract rule 14, for #780: *Choice sites* and the two token
    rows of both READMEs say a token inside a here-document body is not
    read. Red against `a3aa139a`'s texts."""
    assert (
        "**A token counts only where it is typed outside every here-document "
        "body, and a command that does not split carries none from where its "
        "split fails.** The token is read from the command, and only the "
        "command: `hooks/lib/tokens.py#given` takes it only where the command as "
        "written and the command with its here-document bodies taken out"
    ) in _policy_text()
    assert "**Where the token is read from.**" not in _policy_text()
    with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as f:
        readme = f.read()
    with open(os.path.join(ROOT, "README.ko.md"), encoding="utf-8") as f:
        readme_ko = f.read()
    assert (
        "Read as a bare word, so it does not count inside a quoted message, "
        "and not inside a here-document body either."
    ) in readme
    assert "Read as a bare word, and not inside a here-document body." in readme
    assert (
        "따옴표 안의 문장에 적힌 것은 세지 않고, here-document 본문에 적힌 "
        "것도 세지 않는다."
    ) in readme_ko
    assert (
        "명령의 낱말로 있을 때만 세고, here-document 본문에 적힌 것은 세지 않는다."
    ) in readme_ko
