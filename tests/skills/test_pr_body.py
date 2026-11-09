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

import pytest
from conftest import ROOT, census_case, load_module, mark_root, write

TARGET = "skills/code-review/scripts/pr_body.py"

PR = load_module(os.path.join(ROOT, *TARGET.split("/")), "pr_body_under_test")

NAME = "1799000000-a-body"

CHANGELOG = """\
- **The pull request body copies the records.** `seal pr-body` writes it (#1).
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
# with, then one fold whose summary names the copy, a blank line after the
# summary, the sections, and the fold's end.
EXPECTED = """\
## From the records

<details>
<summary>Copied from the records in seal/threads/1799000000-a-body/ by seal pr-body.</summary>

## What changed

From `changelog.md`.

- **The pull request body copies the records.** `seal pr-body` writes it (#1).
- 본문의 사실은 기록에서 옵니다.

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

# The work item's `pr.md`, the body's first part: a quote of a record with
# its coordinate, a CRLF line among them, and the `Closes` line.
OWN = '"`seal pr-body` writes it (#1)." (`changelog.md`, line 1)\r\n\nCloses #1.\n'
# #1453: `config.md`'s table head, and the two language rows the body's
# first part is composed from, as a repository of one language writes them.
TABLE = "| Item | Value |\n|---|---|\n"
LANGUAGES = (
    "| Commit and pull request language | English |\n| Record language | English |\n"
)
# The rows of a repository whose team writes Korean over English records,
# and the work item's `pr.ko.md`, `OWN`'s quote rendered in Korean, with no
# line end after its last line.
DIFFERING = (
    "| Commit and pull request language | Korean |\n| Record language | English |\n"
)
TRANSLATION = '"`seal pr-body` 가 본문을 쓴다 (#1)." (`changelog.md`, line 1)'


def item_of(tmp_path, records, own=OWN, rows=LANGUAGES, translations=None):
    """The work item NAME in the shared root of a git repository at
    `tmp_path`, whose `config.md` table holds ROWS, holding RECORDS by path,
    OWN as its `pr.md`'s bytes, or no `pr.md` where OWN is None, and
    TRANSLATIONS, `{name: text}`, beside it. The repository has no commit:
    `seal pr-body` reads the rows of the root its work item stands in, so a
    case reads its own rows and not the checkout the suite runs in."""
    home = mark_root(tmp_path / "seal")
    write(home, "config.md", TABLE + rows)
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
    fixed = {line.format(name=NAME, path=path) for line in PR.FIXED for path in paths}
    return [
        line
        for line in text.split("\n")
        if line not in lines and line not in demoted and line not in fixed
    ]


# #1204: a manifest with the two fields the mark's address is built from and
# a `version`, which the address does not read (#1452), and the line `seal
# pr-body` writes from it.
MANIFEST = {
    "repository": "https://github.com/owner/plugin",
    "version": "1.2.3",
    "icon": "./.claude-plugin/icon.png",
}
MARK_LINE = (
    '<img src="https://github.com/owner/plugin/raw/HEAD/.claude-plugin/icon.png" '
    'alt="Sealed" width="128">'
)
ROW = "| Pull request seal mark | yes |\n"
SEALED = "Verdict: sealed"


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


def sealed_item(repo, row=ROW, verdict=SEALED, base="feature/x"):
    """The work item NAME in REPO's shared root, holding RECORDS, with
    `config.md`'s table holding the two language rows and ROW, committed;
    then, where VERDICT is given, a `guarantee.md` whose one block names
    that commit against BASE with VERDICT, committed after it, as the
    orchestrator commits the sealer's verdict."""
    home = mark_root(repo / "seal")
    write(home, "config.md", TABLE + LANGUAGES + (row or ""))
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
            "guarantee.md",
            f"# Guarantee: {NAME}\n\n```seal\ntarget: {sha} against {base}\n"
            f"{verdict}\n```\n",
        )
        git_in(repo, "add", "-A")
        git_in(repo, "commit", "-qm", "the seal")
    return item


class Test_compose:
    def test_accepts_a_work_item_as_the_records_text(self, tmp_path):
        """S1, and #1198's scenario *The body copies blocks*. Every section
        the design lays out, in its order, holding the records' lines: each
        round's `seal` blocks verbatim, a finding's heading one level down
        followed by its finding block and its close block, a round with no
        finding, a line in Korean, the line `HEADING` holds first, and one
        `<details>` around the sections, its `<summary>` followed by a blank
        line. Seen red against the copy of a round's labelled lines, which
        held no block."""
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
        to `HEADING`, which would put a second boundary line inside the
        fold, a copied line holding `<details` or `</details` in any case and
        anywhere in it, followed by whitespace, `/`, `>` or the line's end,
        outside a code span, which GitHub reads as a second fold or the
        fold's end (#1218), a second section of one the body copies, and a
        copied line holding a closing keyword, which would close an issue no
        party claimed, are each refused at the record's path and line, with
        a sentence naming what was read there. A closing keyword in a code
        span, a fence or an HTML comment claims nothing, as
        `close_issues_on_release.py#keywords_in` reads it, one beside a
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
        line stands in the fold as written."""
        span = "`</details>` in a span"
        text = PR.compose(NAME, {**RECORDS, "changelog.md": CHANGELOG + span + "\n"})
        assert span in text.split("\n")

    def test_accepts_a_keyword_and_a_details_tag_in_a_closed_comment(self):
        """#1181. GitHub reads neither a closing keyword nor a tag inside a
        comment that closes (#1402, #1403), and the tag and the keyword are
        blanked one way, so each line stands in the fold as written. A line
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
                "command wrote: run `seal pr-body <item> --body <file>`, which "
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
        """The body's first part is `pr.md`'s text with its line ends as
        they stand, and a file whose last line has no line end gets one, so
        the heading after it stands on its own line. Seen red with the line
        end's addition alone removed, where the heading joined the last
        line."""
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
    "`Pull request seal mark` reads `{value}`, not `yes`, so the row is not "
    "read and the body carries no seal mark"
)
NO_FIELD = (
    "`.claude-plugin/plugin.json` has no `{field}`, so the mark's address is "
    "not built and the body carries no seal mark"
)


class Test_seal_mark:
    """#1204. The mark under the heading, where the repository's row reads
    `yes` and the work item is sealed at HEAD."""

    def test_accepts_a_seal_only_its_guarantee_follows(self, repo, tmp_path):
        """S1. The row reads `yes`, the newest block reads `sealed` at a
        commit only the guarantee's own commit follows, and the line is the
        manifest's `repository`, `/raw/HEAD/` and `icon` path."""
        item = sealed_item(repo)
        manifest = manifest_of(tmp_path, MANIFEST)
        assert PR.seal_mark(str(item), str(repo), manifest) == (MARK_LINE, None)

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
        item = sealed_item(repo)
        (tmp_path / "older").mkdir()
        (tmp_path / "newer").mkdir()
        older = manifest_of(tmp_path / "older", MANIFEST)
        newer = manifest_of(
            tmp_path / "newer",
            {key: value for key, value in MANIFEST.items() if key != "version"},
        )
        lines = {PR.seal_mark(str(item), str(repo), m)[0] for m in (older, newer)}
        assert lines == {MARK_LINE}

    def test_accepts_the_plugins_own_manifest(self, repo):
        """S1's address read from the manifest three directories above the
        script, the plugin's own, which this reads and never writes."""
        with open(PR.MANIFEST, encoding="utf-8") as handle:
            own = json.load(handle)
        src = f"{own['repository']}/raw/HEAD/{own['icon'][2:]}"
        item = sealed_item(repo)
        assert PR.seal_mark(str(item), str(repo)) == (
            f'<img src="{src}" alt="Sealed" width="128">',
            None,
        )

    @pytest.mark.parametrize(
        "verdict",
        [
            None,
            "Verdict: withheld reason: a claim does not hold",
            "Verdict: undecided question: which one?",
            "Verdict: done",
            f"{SEALED}\n```\n\n```seal\nVerdict: done",
        ],
        ids=[
            "no guarantee",
            "withheld",
            "undecided",
            "a refused block",
            "a refused block after a sealed one",
        ],
    )
    def test_refuses_a_work_item_not_sealed_saying_nothing(
        self, repo, tmp_path, verdict
    ):
        """S2. No guarantee, a newest block reading `withheld` or
        `undecided`, and a file `lib/fields.py` refuses a line of,
        after a sealed block too: no mark, and no line, since the sealer and
        the pull request's check name those. The last seen red with the
        refusal's read alone removed, where the mark stood."""
        item = sealed_item(repo, verdict=verdict)
        manifest = manifest_of(tmp_path, MANIFEST)
        assert PR.seal_mark(str(item), str(repo), manifest) == (None, None)

    def test_refuses_a_seal_a_later_commit_follows(self, repo, tmp_path):
        """S3. A commit outside the closing records after the sealed one, a
        repair nobody sealed: no mark. Seen red with the `follows` condition
        alone removed, where the mark stood."""
        item = sealed_item(repo)
        write(repo, "f.txt", "a repair\n")
        git_in(repo, "commit", "-qam", "a repair")
        manifest = manifest_of(tmp_path, MANIFEST)
        assert PR.seal_mark(str(item), str(repo), manifest) == (None, None)

    def test_refuses_a_seal_whose_base_does_not_resolve(self, repo, tmp_path):
        """S3's class: `follows` lists the later commits against the base,
        and a base this repository cannot resolve lists none, so a stale
        seal would read as one at HEAD. No mark, and the base named. Seen red
        with the base's read alone removed, where the mark stood."""
        item = sealed_item(repo, base="no-such-base")
        write(repo, "f.txt", "a repair\n")
        git_in(repo, "commit", "-qam", "a repair")
        manifest = manifest_of(tmp_path, MANIFEST)
        assert PR.seal_mark(str(item), str(repo), manifest) == (
            None,
            "the guarantee names the base `no-such-base`, which this "
            "repository cannot resolve, so whether its seal is at HEAD is not "
            "read and the body carries no seal mark",
        )

    @pytest.mark.parametrize("held", ["off", "unseen"])
    def test_refuses_a_seal_head_does_not_hold_naming_it(self, repo, tmp_path, held):
        """Round 1's finding 1's class. A guarantee sealed at a commit HEAD
        does not descend from, as a local-mode work item read from another
        branch's checkout, or at one this repository cannot resolve: whether
        the seal is at HEAD cannot be read there, so no mark, and the commit
        and the checkout named. Seen red with the naming alone removed,
        where nothing was said."""
        item = sealed_item(repo)
        guarantee = item / "guarantee.md"
        if held == "off":
            text = guarantee.read_text(encoding="utf-8")
            sealed = re.search(r"target: (\S+)", text).group(1)
            git_in(repo, "reset", "-q", "--soft", "HEAD~2")
        else:
            sealed = "f" * 40
            text = guarantee.read_text(encoding="utf-8")
            guarantee.write_text(
                re.sub(r"target: \S+", f"target: {sealed}", text), encoding="utf-8"
            )
        manifest = manifest_of(tmp_path, MANIFEST)
        assert PR.seal_mark(str(item), str(repo), manifest) == (
            None,
            f"the guarantee is sealed at `{sealed}`, which HEAD in {repo} does "
            "not hold, so whether its seal is at HEAD is not read and the body "
            "carries no seal mark",
        )

    @pytest.mark.parametrize(
        "row, said",
        [
            (None, None),
            ("| Pull request seal mark |  |\n", None),
            ("| Pull request seal mark | Yes |\n", NOT_YES.format(value="Yes")),
            ("| Pull request seal mark | on |\n", NOT_YES.format(value="on")),
            ("| Pull request seal mark | true |\n", NOT_YES.format(value="true")),
            (
                ROW + ROW,
                "`Pull request seal mark` is not read: `Pull request seal mark` "
                "appears 2 times — one value; the body carries no seal mark",
            ),
        ],
        ids=["absent", "empty", "Yes", "on", "true", "written twice"],
    )
    def test_refuses_a_row_other_than_yes(self, repo, tmp_path, row, said):
        """S4. Only `yes`, exactly so, turns the mark on. An absent or empty
        row says nothing; any other value, and a refused row, is named as
        not read. The `Yes` case seen red with the comparison alone
        case-folded, where the mark stood."""
        item = sealed_item(repo, row=row)
        manifest = manifest_of(tmp_path, MANIFEST)
        assert PR.seal_mark(str(item), str(repo), manifest) == (None, said)

    @pytest.mark.parametrize("field", ["repository", "icon"])
    def test_refuses_a_manifest_lacking_a_field(self, repo, tmp_path, field):
        """S5. A manifest the address cannot be built from: no mark, and
        the field named."""
        item = sealed_item(repo)
        lacking = {key: value for key, value in MANIFEST.items() if key != field}
        manifest = manifest_of(tmp_path, lacking)
        assert PR.seal_mark(str(item), str(repo), manifest) == (
            None,
            NO_FIELD.format(field=field),
        )

    def test_refuses_a_manifest_that_is_not_json(self, repo, tmp_path):
        """S5. A manifest that will not read: no mark, and it named."""
        item = sealed_item(repo)
        manifest = tmp_path / "plugin.json"
        manifest.write_text("{", encoding="utf-8")
        mark, said = PR.seal_mark(str(item), str(repo), str(manifest))
        assert mark is None
        assert said.startswith("`.claude-plugin/plugin.json` is not read ("), said


class Test_main:
    def test_accepts_a_sealed_work_item_with_the_mark_under_the_heading(
        self, repo, tmp_path, monkeypatch, capsys
    ):
        """S1 through the command, run in the repository: the part opens
        with a blank line, the mark, a blank line and the fold, `--check`
        on that body exits 0, and nothing is said about the mark."""
        item = sealed_item(repo)
        monkeypatch.setattr(PR, "MANIFEST", manifest_of(tmp_path, MANIFEST))
        monkeypatch.chdir(repo)
        body = tmp_path / "pr-body.md"
        assert PR.main([str(item), "--body", str(body)]) == 0
        marked = EXPECTED.replace(
            "## From the records\n\n", f"## From the records\n\n{MARK_LINE}\n\n", 1
        )
        assert body.read_bytes() == (OWN + marked).encode("utf-8")
        assert PR.main([str(item), "--body", str(body), "--check"]) == 0
        assert "seal pr-body:" not in capsys.readouterr().out

    def test_accepts_a_sealed_work_item_run_from_another_checkout(
        self, repo, tmp_path, monkeypatch, capsys
    ):
        """Round 1's finding 1. The orchestrator runs from the main checkout
        and reaches the work item in a linked worktree, whose branch the
        main checkout's HEAD does not hold. The row, the base and HEAD are
        read in the work item's own checkout, so the body carries the mark
        as it does when run from the worktree. Seen red with the root read
        from the working directory alone, as it was: no mark."""
        write(mark_root(repo / "seal"), "config.md", TABLE + LANGUAGES + ROW)
        git_in(repo, "add", "-A")
        git_in(repo, "commit", "-qm", "the row")
        worktree = tmp_path / "worktree"
        git_in(repo, "worktree", "add", "-q", "-b", "feat/1-x", str(worktree))
        item = sealed_item(worktree)
        monkeypatch.setattr(PR, "MANIFEST", manifest_of(tmp_path, MANIFEST))
        monkeypatch.chdir(repo)
        body = tmp_path / "pr-body.md"
        assert PR.main([str(item), "--body", str(body)]) == 0
        marked = EXPECTED.replace(
            "## From the records\n\n", f"## From the records\n\n{MARK_LINE}\n\n", 1
        )
        assert body.read_bytes() == (OWN + marked).encode("utf-8")
        assert "seal pr-body:" not in capsys.readouterr().out

    def test_accepts_a_local_mode_work_item_from_the_working_directorys_checkout(
        self, repo, tmp_path, monkeypatch, capsys
    ):
        """Round 1's finding 1, local mode. The work item sits under the
        common git directory, where git finds no checkout, so the row, the
        base and HEAD are read in the working directory's checkout, and a
        seal at its HEAD carries the mark. Seen red with that fallback alone
        removed: no mark."""
        home = mark_root(repo / ".git" / "seal")
        write(home, "config.md", TABLE + LANGUAGES + ROW)
        item = home / "threads" / NAME
        for rel, text in RECORDS.items():
            write(item, rel, text)
        (item / "pr.md").write_bytes(OWN.encode("utf-8"))
        sha = git_in(repo, "rev-parse", "HEAD")
        write(
            item,
            "guarantee.md",
            f"# Guarantee: {NAME}\n\n```seal\ntarget: {sha} against feature/x\n"
            f"{SEALED}\n```\n",
        )
        monkeypatch.setattr(PR, "MANIFEST", manifest_of(tmp_path, MANIFEST))
        monkeypatch.chdir(repo)
        body = tmp_path / "pr-body.md"
        assert PR.main([str(item), "--body", str(body)]) == 0
        marked = EXPECTED.replace(
            "## From the records\n\n", f"## From the records\n\n{MARK_LINE}\n\n", 1
        )
        assert body.read_bytes() == (OWN + marked).encode("utf-8")
        assert "seal pr-body:" not in capsys.readouterr().out

    def test_refuses_the_mark_on_a_row_other_than_yes_and_exits_0(
        self, repo, tmp_path, monkeypatch, capsys
    ):
        """S4 through the command: the row named as not read on one line
        before `wrote:`, the body today's, and exit 0."""
        item = sealed_item(repo, row="| Pull request seal mark | Yes |\n")
        monkeypatch.chdir(repo)
        body = tmp_path / "pr-body.md"
        assert PR.main([str(item), "--body", str(body)]) == 0
        out = capsys.readouterr().out.splitlines()
        assert out[0] == "seal pr-body: " + NOT_YES.format(value="Yes")
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

    @pytest.mark.parametrize(
        "rows, missing",
        [
            ("| Record language | English |\n", ["Commit and pull request language"]),
            ("| Commit and pull request language | English |\n", ["Record language"]),
            (
                "| Commit and pull request language | English |\n"
                "| Record language |  |\n",
                ["Record language"],
            ),
            ("", ["Commit and pull request language", "Record language"]),
        ],
        ids=["no commit row", "no record row", "an empty record row", "neither row"],
    )
    @pytest.mark.parametrize("check", [False, True], ids=["write", "check"])
    def test_refuses_a_repository_without_a_language_row_naming_it(
        self, tmp_path, capsys, rows, missing, check
    ):
        """#1453, *Scope* item 3, the scenario *`seal pr-body` refuses
        without a row*. Either form exits 1, leaves the body file as it
        stood, and prints one `refused:` line for each row that names no
        language, absent or empty, naming `config.md` by its path under the
        `seal/` root, the row, and the section of the template that says
        what it governs. Seen red against `pr_body.py` as the merged base
        left it, where both forms exited 0."""
        item = item_of(tmp_path, RECORDS, rows=rows)
        body = tmp_path / "pr-body.md"
        body.write_bytes((OWN + EXPECTED).encode("utf-8"))
        capsys.readouterr()
        argv = [str(item), "--body", str(body)] + (["--check"] if check else [])
        assert PR.main(argv) == 1
        assert capsys.readouterr().out == "".join(
            f"refused: seal/config.md: names no language in a `{row}` row; "
            f"`templates/setup/config.md` *{row}* says what the row governs, "
            "and the orchestrator asks for it before the first edit\n"
            for row in missing
        )
        assert body.read_bytes() == (OWN + EXPECTED).encode("utf-8")

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
                "| Commit and pull request language | Korean |\n"
                "| Record language | korean |\n",
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
        language*. Where the rows name different languages, the body file
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
        refused* and *Two translations are refused*. Where the rows name
        different languages and the work item holds no `pr.*.md`, or more
        than one, either form exits 1 on one `refused:` line on the work
        item's directory, naming the two rows, or the count and the files,
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
        ],
        ids=["the translation left out", "a line of it changed"],
    )
    def test_refuses_a_first_part_that_is_not_the_translation_then_pr_md(
        self, tmp_path, capsys, first, said
    ):
        """#1453, *Scope* item 3, the scenario *A body without the translation
        fails the check*. Where the rows differ, `--check` compares the whole
        first part, `pr.ko.md` and then `pr.md`, line by line: a body whose
        first part is `pr.md` alone, and one whose line of the translation
        was changed, exit 1 at the body's first line, naming the file that
        gives the line. Seen red against `pr_body.py` as the merged base left
        it, where the first exited 0 and the second named `pr.md`."""
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
            "`seal pr-body` writes it", "`seal pr-body` drafts it"
        )
        body.write_bytes((OWN + edited).encode("utf-8"))
        capsys.readouterr()
        assert PR.main([str(item), "--body", str(body), "--check"]) == 1
        out = capsys.readouterr().out
        assert out.startswith("refused: pr-body.md:13: ")
        assert "`changelog.md:1`" in out
        assert body.read_bytes() == (OWN + edited).encode("utf-8")

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
                "refused: pr-body.md:14: reads `A line.`, then `Another line.`, "
                "which the records do not give\n",
            ),
        ],
        ids=["the mark and its blank line taken out", "two lines added"],
    )
    def test_refuses_a_run_of_lines_in_the_copy_naming_every_line_of_it(
        self, repo, tmp_path, monkeypatch, capsys, old, new, said
    ):
        """#1452, *Scope* item 2, and the design's G12. A body of a sealed
        work item written before the seal lacks the mark and the blank line
        under it, and the comparison aligns the body's blank line with the
        composition's second one, so the run it lacks is the blank line and
        the mark. The check exits 1 on one `refused:` line naming every line
        of the run, the mark among them, at the body's line; a run of lines
        added is named the same way. Seen red against the comparison that
        named the run's first line alone, which named the blank line and not
        the mark."""
        item = sealed_item(repo)
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
        """The sealer copies the first `refused:` line into a committed
        `guarantee.md`, so the line names the body file by its name and a
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

    def test_refuses_an_item_that_is_not_a_directory_at_exit_2(self, tmp_path):
        body = tmp_path / "pr-body.md"
        assert PR.main([str(tmp_path / "absent"), "--body", str(body)]) == 2
        assert not body.exists()


test_census = census_case(TARGET)
