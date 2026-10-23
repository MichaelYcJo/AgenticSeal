"""The behaviour suite's generators: what is left here after #942's phase 5.

The cases of `evals/scripts/noninferiority.py` are in
`tests/test_noninferiority.py`. The cases here pin
`evals/scripts/replay_targets.py`, `evals/scripts/rule_cases.py` and
`evals/scripts/seed_defects.py`, the generators that write the suite's
cases and their `truth-` graders, and they wait for the phase that rebuilds
those modules. A generated truth is read back through
`noninferiority.py#grader_from`, the one reader of a grader file.
"""

import importlib.util
import json
import os
import re
import subprocess

import pytest

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))


def load_script(name):
    path = os.path.join(ROOT, "evals", "scripts", f"{name}.py")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ni = load_script("noninferiority")

TRUTH = r"^location: .*(?:src\/a\.py:(?:10|11|12)(?!\d))"


def test_a_truth_is_a_fixed_finding_the_next_round_confirmed():
    """Guards the replay set's ground truth: a 🟡 closed fixed and named
    closed by the next round's 🟢 row, and no other."""
    rt = load_script("replay_targets")
    nxt = (
        "| 🟢 | round 1's finding 2 is closed — x | `a.md:3` | confirmed | read |\n"
        "| 🟢 | round 1's 🟡 4 is closed — y | `a.md:9` | confirmed | read |\n"
        "| 🟢 | round 2's finding 3 is closed — z | `a.md:9` | confirmed | read |\n"
        "| 🟡 5 | round 1's finding 5 is closed | `a.md:9` | open | read |\n"
    )
    assert rt.confirmed(nxt, 1) == {2, 4}


LABELLED_ROUND_1 = """# i — review round 1

target: 1a2b3c4 against main

## Findings

### 1. a fixed defect

severity: must
location: `src/a.py:12`, `docs/a.md`
evidence: read `src/a.py:12`
verdict: fixed abc1234

why it matters.

answer: fixed

### 2. a finding that does not hold

severity: should
location: `src/b.py:3`
evidence: executed `git grep -n b -- src`
verdict: rejected

answer: it holds

## Confirmations

confirms: none
a claim of the frame that matched.
"""

LABELLED_ROUND_2 = """# i — review round 2

target: 2b3c4d5, fixes 1a2b3c4..2b3c4d5

## Findings

## Confirmations

confirms: round-1#1
holds.

confirms: round-1#2
holds.

confirms: round-3#1
another round's.
"""


def test_a_truth_of_a_labelled_record_is_a_fixed_finding_the_next_round_confirms():
    """Guards the replay set's ground truth on 0.22.0's record: a finding is
    a `### <n>. ` section read through `chain_check.py`'s own reader, with
    its `location:` value whole and whether its `verdict:` is `fixed`, and
    the next round confirms it on a `confirms: round-<N>#<n>` line. The
    table case above reads only the old rows, so without this one a reader
    that found no finding in any labelled record, which is what the
    generator did before #964, left every 0.22.0 round out unnoticed."""
    rt = load_script("replay_targets")
    rel = "seal/specs/i/rounds/round-1.md"
    assert rt.labelled(LABELLED_ROUND_1)
    assert not rt.labelled("| 🟢 | round 1's finding 2 is closed | `a:1` | confirmed |")
    read, why = rt.labelled_round(LABELLED_ROUND_1, rel, 1)
    assert why == ""
    assert read["sha"] == "1a2b3c4"
    assert read["value"] == "1a2b3c4 against main"
    assert read["findings"] == [
        (1, "a fixed defect", "`src/a.py:12`, `docs/a.md`", True),
        (2, "a finding that does not hold", "`src/b.py:3`", False),
    ]
    assert rt.confirmed(LABELLED_ROUND_2, 1) == {1, 2}
    assert rt.confirmed(LABELLED_ROUND_2, 2) == set()


def test_a_labelled_record_the_check_refuses_gives_no_truth():
    """Guards that a replay reads only what a pull request accepted: a
    record `chain_check.py` refuses is left out naming the refusal, and a
    next record it refuses confirms nothing, so a grader is never built on
    a line the check would not read. Nothing else holds the generator to
    the check's refusals, which is the class #923 found leaking three
    times."""
    rt = load_script("replay_targets")
    rel = "seal/specs/i/rounds/round-1.md"
    bad = LABELLED_ROUND_1.replace("fixed abc1234", "fixed abc1234 and more")
    read, why = rt.labelled_round(bad, rel, 1)
    assert read is None
    assert why.startswith("the check refuses the record at line 12: ")
    assert "reads `verdict: fixed abc1234 and more`" in why
    worse = LABELLED_ROUND_2.replace("round-1#1\n", "round-1#1 and more\n")
    assert rt.confirmed(worse, 1) == set()


def test_a_labelled_record_is_read_by_the_grammar_of_the_commit_that_wrote_it(
    tmp_path, monkeypatch
):
    """Guards the owner's decision on #985: a record is judged by the grammar
    in force when it was written. A round written before the table gained
    its `evidence:` row lacks the line, so the tree's check refuses it, and
    the replay set lost 18 of its 31 rounds that way. Read through the check
    of the commit that last wrote it, in the tree or at a release tag, it is
    read as its pull request accepted it. A record no commit wrote is read
    by the tree's check."""
    rt = load_script("replay_targets")
    repo = tmp_path / "repo"
    repo.mkdir()

    who = ["-c", "user.name=x", "-c", "user.email=x@example.com"]

    def git(*args):
        return subprocess.run(
            ["git", "-C", str(repo), *who, *args],
            check=True,
            capture_output=True,
            encoding="utf-8",
        ).stdout.strip()

    def put(rel, text):
        path = repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    git("init", "-q")
    # The check's files as `replay_targets.py` copies them for a commit, the
    # grammar document apart because the commit below holds an older one.
    for rel in (r for r in rt.CHECK_FILES if not r.startswith("docs/")):
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            put(rel, f.read())
    with open(
        os.path.join(ROOT, "docs", "the-review-record.md"), encoding="utf-8"
    ) as f:
        doc = f.read()
    row = next(ln + "\n" for ln in doc.splitlines() if ln.startswith("| `evidence:` |"))
    put("docs/the-review-record.md", doc.replace(row, ""))
    rel = "seal/specs/i/rounds/round-1.md"
    text = re.sub(r"^evidence: .*\n", "", LABELLED_ROUND_1, flags=re.M)
    put(rel, text)
    git("add", "-A")
    git("commit", "-qm", "a round written before the evidence row")
    written = git("rev-parse", "HEAD")
    put("docs/the-review-record.md", doc)
    git("commit", "-qam", "the evidence row")
    git("tag", "v1.0.0")
    monkeypatch.setattr(rt, "ROOT", str(repo))

    assert rt.written_at(rel, []) == written
    refused, why = rt.labelled_round(text, rel, 1)
    assert refused is None and "no `evidence:` line" in why, why
    read, why = rt.labelled_round(text, rel, 1, at=written)
    assert why == ""
    assert read["findings"] == [
        (1, "a fixed defect", "`src/a.py:12`, `docs/a.md`", True),
        (2, "a finding that does not hold", "`src/b.py:3`", False),
    ]
    nxt = LABELLED_ROUND_2.replace(
        "## Findings\n",
        "## Findings\n\n### 1. a deferred defect\n\nseverity: should\n"
        "location: `src/c.py:1`\nverdict: deferred #9\n\nanswer: filed\n",
    )
    assert rt.confirmed(nxt, 1) == set()
    assert rt.confirmed(nxt, 1, at=written) == {1, 2}

    seen = []

    def stub(_text, rel, _n, at=None):
        seen.append((rel, at))
        return None, "stubbed"

    monkeypatch.setattr(rt, "labelled_round", stub)
    assert rt.targets([]) == ([], [("i", 1, "stubbed")])
    assert seen == [(rel, written)]

    git("rm", "-q", rel)
    git("commit", "-qm", "settled")
    assert rt.written_at(rel, ["v1.0.0"]) == written
    assert rt.written_at("seal/specs/i/rounds/round-9.md", ["v1.0.0"]) is None


def test_targets_reads_the_next_round_by_the_commit_that_wrote_it(monkeypatch):
    """Guards the owner's decision on #985 where `targets` reads the round
    after a fixed finding: that round is judged by the check of the commit
    that wrote it, so a round written before the `evidence:` row still
    confirms the fix it names, and the replay keeps the target."""
    rt = load_script("replay_targets")
    two = "seal/specs/i/rounds/round-2.md"
    monkeypatch.setattr(
        rt,
        "records",
        lambda _tags, _items=None: {
            ("i", 1): LABELLED_ROUND_1,
            ("i", 2): LABELLED_ROUND_2,
        },
    )
    monkeypatch.setattr(rt, "written_at", lambda rel, _tags: f"at {rel}")
    monkeypatch.setattr(
        rt,
        "labelled_round",
        lambda _text, _rel, _n, at=None: (
            {
                "sha": "abc1234",
                "value": "abc1234 against main",
                "findings": [(1, "x", "`src/a.py:12`", True)],
                "confirms": set(),
            },
            "",
        ),
    )
    monkeypatch.setattr(rt, "resolve", lambda _rev: True)
    monkeypatch.setattr(
        rt, "target_base", lambda _value, _target, _landed=None: ("abc1234", "main")
    )
    # The one git call left before `confirmed`: routing.md at the target.
    monkeypatch.setattr(rt, "git", lambda *_args, check=True: "| Branch | b |\n")
    asked = []

    def spy(_text, n, rel, at=None):
        asked.append((n, rel, at))
        return set()

    monkeypatch.setattr(rt, "confirmed", spy)
    rt.targets([])
    assert asked == [(1, two, f"at {two}")], asked


def test_a_labelled_target_names_its_base(monkeypatch):
    """Guards where a labelled replay's clone starts: a fix range's first
    commit, an `against <sha>` commit, or the merge-base with
    `origin/<base>` for `against <base>`, and no base where none resolves,
    which leaves the round out rather than cloning the wrong range. The old
    reader found a base only in an asked paragraph, which 0.22.0's record
    does not carry."""
    rt = load_script("replay_targets")
    known = {"1a2b3c4": "1" * 40, "ce448bbe": "c" * 40, "origin/main": "d" * 40}
    monkeypatch.setattr(rt, "resolve", lambda rev: known.get(rev, ""))
    monkeypatch.setattr(
        rt,
        "git",
        lambda *a, **_k: "m" * 40 + "\n" if a[:2] == ("merge-base", "T") else "",
    )
    fixes = rt.target_base("2b3c4d5, fixes 1a2b3c4..2b3c4d5", "T")
    assert fixes == ("1" * 40, None)
    assert rt.target_base("2b3c4d5 against ce448bbe", "T") == ("c" * 40, None)
    assert rt.target_base("2b3c4d5 against main", "T") == ("m" * 40, "origin/main")
    assert rt.target_base("2b3c4d5 against gone", "T") == ("", None)
    # A release branch deleted after its release: the commit the work landed
    # on stands for it where the caller knows that commit (#986).
    landed = ("m" * 40, "origin/gone")
    assert rt.target_base("2b3c4d5 against gone", "T", landed="L") == landed
    assert rt.base_of("Round 1, against origin/gone.", "T") == ("", None)
    assert rt.base_of("Round 1, against origin/gone.", "T", landed="L") == landed


def test_records_read_only_the_named_items(monkeypatch, tmp_path):
    """Guards `--case`'s reach over every release tag: only the named work
    items' records are read, so reading all tags costs one listing a tag and
    a `git show` per named record, never one per record in the history."""
    rt = load_script("replay_targets")
    shown = []

    def git(*args, check=True):
        if args[0] == "ls-tree":
            return (
                "seal/specs/1791-a/rounds/round-1.md\n"
                "seal/specs/1792-b/rounds/round-1.md\n"
            )
        shown.append(args[1])
        return f"text of {args[1]}"

    monkeypatch.setattr(rt, "ROOT", str(tmp_path))
    monkeypatch.setattr(rt, "git", git)
    found = rt.records(["v1.0.0"], {"1791"})
    assert found == {
        ("1791-a", 1): "text of v1.0.0:seal/specs/1791-a/rounds/round-1.md"
    }
    assert shown == ["v1.0.0:seal/specs/1791-a/rounds/round-1.md"]


@pytest.mark.parametrize(
    ("script", "name", "items"),
    [
        ("replay_targets", "replay-1791382684-r2", {"1791382684"}),
        ("seed_defects", "seeded-279a580b", {"279a580b"}),
    ],
)
def test_a_named_case_is_read_at_every_release_tag(monkeypatch, script, name, items):
    """Guards that a committed case regenerates after the release that moved
    its records or commits out of the window `--list` reads: `--case` reads
    every release tag, for the named items alone. Before #964 both
    generators read the last two or three tags, and none of the eight
    committed replay and seeded cases was still on either list once 0.22.0
    was tagged, so `--case` exited 1 for each."""
    module = load_script(script)
    rt = module if script == "replay_targets" else module.rt
    calls = []
    monkeypatch.setattr(rt, "last_tags", lambda count=2: calls.append(count) or [])
    monkeypatch.setattr(
        module, "targets", lambda tags, only=None: calls.append(only) or ([], [])
    )
    monkeypatch.setattr(rt, "origin_url", lambda: "https://example.com/x/y.git")
    assert module.main(["--case", name]) == 1
    assert calls == [None, items]
    calls.clear()
    assert module.main(["--list"]) == 0
    assert calls[1] is None and calls[0] in (2, 3)


def test_a_seeded_case_is_looked_for_among_the_named_commits_alone(monkeypatch):
    """Guards what reading every release tag costs the seeded generator: a
    shipped commit `--case` does not name is skipped before any git call
    for it, so the whole history is listed and only the named commits are
    read. The wiring case above stubs `targets`, so only this one reaches
    the filter."""
    sd = load_script("seed_defects")
    monkeypatch.setattr(sd, "shipped", lambda _tags: ["aaaaaaaa1111", "bbbbbbbb2222"])
    monkeypatch.setattr(sd.rt, "git", lambda *_a, **_k: "")
    kept, left = sd.targets(["v1.0.0"], {"aaaaaaaa"})
    assert kept == []
    assert left == [("aaaaaaaa1111", "not a squashed pull request")]
    assert len(sd.targets(["v1.0.0"])[1]) == 2


def test_a_record_with_no_asked_paragraph_ends_the_spawn_at_the_report():
    """Guards the replay prompt of a labelled record, which carries no asked
    paragraph: the spawn ends at the report's path with nothing after it,
    and a table record's paragraph still follows that sentence after one
    space, as the four committed cases were written."""
    rt = load_script("replay_targets")
    t = {
        "item": "1-i",
        "n": 2,
        "branch": "b",
        "target": "t" * 40,
        "base": "a" * 40,
        "base_ref": None,
        "asked": "",
    }
    assert "and return its path.\n\nEND PROMPT" in rt.prompt(t)
    t["asked"] = "Round 2,\n  the verifying round."
    assert "and return its path. Round 2, the verifying round.\n\nEND" in rt.prompt(t)


def test_a_truth_pattern_holds_its_line_window_and_no_further():
    rt = load_script("replay_targets")
    """A truth reads a finding's `location:` line, the line within ±15 of
    the original's, and never a confirmation's or a table's coordinate."""
    pattern = re.compile(rt.truth_pattern("`docs/x.md:100`", "HEAD"), re.M)
    assert pattern.search("location: `docs/x.md:115`")
    assert pattern.search("location: `a.py:1`, `docs/x.md:85-90`")
    assert not pattern.search("location: `docs/x.md:116`")
    assert not pattern.search("location: `docs/x.md:1000`")
    assert not pattern.search("holds, at `docs/x.md:100`. read.")
    assert not pattern.search("| none | f | `docs/x.md:100` | g |")
    assert not pattern.search("Location: `docs/x.md:100`")


def test_a_truth_never_matches_a_coordinate_the_check_refuses(monkeypatch):
    """`chain_check.py` refuses a `path#unit` coordinate, so a truth that
    matched one would pass a warden for a record the pull request then
    fails. A Python truth reads its unit's lines within ±15 and never the
    unit's name after a `#`, and a truth with no lines reads the bare path
    or `path:<line>`, never `path#<anything>`."""
    rt = load_script("replay_targets")
    source = "x = 0\n\n\ndef f(a):\n    return a\n"
    monkeypatch.setattr(rt, "git", lambda *_a, **_k: source)
    for location in ("`a.py:5`", "`a.py#f`"):
        pattern = re.compile(rt.truth_pattern(location, "HEAD"), re.M)
        assert pattern.search("location: `a.py:5`"), location
        assert pattern.search("location: `b.md:1`, `a.py:4-5`"), location
        assert not pattern.search("location: `a.py:40`"), location
        assert not pattern.search("location: `a.py#f`"), location
        assert not pattern.search("location: `a.py#f:5`"), location
    bare = re.compile(rt.truth_pattern("`docs/x.md#unit`", "HEAD"), re.M)
    assert bare.search("location: `docs/x.md`")
    assert bare.search("location: `docs/x.md:7`")
    assert not bare.search("location: `docs/x.md#unit`")


# --- a truth a run recurred on, added through the generators (#971) ---------

RULE = "rule-warden-one-finding"
SHOUT_BODY = "`shout_twice` joins the two shouts with no space, against S2.\n"


def recurred_file(tmp_path, *entries):
    """The input file of added truths holding ENTRIES, and its path."""
    path = tmp_path / "recurred_truths.json"
    path.write_text(json.dumps(list(entries)), encoding="utf-8")
    return str(path)


def entry(**over):
    """One entry of the input file: a new truth of the rule case, unless
    OVER says otherwise."""
    base = {
        "case": RULE,
        "grader": "truth-no-case",
        "finding": "No case covers `shout_twice`.",
        "locations": ["tests/test_textutil.py"],
        "from": ["baseline rule-warden-one-finding 0 1"],
    }
    base.update(over)
    return base


def rule_truths(tmp_path, monkeypatch, *entries):
    """`{file name: text}` of the truth graders `rule_cases.py` writes for
    the warden's rule case with ENTRIES as its input file."""
    rc = load_script("rule_cases")
    monkeypatch.setattr(rc.rt, "TRUTHS", recurred_file(tmp_path, *entries))
    out = tmp_path / "out"
    assert rc.main(["--out", str(out)]) == 0
    graders = out / "warden" / RULE / "graders"
    return {p.name: p.read_text(encoding="utf-8") for p in graders.glob("truth-*.md")}


def truth_regex(name, text):
    return re.compile(
        ni.grader_from(f"graders/{name}", text)["config"]["pattern"], re.M
    )


def test_an_entry_adds_a_truth_its_case_is_written_with(tmp_path, monkeypatch):
    """Guards S6's added truth: an entry naming a new grader writes it beside
    the case's own truths, its body the entry's finding and its pattern
    `truth_pattern`'s for each location."""
    truths = rule_truths(tmp_path, monkeypatch, entry())
    assert sorted(truths) == ["truth-no-case.md", "truth-shout-twice.md"]
    text = truths["truth-no-case.md"]
    assert text.endswith("No case covers `shout_twice`.\n")
    found = truth_regex("truth-no-case.md", text)
    assert found.search("location: `tests/test_textutil.py`")
    assert not found.search("location: `src/textutil.py:8`")
    assert truths["truth-shout-twice.md"].endswith(SHOUT_BODY)


def test_an_entry_widens_a_truth_and_keeps_what_it_found(tmp_path, monkeypatch):
    """Guards S6's widened truth: an entry that widens a grader adds its
    locations as alternatives, the grader still finds what it found, and its
    body stays the defect it was written for."""
    widen = entry(grader="truth-shout-twice", widens=True)
    truths = rule_truths(tmp_path, monkeypatch, widen)
    assert sorted(truths) == ["truth-shout-twice.md"]
    text = truths["truth-shout-twice.md"]
    assert text.endswith(SHOUT_BODY)
    found = truth_regex("truth-shout-twice.md", text)
    assert found.search("location: `src/textutil.py:8`")
    assert found.search("location: tests/test_textutil.py")
    assert not found.search("location: `src/other.py:8`")


@pytest.mark.parametrize(
    "over, named",
    [
        ({"case": "replay-0-r1"}, "replay-0-r1"),
        ({"grader": "truth-9", "widens": True}, "truth-9"),
        ({"grader": "truth-shout-twice"}, "truth-shout-twice"),
        ({"locations": ["src/textutil.py#shout"]}, "src/textutil.py#shout"),
        ({"locations": ["no path here"]}, "no path here"),
        ({"locations": []}, "names no location"),
        ({"window": "2"}, "is no count"),
        ({"locations": ["src/x.py:100-10"]}, "src/x.py:100-10"),
    ],
    ids=[
        "a-case-no-generator-writes",
        "a-widening-of-a-truth-the-case-lacks",
        "a-new-truth-the-case-already-has",
        "a-coordinate-the-grammar-refuses",
        "no-coordinate",
        "no-location",
        "a-window-that-is-no-count",
        "a-range-that-ends-before-it-starts",
    ],
)
def test_an_entry_the_case_cannot_take_stops_the_generator(
    tmp_path, monkeypatch, over, named
):
    """Guards S6's stale entry: an entry naming a case the suite does not
    hold, a truth to widen that the case lacks, a new truth whose name the
    case already has, a location outside `path`, `path:line` and
    `path:first-last`, or no location at all, which would be a truth every
    row matches, stops the generator with exit 1, naming it, so the file
    cannot go stale silently."""
    with pytest.raises(SystemExit) as stopped:
        rule_truths(tmp_path, monkeypatch, entry(**over))
    assert named in str(stopped.value.code)


def test_an_entry_range_is_read_to_its_last_line(tmp_path, monkeypatch):
    """Guards #971 round 1 finding 2: a `path:first-last` location credits a
    row anywhere in the range, its last line too, and nothing past the
    window after it."""
    truths = rule_truths(tmp_path, monkeypatch, entry(locations=["src/x.py:10-100"]))
    found = truth_regex("truth-no-case.md", truths["truth-no-case.md"])
    assert found.search("location: `src/x.py:60`")
    assert found.search("location: `src/x.py:115`")
    assert not found.search("location: `src/x.py:116`")


def test_an_entry_window_narrows_the_lines_its_truth_accepts(tmp_path, monkeypatch):
    """Guards #971 round 1 finding 1's repair: an entry's `window` replaces
    the ±15 lines around each of its locations, for a line and for a range."""
    narrow = entry(locations=["src/x.py:10", "src/y.py:20-22"], window=2)
    truths = rule_truths(tmp_path, monkeypatch, narrow)
    found = truth_regex("truth-no-case.md", truths["truth-no-case.md"])
    for line in ("src/x.py:8", "src/x.py:12", "src/y.py:18", "src/y.py:24"):
        assert found.search(f"location: `{line}`"), line
    for line in ("src/x.py:7", "src/x.py:13", "src/y.py:17", "src/y.py:25"):
        assert not found.search(f"location: `{line}`"), line


# An alternative of a generated truth's pattern: an escaped path and the
# line list it accepts, or a bare escaped path.
OPTION = re.compile(
    r"((?:[\w-]|\\[./-])+):\(\?:([\d|]+)\)\(\?!\\d\)|((?:[\w-]|\\[./-])+)\(\?!\["
)


def test_no_two_truths_of_a_warden_case_accept_one_location():
    """Guards #971 round 1 finding 1: a `location:` line one truth of a
    committed warden case accepts is accepted by no other truth of that
    case, so one finding is never counted as two. Every line each
    generated alternative lists is tried against every other truth."""
    root = os.path.join(ROOT, "evals", "behaviour", "warden")
    shared = []
    for case in sorted(os.listdir(root)):
        graders = os.path.join(root, case, "graders")
        truths = {}
        for name in sorted(os.listdir(graders)):
            if name.startswith("truth-"):
                with open(os.path.join(graders, name), encoding="utf-8") as f:
                    truths[name] = truth_regex(name, f.read())
        for name, found in truths.items():
            for m in OPTION.finditer(found.pattern):
                path = (m[1] or m[3]).replace("\\", "")
                for n in m[2].split("|") if m[2] else [None]:
                    row = f"location: `{path}:{n}`" if n else f"location: `{path}`"
                    others = [
                        o for o, g in truths.items() if o != name and g.search(row)
                    ]
                    if others:
                        shared.append((case, name, row, others))
    assert not shared, shared[:3]


def test_the_replay_and_seeded_generators_read_the_entries_too(tmp_path, monkeypatch):
    """Guards S6 for the other two generators: each writes an entry's truth
    for the case it names, beside its own."""
    rt = load_script("replay_targets")
    sd = load_script("seed_defects")
    replay = "replay-1791382684-r2"
    seeded = "seeded-279a580b"
    path = recurred_file(
        tmp_path, entry(case=replay, locations=["x.py"]), entry(case=seeded)
    )
    monkeypatch.setattr(rt, "TRUTHS", path)
    monkeypatch.setattr(sd.rt, "TRUTHS", path)
    t = {
        "item": "1791382684-every-reader-and-record-is-inventoried",
        "n": 2,
        "target": "HEAD",
        "truths": [{"k": 1, "finding": "f", "pattern": TRUTH}],
    }
    assert [name for name, _ in rt.graders(t) if name.startswith("truth-")] == [
        "truth-1.md",
        "truth-no-case.md",
    ]
    s = {
        "commit": "279a580b" + "0" * 32,
        "item": "1791384154-a-records-finding-closes-once-at-the-runs-end",
        "n": 1,
        "target": "HEAD",
        "truths": [],
        "path": "a.py",
        "unit": "f",
        "old": "a == b",
        "new": "a != b",
        "pattern": TRUTH,
    }
    assert [name for name, _ in sd.graders(s) if name.startswith("truth-")] == [
        "truth-seeded.md",
        "truth-no-case.md",
    ]


def test_a_seed_lands_on_a_code_token_and_never_in_a_string():
    sd = load_script("seed_defects")
    source = 'def f(a):\n    """a == b"""\n    return a == 1\n'
    tokens = sd.code_tokens(source)
    assert (3, "==") in tokens
    assert (2, "==") not in tokens


# --- a seeded case is the tree its work item's round 1 reviewed (#986) -------

SEEDED_ITEM = "1790000001-a-shipped-item"
SEEDED_BRANCH = "feat/1-a-shipped-item"
# Two units 38 lines apart, so the window of round 1's finding at line 2
# reaches the first and not the second.
SEEDED_SOURCE = (
    "def f(a):\n    return a == 1\n" + "\n" * 34 + "\n\ndef g(b):\n    return b != 2\n"
)


def seeded_round_1(target):
    """Round 1 of the shipped item, written before the `evidence:` row: its
    TARGET against `main`, a branch the clone has no ref for, a finding at
    `a.py:2` closed fixed and one at `b.py:1` rejected."""
    return re.sub(
        r"^evidence: .*\n",
        "",
        LABELLED_ROUND_1.replace("# i ", f"# {SEEDED_ITEM} ")
        .replace("1a2b3c4 against main", f"{target} against main")
        .replace("`src/a.py:12`, `docs/a.md`", "`a.py:2`")
        .replace("`src/b.py:3`", "`b.py:1`"),
        flags=re.M,
    )


def shipped_item(tmp_path, monkeypatch, first=seeded_round_1, second=True, crlf=False):
    """A repository that shipped one work item, with `rt` reading it: a base
    holding the check of a grammar with no `evidence:` row, a branch of a
    code commit and a records commit, and the branch squashed onto the base
    with round 1, FIRST of the target, and round 2 where SECOND is set,
    added as a shipped squash commit holds them. No `main` ref but the
    local branch exists, so the squash's first parent stands for the base
    round 1 names. Every file is written with LF line ends and stored as
    written, `a.py` with CRLF where CRLF is set. `({name: commit}, its
    path)`."""
    rt = load_script("seed_defects").rt
    repo = tmp_path / "shipped"
    repo.mkdir()
    who = ["-c", "user.name=x", "-c", "user.email=x@example.com"]
    # A fixed date, so a commit the scaffold amends today cannot match it.
    dated = dict(os.environ, GIT_COMMITTER_DATE="2026-01-01T00:00:00+00:00")

    def git(*args):
        return subprocess.run(
            ["git", "-C", str(repo), *who, *args],
            check=True,
            capture_output=True,
            encoding="utf-8",
            env=dated,
        ).stdout.strip()

    def put(rel, text, newline="\n"):
        path = repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline=newline)

    git("init", "-q", "-b", "main")
    git("config", "uploadpack.allowAnySHA1InWant", "true")
    git("config", "core.autocrlf", "false")
    for rel in rt.CHECK_FILES:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            text = f.read()
        if rel == "docs/the-review-record.md":
            text = re.sub(r"^\| `evidence:` \|.*\n", "", text, flags=re.M)
        put(rel, text)
    put("b.py", "x = 1\n")
    git("add", "-A")
    git("commit", "-qm", "base")
    commits = {"base": git("rev-parse", "HEAD")}
    git("checkout", "-q", "-b", SEEDED_BRANCH)
    spec = f"seal/specs/{SEEDED_ITEM}"
    put(
        f"{spec}/routing.md",
        f"| Axis | Answer |\n|---|---|\n| Branch | {SEEDED_BRANCH} |\n",
    )
    put("a.py", SEEDED_SOURCE, newline="\r\n" if crlf else "\n")
    git("add", "-A")
    git("commit", "-qm", "feat: f and g")
    commits["code"] = git("rev-parse", "HEAD")
    put(
        f"{spec}/plan.md", f"| Phase | Status |\n|---|---|\n| 1 | {commits['code']} |\n"
    )
    git("add", "-A")
    git("commit", "-qm", "record: phase 1")
    commits["target"] = git("rev-parse", "HEAD")
    git("checkout", "-q", "main")
    git("merge", "-q", "--squash", SEEDED_BRANCH)
    put(f"{spec}/rounds/round-1.md", first(commits["target"]))
    if second:
        put(f"{spec}/rounds/round-2.md", LABELLED_ROUND_2)
    git("add", "-A")
    git("commit", "-qm", "feat: a shipped item (#1)")
    commits["squash"] = git("rev-parse", "HEAD")
    monkeypatch.setattr(rt, "ROOT", str(repo))
    return commits, repo


def test_a_seeded_case_is_built_on_its_round_1_target(tmp_path, monkeypatch):
    """Guards S8: a seeded case is the tree the shipped item's round 1
    reviewed, not the squash commit. Its scaffold fetches round 1's target
    and base, removes no file, and after the amend expires the reflog,
    removes `FETCH_HEAD` and prunes what nothing reaches. Its prompt names
    HEAD and round 1's base, and no commit of the tree without the seed."""
    sd = load_script("seed_defects")
    commits, _repo = shipped_item(tmp_path, monkeypatch)
    t, why = sd.target_of(commits["squash"])
    assert why == "", why
    assert (t["target"], t["base"], t["base_ref"], t["branch"]) == (
        commits["target"],
        commits["base"],
        "origin/main",
        SEEDED_BRANCH,
    )
    lines = sd.scaffold(t, "https://example.com/x/y.git").split("\n")
    assert lines[:6] == [
        "git init -q .",
        "git remote add origin https://example.com/x/y.git",
        f"git fetch -q --no-tags origin {commits['target']}",
        f"git fetch -q --no-tags origin {commits['base']}",
        f"git update-ref refs/remotes/origin/main {commits['base']}",
        f"git checkout -q -b {SEEDED_BRANCH} {commits['target']}",
    ]
    assert lines[-3:] == [
        "git reflog expire --expire=now --all",
        "rm -f .git/FETCH_HEAD",
        "git gc -q --prune=now",
    ]
    assert not any(line.startswith("git rm") for line in lines), lines
    prompt = sd.prompt(t)
    assert f"on branch `{SEEDED_BRANCH}` at HEAD" in prompt
    assert f"the base is `{commits['base']}`" in prompt
    assert commits["target"] not in prompt and commits["squash"] not in prompt


def test_a_seeded_case_counts_round_1s_confirmed_fixes_as_truths(tmp_path, monkeypatch):
    """Guards S9: at round 1's target the tree holds the defects round 1
    found, so each finding round 1 closed fixed that round 2 confirmed is a
    `truth-` grader beside `truth-seeded`, and the seed lands on no line a
    truth's window accepts: `f`'s line is in finding 1's window, so the
    seed goes to `g`."""
    sd = load_script("seed_defects")
    commits, _repo = shipped_item(tmp_path, monkeypatch)
    t, _why = sd.target_of(commits["squash"])
    assert (t["path"], t["line"], t["new"]) == ("a.py", 40, "    return b == 2")
    truths = {
        name: truth_regex(name, text)
        for name, text in sd.graders(t)
        if name.startswith("truth-")
    }
    assert sorted(truths) == ["truth-1.md", "truth-seeded.md"]
    assert truths["truth-1.md"].search("location: `a.py:2`")
    for n in range(1, 60):
        row = f"location: `a.py:{n}`"
        assert sum(bool(g.search(row)) for g in truths.values()) <= 1, row


def two_near_fixes(target):
    """Round 1 with both findings closed fixed, three lines apart."""
    return (
        seeded_round_1(target)
        .replace("`b.py:1`", "`a.py:5`")
        .replace("verdict: rejected", "verdict: fixed abc1234")
    )


def test_a_seeded_case_needs_no_round_after_round_1(tmp_path, monkeypatch):
    """Guards what the seeded generator asks of a round that the replay
    generator does not: a work item whose round 1 no round followed still
    gives a case, its one truth the seed. A replay of that round has
    nothing to confirm a fix and is left out."""
    sd = load_script("seed_defects")
    commits, _repo = shipped_item(tmp_path, monkeypatch, second=False)
    t, why = sd.target_of(commits["squash"])
    assert why == "", why
    assert t["truths"] == []
    names = [name for name, _ in sd.graders(t) if name.startswith("truth-")]
    assert names == ["truth-seeded.md"]


def test_a_shipped_commit_whose_round_1_truths_share_a_line_is_left_out(
    tmp_path, monkeypatch
):
    """Guards S9's rule that one finding is never counted as two: where two
    findings round 1 fixed lie so near that both truths accept one
    `location:` line, the generator leaves the commit out, naming the line,
    rather than writing a case the suite then refuses (`questions.md` Q3
    of #986)."""
    sd = load_script("seed_defects")
    commits, _repo = shipped_item(tmp_path, monkeypatch, first=two_near_fixes)
    t, why = sd.target_of(commits["squash"])
    assert t is None
    assert why == "two of round 1's truths accept `location: `a.py:1``", why


def test_the_seeded_scaffold_leaves_round_1s_tree_and_no_copy_of_it(
    tmp_path, monkeypatch
):
    """Guards S10 on a repository a case can fetch for nothing: the clone
    holds no round record, the commit the plan's Status cell names
    resolves, the target's own commit does not, and no file under `.git`
    outside its objects names it. The amended commit keeps the target's
    committer and date, so no field of the log marks the seed's commit, and
    the clone keeps no remote (`seed_defects.py`'s module docstring says
    what that closes and what it leaves), while the base ref round 1 names
    still resolves."""
    sd = load_script("seed_defects")
    commits, repo = shipped_item(tmp_path, monkeypatch)
    t, _why = sd.target_of(commits["squash"])
    clone = tmp_path / "clone"
    clone.mkdir()
    (clone / "scaffold.sh").write_text(
        # A URL, as `replay_targets.py#origin_url` gives the generator: a
        # native Windows path in an unquoted `sh` word loses its backslashes.
        "set -eu\n" + sd.scaffold(t, repo.as_uri()) + "\n",
        encoding="utf-8",
    )
    run = subprocess.run(
        ["sh", "scaffold.sh"], cwd=clone, capture_output=True, encoding="utf-8"
    )
    assert run.returncode == 0, run.stderr
    assert not (clone / "seal" / "specs" / SEEDED_ITEM / "rounds").exists()
    assert (clone / "a.py").read_text(encoding="utf-8").split("\n")[39] == (
        "    return b == 2"
    )

    def exists(rev):
        return subprocess.run(
            ["git", "-C", str(clone), "cat-file", "-e", f"{rev}^{{commit}}"],
            capture_output=True,
        ).returncode

    assert exists(commits["code"]) == 0
    assert exists(commits["target"]) != 0
    named = []
    for directory, dirs, files in os.walk(clone / ".git"):
        if "objects" in dirs:
            dirs.remove("objects")
        for name in files:
            path = os.path.join(directory, name)
            with open(path, "rb") as f:
                if commits["target"].encode() in f.read():
                    named.append(path)
    assert named == [], named

    def log(where, rev):
        return subprocess.run(
            ["git", "-C", str(where), "log", "-1", "--format=%cn %ce %cI", rev],
            capture_output=True,
            encoding="utf-8",
        ).stdout

    assert log(clone, "HEAD") == log(repo, commits["target"]) != ""
    remotes = subprocess.run(
        ["git", "-C", str(clone), "remote"], capture_output=True, encoding="utf-8"
    )
    assert (remotes.returncode, remotes.stdout) == (0, "")
    assert exists("origin/main") == 0


@pytest.mark.parametrize(
    ("crlf", "autocrlf"),
    [(False, "true"), (True, "false")],
    ids=["an-lf-file-checked-out-with-crlf", "a-file-stored-with-crlf"],
)
def test_the_seeded_scaffold_mutates_a_line_that_ends_with_crlf(
    tmp_path, monkeypatch, crlf, autocrlf
):
    """Guards the scaffold's own check of the line it mutates, on every
    platform. Git for Windows checks a file out with CRLF line ends
    (`core.autocrlf`), so the line read from the checkout carries a carriage
    return, which `tests` run 39691387210 met on a Windows split; a file
    stored with CRLF carries one in the commit too. The carriage return is
    the line's end, not its text: the seed is found and written without it,
    and the mutated line keeps it."""
    sd = load_script("seed_defects")
    commits, repo = shipped_item(tmp_path, monkeypatch, crlf=crlf)
    t, why = sd.target_of(commits["squash"])
    assert why == "", why
    assert (t["line"], t["old"], t["new"]) == (
        40,
        "    return b != 2",
        "    return b == 2",
    )
    clone = tmp_path / "clone"
    clone.mkdir()
    (clone / "scaffold.sh").write_text(
        "set -eu\n" + sd.scaffold(t, repo.as_uri()) + "\n", encoding="utf-8"
    )
    env = dict(
        os.environ,
        GIT_CONFIG_COUNT="1",
        GIT_CONFIG_KEY_0="core.autocrlf",
        GIT_CONFIG_VALUE_0=autocrlf,
    )
    run = subprocess.run(
        ["sh", "scaffold.sh"], cwd=clone, capture_output=True, encoding="utf-8", env=env
    )
    assert run.returncode == 0, run.stderr
    with open(clone / "a.py", encoding="utf-8", newline="") as f:
        assert f.read().split("\n")[39] == "    return b == 2\r"
