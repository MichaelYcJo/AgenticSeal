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

OWN = "Closes #1.\n\nThe motivation, in the orchestrator's words.\r\n"


def item_of(tmp_path, records):
    """The work item NAME under `tmp_path`, holding RECORDS by path."""
    item = tmp_path / NAME
    item.mkdir()
    for rel, text in records.items():
        write(item, rel, text)
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


# #1204: a manifest with the three fields the mark's address is built from,
# and the line `seal pr-body` writes from it.
MANIFEST = {
    "repository": "https://github.com/owner/plugin",
    "version": "1.2.3",
    "icon": "./.claude-plugin/icon.png",
}
MARK_LINE = (
    '<img src="https://github.com/owner/plugin/raw/v1.2.3/.claude-plugin/icon.png" '
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
    `config.md`'s table holding ROW, committed; then, where VERDICT is
    given, a `guarantee.md` whose one block names that commit against BASE
    with VERDICT, committed after it, as the orchestrator commits the
    sealer's verdict."""
    home = mark_root(repo / "seal")
    if row is not None:
        write(home, "config.md", "| Item | Value |\n|---|---|\n" + row)
    item = home / "threads" / NAME
    for rel, text in RECORDS.items():
        write(item, rel, text)
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
        ],
    )
    def test_refuses_a_record_it_cannot_copy_faithfully(self, rel, text, line, said):
        """S6. A round record `chain_check.py` refuses, a gate record whose
        run block `hooks/lib/fields.py` refuses (#1198), a copied line equal
        to `HEADING`, which would put a second boundary line inside the
        fold, a copied line holding `<details` or `</details` in any case and
        anywhere in it, followed by whitespace, `/`, `>` or the line's end,
        outside a code span, which GitHub reads as a second fold or the
        fold's end (#1218), a second section of one the body copies, and a
        copied line holding a closing keyword, which would close an issue no
        party claimed, are each refused at the record's path and line, with
        a sentence naming what was read there. A closing keyword in a code
        span or a fence claims nothing, as
        `close_issues_on_release.py#keywords_in` reads it, and a
        `</details>` in a fence ends no fold."""
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


class Test_split:
    def test_accepts_a_body_at_its_first_heading_line(self):
        """S7. Everything before the first line equal to `HEADING`, the
        orchestrator's part, and everything after it, a second such line
        among the records' copy."""
        copy = EXPECTED[EXPECTED.index("\n") + 1 :] + "## From the records\n"
        assert PR.split(OWN + "## From the records\n" + copy) == (OWN, copy)

    def test_refuses_a_body_with_no_heading_line(self):
        """S7. A body with no line equal to `HEADING` has no part of its own
        to keep; a heading line with a word after it is no such line, and
        nor is the line of the body 0.25.0 wrote. The refusal names the
        repair, so the reader of a body written before 0.25.1 has a way on
        (round 1 of #1148, finding 2)."""
        for body in (
            "## What changed\n\n## From the records, really\n",
            "## What changed\n\n## Not from the records\n",
        ):
            with pytest.raises(PR.Refused) as refused:
                PR.split(body)
            assert (
                f"write your part above a line reading `{PR.HEADING}`, or remove "
                "the file, and run the command again" in refused.value.causes[0][2]
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
        manifest's `repository`, `/raw/v`, `version` and `icon` path."""
        item = sealed_item(repo)
        manifest = manifest_of(tmp_path, MANIFEST)
        assert PR.seal_mark(str(item), str(repo), manifest) == (MARK_LINE, None)

    def test_accepts_the_plugins_own_manifest(self, repo):
        """S1's address read from the manifest three directories above the
        script, the plugin's own, which this reads and never writes."""
        with open(PR.MANIFEST, encoding="utf-8") as handle:
            own = json.load(handle)
        src = f"{own['repository']}/raw/v{own['version']}/{own['icon'][2:]}"
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
        `undecided`, and a file `hooks/lib/fields.py` refuses a line of,
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

    @pytest.mark.parametrize("field", ["repository", "version", "icon"])
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
        assert body.read_text(encoding="utf-8") == marked
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
        write(
            mark_root(repo / "seal"), "config.md", "| Item | Value |\n|---|---|\n" + ROW
        )
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
        assert body.read_text(encoding="utf-8") == marked
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
        write(home, "config.md", "| Item | Value |\n|---|---|\n" + ROW)
        item = home / "threads" / NAME
        for rel, text in RECORDS.items():
            write(item, rel, text)
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
        assert body.read_text(encoding="utf-8") == marked
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
        assert body.read_text(encoding="utf-8") == EXPECTED

    def test_accepts_a_stale_body_and_keeps_its_own_part_byte_for_byte(self, tmp_path):
        """S8. The part above the heading, the orchestrator's, is kept as
        its bytes stood, a CRLF line among them, and the part below it is
        rewritten from the records; with no file, the generated part alone
        is written."""
        item = item_of(tmp_path, RECORDS)
        body = tmp_path / "pr-body.md"
        stale = EXPECTED.replace("the reader | its cases", "the reader | nothing")
        body.write_bytes((OWN + stale).encode("utf-8"))
        assert PR.main([str(item), "--body", str(body)]) == 0
        assert body.read_bytes() == (OWN + EXPECTED).encode("utf-8")
        fresh = tmp_path / "fresh.md"
        assert PR.main([str(item), "--body", str(fresh)]) == 0
        assert fresh.read_bytes() == EXPECTED.encode("utf-8")

    def test_accepts_the_written_body_under_check_and_writes_nothing(
        self, tmp_path, capsys
    ):
        """S9. The file S8 writes is what the records give, and it still is
        once the orchestrator has written its part above the heading: the
        check reads the part below it alone."""
        item = item_of(tmp_path, RECORDS)
        body = tmp_path / "pr-body.md"
        assert PR.main([str(item), "--body", str(body)]) == 0
        written = body.read_bytes()
        assert PR.main([str(item), "--body", str(body), "--check"]) == 0
        assert body.read_bytes() == written
        body.write_bytes(OWN.encode("utf-8") + written)
        assert PR.main([str(item), "--body", str(body), "--check"]) == 0
        assert body.read_bytes() == OWN.encode("utf-8") + written
        assert "refused:" not in capsys.readouterr().out

    def test_refuses_an_edited_copy_naming_both_lines(self, tmp_path, capsys):
        """S9, the class of #857's withheld item 5, a changelog fact restated
        wrongly: one sentence of the copied changelog changed is refused at
        the body's line, counted from the body's first line, the
        orchestrator's part above the heading among them, with the record's
        line it should read."""
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

    @pytest.mark.parametrize(
        "records, text",
        [
            (RECORDS, "## What changed\n\nno heading here\n"),
            (
                {
                    **RECORDS,
                    "trail/rounds/round-1.md": ROUND_1.replace(
                        "verdict: fixed 2222222", "verdict: done"
                    ),
                },
                OWN + EXPECTED,
            ),
        ],
        ids=["no heading", "a refused round record"],
    )
    def test_refuses_and_writes_nothing(self, tmp_path, capsys, records, text):
        """S8's body with no heading, and S6's refused record, each exit 1
        on a `refused:` line and leave the body file as it stood."""
        item = item_of(tmp_path, records)
        body = tmp_path / "pr-body.md"
        body.write_bytes(text.encode("utf-8"))
        assert PR.main([str(item), "--body", str(body)]) == 1
        assert capsys.readouterr().out.startswith("refused: ")
        assert body.read_bytes() == text.encode("utf-8")

    def test_refuses_an_item_that_is_not_a_directory_at_exit_2(self, tmp_path):
        body = tmp_path / "pr-body.md"
        assert PR.main([str(tmp_path / "absent"), "--body", str(body)]) == 2
        assert not body.exists()


test_census = census_case(TARGET)
