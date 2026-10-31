"""`hooks/lib/fields.py`, one class per public function (#1198).

The reader of a work item's `seal` blocks: `frame/design.md` *Data &
interfaces* Table F of work item 1793437163 is the grammar these cases hold
it to. Each refusal path has a case that names its line and its sentence.
"""

import os
import time

import pytest
from conftest import ROOT, census_case, load_hook_module

TARGET = "hooks/lib/fields.py"

fields = load_hook_module("lib/fields.py", "agentic_fields_under_test")

FENCE = "`" * 3
SHA = "abc1234"
BASE = "def5678"


def block(*lines, opener=FENCE + "seal"):
    """A `seal` block holding LINES, closed, with a newline after it."""
    return "\n".join([opener, *lines, FENCE]) + "\n"


def verdict(target=SHA, said="sealed", original=None):
    lines = [f"target: {target} against main"]
    if original:
        lines.append(f"original: {original}")
    return block(*lines, f"Verdict: {said}")


def guarantee(*blocks_):
    """A guarantee: a heading, a table for people, then BLOCKS_."""
    head = "# an item -- guarantee\n\n| Claim | Result |\n|---|---|\n| x | holds |\n\n"
    return head + "\n".join(blocks_)


def finding_with(line):
    """A finding block holding a severity, a location and its evidence, and
    LINE after them, or LINE in the location's place where it is one."""
    lines = ["severity: must", "location: `a.py`", "evidence: read `a.py:1`"]
    if line.startswith("location:"):
        lines = [lines[0], lines[2], line]
    else:
        lines.append(line)
    return block(*lines)


def read(text, kinds=None):
    return fields.read(text, kinds or fields.GUARANTEE)


def line_of(text, line, after=0):
    """The 1-based number of the first line of TEXT equal to LINE, past AFTER."""
    lines = text.split("\n")
    return lines.index(line, after) + 1


class Test_read:
    def test_accepts_stacked_verdict_blocks_in_order(self):
        """Table F, `verdict`: a block per run of the sealer, the last the
        newest; each field's value, line and named parts come back."""
        text = guarantee(
            verdict("aaa1111", "withheld reason: the gate failed"),
            verdict(SHA, "sealed", original=BASE),
        )
        found = read(text)
        assert (found.refusals, found.notices) == ([], [])
        first, newest = found.blocks
        assert (first.kind, newest.kind) == (fields.VERDICT_BLOCK,) * 2
        assert fields.verdict_word(first) == fields.WITHHELD
        assert fields.verdict_word(newest) == fields.SEALED
        target = newest.fields[fields.TARGET]
        assert (target.match["commit"], target.match["base"]) == (SHA, "main")
        assert target.line == line_of(text, f"target: {SHA} against main")
        assert newest.line == target.line - 1
        assert newest.end == target.line + 3
        assert newest.fields[fields.ORIGINAL].match["commit"] == BASE

    def test_accepts_every_kind_of_a_round_record(self):
        """Table F's four kinds of a round record, each with every key its
        kind takes, read through the shapes the grammar table held."""
        text = "\n".join(
            [
                block(f"target: {SHA} against main", f"original: {BASE}"),
                "## Findings\n\n### 1. a symptom\n",
                block(
                    "severity: must",
                    "location: `a/b.py:3-4`, `c.md`",
                    "evidence: read `a/b.py:3`",
                    "regression: round-1#2",
                ),
                block("verdict: deferred #12", "answer:", "location: `d.py`"),
                "### 2. another\n",
                block(
                    "severity: should",
                    "location: `e.py`",
                    "evidence: executed `bin/test x -q`, `git log`",
                    "reopens: round-1#1",
                ),
                block(f"verdict: fixed {SHA}", "answer: done"),
                "## Confirmations\n",
                block("confirms: round-1#3"),
                block("confirms: none"),
            ]
        )
        found = read(text, fields.ROUND_RECORD)
        assert (found.refusals, found.notices) == ([], [])
        assert [b.kind.name for b in found.blocks] == [
            "round",
            "finding",
            "close",
            "finding",
            "close",
            "confirmation",
            "confirmation",
        ]
        close = found.blocks[2].fields
        assert close[fields.VERDICT].match["home"] == "#12"
        assert close[fields.ANSWER].value == ""
        assert found.blocks[4].fields[fields.VERDICT].match["commit"] == SHA

    def test_accepts_run_blocks_of_a_gate_record(self):
        text = "# gate\n\n" + block(f"run: {SHA} against {BASE}") + "\n"
        text += block(f"run: {BASE} against {BASE}")
        found = read(text, fields.GATE)
        assert [b.fields[fields.RUN].match["commit"] for b in found.blocks] == [
            SHA,
            BASE,
        ]

    @pytest.mark.parametrize(
        "opener",
        [
            FENCE + "Seal",
            FENCE + "SEAL",
            "~~~seal",
            FENCE + "`seal",
            FENCE + " seal",
            FENCE + "seal finding",
            FENCE + "seal ",
        ],
    )
    def test_refuses_a_near_opener_and_names_it_as_not_read(self, opener):
        """*Scope* item 1: a fence outside every fence whose info string's
        first word, case folded, is `seal`, and whose line is not exactly
        three backticks and `seal`, is no block; it is named at its line as
        not read, and nothing is refused for it."""
        closer = opener[: len(opener) - len(opener.lstrip(opener[0]))]
        text = guarantee(
            f"{opener}\ntarget: {SHA} against main\nVerdict: sealed\n{closer}\n"
        )
        found = read(text)
        assert (found.blocks, found.refusals) == ([], [])
        assert found.notices == [
            (line_of(text, opener), fields.NEAR.format(line=opener))
        ]

    @pytest.mark.parametrize("info", ["", "markdown", "sealed", "python seal"])
    def test_refuses_to_name_a_fence_whose_first_word_is_not_seal(self, info):
        found = read(guarantee(f"{FENCE}{info}\nVerdict: sealed\n{FENCE}\n"))
        assert (found.blocks, found.refusals, found.notices) == ([], [], [])

    def test_refuses_a_fence_that_never_closes_at_its_opener(self):
        """#1122: a fence nobody closed hides every line after it from a
        renderer, so it is refused at its opener, and a block above it is
        still read; a `seal` block that never closes is refused the same
        way."""
        text = guarantee(
            verdict(), FENCE + "`\n", verdict(said="withheld reason: the gate failed")
        )
        found = read(text)
        assert found.refusals == [(line_of(text, FENCE + "`"), fields.UNCLOSED)]
        open_block = guarantee(f"{FENCE}seal\ntarget: {SHA} against main\n")
        assert read(open_block).refusals == [
            (line_of(open_block, FENCE + "seal"), fields.UNCLOSED)
        ]
        assert read(open_block).blocks == []

    def test_refuses_a_blank_line_inside_a_block_at_its_line(self):
        text = guarantee(block(f"target: {SHA} against main", "", "Verdict: sealed"))
        found = read(text)
        blank = line_of(text, f"target: {SHA} against main") + 1
        assert (found.blocks, found.refusals) == ([], [(blank, fields.BLANK)])

    @pytest.mark.parametrize(
        "line",
        [
            "verdict: sealed",
            "Verdict : sealed",
            "**Verdict:** sealed",
            "Verdict:sealed",
        ],
    )
    def test_refuses_a_line_that_is_no_field_of_its_kind(self, line):
        """A key is spelt as the module spells it; a line that is not a field
        of its kind is refused at its line with the keys the kind takes, and
        the block is read no further."""
        text = guarantee(block(f"target: {SHA} against main", line))
        found = read(text)
        said = fields.NOT_A_FIELD.format(
            line=line,
            kind="verdict",
            keys="`target:`, `original:` and `Verdict:`",
        )
        assert (found.blocks, found.refusals) == ([], [(line_of(text, line), said)])

    def test_refuses_a_key_over_its_count_and_a_second_of_one_of_two(self):
        text = guarantee(
            block(f"target: {SHA} against main", "Verdict: sealed", "Verdict: sealed")
        )
        second = line_of(text, "Verdict: sealed") + 1
        assert read(text).refusals == [
            (second, fields.TWICE.format(key="Verdict:", kind="verdict"))
        ]
        finding = block(
            "severity: must",
            "location: `a.py`",
            "evidence: read `a.py:1`",
            "regression: round-1",
            "reopens: round-1#1",
        )
        said = fields.ONE_OF.format(key="reopens:", other="regression:", kind="finding")
        found = read(finding, fields.ROUND_RECORD)
        assert (found.blocks, found.refusals) == ([], [(6, said)])

    @pytest.mark.parametrize(
        ("line", "says"),
        [
            ("Verdict: Sealed", "Verdict:"),
            ("Verdict: withheld", "Verdict:"),
            ("Verdict: sealed ", "Verdict:"),
            ("original: main", "original:"),
        ],
    )
    def test_refuses_a_value_outside_its_shape_with_the_shape(self, line, says):
        text = guarantee(block(f"target: {SHA} against main", line))
        key = line.split(" ", 1)[0]
        said = fields.SHAPE.format(
            line=line, key=key, says=fields.VERDICT_BLOCK.keys[says].says
        )
        found = read(text)
        assert (found.blocks, found.refusals) == ([], [(line_of(text, line), said)])

    def test_accepts_each_shape_of_a_close_a_location_and_a_reference(self):
        """The values of a round record's blocks the check decides on, each
        read whole with the named part it reads (#1198, moved from the
        `chain_check.py` readers of a labelled line's value)."""
        sha = "1a2b3c4d" * 5
        for value, part in (
            ("rejected", None),
            ("fixed abc1234", "abc1234"),
            (f"fixed {sha}", sha),
            ("deferred #12", "#12"),
            ("deferred the frame", "the frame"),
        ):
            (found,) = read(
                block(f"verdict: {value}", "answer:"), fields.ROUND_RECORD
            ).blocks
            said = found.fields[fields.VERDICT].match
            assert (said["commit"] or said["home"]) == part, value
        for value in (
            "`a.py`",
            "`a.py:12`",
            "`a.py:12-14`",
            "`docs/x/`",
            "`a.py:1`, `docs/b.md:3-4`",
            "`a.py:1`, `b.py`, `c/d.md:9`",
        ):
            assert read(finding_with(f"location: {value}"), fields.ROUND_RECORD).blocks
        for value, ref in (
            ("round-2#3", ("2", "3")),
            ("round-2", ("2", None)),
            ("round-12#10", ("12", "10")),
        ):
            (found,) = read(
                finding_with(f"regression: {value}"), fields.ROUND_RECORD
            ).blocks
            said = found.fields[fields.REGRESSION].match
            assert (said["round"], said["finding"]) == ref, value

    @pytest.mark.parametrize(
        ("key", "value"),
        [
            *(
                ("verdict:", value)
                for value in (
                    "Fixed abc1234",
                    "fixed",
                    "fixed abc1234.",
                    "fixed abc123",
                    "fixed " + "1a2b3c4d" * 5 + "0",
                    "fixed ABC1234",
                    "fixed abc1234 · fix pass: done",
                    "fixed abc1234 and more",
                    "deferred",
                    "deferred ",
                    "confirmed",
                    "**fixed** abc1234",
                    "open",
                    "Open",
                    " rejected",
                    "",
                )
            ),
            *(
                ("location:", value)
                for value in (
                    "`:617`",
                    "`a.py:1`, `:617`",
                    "a.py:12",
                    "`https://example.com/a`",
                    "**`a.py:1`**",
                    "`a.py:1`,`b.py`",
                    "`a.py:1` and `b.py`",
                    "`a.py:1`, ",
                    "`a.py:x`",
                    "`a.py:1-`",
                    "`/abs/a.py`",
                    "`a.py`.",
                    "`a b.py`",
                    "`a.py#unit`",
                    "`a.py:1`, `b.py#unit`",
                    "",
                )
            ),
            *(
                ("regression:", value)
                for value in (
                    "round 2's 3",
                    "Round-2#3",
                    "#3",
                    "round-2#3.",
                    "**round-2#3**",
                    "`round-2#3`",
                    "round-02#3",
                    "round-2#03",
                    "round-0#1",
                    "round-2#",
                    "round-2 #3",
                    " round-2#3",
                    "round-2#3, round-2#4",
                    "none",
                    "",
                )
            ),
        ],
    )
    def test_refuses_a_round_value_outside_its_shape(self, key, value):
        """Every other value of a close's `verdict:`, `open` among them since
        a finding with no close block is open, of a `location:`, the
        `path#unit` coordinate #923 leaked among them, and of a
        `regression:` reference, refused at its line with its shape."""
        line = f"{key} {value}"
        if key == "verdict:":
            text, kind = block(line, "answer:"), fields.CLOSE_BLOCK
        else:
            text, kind = finding_with(line), fields.FINDING_BLOCK
        said = fields.SHAPE.format(line=line, key=key, says=kind.keys[key].says)
        found = read(text, fields.ROUND_RECORD)
        assert (found.blocks, found.refusals) == ([], [(line_of(text, line), said)])

    def test_the_verdict_shape_says_the_three_shapes(self):
        says = fields.VERDICT_BLOCK.keys[fields.SEALER_VERDICT].says
        for shape in (
            "`Verdict: sealed`",
            "`Verdict: withheld reason: <reason>`",
            "`Verdict: undecided question: <question>`",
        ):
            assert shape in says, says

    def test_refuses_a_block_lacking_a_key_it_holds_one_of_at_its_opener(self):
        text = guarantee(block(f"target: {SHA} against main"))
        opener = line_of(text, FENCE + "seal")
        said = fields.MISSING.format(kind="verdict", key="Verdict:")
        assert read(text).refusals == [(opener, said)]

    def test_refuses_an_empty_block_and_one_no_kind_of_the_record_opens(self):
        empty = guarantee(block())
        assert read(empty).refusals == [
            (line_of(empty, FENCE + "seal"), fields.EMPTY.format(openers="`target:`"))
        ]
        other = guarantee(block(f"run: {SHA} against {BASE}"))
        said = fields.NO_KIND.format(
            line=f"run: {SHA} against {BASE}", openers="`target:`"
        )
        assert read(other).refusals == [
            (line_of(other, f"run: {SHA} against {BASE}"), said)
        ]
        openers = "`target:`, `severity:`, `verdict:` or `confirms:`"
        assert fields.EMPTY.format(openers=openers) in [
            why for _n, why in read(block(), fields.ROUND_RECORD).refusals
        ]

    def test_refuses_a_comment_line_outside_every_fence(self):
        """#1012: a record carries no HTML comment, so a line that begins
        one is refused at its line; one quoted inside a fence is the
        fence's. An indented one is refused too, and the walk claims
        nothing after it."""
        text = guarantee(
            "<!-- " + verdict().rstrip("\n") + " -->\n",
            block(f"run: {SHA}", "<!-- quoted", opener=FENCE + "text"),
            verdict(),
            "   <!-- a note\n-->\n",
        )
        found = read(text)
        assert found.refusals == [
            (line_of(text, "<!-- " + FENCE + "seal"), fields.COMMENT_LINE),
            (line_of(text, "   <!-- a note"), fields.COMMENT_LINE),
        ]
        assert len(found.blocks) == 1

    @pytest.mark.parametrize(
        "above",
        ["- " + FENCE + "seal", "> " + FENCE, "  " + FENCE + "seal", "<div>"],
        ids=["list item", "block quote", "indent", "an HTML block"],
    )
    def test_refuses_a_fence_the_walk_cannot_place(self, above):
        """Where `blocks.walk` stops claiming, at a fence in a container or
        an HTML block, a `seal` block below is not read: each fence line it
        cannot place is refused at its line, so a later run's block is never
        silently dropped behind an earlier one."""
        text = guarantee(verdict(), above + "\n", verdict(said="withheld reason: x"))
        found = read(text)
        assert len(found.blocks) == 1
        unsure = [n for n, why in found.refusals if why == fields.UNSURE]
        assert unsure and min(unsure) >= line_of(text, above), found.refusals
        last = text.split("\n").index(FENCE + "seal", line_of(text, above)) + 1
        assert last in unsure, found.refusals

    def test_refuses_to_read_a_block_quoted_inside_another_fence(self):
        """A `seal` block inside a fix's fence belongs to the fix."""
        text = guarantee(FENCE + "`markdown\n" + verdict() + FENCE + "`\n")
        assert read(text) == fields.Read([], [], [])

    def test_reads_a_long_line_in_linear_time(self):
        """#941's round 3 met a pattern that backtracked exponentially; each
        shape is matched whole against a long value inside a bound far above
        the linear time and far below a backtracking one."""
        start = time.monotonic()
        for line in (
            "Verdict: withheld reason: " + "x " * 50000,
            "Verdict: undecided question:" + " " * 100000,
            f"target: {SHA} against " + "x" * 100000 + " ",
        ):
            read(guarantee(block(f"target: {SHA} against main", line)))
        for line in (
            "location: `" + "a:1" * 30000 + "`",
            "evidence: read `" + "a:1-" * 30000,
            "verdict: deferred " + "x " * 50000,
        ):
            read(block("severity: must", line), fields.ROUND_RECORD)
        assert time.monotonic() - start < 5.0


class Test_assemble:
    def test_accepts_pairs_and_writes_the_block_the_reader_reads(self):
        text = fields.assemble([(fields.RUN, f"{SHA} against {BASE}")], fields.GATE)
        assert text == f"{FENCE}seal\nrun: {SHA} against {BASE}\n{FENCE}\n"
        (found,) = fields.read(text, fields.GATE).blocks
        assert found.fields[fields.RUN].value == f"{SHA} against {BASE}"

    def test_refuses_pairs_the_reader_would_refuse(self):
        with pytest.raises(ValueError) as refused:
            fields.assemble([(fields.RUN, "HEAD against main")], fields.GATE)
        assert str(refused.value) == fields.SHAPE.format(
            line="run: HEAD against main",
            key="run:",
            says=fields.RUN_BLOCK.keys[fields.RUN].says,
        )


class Test_verdict_word:
    def test_accepts_each_of_the_three_shapes(self):
        for said, word in (
            ("sealed", fields.SEALED),
            ("withheld reason: x", fields.WITHHELD),
            ("undecided question: y?", fields.UNDECIDED),
        ):
            (found,) = read(verdict(said=said)).blocks
            assert fields.verdict_word(found) == word

    def test_refuses_a_block_of_another_kind(self):
        (found,) = read(block(f"run: {SHA} against {BASE}"), fields.GATE).blocks
        assert fields.verdict_word(found) is None


class Test_module:
    def test_the_round_template_opens_each_block_with_its_kind_and_reads(self):
        """#1198's scenario *The templates parse*, for the round record: the
        template holds a round block, a finding block and its close block,
        and two confirmation blocks, each opening with its kind's key, and
        the reader refuses no line of it, since every value the template
        writes is one its key's shape reads or prose after `answer:`. Seen
        red against the template in labelled lines, which held no block."""
        path = os.path.join(ROOT, "templates", "records", "sdd-round.md")
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        found = fields.read(text, fields.ROUND_RECORD)
        assert (found.refusals, found.notices) == ([], [])
        assert [b.kind for b in found.blocks] == [
            fields.ROUND_BLOCK,
            fields.FINDING_BLOCK,
            fields.CLOSE_BLOCK,
            fields.CONFIRMATION_BLOCK,
            fields.CONFIRMATION_BLOCK,
        ]
        lines = text.split("\n")
        for b in found.blocks:
            assert lines[b.line].startswith(b.kind.opener + " "), lines[b.line]

    def test_the_guarantee_template_refuses_only_its_placeholders(self):
        """#1198's scenario *The templates parse*, for the guarantee: every
        block of the template opens with its kind's key, and every line the
        reader refuses is a field whose value is a placeholder."""
        path = os.path.join(ROOT, "templates", "records", "sdd-guarantee.md")
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        found = fields.read(text, fields.GUARANTEE)
        lines = text.split("\n")
        assert found.notices == []
        assert found.refusals, "the unfilled template reads as a guarantee"
        for number, why in found.refusals:
            line = lines[number - 1]
            _key, _, value = line.partition(" ")
            assert why.startswith(f"`{line}` does not read whole"), (number, why)
            assert value.startswith("<") and value.endswith(">"), line
        firsts = [
            lines[index + 1]
            for index, line in enumerate(lines)
            if line == fields.OPENER
        ]
        assert firsts and all(f.startswith(fields.TARGET + " ") for f in firsts), firsts


test_census = census_case(TARGET)
