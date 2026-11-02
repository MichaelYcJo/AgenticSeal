"""No passage of a rule document is pasted into a second one (#730).

`docs/the-record-layout.md` says that a file stating a rule another file is
the home of links to that home and does not restate it, and that where a copy
is found the copy is the defect. Nothing found copies. Four were measured
before this module existed, each arriving as a paste: #107's contract section
pasted back into `agents/proofer.md`, #292's `CLAUDE.md` block that was 95 %
its template, #715's `CLAUDE.md` and `CONTRIBUTING.md` sentences that
disagreed, and #730's merge table in `CLAUDE.md`, which had gone false where
its home had not.

**What is read.** Every tracked `*.md` under `docs/`, `skills/`, `agents/` and
`templates/`, with `CLAUDE.md`, `CONTRIBUTING.md` and `README.md`. Left out:
every `*.ko.md`, because a Korean edition is a sanctioned mirror in other
words; and everything under `seal/`, which is records.

**How a file is normalised.** Each file is read whole, and no region of
one is sanctioned. Fenced code blocks and heading lines are dropped. A quoted
section name -- a `.md` path followed by `*...*` -- becomes one token, because a link shares its heading's words by
design; the name may wrap across a line, which is the case the first draft
of this method missed. Then the text is lowercased, stripped of `` ` ``, `*`,
`|`, `>` and `#`, and split into words. The selection and the normalisation
are `skills/settle/scripts/passages.py`'s code (`in_corpus`, `words`,
`windows`), which `skills/code-review/scripts/chain_check.py` reads a
design's `to` through as well (#1216), and this module imports them.

**What is counted.** For each unordered pair of files, the number of distinct
runs of `WINDOW` consecutive words the two share. A pair of two agent
definitions, both under `agents/`, is not counted: a passage two definitions
share states a fact about each file that holds it, and each agent reads only
its own definition, so a link would cost every spawn a read and remove
nothing said twice
(`48d035aa:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md`
*The table*, row K2). A definition paired with any other file is counted,
since a skill or a document restating a definition is a copy. `WINDOW` is
`skills/settle/scripts/passages.py`'s, never typed here:
`tests/text/test_a_moved_rule_leaves_its_definition.py` measured it between the longest kept application (10 words) and the
smallest real copy (25), and this is the same question asked of more files.

**Why verbatim.** The measured failure is a paste. A check that tried to
catch a paraphrase would have to decide when two sentences say the same
thing, which no constant can hold: at any similarity that catches a
paraphrase it also matches a heading against the sentence that links it.
The paraphrase half was measured once, by hand, and its result is recorded in
`67694cba:seal/specs/1791076836-every-rule-claude-md-restates-has-one-home/spec.md`
*The method and its result* rather than checked.

**Why a ratchet.** The tree still holds two copies, both in `README.md`,
measured into `BASELINE` below. #1102 rewrites `README.md`, links them, and
removes `BASELINE` and the ratchet with them, so that any shared run fails.
Until then the check fails when a pair not in `BASELINE` shares any run, or
when a pair's count goes above its baseline. It passes when a count goes
down, and the baseline need not be lowered in the same change: otherwise
every branch that edits a duplicated passage would edit this one table,
which is the shared-file conflict `docs/the-record-layout.md` *A change
writes fragments, never a shared file* exists to stop. The cost is slack,
stated: a pair that has drained can take a later copy up to its old count.
The work that drains a pair lowers its entry on purpose.

**What it does not catch.** A rule restated in fresh words. Measured against
the three restatements #730 names, it finds one of three, the merge table,
through its identical rows; *no real identifiers* and the commit cadence were
both restated in other words. Saying otherwise would be the counterfeit
`CONTRIBUTING.md` refuses.
"""

import itertools
import os

import pytest
from conftest import ROOT, git_listing, load_module, on_disk

passages = load_module(
    os.path.join(ROOT, "skills", "settle", "scripts", "passages.py"),
    "agentic_passages_for_the_paste_check",
)
WINDOW, TOP_FILES = passages.WINDOW, passages.TOP_FILES
in_corpus, words, windows = passages.in_corpus, passages.words, passages.windows

# A pair whose two paths both start here is not counted (*What is counted*).
DEFINITIONS = "agents/"

HOME_ACT = "link to the home instead of copying it, per `docs/the-record-layout.md`"


def corpus():
    """The rule documents git tracks, as repository paths, sorted.

    A path git lists and the tree has deleted is skipped: this check judges
    what it finds, and a missing file can only lower a count, which never
    fails it."""
    listed = git_listing(ROOT, "ls-files", "--", "*.md")
    rules = [rel for rel in listed if in_corpus(rel)]
    present, _missing = on_disk(ROOT, rules)
    return sorted(present)


def shared_counts(texts):
    """`{(a, b): n}`, the distinct `WINDOW`-word runs each pair shares.

    TEXTS maps a path to its raw text, so a case can hand in a planted copy."""
    owners = {}
    for rel in sorted(texts):
        for run in windows(words(texts[rel])):
            owners.setdefault(run, []).append(rel)
    counts = {}
    for rels in owners.values():
        for pair in itertools.combinations(rels, 2):
            if pair[0].startswith(DEFINITIONS) and pair[1].startswith(DEFINITIONS):
                continue
            counts[pair] = counts.get(pair, 0) + 1
    return counts


def longest_run(a_text, b_text):
    """The longest run of words A's normalised text shares with B's."""
    a, b = words(a_text), words(b_text)
    common = windows(a) & windows(b)
    best, start = (0, ""), None
    for i in range(len(a) - WINDOW + 2):
        inside = i < len(a) - WINDOW + 1 and " ".join(a[i : i + WINDOW]) in common
        if inside and start is None:
            start = i
        if not inside and start is not None:
            span = a[start : i - 1 + WINDOW]
            best = max(best, (len(span), " ".join(span)))
            start = None
    return best


def over_baseline(texts, baseline):
    """A sentence per pair whose count exceeds its baseline, or that has none."""
    found = []
    for pair, count in sorted(shared_counts(texts).items()):
        allowed = baseline.get(pair, 0)
        if count > allowed:
            length, run = longest_run(texts[pair[0]], texts[pair[1]])
            found.append(
                f"{pair[0]} and {pair[1]} share {count} runs of {WINDOW} words "
                f"where {allowed} were measured; the longest is {length} words: "
                f"{run[:240]!r}. {HOME_ACT[0].upper()}{HOME_ACT[1:]}"
            )
    return found


def tree():
    """`{path: text}` for the corpus, each file read whole."""
    texts = {}
    for rel in corpus():
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            texts[rel] = f.read()
    return texts


# A stored count, which `skills/core/SKILL.md` *The rule a mechanism is kept
# against* refuses, standing until #1102 links the two `README.md` passages
# these entries count and removes them with `BASELINE` and the ratchet.
BASELINE = {
    ("README.md", "skills/implement/SKILL.md"): 2,
    # The acts row of the verifying round, which moved with its table to
    # `skills/implement/acts.md` in #1148.
    ("README.md", "skills/implement/acts.md"): 1,
}


def test_the_corpus_is_found():
    """A glob that matches nothing passes every pair it would have judged."""
    found = corpus()
    assert len(found) >= 50, f"the rule corpus has {len(found)} files"
    for rel in TOP_FILES:
        assert rel in found, f"{rel} is missing from the corpus"
    assert not [rel for rel in found if rel.endswith(".ko.md")]


def test_no_pair_shares_more_than_it_was_measured_at():
    found = over_baseline(tree(), BASELINE)
    assert not found, "\n".join(found)


# --- the check can fail, and it does not fail the wrong way ------------------


def a_sentence_of(text, length=20):
    """LENGTH consecutive words from TEXT's prose, normalised, as raw text."""
    return " ".join(words(text)[200 : 200 + length])


@pytest.mark.parametrize(
    "source, planted",
    [
        ("CONTRIBUTING.md", "docs/planted.md"),
        # A definition paired with a file outside `agents/` is still counted:
        # a skill restating a definition is the paste #1231 linked away.
        ("agents/crafter.md", "skills/planted/SKILL.md"),
    ],
)
def test_a_paste_is_named_with_the_pair_the_run_and_the_act(source, planted):
    """S6: twenty words of a rule document pasted into another are named,
    with both files, the count, the run and the act.

    The paste lands in a document of its own, so the pair is new and the
    longest run it reports is the paste and not a copy the tree already
    held."""
    texts = tree()
    paste = a_sentence_of(texts[source])
    texts[planted] = "Some words of its own.\n\n" + paste + "\n"
    found = over_baseline(texts, BASELINE)
    named = [f for f in found if f"{source} and {planted}" in f]
    assert named, found
    assert f"share {20 - WINDOW + 1} runs" in named[0], named[0]
    assert "longest is 20 words" in named[0], named[0]
    assert paste in named[0]
    assert "link to the home instead of copying it" in named[0].lower()


def planted_pair(length=40):
    """Two rule documents sharing a passage of LENGTH placeholder words.

    The ratchet's cases plant their pair rather than read the tree's
    largest one, so they hold on a tree that shares no run at all."""
    passage = " ".join(f"w{i}" for i in range(length))
    return {
        "docs/one.md": f"Words of the first file.\n\n{passage}\n",
        "skills/two/SKILL.md": f"Other words, the second's.\n\n{passage}\n",
    }


def test_a_count_over_its_baseline_is_named_and_one_at_it_is_not():
    """The ratchet's own edge: a pair at its entry passes, one above it is
    named."""
    texts = planted_pair()
    counts = shared_counts(texts)
    pair = ("docs/one.md", "skills/two/SKILL.md")
    assert counts[pair] > 1, counts
    assert not over_baseline(texts, {pair: counts[pair]})
    found = over_baseline(texts, {pair: counts[pair] - 1})
    assert [f for f in found if f.startswith(f"{pair[0]} and {pair[1]} share")]


def test_a_removed_copy_passes_without_a_baseline_edit():
    """S7: a pair whose count goes down passes, whatever the table says.

    One shared run is broken in the second file, so the pair still shares
    something and is still judged; a check that held counts exactly, rather
    than at most, fails here."""
    texts = planted_pair()
    counts = shared_counts(texts)
    a, b = "docs/one.md", "skills/two/SKILL.md"
    mine = words(texts[b])
    common = windows(words(texts[a])) & windows(mine)
    first = next(
        i
        for i in range(len(mine) - WINDOW + 1)
        if " ".join(mine[i : i + WINDOW]) in common
    )
    del mine[first + WINDOW // 2]
    texts[b] = " ".join(mine)
    after = shared_counts(texts)
    assert 0 < after[(a, b)] < counts[(a, b)]
    assert not over_baseline(texts, {(a, b): counts[(a, b)]})


def test_a_run_two_definitions_share_is_not_counted_and_one_beside_a_skill_is():
    """A pair of two agent definitions is left out of the count, and a
    definition paired with a file outside `agents/` is still counted."""
    run = " ".join(f"w{i}" for i in range(WINDOW))
    texts = {"agents/a.md": run, "agents/b.md": run, "skills/c/SKILL.md": run}
    assert shared_counts(texts) == {
        ("agents/a.md", "skills/c/SKILL.md"): 1,
        ("agents/b.md", "skills/c/SKILL.md"): 1,
    }
