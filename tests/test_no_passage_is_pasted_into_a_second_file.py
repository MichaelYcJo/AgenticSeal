"""No passage of a rule document is pasted into a second one (#730).

`docs/the-record-layout.md` says that a file stating a rule another file is
the home of links to that home and does not restate it, and that where a copy
is found the copy is the defect. Nothing found copies. Four were measured
before this module existed, each arriving as a paste: #107's contract section
pasted back into `agents/warden.md`, #292's `CLAUDE.md` block that was 95 %
its template, #715's `CLAUDE.md` and `CONTRIBUTING.md` sentences that
disagreed, and #730's merge table in `CLAUDE.md`, which had gone false where
its home had not.

**What is read.** Every tracked `*.md` under `docs/`, `skills/`, `agents/` and
`templates/`, with `CLAUDE.md`, `CONTRIBUTING.md` and `README.md`. Left out:
every `*.ko.md`, because a Korean edition is a sanctioned mirror in other
words; everything under `seal/`, which is records; and `CHANGELOG.md`.

**How a file is normalised.** Each file is read whole: `CLAUDE.md` carries
no copy of `templates/claude-md-block.md` since #940, so no region is
sanctioned. Fenced code blocks and heading lines are dropped. A quoted
section name -- a `.md` path followed by `*...*` -- becomes one token, because a link shares its heading's words by
design; the name may wrap across a line, which is the case the first draft
of this method missed. Then the text is lowercased, stripped of `` ` ``, `*`,
`|`, `>` and `#`, and split into words.

**What is counted.** For each unordered pair of files, the number of distinct
runs of `WINDOW` consecutive words the two share. `WINDOW` is imported from
`tests/test_a_moved_rule_leaves_its_definition.py`, never typed here: that
module measured it between the longest kept application (10 words) and the
smallest real copy (25), and this is the same question asked of more files.

**Why verbatim.** The measured failure is a paste. A check that tried to
catch a paraphrase would have to decide when two sentences say the same
thing, which no constant can hold: at any similarity that catches a
paraphrase it also matches a heading against the sentence that links it.
The paraphrase half was measured once, by hand, and its result is recorded in
`seal/specs/1791076836-every-rule-claude-md-restates-has-one-home/spec.md`
*The method and its result* at `67694cba` rather than checked.

**Why a ratchet.** The tree already holds copies, measured into `BASELINE`
below, and moving them is #755's work, cluster by cluster. So the check fails
when a pair not in `BASELINE` shares any run, or when a pair's count goes
above its baseline. It passes when a count goes down, and the baseline need
not be lowered in the same change: otherwise every branch that edits a
duplicated passage would edit this one table, which is the shared-file
conflict `docs/the-record-layout.md` *A change writes fragments, never a
shared file* exists to stop. The cost is slack, stated: a pair that has
drained can take a later copy up to its old count. The work that drains a
pair lowers its entry on purpose.

**What it does not catch.** A rule restated in fresh words. Measured against
the three restatements #730 names, it finds one of three, the merge table,
through its identical rows; *no real identifiers* and the commit cadence were
both restated in other words. Saying otherwise would be the counterfeit
`CONTRIBUTING.md` refuses.
"""

import itertools
import os
import re

from conftest import git_listing, on_disk
from test_a_moved_rule_leaves_its_definition import WINDOW

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

TOP_FILES = ("CLAUDE.md", "CONTRIBUTING.md", "README.md")
TOP_DIRS = ("docs/", "skills/", "agents/", "templates/")

HOME_ACT = "link to the home instead of copying it, per `docs/the-record-layout.md`"

FENCE = re.compile(r"^ *(`{3,}|~{3,})")
HEADING = re.compile(r"^ {0,3}#{1,6}(\s|$)")
# A section quoted by name after a `.md` path (with or without its
# possessive). `[^*]` crosses a line break, so a wrapped name is one name.
SECTION = re.compile(r"`?[\w./-]+\.md`?(?:'s)?\s+\*[^*]{1,200}\*")
SECTION_TOKEN = " section-citation "
STRIP = str.maketrans("", "", "`*|>#")


def corpus():
    """The rule documents git tracks, as repository paths, sorted.

    A path git lists and the tree has deleted is skipped: this check judges
    what it finds, and a missing file can only lower a count, which never
    fails it."""
    listed = git_listing(ROOT, "ls-files", "--", "*.md")
    rules = [
        rel
        for rel in listed
        if (rel in TOP_FILES or rel.startswith(TOP_DIRS)) and not rel.endswith(".ko.md")
    ]
    present, _missing = on_disk(ROOT, rules)
    return sorted(present)


def lines(text):
    """TEXT's lines, ended where GFM ends one: LF, CR or CRLF alone."""
    return text.replace("\r\n", "\n").replace("\r", "\n").split("\n")


def words(text):
    """TEXT normalised as the docstring says, as a list of words."""
    kept, fence = [], None
    for line in lines(text):
        opened = FENCE.match(line)
        if fence:
            if (
                opened
                and opened.group(1)[0] == fence[0]
                and len(opened.group(1)) >= len(fence)
                and not line.strip().strip(fence[0])
            ):
                fence = None
            continue
        if opened:
            fence = opened.group(1)
            continue
        if HEADING.match(line):
            continue
        kept.append(line)
    text = SECTION.sub(SECTION_TOKEN, "\n".join(kept))
    return text.lower().translate(STRIP).split()


def windows(word_list):
    return {
        " ".join(word_list[i : i + WINDOW]) for i in range(len(word_list) - WINDOW + 1)
    }


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


# Measured on 2026-10-04 at this work item's phase 1 tree, and again after
# `release/v0.18.1` was merged in at edee5ca2. Every entry is debt
# that #755 moves, cluster by cluster, except where a comment names the rule
# that makes the copy sanctioned. A change that drains a pair may lower its
# entry; nothing has to.
BASELINE = {
    # Sanctioned: the opening paragraph every agent definition carries,
    # which tests/test_every_agent_reads_the_contract.py requires word for
    # word. framer-smith adds the shared `skills:` list, and smith-warden
    # adds debt of its own (cluster b of the remainder issue). The framer's
    # entries were measured on its rewrite (#968): the opening, the step
    # sentence saying whose `skills/` paths are, the step opening
    # `writing-style` by section, and with the smith the reference-root
    # sentence and its `## Never` line, each the same words in every
    # definition of #957's shape. framer-scribe was measured again at the
    # merge of `release/v0.22.2`, once #970 gave the scribe the same
    # step sentence.
    ("agents/framer.md", "agents/scribe.md"): 4,
    ("agents/framer.md", "agents/sealer.md"): 14,
    ("agents/framer.md", "agents/smith.md"): 24,
    ("agents/framer.md", "agents/warden.md"): 31,
    ("agents/scribe.md", "agents/sealer.md"): 5,
    ("agents/scribe.md", "agents/smith.md"): 4,
    ("agents/scribe.md", "agents/warden.md"): 4,
    ("agents/sealer.md", "agents/smith.md"): 14,
    ("agents/sealer.md", "agents/warden.md"): 14,
    ("agents/smith.md", "agents/warden.md"): 18,
    # Debt, every entry below. Lowered to the counts measured at #940's
    # last phase; each pair that measured zero left the table.
    ("README.md", "skills/config/SKILL.md"): 22,
    ("README.md", "skills/implement/SKILL.md"): 2,
    ("README.md", "skills/implement/orchestration.md"): 1,
    ("README.md", "skills/parity-setup/SKILL.md"): 1,
    ("agents/smith.md", "skills/implement/SKILL.md"): 3,
    ("docs/one-root-by-lifetime.md", "skills/implement/SKILL.md"): 4,
    ("docs/the-agent-set.md", "skills/implement/SKILL.md"): 20,
    ("skills/agent-contract/SKILL.md", "skills/implement/SKILL.md"): 1,
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


def test_a_paste_is_named_with_the_pair_the_run_and_the_act():
    """S6: twenty words of `CONTRIBUTING.md` pasted into another rule document
    are named, with both files, the count, the run and the act.

    The paste lands in a document of its own, so the pair is new and the
    longest run it reports is the paste and not a copy the tree already
    held."""
    texts = tree()
    paste = a_sentence_of(texts["CONTRIBUTING.md"])
    texts["docs/planted.md"] = "Some words of its own.\n\n" + paste + "\n"
    found = over_baseline(texts, BASELINE)
    named = [f for f in found if "CONTRIBUTING.md and docs/planted.md" in f]
    assert named, found
    assert f"share {20 - WINDOW + 1} runs" in named[0], named[0]
    assert "longest is 20 words" in named[0], named[0]
    assert paste in named[0]
    assert "link to the home instead of copying it" in named[0].lower()


def test_a_paste_into_the_block_template_is_named():
    """The block `install.sh` distributes is a rule document: a paste inside
    its marker region is named like a paste anywhere else (round 1)."""
    texts = tree()
    paste = a_sentence_of(texts["CONTRIBUTING.md"])
    rel = "templates/claude-md-block.md"
    planted = texts[rel].replace(
        "specseal:start -->", "specseal:start -->\n" + paste, 1
    )
    assert planted != texts[rel]
    texts[rel] = planted
    assert [f for f in over_baseline(texts, BASELINE) if rel in f]


def test_a_count_over_its_baseline_is_named_and_one_at_it_is_not():
    """The ratchet's own edge, on a pair the table already holds."""
    texts = tree()
    counts = shared_counts(texts)
    pair = max(counts, key=counts.get)
    assert not [
        f
        for f in over_baseline(texts, {**BASELINE, pair: counts[pair]})
        if f.startswith(f"{pair[0]} and {pair[1]} share")
    ]
    found = over_baseline(texts, {**BASELINE, pair: counts[pair] - 1})
    assert [f for f in found if f.startswith(f"{pair[0]} and {pair[1]} share")]


def test_a_removed_copy_passes_without_a_baseline_edit():
    """S7: a pair whose count goes down passes, whatever the table says.

    One shared run is broken in the second file, so the pair still shares
    something and is still judged; a check that held counts exactly, rather
    than at most, fails here."""
    texts = tree()
    counts = shared_counts(texts)
    a, b = max(counts, key=counts.get)
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
    assert not over_baseline(texts, {**BASELINE, (a, b): counts[(a, b)]})


def test_a_wrapped_section_name_is_one_token():
    """A link carries its heading's words; a name broken across a line is
    still the name, and two links to one long heading share nothing."""
    name = (
        "A change writes fragments, never a shared file, and the release "
        "gathers every one of them before it folds"
    )
    assert len(name.split()) > WINDOW
    one = f"See `docs/the-record-layout.md` *{name}* for where it goes.\n"
    wrapped = name.replace(" a shared", chr(10) + "a shared")
    two = f"Read `docs/the-record-layout.md`\n*{wrapped}*\nfirst.\n"
    path = f"`CONTRIBUTING.md`'s *{name}*\n"
    other = f"As docs/the-record-layout.md *{name}* says.\n"
    assert not shared_counts(
        {"one.md": one, "two.md": two, "three.md": path, "four.md": other}
    )


def test_the_block_template_is_read_whole_and_fences_and_headings_are_not():
    """The block's template is a rule document like any other and is read
    whole (round 1); `CLAUDE.md` carries no copy of it since #940, so no
    region of either file is dropped."""
    texts = tree()
    rel = "templates/claude-md-block.md"
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        assert words(texts[rel]) == words(f.read())
    run = " ".join(f"w{i}" for i in range(WINDOW))
    fenced = f"```\n{run}\n```\n"
    heading = f"## {run}\n"
    for skipped in (fenced, heading):
        assert not shared_counts({"a.md": skipped, "b.md": run}), skipped
    assert shared_counts({"a.md": run, "b.md": run}) == {("a.md", "b.md"): 1}
    # A copy whose first word was capitalised by its new sentence is a copy.
    assert shared_counts({"a.md": run.upper(), "b.md": f"`{run}`"}) == {
        ("a.md", "b.md"): 1
    }
