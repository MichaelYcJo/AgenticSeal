"""`.github/scripts/release_seal.py`, one class per function.

The release seal is drawn and attached at publish time (#718). The tag push
publishes the note; a second job then runs the suite at the tag, draws one
seal for the release, attaches it, and puts it where the note's glance table
stood. Any failure leaves the note as it was.

Since #1009 (work item 1792624592) the seal is the terminal stamp's disc:
`release_seal.py#draw` paints each cell of `seal_stamp.py#build` as one
square block of pixels in that cell's colour. The pixel cases import Pillow,
which `bin/test` installs, inside the case. Every other case runs a
stand-in for `draw`, or the real `draw` with Pillow blocked or stood in for,
and imports nothing beyond the standard library.

**The cells here are not read through the code under test.** The pixel
cases load `seal_stamp.py` by path under a name of their own, so a draw
that kept a copy of the chart or the colours cannot agree with itself.

#942's phase 6 placed these cases from
`tests/test_the_release_seal_is_drawn.py`, which keeps the cases that read
the publishing workflow and the documents.
"""

import json
import os
import subprocess
import sys
import types

import pytest
from conftest import census_case, mark_root
from conftest import load_module as load

TARGET = ".github/scripts/release_seal.py"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, ".github", "scripts", "release_seal.py")
STAMP_SCRIPT = os.path.join(ROOT, "skills", "verify", "scripts", "seal_stamp.py")

# A release's rows in the shape `release_rows` returns. The version is the
# illustrative one `tests/test_release_hygiene.py` exempts; the rest are
# neutral numbers in the widths a real release has.
ROWS = [
    ("SEALED", "v1.2.3"),
    ("tag", "aaa11111"),
    ("", "main"),
    ("PRs", "10 merged"),
    ("issues", "11 closed"),
    ("suite", "7003 passed, 66 skipped"),
    ("items", "10 . 27 rounds"),
    ("capped", "6 of 10"),
    ("deferred", "13 issues"),
]


def seal():
    return load(SCRIPT, "specseal_release_seal_for_tests")


def stamp(name):
    """`seal_stamp.py` loaded by path under `name`, apart from the module
    `release_seal.py` loads, so its cells are not read through the code
    under test."""
    return load(STAMP_SCRIPT, name)


def blocks(png, px, w, cell):
    """The cells whose block of `cell` by `cell` pixels in the PNG at `png`
    is not every pixel `px(x, y)` with alpha 255, or alpha 0 where
    `px(x, y)` is None, as `(x, y, two of the block's pixels)`. An empty
    list is a PNG that is exactly the cells."""
    from PIL import Image

    pixels = Image.open(png).load()
    wrong = []
    for y in range(w):
        for x in range(w):
            colour = px(x, y)
            block = {
                pixels[u, v]
                for u in range(x * cell, (x + 1) * cell)
                for v in range(y * cell, (y + 1) * cell)
            }
            if colour is None:
                held = all(pixel[3] == 0 for pixel in block)
            else:
                held = block == {(*colour, 255)}
            if not held:
                wrong.append((x, y, sorted(block)[:2]))
    return wrong


SUITE_KEY = "seal-1234567890"


def recorded(tmp_path, *sessions, key=SUITE_KEY, extra=""):
    """A records directory under `tmp_path` holding one file per session,
    each a `session` line carrying `key`, a `test` line per report counted —
    `sessions` are dicts of category to count — and an `end` line with
    nothing stopped. `extra` is written as it is after the last session's
    `test` lines. Returns the directory."""
    directory = tmp_path / "records"
    directory.mkdir(exist_ok=True)
    for n, counts in enumerate(sessions):
        lines = [{"kind": "session", "key": key, "pid": n, "rootdir": str(tmp_path)}]
        for category, count in counts.items():
            outcome = "passed" if category == "passed" else "failed"
            lines += [
                {
                    "kind": "test",
                    "nodeid": f"tests/test_x.py::t{n}_{category}_{i}",
                    "when": "call",
                    "outcome": outcome,
                    "path": str(tmp_path / "tests" / "test_x.py"),
                    "category": category,
                }
                for i in range(count)
            ]
        body = "".join(json.dumps(line) + "\n" for line in lines)
        if n == len(sessions) - 1:
            body += extra
        end = {"kind": "end", "exitstatus": 0, "unplaced": 0, "stopped": []}
        body += json.dumps(end) + "\n"
        (directory / f"{key}-{n}.jsonl").write_text(body, encoding="utf-8")
    return str(directory)


ROUTING = """| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Branch | {branch} |
"""
ROUND = """# round {n}

target: abc1234 against base

## Findings

{findings}
## Probes
"""
# The table the old generator's records carried, which the check's reader
# refuses.
OLD_ROUND = """# round {n}

## Verdicts

| # | Verdict | Grounds |
|---|---|---|
| 1 | deferred #12 | why |
"""


def finding(i, verdict):
    """One finding of `templates/sdd-round.md`'s shape, at `verdict`."""
    return (
        f"### {i}. a finding\n\nseverity: should\nlocation: `f.py:{i}`\n"
        f"evidence: read `f.py:{i}`\nverdict: {verdict}\n\nwhy\n\nanswer: \n\n"
    )


def tree(tmp_path, branch="feat/12-an-item", verdicts=()):
    """A repository root holding one work item that declares `branch`, with
    one round record per entry of `verdicts`, each a list of `verdict:`
    values, one finding each."""
    item = mark_root(tmp_path / "seal") / "threads" / "1700000000-an-item"
    (item / "trail" / "rounds").mkdir(parents=True)
    (item / "routing.md").write_text(ROUTING.format(branch=branch), encoding="utf-8")
    for n, values in enumerate(verdicts, 1):
        found = "".join(finding(i, value) for i, value in enumerate(values, 1))
        (item / "trail" / "rounds" / f"round-{n}.md").write_text(
            ROUND.format(n=n, findings=found), encoding="utf-8"
        )
    return str(tmp_path)


def pr(number, branch, *labels):
    return {
        "number": number,
        "headRefName": branch,
        "labels": [{"name": name} for name in labels],
    }


REPO = "example/repo"
TAG = "v1.2.3"
SHA = "aaa11111bbbbccccddddeeeeffff000011112222"
PUBLISHER = os.path.join(ROOT, ".github", "scripts", "publish_release_note.py")
OWNER = REPO.split("/")[0]
SECTION = "- **A thing that changed.** And what it changes for a reader."


def pull(number, branch, title, body="", *labels, login=OWNER):
    return {
        "number": number,
        "title": title,
        "body": body,
        "author": {"login": login, "is_bot": False},
        "headRefName": branch,
        "labels": [{"name": name} for name in labels],
    }


PULLS = [
    pull(9, "chore/the-fragments", "chore: release 1.2.3 — the gathering"),
    pull(10, "feat/12-an-item", "feat: a thing", "Closes #12", "chain: capped"),
    pull(11, "fix/13-another", "fix: another thing", "Closes #13", login="someone"),
]


class GitHub:
    """`gh` and `git` as the seal calls them: every call recorded in order,
    the note served from `body`, and any verb in `fails` answered with the
    refusal `main` turns into today's note."""

    def __init__(self, mod, body, fails=()):
        self.mod, self.body, self.fails, self.calls = mod, body, set(fails), []

    def gh(self, *args):
        self.calls.append(args)
        verb = args[1] if args[0] == "release" else args[0]
        if verb in self.fails:
            raise self.mod.Refused(f"gh {' '.join(args[:2])} failed: HTTP 502")
        if args[:2] == ("release", "view"):
            import json

            return json.dumps({"body": self.body})
        return ""

    def writes(self, verb):
        return [a for a in self.calls if a[:2] == ("release", verb)]


def note(pulls=PULLS):
    """The note `publish_release_note.release_body` publishes for `pulls`."""
    publisher = load(PUBLISHER, "publish_release_note_for_the_seal")
    return publisher.release_body(SECTION, pulls, OWNER, REPO, TAG)


# The width the stand-in for `draw` answers. The real draw never answers
# it, so a note carrying it took its width from `draw`'s answer.
DRAWN_WIDTH = 123


def drawn(png):
    """`draw` as the publishing cases meet it: it writes a PNG's eight-byte
    signature at `png` and answers `DRAWN_WIDTH`, with no Pillow."""
    with open(png, "wb") as handle:
        handle.write(b"\x89PNG\r\n\x1a\n")
    return DRAWN_WIDTH


def pillow_that_cannot_save():
    """A stand-in for the `PIL` package whose image takes every block and
    whose save raises what a full disk raises, so the case reaches the save
    with no Pillow installed."""

    class Image:
        def paste(self, colour, box):
            pass

        def save(self, path, kind):
            raise OSError(28, "No space left on device")

    pil = types.ModuleType("PIL")
    pil.Image = types.SimpleNamespace(new=lambda mode, size, colour: Image())
    return pil


def wired(
    monkeypatch, tmp_path, body=None, fails=(), pulls=PULLS, stand_in=True, **env
):
    """The seal with a fixture suite, a fixture tree, no route to GitHub,
    and `drawn` standing in for `draw`, or the real `draw` where `stand_in`
    is False."""
    mod = seal()
    hub = GitHub(mod, note(pulls) if body is None else body, fails)
    if stand_in:
        monkeypatch.setattr(mod, "draw", drawn)
    monkeypatch.setattr(mod, "gh", hub.gh)
    monkeypatch.setattr(mod, "tagged", lambda tag: SHA)
    monkeypatch.setattr(mod, "ROOT", tree(tmp_path, verdicts=[["deferred #12"]]))
    publisher = mod.publisher()
    monkeypatch.setattr(
        publisher,
        "merged_pulls",
        lambda repo, version: None if pulls is None else pulls,
    )
    defaults = {"TAG": TAG, "REPO": REPO, "SUITE_OUTCOME": "success"}
    defaults.update(env)
    if "SUITE_RECORDS" not in defaults:
        defaults["SUITE_RECORDS"] = recorded(tmp_path, {"passed": 7003, "skipped": 66})
    defaults.setdefault("SUITE_KEY", SUITE_KEY)
    for key in ("DRY_RUN", "SEAL_PNG"):
        monkeypatch.delenv(key, raising=False)
    for key, value in defaults.items():
        monkeypatch.setenv(key, value)
    return mod, hub


# What each failure's reason says, so a case that stopped at an EARLIER
# guard than the one it is named for fails rather than passing on the wrong
# reason.
REASONS = {
    "the suite step failed": "ended failure",
    "no record carries the key": "the suite's counts cannot be read: no record under",
    "a line of the record did not parse": "did not parse as the recorder's",
    "a session of the suite stopped part-way": "sessions stopped part-way",
    "the suite counts a failure": "did not pass: 1 failed and 0 errors",
    "the suite counts an error": "did not pass: 0 failed and 1 errors",
    "Pillow is not installed": "Pillow is not installed or will not import",
    "the stamp's module will not load": (
        "the stamp's module skills/verify/scripts/seal_stamp.py would not load "
        "(ImportError: no stamp)"
    ),
    "the PNG cannot be saved": "could not be written",
    "gh pr list fails": "gh pr list could not list",
    "gh release view fails": "gh release view failed",
    "gh release upload fails": "gh release upload failed",
    "the glance table is not there": "not in the note exactly once",
    "the glance table is there twice": "not in the note exactly once",
    "gh release edit fails": "gh release edit failed",
    "a module will not load": "ImportError: no publisher",
}
# The failures `draw` raises itself, which the case meets with the real
# `draw` rather than its stand-in.
REASONS_OF_THE_DRAW = (
    "Pillow is not installed",
    "the stamp's module will not load",
    "the PNG cannot be saved",
)


class Test_release_rows:
    def test_accepts_the_fixed_set_of_rows_in_order_and_fits_the_panel(self):
        """S8. `release_rows` returns the fixed label set in order, the tag's
        continuation carrying `main`. Every label fits the eight-wide label
        column a dry run prints the rows in -- `deferred` is exactly eight,
        which is the only reason the column looks set by it -- and no value is
        wider than the
        release's own `PANEL_VALUE_WIDTH`, 23. A count of 0 still draws its row.

        The two widths were one number until #832: `broad_gate`'s became 41 for
        the open layout's 80 columns (S5a), and the release's rows are out of
        that work item's scope, so the release keeps 23 and no longer follows
        the gate's. The gate's width is `seal_stamp.py`'s since #975."""
        mod = seal()
        rows = mod.release_rows(
            "1.2.3", "aaa11111bbbb", 10, 0, (7003, 66), (10, 27, 6, 13)
        )
        assert rows == [*ROWS[:4], ("issues", "0 closed"), *ROWS[5:]], rows
        assert all(len(label) <= 8 for label in mod.LABELS), mod.LABELS
        assert [label for label, _ in rows if label] == list(mod.LABELS)
        width = load(STAMP_SCRIPT, "seal_stamp_for_the_release_rows").PANEL_VALUE_WIDTH
        assert mod.PANEL_VALUE_WIDTH == 23 < width, (mod.PANEL_VALUE_WIDTH, width)
        assert all(len(value) <= mod.PANEL_VALUE_WIDTH for _, value in rows), rows

    def test_a_suite_wider_than_the_value_column_moves_skipped_to_its_own_row(self):
        """S8, `questions.md` Q6. `7003 passed, 66 skipped` is exactly 23; a
        five-digit suite is 25, so `S skipped` moves under `P passed` on a
        continuation row rather than being cut at the frame. Seen red against
        the rows that wrote the value whole."""
        mod = seal()
        rows = mod.release_rows("1.2.3", "aaa11111", 1, 1, (10003, 166), (1, 1, 0, 0))
        at = [label for label, _ in rows].index("suite")
        assert rows[at : at + 2] == [("suite", "10003 passed"), ("", "166 skipped")]
        assert ("suite", "7003 passed, 66 skipped") in mod.release_rows(
            "1.2.3", "aaa11111", 1, 1, (7003, 66), (1, 1, 0, 0)
        )

    def test_refuses_to_count_a_chain_count_nobody_could_read(self):
        """S8, S10, `questions.md` Q8. A chain count that is None was not read:
        its row stays and says `not read`, never dropped and never 0. One issue
        and one round are singular."""
        mod = seal()
        rows = dict(
            (label, value)
            for label, value in mod.release_rows(
                "1.2.3", "aaa11111", 1, 1, (5, 0), (None, None, None, None)
            )
            if label
        )
        assert rows["items"] == rows["capped"] == rows["deferred"] == "not read"
        # Each row that needs two counts says `not read` when either is missing.
        half = dict(
            mod.release_rows("1.2.3", "aaa11111", 1, 1, (5, 0), (1, None, 0, 0))
        )
        assert half["items"] == "not read", half
        labels = dict(
            mod.release_rows("1.2.3", "aaa11111", 1, 1, (5, 0), (None, None, 2, None))
        )
        assert labels["capped"] == "not read", labels
        one = dict(mod.release_rows("1.2.3", "aaa11111", 1, 1, (5, 0), (1, 1, 0, 1)))
        assert one["items"] == "1 . 1 round" and one["deferred"] == "1 issue", one
        assert one["capped"] == "0 of 1", one


class Test_suite_counts:
    def test_accepts_the_record_and_reads_it_through_the_gates_reader(
        self,
        tmp_path,
    ):
        """S9 and S12 of 1791384158. `(passed, skipped)` are the counts the
        broad gate's own reader and counter give over the sessions carrying the
        key, summed; xfails and xpasses are counted and neither passed nor
        skipped, as on pytest's line."""
        mod = seal()
        directory = recorded(
            tmp_path,
            {"passed": 7000, "skipped": 60, "xfailed": 2},
            {"passed": 69, "skipped": 6, "xpassed": 1},
        )
        assert mod.suite_counts(directory, SUITE_KEY) == (7069, 66)
        assert not hasattr(mod, "ElementTree")

    @pytest.mark.parametrize(
        "case",
        [
            "no directory named",
            "no key named",
            "a directory that is not there",
            "no session carries the key",
            "a line that did not parse",
            "a session that stopped part-way",
            "a report with no file of its own",
        ],
    )
    def test_refuses_a_record_that_cannot_vouch_for_the_counts(self, tmp_path, case):
        """S9 and S12. A record nobody can read for the whole suite raises, so
        the seal falls back (S2) rather than drawing a count."""
        directory, key = recorded(tmp_path, {"passed": 10}), SUITE_KEY
        if case == "no directory named":
            directory = ""
        elif case == "no key named":
            key = ""
        elif case == "a directory that is not there":
            directory = str(tmp_path / "absent")
        elif case == "no session carries the key":
            key = "seal-0000000000"
        elif case == "a line that did not parse":
            directory = recorded(tmp_path, {"passed": 10}, extra="{cut off\n")
        elif case == "a session that stopped part-way":
            stopped = tmp_path / "records" / f"{SUITE_KEY}-0.jsonl"
            stopped.write_text(
                stopped.read_text(encoding="utf-8").replace(
                    '"stopped": []', '"stopped": [{"by": "failures", "what": "x"}]'
                ),
                encoding="utf-8",
            )
        elif case == "a report with no file of its own":
            # #869 round 1's finding 2: a report written as no line counts under
            # no category, so `passed` would be short of pytest's own line.
            left_out = tmp_path / "records" / f"{SUITE_KEY}-0.jsonl"
            left_out.write_text(
                left_out.read_text(encoding="utf-8").replace(
                    '"unplaced": 0', '"unplaced": 1'
                ),
                encoding="utf-8",
            )
        said = {
            "no directory named": "SUITE_RECORDS names no directory",
            "no key named": "SUITE_KEY names no key",
            "a directory that is not there": "carries the key",
            "no session carries the key": "carries the key",
            "a line that did not parse": "did not parse",
            "a session that stopped part-way": "stopped part-way",
            "a report with no file of its own": "counted under no category",
        }[case]
        with pytest.raises(ValueError, match=said):
            seal().suite_counts(directory, key)

    @pytest.mark.parametrize("category", ["failed", "error"])
    def test_a_suite_that_did_not_pass_is_not_sealed(self, tmp_path, category):
        """S9. A failure or an error in the record raises: a `SEALED` above a red
        suite would say something false."""
        directory = recorded(tmp_path, {"passed": 10, category: 1})
        with pytest.raises(ValueError, match="did not pass"):
            seal().suite_counts(directory, SUITE_KEY)


class Test_chain_counts:
    def test_accepts_a_tree_and_counts_items_rounds_capped_and_deferred(self, tmp_path):
        """S10. One work item declaring the pull request's branch, three rounds
        whose verdicts defer #12, then #13 and #14, then a file: one item, three
        rounds, one capped, three distinct issues. A pull request no declaration
        names is not an item, and its label still counts. Each home is one
        `verdict:` line's (#866), so the answer naming #99 counts no fourth."""
        root = tree(
            tmp_path,
            verdicts=[
                ["fixed abc1234", "deferred #12"],
                ["deferred #13", "deferred #14", "rejected"],
                ["deferred seal/follow-up.md", "deferred #12"],
            ],
        )
        record = (
            tmp_path
            / "seal"
            / "threads"
            / "1700000000-an-item"
            / "trail"
            / "rounds"
            / "round-2.md"
        )
        text = record.read_text(encoding="utf-8")
        answered = text.replace(
            "answer: \n", "answer: #99 was deferred by another round\n"
        )
        assert answered != text
        record.write_text(answered, encoding="utf-8")
        pulls = [
            pr(20, "feat/12-an-item", "chain: capped"),
            pr(21, "fix/nobody-declared-this"),
        ]
        assert seal().chain_counts(root, pulls) == (1, 3, 1, 3)

    def test_the_seal_counts_the_issue_a_deferral_went_to_not_every_mention(
        self, tmp_path
    ):
        """#866 S3. A home is the whole of what follows `deferred`, and it names
        an issue only where it is exactly `#N`: `deferred #854 — fixed in 0.20.0
        as #858` names neither #854 nor #858, since a note belongs on the
        finding's `answer:` line. With `deferred #854` beside it, one issue was
        deferred to. A home written as prose, `deferred to #700`, names none."""
        root = tree(
            tmp_path,
            verdicts=[
                ["deferred #854 — fixed in 0.20.0 as #858", "deferred #854"],
                ["deferred to #700"],
            ],
        )
        assert seal().chain_counts(root, [pr(20, "feat/12-an-item")]) == (1, 2, 0, 1)

    def test_refuses_to_count_a_tree_whose_records_are_not_there(
        self, tmp_path, capsys
    ):
        """S10, `questions.md` Q1 (round 1's finding 1). A root with no
        declaration -- the records moved by #715, or retired before the tag --
        leaves the three tree rows None, and the log says why; capped is read
        from the labels alone. Seen red at `e01e1b12`, which drew
        `(0, 0, 1, 0)` and said nothing."""
        counts = seal().chain_counts(
            str(tmp_path), [pr(20, "feat/12-an-item", "chain: capped")]
        )
        assert counts == (None, None, 1, None), counts
        assert "not read" in capsys.readouterr().out
        # With no capped pull request to miss, the empty tree alone is the reason.
        counts = seal().chain_counts(str(tmp_path), [pr(20, "feat/12-an-item")])
        assert counts == (None, None, 0, None), counts
        assert "no routing.md" in capsys.readouterr().out

    def test_a_capped_pull_request_with_no_work_item_leaves_the_tree_rows_unread(
        self, tmp_path, capsys
    ):
        """S10 (round 1's finding 1). A pull request labelled `chain: capped`
        was reviewed, so one that resolves to no declaration makes the item
        count incomplete, and the log names it."""
        root = tree(tmp_path, verdicts=[["deferred #12"]])
        pulls = [pr(20, "feat/12-an-item"), pr(21, "feat/99-retired", "chain: capped")]
        assert seal().chain_counts(root, pulls) == (None, None, 1, None)
        assert "#21" in capsys.readouterr().out

    def test_an_unlistable_rounds_leaves_rounds_unread_not_zero(self, tmp_path, capsys):
        """S10 (round 1's finding 2). A `rounds` that is a file holds records
        nobody can count: the rounds row is not read, and the log names it.
        Seen red at `7966a9f9`, which drew `(1, 0, 0, None)`."""
        root = tree(tmp_path)
        item = tmp_path / "seal" / "threads" / "1700000000-an-item"
        (item / "trail" / "rounds").rmdir()
        (item / "trail" / "rounds").write_text("# round 1\n", encoding="utf-8")
        assert seal().chain_counts(root, [pr(20, "feat/12-an-item")]) == (
            1,
            None,
            0,
            None,
        )
        out = capsys.readouterr().out
        assert "rounds" in out and "not read" in out, out

    def test_a_finding_the_reader_refuses_leaves_deferred_unread(
        self, tmp_path, capsys
    ):
        """S10 (round 1's finding 2). A finding the check's reader refuses —
        here a `deferred` with no home — is a count nobody made, so deferred is
        not read and the log names the record. Seen red at `7966a9f9`, which
        counted 1."""
        root = tree(tmp_path, verdicts=[["deferred #12", "deferred"]])
        assert seal().chain_counts(root, [pr(20, "feat/12-an-item")]) == (1, 1, 0, None)
        assert "round-1.md" in capsys.readouterr().out

    def test_a_deferred_count_nobody_could_read_is_none_and_the_log_says_why(
        self, tmp_path, capsys
    ):
        """S10, S11 (T30). A round record the check's reader refuses — the old
        table's shape, with no `## Findings` — leaves the deferred count None,
        which the row shows as `not read`, and the log names the file; the items
        and rounds it could count stand."""
        root = tree(tmp_path, verdicts=[["deferred #12"]])
        record = (
            tmp_path / "seal" / "threads" / "1700000000-an-item" / "trail" / "rounds"
        )
        (record / "round-2.md").write_text(OLD_ROUND.format(n=2), encoding="utf-8")
        counts = seal().chain_counts(root, [pr(20, "feat/12-an-item")])
        assert counts == (1, 2, 0, None), counts
        out = capsys.readouterr().out
        assert "round-2.md" in out and "deferred" in out, out

    def test_readers_that_will_not_load_leave_every_tree_row_unread(
        self, tmp_path, monkeypatch, capsys
    ):
        """S10. Where the shared readers cannot be loaded, the three tree rows are
        None and the log says why; capped is read from the labels alone."""
        mod = seal()

        def broken(*_):
            raise ImportError("no reader")

        monkeypatch.setattr(mod, "readers", broken)
        counts = mod.chain_counts(
            tree(tmp_path), [pr(20, "feat/12-an-item", "chain: capped")]
        )
        assert counts == (None, None, 1, None), counts
        assert "no reader" in capsys.readouterr().out


class Test_main:
    def test_accepts_a_published_note_and_replaces_its_glance_table(
        self, monkeypatch, tmp_path
    ):
        """S1, S7, and #1009 S3. The PNG is uploaded as `seal.png`, and the
        edited note is the published one with its glance block replaced by the
        heading, the image at the release-download URL with its alt text and the
        display width `draw` answered, a blank line and one line of the counts
        -- every other byte unchanged. The PNG is `DENSITY` times that width
        (#1009 S1), so the width is what keeps it from showing twice its size.
        Seen red before `main` existed, before the image carried a width, and
        by a width the note computed apart from `draw`."""
        mod, hub = wired(monkeypatch, tmp_path)
        assert mod.main() == 0
        (upload,) = hub.writes("upload")
        assert upload[:3] == ("release", "upload", TAG)
        assert os.path.basename(upload[3]) == "seal.png" and os.path.isfile(upload[3])
        assert upload[4:] == ("--repo", REPO)
        (edit,) = hub.writes("edit")
        assert edit[:5] == ("release", "edit", TAG, "--repo", REPO)
        body = edit[edit.index("--notes") + 1]
        publisher = load(PUBLISHER, "publish_release_note_for_s1")
        work, closed, people = publisher.tally(PULLS, OWNER)
        rows = mod.release_rows("1.2.3", SHA, 2, 2, (7003, 66), (1, 1, 1, 1))
        image = f"https://github.com/{REPO}/releases/download/{TAG}/seal.png"
        sealed = publisher.sealed_glance(
            image, mod.alt_text(rows), DRAWN_WIDTH, work, closed, people
        )
        assert body == note().replace(publisher.glance(work, closed, people), sealed)
        assert body.startswith(
            f'### \U0001f4ca At a glance\n\n<img src="{image}" alt="The 1.2.3 release seal: '
            "SEALED v1.2.3 at aaa11111 on main, 2 pull requests merged, 2 issues "
            "closed, the suite at 7003 passed and 66 skipped, 1 work item over 1 "
            f'review round, 1 of them capped, 1 issue deferred" width="{DRAWN_WIDTH}">\n\n'
            "\U0001f500 Pull requests **2** · ✅ Issues closed **2** · \U0001f64c Outside contributors **1**"
            "\n\n### ✨ Features"
        ), body[:600]
        assert hub.calls.index(upload) < hub.calls.index(edit)

    @pytest.mark.parametrize(
        "case",
        [
            "the suite step failed",
            "no record carries the key",
            "a line of the record did not parse",
            "a session of the suite stopped part-way",
            "the suite counts a failure",
            "the suite counts an error",
            "Pillow is not installed",
            "the stamp's module will not load",
            "the PNG cannot be saved",
            "gh pr list fails",
            "gh release view fails",
            "gh release upload fails",
            "the glance table is not there",
            "the glance table is there twice",
            "gh release edit fails",
            "a module will not load",
        ],
    )
    def test_refuses_on_any_failure_and_leaves_the_note_as_published(
        self, monkeypatch, tmp_path, capsys, case
    ):
        """S2, the case #718's box 2 asks for. Each failure, one at a time: the
        process exits 0, prints a line naming the failure and a `::warning::`
        with the same reason, and calls no `gh release edit` -- except where the
        edit is the call that failed. Nothing is uploaded either, except where
        the upload or the edit is the call that failed. Seen red by removing the
        guard each pins. The three draw cases (#1009 S4 and S5) run the real
        `draw` with no Pillow behind it: blocked, or a stand-in whose save
        fails; seen red by `draw` letting each error through unnamed."""
        env, fails, body, pulls = {}, (), None, PULLS
        stand_in = case not in REASONS_OF_THE_DRAW
        if case == "the suite step failed":
            env["SUITE_OUTCOME"] = "failure"
        elif case == "no record carries the key":
            env["SUITE_KEY"] = "seal-0000000000"
        elif case == "a line of the record did not parse":
            env["SUITE_RECORDS"] = recorded(
                tmp_path, {"passed": 10}, extra="{cut off\n"
            )
        elif case == "a session of the suite stopped part-way":
            env["SUITE_RECORDS"] = recorded(tmp_path, {"passed": 10}, extra="")
            stopped = tmp_path / "records" / f"{SUITE_KEY}-0.jsonl"
            stopped.write_text(
                stopped.read_text(encoding="utf-8").replace(
                    '"exitstatus": 0', '"exitstatus": 2'
                ),
                encoding="utf-8",
            )
        elif case == "the suite counts a failure":
            env["SUITE_RECORDS"] = recorded(tmp_path, {"passed": 10, "failed": 1})
        elif case == "the suite counts an error":
            env["SUITE_RECORDS"] = recorded(tmp_path, {"passed": 10, "error": 1})
        elif case == "gh pr list fails":
            pulls = None
        elif case == "gh release view fails":
            fails = ("view",)
        elif case == "gh release upload fails":
            fails = ("upload",)
        elif case == "gh release edit fails":
            fails = ("edit",)
        elif case == "the glance table is not there":
            body = note().replace(
                "| ✅ Issues closed | **2** |", "| ✅ Issues closed | **3** |"
            )
        elif case == "the glance table is there twice":
            body = note() + "\n\n" + note().split("\n\n### ✨")[0]
        mod, hub = wired(
            monkeypatch,
            tmp_path,
            body=body if body is not None else (note() if pulls is not None else ""),
            fails=fails,
            pulls=pulls,
            stand_in=stand_in,
            **env,
        )
        if case == "Pillow is not installed":
            monkeypatch.setitem(sys.modules, "PIL", None)
        elif case == "the stamp's module will not load":

            def broken():
                raise ImportError("no stamp")

            monkeypatch.setattr(mod, "stamp", broken)
        elif case == "the PNG cannot be saved":
            monkeypatch.setitem(sys.modules, "PIL", pillow_that_cannot_save())
        elif case == "a module will not load":

            def publisher():
                raise ImportError("no publisher")

            monkeypatch.setattr(mod, "publisher", publisher)
        assert mod.main() == 0
        out = capsys.readouterr().out.splitlines()
        warnings = [line for line in out if line.startswith("::warning::")]
        assert len(warnings) == 1, out
        reason = warnings[0].removeprefix("::warning::release seal skipped: ")
        assert reason and [line for line in out if line.startswith("no seal: ")] == [
            f"no seal: {reason} -- the note stays as it was published"
        ], out
        assert REASONS[case] in reason, (case, reason)
        edits = hub.writes("edit")
        if case == "gh release edit fails":
            assert len(edits) == 1 and "uploaded" in reason, (edits, reason)
        else:
            assert edits == [], (case, hub.calls)
        if case not in ("gh release upload fails", "gh release edit fails"):
            assert hub.writes("upload") == [], (case, hub.calls)

    def test_a_hand_edited_note_is_left_alone_and_nothing_is_uploaded(
        self, monkeypatch, tmp_path, capsys
    ):
        """S3. A glance table changed by one character after publication is not
        the generated shape: the note is not edited, the asset is not uploaded,
        and the log says the table was not found."""
        edited = note().replace(
            "| \U0001f500 Pull requests | **2** |",
            "| \U0001f500 Pull requests | **2**  |",
        )
        mod, hub = wired(monkeypatch, tmp_path, body=edited)
        assert mod.main() == 0
        assert hub.writes("upload") == [] and hub.writes("edit") == []
        out = capsys.readouterr().out
        # Round 1's finding 7: the refusal names every way the table can be
        # missing, not a hand edit alone.
        assert (
            "the glance table is not in the note exactly once as `glance` writes it "
            "for this release -- the note was edited after publication, went out "
            "without one, or the pull requests moved between the two lists; nothing "
            "was uploaded"
        ) in out, out

    def test_a_dry_run_draws_and_prints_and_writes_nothing(
        self, monkeypatch, tmp_path, capsys
    ):
        """S12. `DRY_RUN=1` writes the PNG where `SEAL_PNG` says, prints the rows
        and the edited note, and calls neither `gh release upload` nor
        `gh release edit`."""
        target = tmp_path / "out" / "seal.png"
        target.parent.mkdir()
        mod, hub = wired(
            monkeypatch,
            tmp_path,
            fails=("upload", "edit"),
            DRY_RUN="1",
            SEAL_PNG=str(target),
        )
        assert mod.main() == 0
        assert target.is_file()
        assert hub.writes("upload") == [] and hub.writes("edit") == []
        out = capsys.readouterr().out
        assert (
            "deferred 1 issue" in out and "suite    7003 passed, 66 skipped" in out
        ), out
        assert 'alt="The 1.2.3 release seal: SEALED v1.2.3 at aaa11111' in out, out
        assert "::warning::" not in out, out


class Test_module:
    def test_the_png_is_the_stamps_cells_one_square_block_each(self, tmp_path):
        """#1009 S1. `draw` writes an RGBA PNG `w * CELL_PX` pixels square,
        where `w` is the width `seal_stamp.py#build` gives, and every pixel of
        the block for cell `(x, y)` is `px(x, y)` with alpha 255, or alpha 0
        where `px(x, y)` is None. It answers the note's width, the side divided
        by `DENSITY`. The cells are read from `seal_stamp.py` loaded here by
        path, apart from the module `release_seal.py` loaded. Seen red with one
        cell's colour changed in the draw."""
        from PIL import Image

        mod = seal()
        w, h, px = stamp("seal_stamp_for_the_release_png").build()
        out = tmp_path / "seal.png"
        width = mod.draw(str(out))
        image = Image.open(out)
        side = w * mod.CELL_PX
        assert (mod.CELL_PX, mod.DENSITY) == (12, 2)
        assert w == h and image.mode == "RGBA" and image.size == (side, side)
        assert width == side // mod.DENSITY, (width, side)
        assert blocks(out, px, w, mod.CELL_PX) == []

    def test_the_png_follows_whatever_chart_the_stamp_module_has(
        self, monkeypatch, tmp_path
    ):
        """#1009 S2. With the `CHART` of the stamp module `release_seal.py`
        loaded replaced by a chart this case builds, 28 lines of 28 with one
        `M` inside the field, and its `LIGHT` replaced by a colour no cell of the
        tree's stamp has, the PNG's cells are that module's `build`, and the PNG
        differs from the one drawn with the tree's chart. So the disc's mark and
        its colours are read from the stamp module, and #857's choice reaches the
        release image with nothing else changed. Pillow is imported first, as in
        S1, so where it is absent this case fails with a `ModuleNotFoundError`,
        as `bin/test` says. Seen red against a draw that loads a copy of the
        stamp module of its own, and against one that maps a cell's colour to a
        colour of its own."""
        from PIL import Image

        mod = seal()
        before = tmp_path / "tree.png"
        mod.draw(str(before))
        n = 28
        chart = tuple(
            "." * 14 + "M" + "." * 13 if y == 14 else "." * n for y in range(n)
        )
        # The mark's lit cell, (14, 14) in this chart, in a colour the tree has not.
        lit = (1, 2, 3)
        expected = stamp("seal_stamp_for_the_built_chart")
        for loaded in (expected, mod.stamp()):
            monkeypatch.setattr(loaded, "CHART", chart)
            monkeypatch.setattr(loaded, "LIGHT", lit)
        w, _, px = expected.build()
        assert px(14, 14) == lit
        after = tmp_path / "built.png"
        mod.draw(str(after))
        assert blocks(after, px, w, mod.CELL_PX) == []
        assert Image.open(before).tobytes() != Image.open(after).tobytes()

    def test_the_release_script_loads_with_pillow_blocked(self):
        """#1009 S6. With `PIL` blocked, `release_seal.py` loads: Pillow is
        imported inside `draw` and nowhere else, so every publishing case runs
        with a stand-in for `draw` where Pillow is absent. Seen red with
        `import PIL` at the module's top."""
        script = (
            "import sys, importlib.util\n"
            "sys.modules['PIL'] = None\n"
            f"spec = importlib.util.spec_from_file_location('s', {SCRIPT!r})\n"
            "mod = importlib.util.module_from_spec(spec)\n"
            "spec.loader.exec_module(mod)\n"
            "assert callable(mod.draw)\n"
        )
        r = subprocess.run(
            [sys.executable, "-c", script],
            capture_output=True,
            encoding="utf-8",
            timeout=120,
        )
        assert r.returncode == 0, r.stderr

    def test_the_alt_text_is_one_sentence_carrying_every_value(self):
        """S11. One sentence in the shape of 0.17.0's hand-written alt text,
        carrying every value of the rows, with no `]` and no line break, so the
        Markdown image it sits in cannot end early."""
        text = seal().alt_text(ROWS)
        assert text == (
            "The 1.2.3 release seal: SEALED v1.2.3 at aaa11111 on main, 10 pull "
            "requests merged, 11 issues closed, the suite at 7003 passed and 66 "
            "skipped, 10 work items over 27 review rounds, 6 of them capped, 13 "
            "issues deferred"
        ), text
        unread = seal().release_rows("1.2.3", "aaa11111", 1, 1, (5, 0), (None,) * 4)
        text = seal().alt_text(unread)
        assert "work items not read" in text and "deferred not read" in text, text
        assert "]" not in text and "\n" not in text
        # A value carrying either cannot end the image early.
        odd = [(label, f"{value}]\n[") for label, value in ROWS]
        assert not set("[]\n") & set(seal().alt_text(odd))

    def test_a_refused_gh_or_git_call_is_a_reason_naming_the_call(self, monkeypatch):
        """S2's inputs. `gh` answers a call's stdout and turns a non-zero exit
        into `Refused` naming the call and what it printed; `tagged` does the
        same for the commit a tag names. Both are what the failure cases above
        stand in for."""

        mod = seal()
        seen = []

        def run(args, **_):
            seen.append(args)
            code = 1 if "edit" in args or "nope" in args[-1] else 0
            return subprocess.CompletedProcess(
                args, code, stdout=f"{SHA}\n", stderr="HTTP 502\n"
            )

        monkeypatch.setattr(mod.subprocess, "run", run)
        assert mod.gh("release", "view", TAG) == f"{SHA}\n"
        with pytest.raises(mod.Refused, match=r"^gh release edit failed: HTTP 502$"):
            mod.gh("release", "edit", TAG, "--notes", "x")
        assert mod.tagged(TAG) == SHA
        assert seen[-1] == ["git", "rev-parse", f"{TAG}^{{commit}}"]
        with pytest.raises(mod.Refused, match=r"^git rev-parse nope failed: HTTP 502$"):
            mod.tagged("nope")


test_census = census_case(TARGET)
