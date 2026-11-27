"""`skills/code-review/scripts/pr_body.py`, one class per function.

Written by #1044's phase 1. The generator's units run in the process over a
work item written under a case's own directory, and the command with its own
`main`, so no shell runs under them. The fixture's records are the shapes
the templates under `templates/records/` give, and its round records hold
the `seal` blocks `chain_check.py` reads.
"""

import json
import os
import re
import subprocess
import sys

import pytest
from conftest import (
    ROOT,
    census_case,
    config_json,
    load_module,
    mark_root,
    write,
)

TARGET = "skills/code-review/scripts/pr_body.py"

PR = load_module(os.path.join(ROOT, *TARGET.split("/")), "pr_body_under_test")

NAME = "1799000000-a-body"

CHANGELOG = """\
- **The pull request body copies the records.** `iadd pr-body` writes it (#1).
- 본문의 사실은 기록에서 옵니다.
"""

PLAN = """\
# Implementation Plan: 1799000000-a-body

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | the reader | its cases | 1111111 |
| 2 | the writer | its cases | 2222222 |

## Operational impact

None.
"""

ROUND_1 = """\
# Review round 1: 1799000000-a-body

```seal
target: 1111111 against main
```

## Findings

### 1. The writer drops the last line

```seal
severity: must
location: `skills/x.py:3`
evidence: read `skills/x.py:1-3`
```

Why it matters, with its grounds.

```seal
verdict: fixed 2222222
answer: fixed in 2222222: the writer keeps the last line now.
```

## Confirmations

The reader holds.
"""

ROUND_2 = """\
# Review round 2: 1799000000-a-body

```seal
target: 3333333, fixes 1111111..3333333
```

## Findings

None. The fix closes round 1's finding.

## Confirmations

```seal
confirms: round-1#1
```
The close holds.
"""

GATE = """\
# 1799000000-a-body: broad gate

```seal
run: 2222222 against 4444444
```

```seal
run: 3333333 against 4444444
```
"""

GAPS = """\
# Closing memo: 1799000000-a-body

## Not verified

| Item | Who must answer |
|---|---|
| the full suite | the orchestrator |

## Not done

nothing
"""

QUESTIONS = """\
# Questions for the planner: 1799000000-a-body

## Rows

| # | Question | Who can answer | Options | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Which part first? | a person | (a) or (b) | (a) | open |
| Q2 | Which heading? | a person | (a) or (b) | (a) | answered 2026-10-28 by the owner |
"""

RECORDS = {
    "changelog.md": CHANGELOG,
    "frame/plan.md": PLAN,
    "trail/phases/phase-1.md": "# Phase 1: 1799000000-a-body\n",
    "trail/phases/phase-2.md": "# Phase 2: 1799000000-a-body\n",
    "trail/rounds/round-1.md": ROUND_1,
    "trail/rounds/round-2.md": ROUND_2,
    "trail/gate.md": GATE,
    "gaps.md": GAPS,
    "frame/questions.md": QUESTIONS,
}

# S1: the fixture's generated part, written out section for section as
# `frame/design.md` *Data & interfaces* lays it out: the line it opens
# with, the changelog's section outside any fold (#1478), then one fold
# whose summary names the copy, a blank line after the summary, the other
# sections, and the fold's end.
EXPECTED = """\
## From the records

## What changed

From `changelog.md`.

- **The pull request body copies the records.** `iadd pr-body` writes it (#1).
- 본문의 사실은 기록에서 옵니다.

<details>
<summary>Copied from the records in seal/threads/1799000000-a-body/ by iadd pr-body.</summary>

## How it was built

From `frame/plan.md`, its *Phases* section.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | the reader | its cases | 1111111 |
| 2 | the writer | its cases | 2222222 |

The phase records:

- `trail/phases/phase-1.md`
- `trail/phases/phase-2.md`

## Review rounds

### `trail/rounds/round-1.md`

```seal
target: 1111111 against main
```

#### 1. The writer drops the last line

```seal
severity: must
location: `skills/x.py:3`
evidence: read `skills/x.py:1-3`
```

```seal
verdict: fixed 2222222
answer: fixed in 2222222: the writer keeps the last line now.
```

### `trail/rounds/round-2.md`

```seal
target: 3333333, fixes 1111111..3333333
```

None. The fix closes round 1's finding.

```seal
confirms: round-1#1
```

## Broad gate

From `trail/gate.md`.

```seal
run: 2222222 against 4444444
```

```seal
run: 3333333 against 4444444
```

## Not verified

From `gaps.md`.

| Item | Who must answer |
|---|---|
| the full suite | the orchestrator |

## Not done

From `gaps.md`.

nothing

## Questions

From `frame/questions.md`.

| # | Question | Who can answer | Options | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Which part first? | a person | (a) or (b) | (a) | open |
| Q2 | Which heading? | a person | (a) or (b) | (a) | answered 2026-10-28 by the owner |

</details>
"""

# The work item's `pr.md`, the body's first part where the two language keys
# name one language: a quote of a record in the form `first_part` reads, with
# its coordinate, a CRLF line among them, and the `Closes` line.
OWN = '- "`iadd pr-body` writes it (#1)." (`changelog.md`, line 1)\r\n\nCloses #1.\n'
# #1453: the two language keys the body's first part is composed from, as a
# repository of one language writes them.
LANGUAGES = [
    ("Commit and pull request language", "English"),
    ("Record language", "English"),
]
# The keys of a repository whose team writes Korean over English records,
# and the work item's `pr.ko.md`, `OWN`'s quote rendered in Korean, with no
# line end after its last line.
DIFFERING = [
    ("Commit and pull request language", "Korean"),
    ("Record language", "English"),
]
TRANSLATION = '"`iadd pr-body` 가 본문을 쓴다 (#1)." (`changelog.md`, line 1)'


def item_of(tmp_path, records, own=OWN, rows=LANGUAGES, translations=None):
    """The work item NAME in the shared root of a git repository at
    `tmp_path`, whose `config.json` holds ROWS as its keys, holding RECORDS
    by path, OWN as its `pr.md`'s bytes, or no `pr.md` where OWN is None, and
    TRANSLATIONS, `{name: text}`, beside it. The repository has no commit:
    `iadd pr-body` reads the keys of the root its work item stands in, so a
    case reads its own keys and not the checkout the suite runs in."""
    home = mark_root(tmp_path / "seal")
    write(home, "config.json", config_json(*rows))
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    item = home / "threads" / NAME
    item.mkdir(parents=True)
    for name, text in (translations or {}).items():
        (item / name).write_bytes(text.encode("utf-8"))
    for rel, text in records.items():
        write(item, rel, text)
    if own is not None:
        (item / "pr.md").write_bytes(own.encode("utf-8"))
    return item


def unsourced(text, texts):
    """The lines of TEXT that are no line of a record in TEXTS, no finding
    heading of one demoted a level, and no line `FIXED` gives with NAME or a
    record's path filled in."""
    lines = {line for record in texts.values() for line in record.split("\n")}
    demoted = {"#" + line for line in lines}
    paths = {*texts, *RECORDS, "trail/phases/", "trail/rounds/"}
    fixed = {
        line.format(home="seal", name=NAME, path=path)
        for line in PR.FIXED
        for path in paths
    }
    return [
        line
        for line in text.split("\n")
        if line not in lines and line not in demoted and line not in fixed
    ]


# #1559: GitHub's limit on a pull request body, and the count the body is held
# to it in, UTF-16 code units, written here apart from `pr_body.py`'s own, so
# a case measures a body with a count it does not take from the module.
LIMIT = 65536
# The line a folded section holds for each record it names, as a person
# reads it.
FOLDED = (
    "Not copied here, so the body stays within GitHub's 65,536 characters: "
    "`{path}` holds what this section copies."
)
# What `iadd pr-body` says where the fold folded one section, `## Not
# verified`.
FOLDED_NOT_VERIFIED = (
    "folded `## Not verified` so the body stays within GitHub's 65,536 "
    "characters; each folded section names the record that holds it"
)


# The length of the body S5's case refuses, with every section a fold shortens
# folded: its `pr.md`, the heading line, and the copy under it with the room
# of the fixture's mark. `## Broad gate`, `## Not verified` and `## Not done`
# stay whole there, since each one's fold line is longer than its copy;
# folding them as well would give 71,382.
LENGTH = 71263


def units(text):
    """TEXT's length in UTF-16 code units."""
    return len(text.encode("utf-16-le")) // 2


def long_gaps(rows, cell="x" * 90):
    """`GAPS` with ROWS more rows in its `## Not verified` table, each
    holding CELL."""
    first = "| the full suite | the orchestrator |\n"
    extra = "".join(f"| item {n} {cell} | the orchestrator |\n" for n in range(rows))
    return GAPS.replace(first, first + extra)


def long_questions(rows, cell="x" * 90):
    """`QUESTIONS` with ROWS more rows in its table, each holding CELL."""
    extra = "".join(
        f"| Q{n + 3} | {cell} | a person | (a) | (a) | open |\n" for n in range(rows)
    )
    return QUESTIONS + extra


def section_of(text, heading):
    """The lines of TEXT from the line HEADING to the next `## ` line, or to
    the fold's end."""
    lines = text.split("\n")
    first = lines.index(heading)
    stop = next(
        i
        for i in range(first + 1, len(lines))
        if lines[i].startswith("## ") or lines[i] == "</details>"
    )
    return lines[first:stop]


# #1204: a manifest with the two fields the mark's address is built from and
# a `version`, which the address does not read (#1452), and the line `iadd
# pr-body` writes from it.
MANIFEST = {
    "repository": "https://github.com/owner/plugin",
    "version": "1.2.3",
    "icon": "./.claude-plugin/icon.png",
}
MARK_LINE = (
    '<img src="https://github.com/owner/plugin/raw/HEAD/.claude-plugin/icon.png" '
    'alt="Cleared" width="128">'
)
ROW = [("Pull request inspection mark", "yes")]
CLEARED = "Verdict: cleared"


def manifest_of(tmp_path, fields):
    """FIELDS written as a manifest under `tmp_path`, and its path."""
    path = tmp_path / "plugin.json"
    path.write_text(json.dumps(fields), encoding="utf-8")
    return str(path)


def git_in(repo, *args):
    """`git -C REPO <args>`'s stdout, stripped."""
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        encoding="utf-8",
    ).stdout.strip()


def cleared_item(repo, row=ROW, verdict=CLEARED, base="feature/x"):
    """The work item NAME in REPO's shared root, holding RECORDS, with
    `config.json` holding the two language keys and ROW, committed; then,
    where VERDICT is given, an `inspection.md` whose one block names that
    commit against BASE with VERDICT, committed after it, as the
    orchestrator commits the inspector's verdict."""
    home = mark_root(repo / "seal")
    write(home, "config.json", config_json(*LANGUAGES, *(row or [])))
    item = home / "threads" / NAME
    for rel, text in RECORDS.items():
        write(item, rel, text)
    (item / "pr.md").write_bytes(OWN.encode("utf-8"))
    git_in(repo, "add", "-A")
    git_in(repo, "commit", "-qm", "the build")
    if verdict is not None:
        sha = git_in(repo, "rev-parse", "HEAD")
        write(
            item,
            "inspection.md",
            f"# Inspection: {NAME}\n\n```seal\ntarget: {sha} against {base}\n"
            f"{verdict}\n```\n",
        )
        git_in(repo, "add", "-A")
        git_in(repo, "commit", "-qm", "the inspection")
    return item


class Test_compose:
    def test_accepts_a_work_item_as_the_records_text(self, tmp_path):
        """S1, and #1198's scenario *The body copies blocks*. Every section
        the design lays out, in its order, holding the records' lines: each
        round's `seal` blocks verbatim, a finding's heading one level down
        followed by its finding block and its close block, a round with no
        finding, a line in Korean, the line `HEADING` holds first, the
        changelog's section under it and outside any fold, and one
        `<details>` around the other sections, its `<summary>` followed by a
        blank line. Seen red against the copy of a round's labelled lines,
        which held no block, and against `_composed` as 0.37.1 shipped it,
        which put the changelog's section inside the fold (#1478)."""
        texts = PR.read_item(str(item_of(tmp_path, RECORDS)))
        assert PR.compose(NAME, texts) == EXPECTED

    def test_accepts_only_lines_of_the_records_or_of_fixed(self, tmp_path):
        """S2. No count, summary or rewording can appear: each line is a
        record's, a demoted finding heading, or one of `FIXED`'s."""
        texts = PR.read_item(str(item_of(tmp_path, RECORDS)))
        assert unsourced(PR.compose(NAME, texts), texts) == []

    def test_accepts_every_round_once_in_number_order(self):
        """S3, the class of #1051's withheld body, which counted four rounds
        where five records stood: ten rounds, each listed once, `round-2.md`
        before `round-10.md`, and nothing the generator states about them."""
        texts = {
            f"trail/rounds/round-{n}.md": ROUND_2.replace("3333333", f"{n}{n}{n}abcd")
            for n in range(1, 11)
        }
        text = PR.compose(NAME, texts)
        lines = text.split("\n")
        heads = [f"### `trail/rounds/round-{n}.md`" for n in range(1, 11)]
        assert [lines.count(head) for head in heads] == [1] * 10
        assert [lines.index(head) for head in heads] == sorted(
            lines.index(head) for head in heads
        )
        assert unsourced(text, texts) == []

    def test_accepts_every_question_row_as_written(self):
        """S4, the class of #1060's and #857's withheld bodies, each of which
        left an `open` row out: every table line is copied with its `Status`
        cell as written, whatever its language, and the prose around the
        table is not."""
        questions = QUESTIONS.replace("| open |", "| 열림 |") + "\nA closing note.\n"
        text = PR.compose(NAME, {"frame/questions.md": questions})
        part = text[text.index("## Questions") :]
        rows = [line for line in questions.split("\n") if line.startswith("|")]
        assert part.split("\n")[4:8] == rows
        assert "A closing note." not in text
        assert "## Rows" not in text

    def test_accepts_a_missing_record_as_its_fixed_line(self):
        """S5. A record that is not there is named in its section, never
        skipped."""
        text = PR.compose(NAME, {"changelog.md": CHANGELOG, "gaps.md": "# Overview\n"})
        gate = PR.compose(NAME, {"trail/gate.md": "# a gate record\n"})
        assert "`trail/gate.md` holds no run block." in gate.split("\n")
        for line in (
            "`frame/plan.md` is not in this work item.",
            "`trail/phases/` holds no phase record.",
            "`trail/rounds/` holds no round record.",
            "`trail/gate.md` is not in this work item.",
            "`gaps.md` has no `## Not verified` section.",
            "`gaps.md` has no `## Not done` section.",
            "`frame/questions.md` is not in this work item.",
        ):
            assert line in text.split("\n"), line

    def test_accepts_a_missing_changelog_above_the_fold(self):
        """S2 of #1478. Where `changelog.md` is not there, its section and
        the line naming it absent stand under `HEADING` and before the fold,
        where the fragment would stand. Seen red against `_composed` as
        0.37.1 shipped it, which put them inside the fold."""
        texts = {rel: text for rel, text in RECORDS.items() if rel != "changelog.md"}
        lines = PR.compose(NAME, texts).split("\n")
        assert lines[: lines.index(PR.FOLD)] == [
            "## From the records",
            "",
            "## What changed",
            "",
            "`changelog.md` is not in this work item.",
            "",
        ]

    @pytest.mark.parametrize(
        "rel, text, line, said",
        [
            (
                "trail/rounds/round-1.md",
                ROUND_1.replace("verdict: fixed 2222222", "verdict: done"),
                20,
                "verdict: done",
            ),
            (
                "changelog.md",
                CHANGELOG + "## From the records\n",
                3,
                "## From the records",
            ),
            ("changelog.md", CHANGELOG + "<details>\n", 3, "<details>"),
            (
                "trail/gate.md",
                GATE.replace("run: 3333333", "run: HEAD"),
                8,
                "run: HEAD against 4444444",
            ),
            ("gaps.md", GAPS + "</details>\n", 12, "</details>"),
            (
                "changelog.md",
                CHANGELOG + "a sentence with </details> inside it\n",
                3,
                "`</details>`",
            ),
            ("changelog.md", CHANGELOG + "  </details>\n", 3, "`</details>`"),
            ("changelog.md", CHANGELOG + "</DETAILS>\n", 3, "`</DETAILS>`"),
            ("changelog.md", CHANGELOG + "<details open>\n", 3, "`<details open>`"),
            ("changelog.md", CHANGELOG + "a <details/> b\n", 3, "`<details/>`"),
            (
                "changelog.md",
                CHANGELOG + "a sentence <details\n",
                3,
                "holds `<details`, a `details` tag GitHub would read as a second "
                "fold or as the end of the copy's one `<details>`; write it in a "
                "code span",
            ),
            ("frame/plan.md", PLAN + "\n## Phases\n\nagain\n", 14, "## Phases"),
            (
                "changelog.md",
                CHANGELOG
                + "This closes #7.\n\n`Closes #8` in a span.\n\n"
                + "```\nFixes #9\n</details>\n```\n",
                3,
                "#7",
            ),
            ("changelog.md", CHANGELOG + "a note <!-- x --> Closes #5\n", 3, "#5"),
            ("changelog.md", CHANGELOG + "text <!-- Closes #5\n", 3, "#5"),
            (
                "changelog.md",
                CHANGELOG + "<!-- Closes #5\n",
                3,
                "begins with a `<!--` that no `-->` closes on the line",
            ),
            (
                "changelog.md",
                CHANGELOG + "- <!-- note\n",
                3,
                "begins with a `<!--` that no `-->` closes on the line",
            ),
        ],
    )
    def test_refuses_a_record_it_cannot_copy_faithfully(self, rel, text, line, said):
        """S6. A round record `chain_check.py` refuses, a gate record whose
        run block `lib/fields.py` refuses (#1198), a copied line equal
        to `HEADING`, which would put a second boundary line in the copy, a
        copied line holding `<details` or `</details` in any case and
        anywhere in it, followed by whitespace, `/`, `>` or the line's end,
        outside a code span, which GitHub reads as a second fold or the
        fold's end (#1218), a second section of one the body copies, and a
        copied line holding a closing keyword, which would close an issue no
        party claimed, are each refused at the record's path and line, with
        a sentence naming what was read there. A closing keyword in a code
        span, a fence or an HTML comment claims nothing, as
        `lib/closing.py#keywords_in` reads it, one beside a
        comment or after a `<!--` that never closes and stands after text
        still claims, as GitHub reads it (#1404), and a `</details>` in a
        fence ends no fold. A copied line that begins with a `<!--` that no
        `-->` closes on the line, at its start or behind a list marker, is
        refused for the opener, with a keyword after it or without one:
        GitHub hides the lines that follow it, the fold's end among them
        (#1405, and #1408 behind a list marker)."""
        with pytest.raises(PR.Refused) as refused:
            PR.compose(NAME, {**RECORDS, rel: text})
        assert [(where, at) for where, at, _ in refused.value.causes] == [(rel, line)]
        assert said in refused.value.causes[0][2]

    def test_accepts_a_details_tag_in_a_code_span(self):
        """S3 of #1218. A `details` tag in a code span is text to GitHub, and
        the code span is the one spelling of it a copied line passes in; the
        line stands in the copy as written."""
        span = "`</details>` in a span"
        text = PR.compose(NAME, {**RECORDS, "changelog.md": CHANGELOG + span + "\n"})
        assert span in text.split("\n")

    def test_accepts_a_keyword_and_a_details_tag_in_a_closed_comment(self):
        """#1181. GitHub reads neither a closing keyword nor a tag inside a
        comment that closes (#1402, #1403), and the tag and the keyword are
        blanked one way, so each line stands in the copy as written. A line
        that begins with a comment closing on it passes too: GitHub ends that
        HTML block on the same line and reads the text after its `-->`
        (#1407), so nothing below it is hidden."""
        lines = [
            "a note <!-- Closes #5 -->",
            "a note <!-- <details> --> here",
            "<!-- a note --> and text after it",
        ]
        changelog = CHANGELOG + "\n".join(lines) + "\n"
        text = PR.compose(NAME, {**RECORDS, "changelog.md": changelog})
        for line in lines:
            assert line in text.split("\n"), line

    def test_folds_a_section_until_the_body_fits(self):
        """S1 of #1559. A body past GitHub's limit folds its longest section,
        here `## Not verified`, to its heading and one fixed line naming
        `gaps.md`, and then measures within the limit. `## What changed`
        stands whole above the fold, the other sections are copied whole,
        and every line is a record's or a line of `FIXED`. Seen red against
        `_composed` as 0.38.2 shipped it, whose body passed the limit."""
        texts = {**RECORDS, "gaps.md": long_gaps(700)}
        text = PR.compose(NAME, texts)
        assert units(text) <= LIMIT, units(text)
        assert section_of(text, "## Not verified") == [
            "## Not verified",
            "",
            FOLDED.format(path="gaps.md"),
            "",
        ]
        fold = EXPECTED.index(PR.FOLD)
        assert text[:fold] == EXPECTED[:fold]
        for heading in ("## How it was built", "## Review rounds", "## Not done"):
            assert section_of(text, heading) == section_of(EXPECTED, heading)
        assert unsourced(text, texts) == []

    def test_folds_by_the_body_the_first_part_opens(self):
        """D7 of #1559. The fold measures the body the caller writes, the
        first part's files in front of the text `compose` returns, so
        records that fit alone fold behind a long `pr.md`, and the two
        together fit. Seen red with `parts` left out of the measure."""
        texts = {**RECORDS, "gaps.md": long_gaps(400)}
        assert "Not copied here" not in PR.compose(NAME, texts)
        own = OWN + "p" * 20000 + "\n"
        text = PR.compose(NAME, texts, parts=[("pr.md", own)])
        assert FOLDED.format(path="gaps.md") in text.split("\n")
        assert units(own + text) <= LIMIT, units(own + text)

    def test_folds_only_the_longer_of_two_sections_either_of_which_fits(self):
        """S2 of #1559. Where folding either of two long sections would fit
        the body, the longer one folds, here `## Questions`, and the shorter
        one, earlier in the body, is copied whole. Seen red with the sort by
        length removed, where the sections folded in body order and
        `## Not verified` folded."""
        texts = {
            **RECORDS,
            "gaps.md": long_gaps(280),
            "frame/questions.md": long_questions(300),
        }
        text = PR.compose(NAME, texts)
        assert units(text) <= LIMIT, units(text)
        assert section_of(text, "## Questions") == [
            "## Questions",
            "",
            FOLDED.format(path="frame/questions.md"),
            "",
        ]
        assert len(section_of(text, "## Not verified")) > 280

    def test_folds_the_same_sections_with_the_mark_and_without(self):
        """S4 of #1559. A body within the limit without the inspection mark's line
        and past it with the line folds the same sections either way, so
        the body written after the inspection differs from the one written before
        it by the mark and its blank line alone; and a body that fits with
        the line folds nothing either way. Seen red with the mark's room
        removed, where the body without the mark folded nothing, and with
        the room added beside a mark the body holds, where the body that
        fits with the mark folded."""
        mark = PR._mark_line(PR.MANIFEST)[0]
        room = units(mark) + 2
        base = {**RECORDS, "gaps.md": long_gaps(450)}
        plain = PR.compose(NAME, base)
        assert "Not copied here" not in plain
        heading = PR.HEADING + "\n\n"
        for pad, folds in (
            (LIMIT - room // 2 - units(plain), True),
            (LIMIT - room - units(plain), False),
        ):
            texts = {**base, "changelog.md": CHANGELOG + "- " + "y" * (pad - 3) + "\n"}
            without = PR.compose(NAME, texts)
            marked = PR.compose(NAME, texts, mark)
            assert (FOLDED.format(path="gaps.md") in without.split("\n")) is folds
            assert marked == without.replace(heading, f"{heading}{mark}\n\n", 1)
            assert units(marked) <= LIMIT, units(marked)

    def test_folds_the_earlier_of_two_sections_of_one_length(self):
        """D3 of #1559. Of two sections of one length, either of which fits
        the body when folded, the earlier in the body folds, here `## Not
        verified` before `## Not done`. Seen red with the tie given to the
        later section."""
        rows = "".join(
            f"| item {n} {'x' * 90} | the orchestrator |\n" for n in range(330)
        )
        table = "| Item | Who must answer |\n|---|---|\n" + rows
        # `## Not verified` is four characters longer than `## Not done`, and
        # the line `abc` with its line end gives those four back.
        gaps = (
            f"# Closing memo\n\n## Not verified\n\n{table}\n## Not done\n\n{table}abc\n"
        )
        text = PR.compose(NAME, {**RECORDS, "gaps.md": gaps})
        assert section_of(text, "## Not verified") == [
            "## Not verified",
            "",
            FOLDED.format(path="gaps.md"),
            "",
        ]
        assert section_of(text, "## Not done")[-2:] == ["abc", ""]

    def test_refuses_a_copied_line_in_a_section_the_fold_removes(self):
        """S8 of #1559. A copied line `_unfolded` refuses, here one holding a
        `details` tag, is refused at its line in a section that the fold
        removes from the page, so whether a line passes does not hang on
        the length of other records. Seen red with the refusal run over the
        sections as they are folded, where the line passed."""
        gaps = long_gaps(700).replace(
            "| the full suite |", "| the full suite <details> |", 1
        )
        with pytest.raises(PR.Refused) as refused:
            PR.compose(NAME, {**RECORDS, "gaps.md": gaps})
        assert [(where, at) for where, at, _ in refused.value.causes] == [
            ("gaps.md", 7)
        ]
        assert "`<details>`" in refused.value.causes[0][2]

    def test_counts_a_character_outside_the_basic_plane_as_two(self):
        """S10 of #1559. A body within the limit counted in code points and
        past it counted in UTF-16 code units, its rows holding emoji, folds
        a section, so it fits under either count. Seen red with the count
        replaced by `len`, where nothing folded."""
        texts = {**RECORDS, "gaps.md": long_gaps(700, "\U0001f916" * 40)}
        assert sum(map(len, texts.values())) + 10_000 < LIMIT
        assert sum(map(units, texts.values())) > LIMIT
        text = PR.compose(NAME, texts)
        assert FOLDED.format(path="gaps.md") in text.split("\n")
        assert units(text) <= LIMIT, units(text)

    def test_refuses_a_first_part_alone_past_the_limit(self):
        """D5 of #1559. Where the first part alone passes the limit and the
        work item holds no `changelog.md`, the refusal names the one file
        and asks for it to be shortened. Seen red with the refusal's words
        for several files written for one."""
        texts = {rel: text for rel, text in RECORDS.items() if rel != "changelog.md"}
        own = "p" * 70000 + "\n"
        with pytest.raises(PR.Refused) as refused:
            PR.compose(NAME, texts, parts=[("pr.md", own)])
        [(where, line, why)] = refused.value.causes
        assert (where, line) == ("", 0)
        assert why.endswith(
            f"; `pr.md` holds {units(own):,}, so it is shortened before "
            "`iadd pr-body` runs again"
        )


class Test_split:
    def test_accepts_a_body_at_its_first_heading_line(self):
        """S7. Everything before the first line equal to `HEADING`, the
        orchestrator's part, and everything after it, a second such line
        among the records' copy."""
        copy = EXPECTED[EXPECTED.index("\n") + 1 :] + "## From the records\n"
        assert PR.split(OWN + "## From the records\n" + copy) == (OWN, copy)

    def test_refuses_a_body_with_no_heading_line(self):
        """S7. A body with no line equal to `HEADING` is not one the command
        wrote; a heading line with a word after it is no such line, and nor
        is the line of the body 0.25.0 wrote. The refusal names the repair,
        the writing form, which writes the body whole from `pr.md` and the
        records (round 1 of #1148, finding 2)."""
        for body in (
            "## What changed\n\n## From the records, really\n",
            "## What changed\n\n## Not from the records\n",
        ):
            with pytest.raises(PR.Refused) as refused:
                PR.split(body)
            assert refused.value.causes[0][2] == (
                f"no line reads `{PR.HEADING}`, so the body is not one this "
                "command wrote: run `iadd pr-body <item> --body <file>`, which "
                "writes it whole, and check it again"
            ), refused.value.causes


class Test_read_item:
    def test_accepts_a_work_item_as_its_records_by_path(self, tmp_path):
        """The records the generator copies, by their path under the work
        item, read with universal newlines; a file it does not copy is not
        read."""
        item = item_of(
            tmp_path,
            {**RECORDS, "routing.md": "x\n", "trail/rounds/notes.md": "x\n"},
        )
        (item / "gaps.md").write_bytes(GAPS.replace("\n", "\r\n").encode("utf-8"))
        assert PR.read_item(str(item)) == RECORDS

    def test_refuses_a_path_that_is_not_a_directory(self, tmp_path):
        path = tmp_path / "gaps.md"
        path.write_text(GAPS, encoding="utf-8")
        with pytest.raises(PR.Refused):
            PR.read_item(str(path))


class Test_read_own:
    def test_accepts_pr_md_as_its_bytes_stand(self, tmp_path):
        """`pr.md`, a file of the body's first part, is read as its text
        with its line ends as they stand, and a file whose last line has no
        line end gets one, so the heading after it stands on its own line.
        Seen red with the line end's addition alone removed, where the
        heading joined the last line."""
        item = item_of(tmp_path, RECORDS)
        assert PR.read_own(str(item)) == OWN
        (item / "pr.md").write_bytes(b"Closes #1.")
        assert PR.read_own(str(item)) == "Closes #1.\n"

    def test_refuses_a_line_equal_to_the_heading(self, tmp_path):
        """A line of `pr.md` equal to `HEADING` would split the body at
        `pr.md`'s line rather than at the heading the command writes, so it
        is refused at that line of `pr.md`."""
        item = item_of(tmp_path, RECORDS, own=OWN + "## From the records\n")
        with pytest.raises(PR.Refused) as refused:
            PR.read_own(str(item))
        assert refused.value.causes == [
            (
                "pr.md",
                4,
                "reads `## From the records`, the line the body's two parts split at",
            )
        ]

    def test_refuses_a_pr_md_that_is_not_utf_8(self, tmp_path):
        """A `pr.md` that does not decode as UTF-8 is refused at `pr.md`,
        with no line, rather than raising out of the command, whose `main`
        catches `Refused` alone. Seen red with `UnicodeDecodeError` taken
        out of the `except` in `read_own`, where the decode error escaped."""
        item = item_of(tmp_path, RECORDS)
        (item / "pr.md").write_bytes(b"Closes #1.\n\xff\n")
        with pytest.raises(PR.Refused) as refused:
            PR.read_own(str(item))
        ((where, line, why),) = refused.value.causes
        assert (where, line) == ("pr.md", 0)
        assert why.startswith("cannot be read as UTF-8 text ("), why


NOT_YES = (
    "`Pull request inspection mark` reads `{value}`, not `yes`, so the key is not "
    "read and the body carries no inspection mark"
)
NO_FIELD = (
    "`.claude-plugin/plugin.json` has no `{field}`, so the mark's address is "
    "not built and the body carries no inspection mark"
)


class Test_inspection_mark:
    """#1204. The mark under the heading, where the repository's row reads
    `yes` and the work item is cleared at HEAD."""

    def test_accepts_an_inspection_only_its_own_record_follows(self, repo, tmp_path):
        """S1. The row reads `yes`, the newest block reads `cleared` at a
        commit only the inspection's own commit follows, and the line is the
        manifest's `repository`, `/raw/HEAD/` and `icon` path."""
        item = cleared_item(repo)
        manifest = manifest_of(tmp_path, MANIFEST)
        assert PR.inspection_mark(str(item), str(repo), manifest) == (MARK_LINE, None)

    def test_accepts_one_mark_line_from_two_releases_of_the_plugin(
        self, repo, tmp_path
    ):
        """#1452, *Scope* item 6 and S10. The installed plugin writes the
        body and the check's copy composes it again, and the two can be
        different releases. A manifest with a `version` and one with none
        give one mark line, the icon at the repository's default branch, so
        the address reads no version and the manifest need not hold one
        (round-1#4). Seen red with `version` put back into `MARK_FIELDS`,
        where the second manifest gave no line and the set held None."""
        item = cleared_item(repo)
        (tmp_path / "older").mkdir()
        (tmp_path / "newer").mkdir()
        older = manifest_of(tmp_path / "older", MANIFEST)
        newer = manifest_of(
            tmp_path / "newer",
            {key: value for key, value in MANIFEST.items() if key != "version"},
        )
        lines = {PR.inspection_mark(str(item), str(repo), m)[0] for m in (older, newer)}
        assert lines == {MARK_LINE}

    def test_accepts_the_plugins_own_manifest(self, repo):
        """S1's address read from the manifest three directories above the
        script, the plugin's own, which this reads and never writes."""
        with open(PR.MANIFEST, encoding="utf-8") as handle:
            own = json.load(handle)
        src = f"{own['repository']}/raw/HEAD/{own['icon'][2:]}"
        item = cleared_item(repo)
        assert PR.inspection_mark(str(item), str(repo)) == (
            f'<img src="{src}" alt="Cleared" width="128">',
            None,
        )

    @pytest.mark.parametrize(
        "verdict",
        [
            None,
            "Verdict: withheld reason: a claim does not hold",
            "Verdict: undecided question: which one?",
            "Verdict: done",
            f"{CLEARED}\n```\n\n```seal\nVerdict: done",
        ],
        ids=[
            "no inspection",
            "withheld",
            "undecided",
            "a refused block",
            "a refused block after a cleared one",
        ],
    )
    def test_refuses_a_work_item_not_cleared_saying_nothing(
        self, repo, tmp_path, verdict
    ):
        """S2. No inspection, a newest block reading `withheld` or
        `undecided`, and a file `lib/fields.py` refuses a line of,
        after a cleared block too: no mark, and no line, since the inspector and
        the pull request's check name those. The last seen red with the
        refusal's read alone removed, where the mark stood."""
        item = cleared_item(repo, verdict=verdict)
        manifest = manifest_of(tmp_path, MANIFEST)
        assert PR.inspection_mark(str(item), str(repo), manifest) == (None, None)

    def test_refuses_an_inspection_a_later_commit_follows(self, repo, tmp_path):
        """S3. A commit outside the closing records after the cleared one, a
        repair nobody cleared: no mark. Seen red with the `follows` condition
        alone removed, where the mark stood."""
        item = cleared_item(repo)
        write(repo, "f.txt", "a repair\n")
        git_in(repo, "commit", "-qam", "a repair")
        manifest = manifest_of(tmp_path, MANIFEST)
        assert PR.inspection_mark(str(item), str(repo), manifest) == (None, None)

    def test_refuses_an_inspection_whose_base_does_not_resolve(self, repo, tmp_path):
        """S3's class: `follows` lists the later commits against the base,
        and a base this repository cannot resolve lists none, so a lapsed
        inspection would read as one cleared at HEAD. No mark, and the base named. Seen red
        with the base's read alone removed, where the mark stood."""
        item = cleared_item(repo, base="no-such-base")
        write(repo, "f.txt", "a repair\n")
        git_in(repo, "commit", "-qam", "a repair")
        manifest = manifest_of(tmp_path, MANIFEST)
        assert PR.inspection_mark(str(item), str(repo), manifest) == (
            None,
            "the inspection names the base `no-such-base`, which this "
            "repository cannot resolve, so whether it has lapsed is not read "
            "and the body carries no inspection mark",
        )

    @pytest.mark.parametrize("held", ["off", "unseen"])
    def test_refuses_an_inspection_head_does_not_hold_naming_it(
        self, repo, tmp_path, held
    ):
        """Round 1's finding 1's class. An inspection cleared at a commit HEAD
        does not descend from, as a local-mode work item read from another
        branch's checkout, or at one this repository cannot resolve: whether
        the inspection has lapsed cannot be read there, so no mark, and the commit
        and the checkout named. Seen red with the naming alone removed,
        where nothing was said."""
        item = cleared_item(repo)
        inspection = item / "inspection.md"
        if held == "off":
            text = inspection.read_text(encoding="utf-8")
            cleared = re.search(r"target: (\S+)", text).group(1)
            git_in(repo, "reset", "-q", "--soft", "HEAD~2")
        else:
            cleared = "f" * 40
            text = inspection.read_text(encoding="utf-8")
            inspection.write_text(
                re.sub(r"target: \S+", f"target: {cleared}", text), encoding="utf-8"
            )
        manifest = manifest_of(tmp_path, MANIFEST)
        assert PR.inspection_mark(str(item), str(repo), manifest) == (
            None,
            f"the inspection is cleared at `{cleared}`, which HEAD in {repo} does "
            "not hold, so whether it has lapsed is not read and the body "
            "carries no inspection mark",
        )

    @pytest.mark.parametrize(
        "row, said",
        [
            (None, None),
            ([("Pull request inspection mark", "")], None),
            ([("Pull request inspection mark", "Yes")], NOT_YES.format(value="Yes")),
            ([("Pull request inspection mark", "on")], NOT_YES.format(value="on")),
            ([("Pull request inspection mark", "true")], NOT_YES.format(value="true")),
            (
                ROW + ROW,
                "`Pull request inspection mark` is not read: `Pull request inspection mark` "
                "appears 2 times — one value; the body carries no inspection mark",
            ),
        ],
        ids=["absent", "empty", "Yes", "on", "true", "written twice"],
    )
    def test_refuses_a_row_other_than_yes(self, repo, tmp_path, row, said):
        """S4. Only `yes`, exactly so, turns the mark on. An absent or empty
        row says nothing; any other value, and a refused row, is named as
        not read. The `Yes` case seen red with the comparison alone
        case-folded, where the mark stood."""
        item = cleared_item(repo, row=row)
        manifest = manifest_of(tmp_path, MANIFEST)
        assert PR.inspection_mark(str(item), str(repo), manifest) == (None, said)

    @pytest.mark.parametrize("field", ["repository", "icon"])
    def test_refuses_a_manifest_lacking_a_field(self, repo, tmp_path, field):
        """S5. A manifest the address cannot be built from: no mark, and
        the field named."""
        item = cleared_item(repo)
        lacking = {key: value for key, value in MANIFEST.items() if key != field}
        manifest = manifest_of(tmp_path, lacking)
        assert PR.inspection_mark(str(item), str(repo), manifest) == (
            None,
            NO_FIELD.format(field=field),
        )

    def test_refuses_a_manifest_that_is_not_json(self, repo, tmp_path):
        """S5. A manifest that will not read: no mark, and it named."""
        item = cleared_item(repo)
        manifest = tmp_path / "plugin.json"
        manifest.write_text("{", encoding="utf-8")
        mark, said = PR.inspection_mark(str(item), str(repo), str(manifest))
        assert mark is None
        assert said.startswith("`.claude-plugin/plugin.json` is not read ("), said


class Test_main:
    def test_a_script_copied_alone_exits_2_and_names_what_it_misses(self, tmp_path):
        """S4 of #1482. A copy of this script taken without its siblings
        exits 2, with the loader's one sentence naming the absent
        `lib/sibling.py` by its path: 2 means nothing was read, and a
        sibling that is not beside the command is that kind. It printed a
        line of its own before."""
        alone = tmp_path / "alone"
        alone.mkdir()
        copy = alone / TARGET.rsplit("/", 1)[1]
        with open(os.path.join(ROOT, *TARGET.split("/")), encoding="utf-8") as f:
            copy.write_text(f.read(), encoding="utf-8")
        repo = tmp_path / "repo"
        repo.mkdir()
        done = subprocess.run(
            [sys.executable, str(copy), str(repo)],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            cwd=str(repo),
        )
        assert done.returncode == 2, (done.returncode, done.stderr)
        lib = os.path.join(str(alone), "..", "..", "..", "lib", "sibling.py")
        said = PR.sibling.MISSING.format(path=os.path.normpath(lib))
        assert done.stderr == said + "\n", done.stderr

    def test_accepts_a_cleared_work_item_with_the_mark_under_the_heading(
        self, repo, tmp_path, monkeypatch, capsys
    ):
        """S1 through the command, run in the repository: the part opens
        with a blank line, the mark, a blank line and the changelog's
        section, `--check` on that body exits 0, and nothing is said about
        the mark."""
        item = cleared_item(repo)
        monkeypatch.setattr(PR, "MANIFEST", manifest_of(tmp_path, MANIFEST))
        monkeypatch.chdir(repo)
        body = tmp_path / "pr-body.md"
        assert PR.main([str(item), "--body", str(body)]) == 0
        marked = EXPECTED.replace(
            "## From the records\n\n", f"## From the records\n\n{MARK_LINE}\n\n", 1
        )
        assert body.read_bytes() == (OWN + marked).encode("utf-8")
        assert PR.main([str(item), "--body", str(body), "--check"]) == 0
        assert "iadd pr-body:" not in capsys.readouterr().out

    def test_accepts_a_cleared_work_item_run_from_another_checkout(
        self, repo, tmp_path, monkeypatch, capsys
    ):
        """Round 1's finding 1. The orchestrator runs from the main checkout
        and reaches the work item in a linked worktree, whose branch the
        main checkout's HEAD does not hold. The row, the base and HEAD are
        read in the work item's own checkout, so the body carries the mark
        as it does when run from the worktree. Seen red with the root read
        from the working directory alone, as it was: no mark."""
        write(mark_root(repo / "seal"), "config.json", config_json(*LANGUAGES, *ROW))
        git_in(repo, "add", "-A")
        git_in(repo, "commit", "-qm", "the row")
        worktree = tmp_path / "worktree"
        git_in(repo, "worktree", "add", "-q", "-b", "feat/1-x", str(worktree))
        item = cleared_item(worktree)
        monkeypatch.setattr(PR, "MANIFEST", manifest_of(tmp_path, MANIFEST))
        monkeypatch.chdir(repo)
        body = tmp_path / "pr-body.md"
        assert PR.main([str(item), "--body", str(body)]) == 0
        marked = EXPECTED.replace(
            "## From the records\n\n", f"## From the records\n\n{MARK_LINE}\n\n", 1
        )
        assert body.read_bytes() == (OWN + marked).encode("utf-8")
        assert "iadd pr-body:" not in capsys.readouterr().out

    def test_accepts_a_local_mode_work_item_from_the_working_directorys_checkout(
        self, repo, tmp_path, monkeypatch, capsys
    ):
        """Round 1's finding 1, local mode. The work item sits under the
        common git directory, where git finds no checkout, so the row, the
        base and HEAD are read in the working directory's checkout, and an
        inspection cleared at its HEAD carries the mark. Seen red with that fallback alone
        removed: no mark."""
        home = mark_root(repo / ".git" / "seal")
        write(home, "config.json", config_json(*LANGUAGES, *ROW))
        item = home / "threads" / NAME
        for rel, text in RECORDS.items():
            write(item, rel, text)
        (item / "pr.md").write_bytes(OWN.encode("utf-8"))
        sha = git_in(repo, "rev-parse", "HEAD")
        write(
            item,
            "inspection.md",
            f"# Inspection: {NAME}\n\n```seal\ntarget: {sha} against feature/x\n"
            f"{CLEARED}\n```\n",
        )
        monkeypatch.setattr(PR, "MANIFEST", manifest_of(tmp_path, MANIFEST))
        monkeypatch.chdir(repo)
        body = tmp_path / "pr-body.md"
        assert PR.main([str(item), "--body", str(body)]) == 0
        marked = EXPECTED.replace(
            "## From the records\n\n", f"## From the records\n\n{MARK_LINE}\n\n", 1
        )
        assert body.read_bytes() == (OWN + marked).encode("utf-8")
        assert "iadd pr-body:" not in capsys.readouterr().out

    def test_refuses_the_mark_on_a_row_other_than_yes_and_exits_0(
        self, repo, tmp_path, monkeypatch, capsys
    ):
        """S4 through the command: the row named as not read on one line
        before `wrote:`, the body today's, and exit 0."""
        item = cleared_item(repo, row=[("Pull request inspection mark", "Yes")])
        monkeypatch.chdir(repo)
        body = tmp_path / "pr-body.md"
        assert PR.main([str(item), "--body", str(body)]) == 0
        out = capsys.readouterr().out.splitlines()
        assert out[0] == "iadd pr-body: " + NOT_YES.format(value="Yes")
        assert out[1].startswith("wrote: ")
        assert body.read_bytes() == (OWN + EXPECTED).encode("utf-8")

    def test_accepts_pr_md_above_the_heading_whatever_the_body_held(
        self, tmp_path, capsys
    ):
        """S8, and the scenario *The body opens with `pr.md`* of the work item
        that made `pr.md` the first part. The body file is written as
        `pr.md`'s bytes, a CRLF line among them, then the heading, then the
        copy, whatever the file held before: a first part of its own and a
        stale copy are both replaced, and a missing file is written whole.
        Seen red against `pr_body.py` as 0.33.0 shipped it, which kept the file's
        own first part and wrote none where there was no file."""
        item = item_of(tmp_path, RECORDS)
        body = tmp_path / "pr-body.md"
        stale = EXPECTED.replace("the reader | its cases", "the reader | nothing")
        body.write_bytes(("A first part of its own.\n\n" + stale).encode("utf-8"))
        capsys.readouterr()
        assert PR.main([str(item), "--body", str(body)]) == 0
        assert body.read_bytes() == (OWN + EXPECTED).encode("utf-8")
        assert capsys.readouterr().out == (
            f"wrote: {body} from {item}'s `pr.md` and records\n"
        )
        fresh = tmp_path / "fresh.md"
        assert PR.main([str(item), "--body", str(fresh)]) == 0
        assert fresh.read_bytes() == (OWN + EXPECTED).encode("utf-8")

    def test_accepts_the_written_body_under_check_and_writes_nothing(
        self, tmp_path, capsys
    ):
        """S9. The file S8 writes is `pr.md` above the heading and what the
        records give below it, and the check says so and writes nothing."""
        item = item_of(tmp_path, RECORDS)
        body = tmp_path / "pr-body.md"
        assert PR.main([str(item), "--body", str(body)]) == 0
        written = body.read_bytes()
        capsys.readouterr()
        assert PR.main([str(item), "--body", str(body), "--check"]) == 0
        assert body.read_bytes() == written
        assert capsys.readouterr().out == (
            f"matches: {body} is `pr.md` above `{PR.HEADING}` and the records' "
            "text below it\n"
        )

    @pytest.mark.parametrize(
        "old, new, said",
        [
            (
                b"Closes #1.",
                b"Closes #2.",
                "refused: pr-body.md:3: reads `Closes #2.`; pr.md gives `Closes #1.`\n",
            ),
            (
                b"\nCloses #1.\n",
                b"\nCloses #1.\nA sentence of the orchestrator's own.\n",
                "refused: pr-body.md:4: reads `A sentence of the orchestrator's "
                "own.`, which pr.md does not give\n",
            ),
            (
                b"\nCloses #1.\n",
                b"\n",
                "refused: pr-body.md:3: lacks `Closes #1.`, which pr.md gives\n",
            ),
            (
                b"\nCloses #1.\n",
                b"\nCloses #1.\nA sentence of its own.\nAnother of its own.\n",
                "refused: pr-body.md:4: reads `A sentence of its own.`, then "
                "`Another of its own.`, which pr.md does not give\n",
            ),
            (
                b"\r\n\nCloses #1.\n",
                b"\r\n",
                "refused: pr-body.md:2: lacks ``, then `Closes #1.`, which pr.md "
                "gives\n",
            ),
        ],
        ids=[
            "a line changed",
            "a line added",
            "a line taken out",
            "two lines added",
            "two lines taken out",
        ],
    )
    def test_refuses_a_first_part_that_is_not_pr_md_naming_its_line(
        self, tmp_path, capsys, old, new, said
    ):
        """The scenario *A first part that is not `pr.md` is refused*. A
        body whose part above the heading differs from `pr.md` at one line,
        changed, added or taken out, exits 1 on one `refused:` line naming
        that line of the body, counted from its first line, and the line
        `pr.md` gives where it gives one; the file is left as it stood. Seen
        red with the comparison of the first part removed, where the check
        exited 0. A run of lines added or taken out is one `refused:` line
        naming every line of the run (#1452, *Scope* item 2); seen red
        against the comparison that named the run's first line alone."""
        item = item_of(tmp_path, RECORDS)
        body = tmp_path / "pr-body.md"
        assert PR.main([str(item), "--body", str(body)]) == 0
        edited = body.read_bytes().replace(old, new, 1)
        body.write_bytes(edited)
        capsys.readouterr()
        assert PR.main([str(item), "--body", str(body), "--check"]) == 1
        assert capsys.readouterr().out == said
        assert body.read_bytes() == edited

    @pytest.mark.parametrize("check", [False, True], ids=["write", "check"])
    def test_refuses_a_work_item_with_no_pr_md(self, tmp_path, capsys, check):
        """The scenario *A work item with no `pr.md` is refused*. Either form
        exits 1 on one `refused:` line naming `pr.md` by its path under the
        `seal/` root and the repair, and leaves the body file as it stood.
        Seen red against `pr_body.py` as 0.33.0 shipped it, where both forms
        exited 0."""
        item = item_of(tmp_path, RECORDS, own=None)
        body = tmp_path / "pr-body.md"
        body.write_bytes(EXPECTED.encode("utf-8"))
        capsys.readouterr()
        argv = [str(item), "--body", str(body)] + (["--check"] if check else [])
        assert PR.main(argv) == 1
        assert capsys.readouterr().out == (
            f"refused: seal/threads/{NAME}/pr.md: is not there; the orchestrator "
            "writes it before the first round\n"
        )
        assert body.read_bytes() == EXPECTED.encode("utf-8")

    @pytest.mark.parametrize("check", [False, True], ids=["write", "check"])
    def test_refuses_a_quote_its_source_no_longer_holds_naming_its_line(
        self, tmp_path, capsys, check
    ):
        """A1 of #1612. A quote of `pr.md` whose words `frame/plan.md` no
        longer holds, after a fix rewrote the row, is refused by either form
        at `pr.md`'s line, naming the file that does not hold it, and the
        body file is left as it stood. Seen red against `first_part` as
        0.38.8 shipped it, where both forms exited 0."""
        own = '- "the writer | its cases" (`frame/plan.md` *Phases*, row 2)\n'
        records = {**RECORDS, "frame/plan.md": PLAN.replace("the writer", "the pen")}
        item = item_of(tmp_path, records, own=own + "\nCloses #1.\n")
        body = tmp_path / "pr-body.md"
        body.write_bytes(EXPECTED.encode("utf-8"))
        capsys.readouterr()
        argv = [str(item), "--body", str(body)] + (["--check"] if check else [])
        assert PR.main(argv) == 1
        assert capsys.readouterr().out == (
            f"refused: seal/threads/{NAME}/pr.md:1: quotes words `frame/plan.md` "
            "does not hold, with runs of whitespace collapsed; the orchestrator "
            "rewrites the quote from the record as it stands\n"
        )
        assert body.read_bytes() == EXPECTED.encode("utf-8")

    def test_accepts_a_quote_that_stands_across_a_line_break(self, tmp_path, capsys):
        """A2 of #1612. A quote whose words stand in its source with a line
        break and an indent where the quote has one space, and one space
        where the quote has two, passes both forms, which print no note."""
        design = "# Design\n\nThe body copies\n  the records, and composes none.\n"
        own = (
            '- "copies the records,  and composes none." '
            "(`frame/design.md` *Design*, line 3)\n\nCloses #1.\n"
        )
        item = item_of(tmp_path, {**RECORDS, "frame/design.md": design}, own=own)
        body = tmp_path / "pr-body.md"
        capsys.readouterr()
        assert PR.main([str(item), "--body", str(body)]) == 0
        assert capsys.readouterr().out == (
            f"wrote: {body} from {item}'s `pr.md` and records\n"
        )
        assert PR.main([str(item), "--body", str(body), "--check"]) == 0
        assert capsys.readouterr().out.startswith(f"matches: {body} is `pr.md`")

    @pytest.mark.parametrize(
        "path",
        ["frame/nothing.md", "../../config.json", "/frame/plan.md"],
        ids=["absent", "outside", "absolute"],
    )
    @pytest.mark.parametrize("check", [False, True], ids=["write", "check"])
    def test_refuses_a_quote_of_a_file_the_item_does_not_hold(
        self, tmp_path, capsys, check, path
    ):
        """A3 of #1612. A quote whose path names no file of the work item's
        directory is refused by either form at its line, naming the path:
        one that is not there, the root's `config.json`, a file that stands
        outside the directory, and an absolute path, which names no file
        under it whatever file the path ends in. Seen red against `first_part` as
        0.38.8 shipped it, where both forms exited 0."""
        own = f'- "English" (`{path}`, line 2)\n\nCloses #1.\n'
        item = item_of(tmp_path, RECORDS, own=own)
        body = tmp_path / "pr-body.md"
        body.write_bytes(EXPECTED.encode("utf-8"))
        capsys.readouterr()
        argv = [str(item), "--body", str(body)] + (["--check"] if check else [])
        assert PR.main(argv) == 1
        assert capsys.readouterr().out == (
            f"refused: seal/threads/{NAME}/pr.md:1: names `{path}`, which is not "
            "a file of the work item's directory\n"
        )

    def test_refuses_a_quote_of_a_file_that_is_not_utf_8(self, tmp_path, capsys):
        """*Scope* item 1 of #1612. A quote whose file will not read as
        UTF-8 text is refused at its line, naming the path and the error,
        and the run does not end on the decode error."""
        own = '- "English" (`frame/design.md`, line 1)\n\nCloses #1.\n'
        item = item_of(tmp_path, RECORDS, own=own)
        (item / "frame" / "design.md").write_bytes(b"\xff English\n")
        body = tmp_path / "pr-body.md"
        capsys.readouterr()
        assert PR.main([str(item), "--body", str(body)]) == 1
        assert capsys.readouterr().out.startswith(
            f"refused: seal/threads/{NAME}/pr.md:1: names `frame/design.md`, "
            "which cannot be read as UTF-8 text ("
        )

    @pytest.mark.parametrize(
        "own, named",
        [
            (
                '"words no record holds." (`changelog.md`, line 1)\n'
                '- a list item\n  - "nor these." (`changelog.md`, line 2)\n'
                '- " (`changelog.md`, line 1)\n'
                '- "nor these." (`changelog.md, line 1)\n'
                '- "nor these." (``, line 1)\n'
                '- "nor these." (`changelog.md`, line 1\n'
                "\nCloses #1.\n",
                "lines 1, 3, 4, 5, 6 and 7 of `pr.md`, which hold",
            ),
            (
                '"words no record holds." (`changelog.md`, line 1)\n\nCloses #1.\n',
                "line 1 of `pr.md`, which holds",
            ),
        ],
        ids=["six lines", "one line"],
    )
    def test_names_a_line_that_looks_like_a_quote_and_decides_nothing(
        self, tmp_path, capsys, own, named
    ):
        """A4 of #1612. A line holding `" (` before a backtick outside the
        quote form is named on the line opening `iadd pr-body:` by both
        forms as a line not read, and decides nothing: no quote among them
        stands in `changelog.md`, and both forms exit 0. The lines lack the
        list marker, stand indented under a list item, hold a `" (` that is
        the opening quote's own mark, lack the path's closing backtick,
        name an empty path, and lack the `)` at the line's end. Seen red
        against `first_part` as 0.38.8 shipped it, which printed no
        note."""
        item = item_of(tmp_path, RECORDS, own=own)
        body = tmp_path / "pr-body.md"
        note = (
            f"iadd pr-body: not read as a quote: {named} "
            '`" (` before a backtick outside the form '
            '`- "<quote>" (`<path>` <coordinate>)`\n'
        )
        capsys.readouterr()
        assert PR.main([str(item), "--body", str(body)]) == 0
        assert capsys.readouterr().out == (
            f"{note}wrote: {body} from {item}'s `pr.md` and records\n"
        )
        assert PR.main([str(item), "--body", str(body), "--check"]) == 0
        assert capsys.readouterr().out.startswith(f"{note}matches: {body} is ")

    @pytest.mark.parametrize(
        "rows, missing",
        [
            (LANGUAGES[1:], ["Commit and pull request language"]),
            (LANGUAGES[:1], ["Record language"]),
            (
                [*LANGUAGES[:1], ("Record language", "")],
                ["Record language"],
            ),
            ([], ["Commit and pull request language", "Record language"]),
        ],
        ids=["no commit row", "no record row", "an empty record row", "neither row"],
    )
    @pytest.mark.parametrize("check", [False, True], ids=["write", "check"])
    def test_refuses_a_repository_without_a_language_row_naming_it(
        self, tmp_path, capsys, rows, missing, check
    ):
        """#1453, *Scope* item 3, the scenario *`iadd pr-body` refuses
        without a row*. Either form exits 1, leaves the body file as it
        stood, and prints one `refused:` line for each key that names no
        language, absent or empty, naming `config.json` by its path under the
        `seal/` root, the key, and the section of the template that says
        what it governs. Seen red against `pr_body.py` as the merged base
        left it, where both forms exited 0."""
        item = item_of(tmp_path, RECORDS, rows=rows)
        body = tmp_path / "pr-body.md"
        body.write_bytes((OWN + EXPECTED).encode("utf-8"))
        capsys.readouterr()
        argv = [str(item), "--body", str(body)] + (["--check"] if check else [])
        assert PR.main(argv) == 1
        assert capsys.readouterr().out == "".join(
            f"refused: seal/config.json: names no language in a `{row}` key; "
            f"`templates/setup/config.md` *{row}* says what the key governs, "
            "and the orchestrator asks for it before the first edit\n"
            for row in missing
        )
        assert body.read_bytes() == (OWN + EXPECTED).encode("utf-8")

    @pytest.mark.parametrize(
        "unread, said",
        [
            ("directory", "is there and cannot be read as UTF-8 text ("),
            (
                "doubled",
                "`Record language` appears 2 times — one value",
            ),
            ("unparseable", "does not parse as JSON ("),
        ],
        ids=[
            "a config that will not read",
            "a row written twice",
            "a config that will not parse",
        ],
    )
    def test_refuses_a_language_row_no_one_reads_naming_no_machine_path(
        self, tmp_path, capsys, unread, said
    ):
        """#1453, *Data & interfaces*: a `config.json` that will not read or
        parse, and a key written twice, reach the command as a refusal at
        `config.json`, in `lib/config.py`'s sentence. The file is named once,
        by its path under the `seal/` root and not by the machine's, since
        the inspector copies the line into a committed `inspection.md`. Seen red
        against `pr_body.py` as the merged base left it, where the command
        exited 0."""
        rows = [*LANGUAGES, ("Record language", "English")]
        item = item_of(tmp_path, RECORDS, rows=rows)
        config = tmp_path / "seal" / "config.json"
        if unread == "directory":
            config.unlink()
            config.mkdir()
        elif unread == "unparseable":
            config.write_text('{"Record language": "English",}\n', encoding="utf-8")
        body = tmp_path / "pr-body.md"
        capsys.readouterr()
        assert PR.main([str(item), "--body", str(body)]) == 1
        [line] = capsys.readouterr().out.splitlines()
        assert line.startswith(f"refused: seal/config.json: {said}"), line
        assert str(tmp_path) not in line

    @pytest.mark.parametrize(
        "rows, translations, first, names",
        [
            (
                DIFFERING,
                {"pr.ko.md": TRANSLATION},
                TRANSLATION + "\n" + OWN,
                "`pr.ko.md` then `pr.md`",
            ),
            (
                [
                    ("Commit and pull request language", "Korean"),
                    ("Record language", "korean"),
                ],
                {},
                OWN,
                "`pr.md`",
            ),
            (
                LANGUAGES,
                {"pr.en.md": "A mirror.\n"},
                OWN + "A mirror.\n",
                "`pr.md` then `pr.en.md`",
            ),
        ],
        ids=[
            "rows that differ",
            "one language in two cases",
            "one language and a pr.en.md",
        ],
    )
    def test_accepts_the_first_part_the_rows_ask_for(
        self, tmp_path, capsys, rows, translations, first, names
    ):
        """#1453, *Scope* item 3, the scenario *The body opens in the team's
        language*. Where the keys name different languages, the body file
        holds the one `pr.*.md`, given a line end after its last line, then
        `pr.md`, then the heading and the copy; where they name one
        language, compared with case folded, `pr.md` leads and a `pr.*.md`
        follows it. `wrote:` and `--check`'s `matches:` name the files in
        that order. The first and third seen red against `pr_body.py` as the
        merged base left it, which wrote `pr.md` alone; the second is the
        case fold's, seen red with `casefold` taken out of the comparison."""
        item = item_of(tmp_path, RECORDS, rows=rows, translations=translations)
        body = tmp_path / "pr-body.md"
        capsys.readouterr()
        assert PR.main([str(item), "--body", str(body)]) == 0
        assert body.read_bytes() == (first + EXPECTED).encode("utf-8")
        assert PR.main([str(item), "--body", str(body), "--check"]) == 0
        assert capsys.readouterr().out == (
            f"wrote: {body} from {item}'s {names} and records\n"
            f"matches: {body} is {names} above `{PR.HEADING}` and the records' "
            "text below it\n"
        )

    @pytest.mark.parametrize(
        "translations, said",
        [
            (
                {},
                "`Commit and pull request language` reads `Korean` and `Record "
                "language` reads `English`, and no `pr.<lang>.md` stands beside "
                "`pr.md`; the orchestrator writes it before the first round",
            ),
            (
                {"pr.ko.md": TRANSLATION, "pr.ja.md": "A rendering.\n"},
                "holds 2 files matching `pr.*.md`, `pr.ja.md` and `pr.ko.md`, and "
                "one body has one translation",
            ),
        ],
        ids=["none", "two"],
    )
    @pytest.mark.parametrize("check", [False, True], ids=["write", "check"])
    def test_refuses_rows_that_differ_without_one_translation(
        self, tmp_path, capsys, translations, said, check
    ):
        """#1453, *Scope* item 3, the scenarios *A missing translation is
        refused* and *Two translations are refused*. Where the keys name
        different languages and the work item holds no `pr.*.md`, or more
        than one, either form exits 1 on one `refused:` line on the work
        item's directory, naming the two keys, or the count and the files,
        and leaves the body file as it stood. Seen red against `pr_body.py`
        as the merged base left it, where both forms exited 0."""
        item = item_of(tmp_path, RECORDS, rows=DIFFERING, translations=translations)
        body = tmp_path / "pr-body.md"
        body.write_bytes((OWN + EXPECTED).encode("utf-8"))
        capsys.readouterr()
        argv = [str(item), "--body", str(body)] + (["--check"] if check else [])
        assert PR.main(argv) == 1
        assert capsys.readouterr().out == f"refused: seal/threads/{NAME}: {said}\n"
        assert body.read_bytes() == (OWN + EXPECTED).encode("utf-8")

    @pytest.mark.parametrize(
        "first, said",
        [
            (
                OWN,
                f"refused: pr-body.md:1: lacks `{TRANSLATION}`, which pr.ko.md gives\n",
            ),
            (
                TRANSLATION.replace("쓴다", "썼다") + "\n" + OWN,
                f"refused: pr-body.md:1: reads `{TRANSLATION.replace('쓴다', '썼다')}`; "
                f"pr.ko.md gives `{TRANSLATION}`\n",
            ),
            (
                "A line of its own.\n" + TRANSLATION + "\n" + OWN,
                "refused: pr-body.md:1: reads `A line of its own.`, which "
                "pr.ko.md and pr.md do not give\n",
            ),
        ],
        ids=["the translation left out", "a line of it changed", "a line added"],
    )
    def test_refuses_a_first_part_that_is_not_the_translation_then_pr_md(
        self, tmp_path, capsys, first, said
    ):
        """#1453, *Scope* item 3, the scenario *A body without the translation
        fails the check*. Where the keys differ, `--check` compares the whole
        first part, `pr.ko.md` and then `pr.md`, line by line: a body whose
        first part is `pr.md` alone, and one whose line of the translation
        was changed, exit 1 at the body's first line, naming the file that
        gives the line, and a line of the body's own is named with both
        files, neither of which gives it. Seen red against `pr_body.py` as
        the merged base left it, where the first exited 0 and the other two
        named `pr.md` alone."""
        item = item_of(
            tmp_path, RECORDS, rows=DIFFERING, translations={"pr.ko.md": TRANSLATION}
        )
        body = tmp_path / "pr-body.md"
        body.write_bytes((first + EXPECTED).encode("utf-8"))
        capsys.readouterr()
        assert PR.main([str(item), "--body", str(body), "--check"]) == 1
        assert capsys.readouterr().out == said

    def test_refuses_an_edited_copy_naming_both_lines(self, tmp_path, capsys):
        """S9, the class of #857's withheld item 5, a changelog fact restated
        wrongly: one sentence of the copied changelog changed is refused at
        the body's line, counted from the body's first line, `pr.md`'s lines
        above the heading among them, with the record's line it should
        read."""
        item = item_of(tmp_path, RECORDS)
        body = tmp_path / "pr-body.md"
        edited = EXPECTED.replace(
            "`iadd pr-body` writes it", "`iadd pr-body` drafts it"
        )
        body.write_bytes((OWN + edited).encode("utf-8"))
        capsys.readouterr()
        assert PR.main([str(item), "--body", str(body), "--check"]) == 1
        out = capsys.readouterr().out
        assert out.startswith("refused: pr-body.md:10: ")
        assert "`changelog.md:1`" in out
        assert body.read_bytes() == (OWN + edited).encode("utf-8")

    def test_refuses_the_changelog_inside_the_fold_until_written_again(
        self, tmp_path, capsys
    ):
        """S4 of #1478. A body holding the changelog's section inside the
        fold, as 0.37.1 composed it, exits 1 under `--check`, each
        `refused:` line naming the body file and the body's line; once the
        command writes the file again, `--check` exits 0. Seen red against
        `_composed` as 0.37.1 shipped it, where that body matched."""
        item = item_of(tmp_path, RECORDS)
        changed = EXPECTED[EXPECTED.index("## What changed") : EXPECTED.index(PR.FOLD)]
        fold = EXPECTED[EXPECTED.index(PR.FOLD) : EXPECTED.index("## How it was built")]
        stale = EXPECTED.replace(changed + fold, fold + changed, 1)
        assert stale != EXPECTED
        body = tmp_path / "pr-body.md"
        body.write_bytes((OWN + stale).encode("utf-8"))
        capsys.readouterr()
        assert PR.main([str(item), "--body", str(body), "--check"]) == 1
        summary = PR.SUMMARY.format(home="seal", name=NAME)
        assert capsys.readouterr().out == (
            f"refused: pr-body.md:5: reads ``, then `<details>`, then `{summary}`, "
            "which the records do not give\n"
            "refused: pr-body.md:15: lacks ``, a fixed line, then `<details>`, a "
            f"fixed line, then `{summary}`, a fixed line\n"
        )
        assert body.read_bytes() == (OWN + stale).encode("utf-8")
        assert PR.main([str(item), "--body", str(body)]) == 0
        capsys.readouterr()
        assert PR.main([str(item), "--body", str(body), "--check"]) == 0

    @pytest.mark.parametrize(
        "old, new, said",
        [
            (
                f"## From the records\n\n{MARK_LINE}\n\n",
                "## From the records\n\n",
                f"refused: pr-body.md:5: lacks ``, a fixed line, then "
                f"`{MARK_LINE}`, a fixed line\n",
            ),
            (
                "From `changelog.md`.\n",
                "From `changelog.md`.\nA line.\nAnother line.\n",
                "refused: pr-body.md:11: reads `A line.`, then `Another line.`, "
                "which the records do not give\n",
            ),
        ],
        ids=["the mark and its blank line taken out", "two lines added"],
    )
    def test_refuses_a_run_of_lines_in_the_copy_naming_every_line_of_it(
        self, repo, tmp_path, monkeypatch, capsys, old, new, said
    ):
        """#1452, *Scope* item 2, and the design's G12. A body of a cleared
        work item written before the inspection lacks the mark and the blank line
        under it, and the comparison aligns the body's blank line with the
        composition's second one, so the run it lacks is the blank line and
        the mark. The check exits 1 on one `refused:` line naming every line
        of the run, the mark among them, at the body's line; a run of lines
        added is named the same way. Seen red against the comparison that
        named the run's first line alone, which named the blank line and not
        the mark."""
        item = cleared_item(repo)
        monkeypatch.setattr(PR, "MANIFEST", manifest_of(tmp_path, MANIFEST))
        monkeypatch.chdir(repo)
        body = tmp_path / "pr-body.md"
        assert PR.main([str(item), "--body", str(body)]) == 0
        text = body.read_bytes().decode("utf-8")
        assert old in text
        body.write_bytes(text.replace(old, new, 1).encode("utf-8"))
        capsys.readouterr()
        assert PR.main([str(item), "--body", str(body), "--check"]) == 1
        assert capsys.readouterr().out == said

    def test_refuses_naming_no_machine_path(self, tmp_path, capsys):
        """The inspector copies the first `refused:` line into a committed
        `inspection.md`, so the line names the body file by its name and a
        record by its path under the `seal/` root, whatever absolute paths
        the command was given."""
        item = item_of(
            tmp_path,
            {
                **RECORDS,
                "trail/rounds/round-1.md": ROUND_1.replace(
                    "verdict: fixed 2222222", "verdict: done"
                ),
            },
        )
        body = tmp_path / "pr-body.md"
        body.write_bytes((OWN + EXPECTED).encode("utf-8"))
        capsys.readouterr()
        assert PR.main([str(item), "--body", str(body), "--check"]) == 1
        out = capsys.readouterr().out
        assert out.startswith(
            f"refused: seal/threads/{NAME}/trail/rounds/round-1.md:20: "
        )
        assert str(tmp_path) not in out

    def test_refuses_and_writes_nothing(self, tmp_path, capsys):
        """S6's refused record exits 1 on a `refused:` line and leaves the
        body file as it stood."""
        records = {
            **RECORDS,
            "trail/rounds/round-1.md": ROUND_1.replace(
                "verdict: fixed 2222222", "verdict: done"
            ),
        }
        item = item_of(tmp_path, records)
        body = tmp_path / "pr-body.md"
        text = OWN + EXPECTED
        body.write_bytes(text.encode("utf-8"))
        assert PR.main([str(item), "--body", str(body)]) == 1
        assert capsys.readouterr().out.startswith("refused: ")
        assert body.read_bytes() == text.encode("utf-8")

    def test_refuses_a_first_part_and_changelog_past_the_limit(
        self, tmp_path, monkeypatch, capsys
    ):
        """S5 of #1559. Where the first part, here `pr.ko.md` and `pr.md`,
        and `changelog.md`, none of which folds, pass GitHub's limit
        together, both forms exit 1 on one `refused:` line on the work
        item's directory naming the body's length with every section that a
        fold shortens folded, the inspection mark's room counted and said to be,
        the limit, and each of the three files with its length; the body
        file is left as it stood. The length is
        `LENGTH` with `pr.ko.md`'s text and the line end `read_own` gives it.
        Seen red against `main` as 0.38.2 shipped it, which exited 0 and
        wrote the body."""
        monkeypatch.setattr(PR, "MANIFEST", manifest_of(tmp_path, MANIFEST))
        own = OWN + "p" * 40000 + "\n"
        changelog = CHANGELOG + "- " + "c" * 30000 + "\n"
        item = item_of(
            tmp_path,
            {**RECORDS, "changelog.md": changelog},
            own=own,
            rows=DIFFERING,
            translations={"pr.ko.md": TRANSLATION},
        )
        body = tmp_path / "pr-body.md"
        body.write_bytes(b"as it stood\n")
        translation = units(TRANSLATION) + 1
        said = (
            f"refused: seal/threads/{NAME}: the body, counted with room for the "
            "inspection mark's line whether or not it is written, would be "
            f"{LENGTH + translation:,} characters with every section after "
            "`## What changed` folded that a fold shortens, past GitHub's "
            f"65,536; `pr.ko.md` holds {translation:,}, `pr.md` holds "
            f"{units(own):,} and `changelog.md` holds {units(changelog):,}, so "
            "one of them is shortened before `iadd pr-body` runs again\n"
        )
        for extra in ([], ["--check"]):
            assert PR.main([str(item), "--body", str(body), *extra]) == 1
            assert capsys.readouterr().out == said
        assert body.read_bytes() == b"as it stood\n"

    def test_names_the_folded_sections_when_writing_and_checking(
        self, tmp_path, capsys
    ):
        """S6 of #1559. The command that writes a folded body says on one
        line which sections it folded, after the mark key's sentence and
        `; `, `--check` on that body exits 0 and says the same, and a body
        with the folded section's text copied back in place of its fixed
        line is refused at that line."""
        item = item_of(
            tmp_path,
            {**RECORDS, "gaps.md": long_gaps(700)},
            rows=[*LANGUAGES, ("Pull request inspection mark", "Yes")],
        )
        body = tmp_path / "pr-body.md"
        note = f"iadd pr-body: {NOT_YES.format(value='Yes')}; {FOLDED_NOT_VERIFIED}\n"
        assert PR.main([str(item), "--body", str(body)]) == 0
        assert capsys.readouterr().out == (
            f"{note}wrote: {body} from {item}'s `pr.md` and records\n"
        )
        written = body.read_bytes().decode("utf-8")
        assert units(written) <= LIMIT, units(written)
        assert PR.main([str(item), "--body", str(body), "--check"]) == 0
        assert capsys.readouterr().out == (
            f"{note}matches: {body} is `pr.md` above `{PR.HEADING}` and the "
            "records' text below it\n"
        )
        folded = FOLDED.format(path="gaps.md")
        line = written.split("\n").index(folded) + 1
        body.write_bytes(
            written.replace(
                folded, "From `gaps.md`.\n\n" + GAPS.split("\n")[6], 1
            ).encode("utf-8")
        )
        assert PR.main([str(item), "--body", str(body), "--check"]) == 1
        out = capsys.readouterr().out
        assert out.startswith(f"refused: pr-body.md:{line}: reads `From `gaps.md`.`")

    def test_refuses_an_item_that_is_not_a_directory_at_exit_2(self, tmp_path):
        body = tmp_path / "pr-body.md"
        assert PR.main([str(tmp_path / "absent"), "--body", str(body)]) == 2
        assert not body.exists()


test_census = census_case(TARGET)
