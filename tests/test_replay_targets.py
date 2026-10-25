"""`evals/scripts/replay_targets.py`, one class per function.

The replay generator writes a behaviour case from a review round this
repository already ran: the target the round reviewed, and a `truth-`
grader for each finding the next round confirmed fixed. These cases pin
which findings count as truths, how a labelled record is read by the
grammar of the commit that wrote it, and the line window a truth accepts.
`test_a_named_case_is_read_at_every_release_tag` holds the seeded
generator too, because both read the release tags through this module.

#942's phase 6 placed these cases from
`tests/test_a_rewritten_definition_proved_non_inferior.py`.
"""

import importlib.util
import os
import re
import subprocess

import pytest
from conftest import census_case

TARGET = "evals/scripts/replay_targets.py"

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))


def load_script(name):
    path = os.path.join(ROOT, "evals", "scripts", f"{name}.py")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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


class Test_confirmed:
    def test_accepts_a_fixed_finding_the_next_round_confirmed(self):
        """Guards the replay set's ground truth: a finding of the old table
        closed fixed and named closed by the next round's closing row, and no
        other."""
        rt = load_script("replay_targets")
        nxt = (
            "| \U0001f7e2 | round 1's finding 2 is closed — x | `a.md:3` | confirmed | read |\n"
            "| \U0001f7e2 | round 1's \U0001f7e1 4 is closed — y | `a.md:9` | confirmed | read |\n"
            "| \U0001f7e2 | round 2's finding 3 is closed — z | `a.md:9` | confirmed | read |\n"
            "| \U0001f7e1 5 | round 1's finding 5 is closed | `a.md:9` | open | read |\n"
        )
        assert rt.confirmed(nxt, 1) == {2, 4}

    def test_a_truth_of_a_labelled_record_is_a_fixed_finding_the_next_round_confirms(
        self,
    ):
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
        assert not rt.labelled(
            "| \U0001f7e2 | round 1's finding 2 is closed | `a:1` | confirmed |"
        )
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

    def test_refuses_a_labelled_record_the_check_refuses(self):
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


class Test_truth_pattern:
    def test_accepts_a_location_inside_its_line_window_and_no_further(self):
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

    def test_refuses_a_coordinate_the_check_refuses(self, monkeypatch):
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


class Test_module:
    def test_a_labelled_record_is_read_by_the_grammar_of_the_commit_that_wrote_it(
        self, tmp_path, monkeypatch
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
        row = next(
            ln + "\n" for ln in doc.splitlines() if ln.startswith("| `evidence:` |")
        )
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

    def test_a_labelled_record_is_read_by_the_reader_that_judged_it(self, monkeypatch):
        """S10 of #1012: a record at a release tag can carry a template
        comment, and the reader of the commit that wrote it hid the comment
        while this tree's reads it as text. The record's lines are read by
        the reader that judged it, so a `location:` line inside the comment
        is no finding's location. Seen red against the generator that judged
        with the commit's reader and read with this tree's: it took the
        comment's line."""
        rt = load_script("replay_targets")
        check, reader = rt.record_reader()

        class Judged:
            """This tree's reader as a reader before #1012 read a record: a
            comment's lines are blank, and none is refused."""

            def __getattr__(self, name):
                return getattr(reader, name)

            def readable(self, text):
                lines, inside = reader.readable(text), False
                for i, line in enumerate(lines):
                    opens = line.lstrip().startswith("<!--")
                    if inside or opens:
                        inside = "-->" not in line
                        lines[i] = ""
                return lines

            def comment_lines(self, lines):
                return []

        monkeypatch.setattr(rt, "checks_at", lambda at: (check, Judged()))
        text = LABELLED_ROUND_1.replace(
            "severity: must\n",
            "<!-- guidance copied from the template\nlocation: `src/z.py:1`\n-->\n"
            "severity: must\n",
        )
        rel = "seal/specs/i/rounds/round-1.md"
        read, why = rt.labelled_round(text, rel, 1, at="abc1234")
        assert why == ""
        assert read["findings"] == [
            (1, "a fixed defect", "`src/a.py:12`, `docs/a.md`", True),
            (2, "a finding that does not hold", "`src/b.py:3`", False),
        ]

    def test_targets_reads_the_next_round_by_the_commit_that_wrote_it(
        self, monkeypatch
    ):
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

    def test_a_labelled_target_names_its_base(self, monkeypatch):
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

    def test_records_read_only_the_named_items(self, monkeypatch, tmp_path):
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
    def test_a_named_case_is_read_at_every_release_tag(
        self, monkeypatch, script, name, items
    ):
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

    def test_a_record_with_no_asked_paragraph_ends_the_spawn_at_the_report(self):
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
        assert "and return its path. Round 2, the verifying round.\n\nEND" in rt.prompt(
            t
        )


test_census = census_case(TARGET)
