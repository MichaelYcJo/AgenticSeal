"""`skills/code-review/scripts/chain_check.py`, one group per function.

Each group holds a case on good input and a case on bad input. The `main`
group runs the check end to end over a real git repository: a branch with a
routing declaration, a round record and a `broad-gate.md`, judged as a ready
or a draft pull request through the event payload GitHub writes.
"""

import importlib.util
import json
import os
import pathlib
import re
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHAIN = ROOT / "skills" / "code-review" / "scripts" / "chain_check.py"
READER = ROOT / "skills" / "verify" / "scripts" / "unverified_check.py"
ITEM = "seal/specs/1791999999-a-work-item"
# The pictographs and symbols a mark is drawn from: the colour circles and
# squares, the check and cross marks, the question mark ornament and the
# variation selector that follows them.
EMOJI = re.compile("[⌀-⏿☀-➿⬀-⯿️\U0001f000-\U0001faff]")


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


chain = load(CHAIN, "chain_check_under_test")
reader = load(READER, "unverified_reader_for_chain_tests")


def git(d, *args):
    return subprocess.run(
        ["git", "-C", str(d), *args],
        check=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    ).stdout.strip()


def write(d, rel, text):
    p = pathlib.Path(d) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def commit(d, message):
    git(d, "add", "-A")
    git(d, "commit", "-qm", message)
    return git(d, "rev-parse", "HEAD")


ROUTING = """# a work item -- routing

| Axis | Answer |
|---|---|
| Review | {review} |
| Destination | open the pull request |
| Planning | {planning} |
| Branch | feature/x |
"""


def finding(
    n,
    verdict,
    severity="must",
    title="the parser drops a row",
    location="`f.txt:1`",
    regression=None,
    reopens=None,
    evidence="read `f.txt:1`",
):
    """One `### ` section of `## Findings`, in `templates/sdd-round.md`'s
    shape, its `verdict:` line reading `verdict` and its `evidence:` line
    `evidence`, or none where that is None."""
    return (
        f"### {n}. {title}\n\n"
        f"severity: {severity}\n"
        f"location: {location}\n"
        + (f"evidence: {evidence}\n" if evidence is not None else "")
        + f"verdict: {verdict}\n"
        + (f"regression: {regression}\n" if regression else "")
        + (f"reopens: {reopens}\n" if reopens else "")
        + "\nWhy it matters.\n\n"
        "```python\nx = 1\n```\n\n"
        "answer: \n"
    )


def confirm(reference, what="the fix holds"):
    """One entry of `## Confirmations`: its `confirms:` line reading
    `reference`, then the prose saying what holds, where and how."""
    return f"confirms: {reference}\n{what}, at `f.txt:1`. read.\n\n"


def record(target, findings=(), confirmations="", n=1):
    """A round record in `templates/sdd-round.md`'s shape: `findings` are
    `finding()` sections, `confirmations` entries of `## Confirmations`."""
    return (
        f"# 1791999999-a-work-item — review round {n}\n\n"
        f"target: {target} against main\n\n"
        "## Findings\n\n" + "\n".join(findings) + "\n## Confirmations\n\n"
        f"{confirmations}\n"
        "## Not judged\n\n"
        "| What | Location | Who answers |\n|---|---|---|\n\n"
        "## Probes\n\n"
        "| Command | Result |\n|---|---|\n"
    )


def rounds_of(*texts):
    """The records `texts`, numbered from 1, read as `channel` takes them."""
    out, errors = [], []
    for n, text in enumerate(texts, 1):
        read, said = chain.round_of(reader, text, f"round-{n}.md", n)
        out.append(read)
        errors.extend(said)
    return out, errors


# The table the old generator's records carried, which the check never judges
# again: a merged item keeps one in the fixture, and the check must never open
# it.
OLD_RECORD = (
    "# 1788999999-a-merged-item — review round 1\n\n"
    "| Field | Value |\n|---|---|\n"
    "| Target SHA | 0000000 against main |\n\n"
    "## Verdicts\n\n"
    "| # | Finding | Location | Verdict | Grounds |\n"
    "|---|---|---|---|---|\n"
    "| 🔴 1 | wrong | `f.txt:1` | open | g |\n"
)
MERGED_ITEM = "seal/specs/1788999999-a-merged-item"


def gate_file(sha):
    return (
        "# 1791999999-a-work-item — broad gate\n\n"
        "| Field | Value |\n|---|---|\n"
        f"| Broad gate | {sha} against main |\n"
    )


def guarantee_file(sha, verdict="sealed"):
    return (
        "# 1791999999-a-work-item — guarantee\n\n"
        "| Field | Value |\n|---|---|\n"
        f"| Target SHA | {sha} against main |\n\n"
        f"Verdict: {verdict}\n"
    )


SPEC = "# spec\n\nbody\n\nFramed 2026-10-15 by framer, before the build.\n"


@pytest.fixture
def branch(tmp_path):
    """A repository whose `feature/x` declares a work item and reviewed it.

    `main` holds one file and a work item another pull request merged, its
    declaration naming another branch and its one record in the old table's
    shape with a finding open (S11). `feature/x` adds the declaration, a code
    commit, round 1 at that commit with its one finding `fixed` by it, round
    2 — the verifying round — confirming `round-1#1` with nothing of its own,
    and the closing records. Returns `(root, code commit)`.
    """
    d = tmp_path / "r"
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "t@t")
    git(d, "config", "user.name", "t")
    write(d, "f.txt", "one\n")
    write(
        d,
        f"{MERGED_ITEM}/routing.md",
        ROUTING.format(
            review="through the review chain", planning="the session"
        ).replace("feature/x", "feature/merged"),
    )
    write(d, f"{MERGED_ITEM}/rounds/round-1.md", OLD_RECORD)
    commit(d, "base")
    git(d, "switch", "-q", "-c", "feature/x")
    write(
        d,
        f"{ITEM}/routing.md",
        ROUTING.format(review="through the review chain", planning="the session"),
    )
    commit(d, "routing")
    write(d, "f.txt", "two\n")
    code = commit(d, "code")
    write(
        d,
        f"{ITEM}/rounds/round-1.md",
        record(code, [finding(1, f"fixed {code[:8]}")]),
    )
    commit(d, "the round record")
    write(
        d,
        f"{ITEM}/rounds/round-2.md",
        record(code, confirmations=confirm("round-1#1"), n=2),
    )
    reviewed = commit(d, "the verifying round")
    # Two runs, newest first: the earlier one names a commit nobody can see,
    # so a reader that took any run but the first would refuse the file.
    write(
        d,
        f"{ITEM}/broad-gate.md",
        gate_file(f"{reviewed} against main; earlier run: {'1' * 40}"),
    )
    write(d, f"{ITEM}/guarantee.md", guarantee_file(reviewed))
    commit(d, "the closing records")
    return d, code


def seal(d):
    """The closing records naming HEAD, committed: what a branch carries
    once the sealer has audited what is on it."""
    head = git(d, "rev-parse", "HEAD")
    write(d, f"{ITEM}/broad-gate.md", gate_file(f"{head} against main"))
    write(d, f"{ITEM}/guarantee.md", guarantee_file(head))
    commit(d, "the closing records, again")


@pytest.fixture
def ready(tmp_path, monkeypatch):
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": False}}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    monkeypatch.delenv("GITHUB_HEAD_REF", raising=False)


@pytest.fixture
def draft(tmp_path, monkeypatch):
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": True}}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    monkeypatch.delenv("GITHUB_HEAD_REF", raising=False)


def check(root, capsys, *extra):
    code = chain.main(["--baseline", "main", "--root", str(root), *extra])
    return code, capsys.readouterr().out


# --- changed ------------------------------------------------------------------


def two_declarations(tmp_path):
    """`main` holds one declaration; `feature/y` checked out, nothing yet."""
    d = tmp_path / "c"
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "t@t")
    git(d, "config", "user.name", "t")
    old = ROUTING.format(review="straight to the PR", planning="the session")
    write(d, "seal/specs/1788000000-old/routing.md", old)
    commit(d, "base")
    git(d, "switch", "-q", "-c", "feature/y")
    return d, old


class TestChanged:
    def test_a_declaration_moved_unchanged_is_neither_judged_nor_missed(self, tmp_path):
        """A move of the whole root renames every declaration at once, and a
        declaration the pull request only moved is not one it made (#90)."""
        d, _old = two_declarations(tmp_path)
        git(d, "mv", "seal/specs/1788000000-old", "seal/specs/1788000000-moved")
        commit(d, "moved")
        paths, renamed = chain.changed(str(d), "main")
        assert renamed == {
            "seal/specs/1788000000-old/routing.md",
            "seal/specs/1788000000-moved/routing.md",
        }
        assert chain.changed_routing(paths, renamed, "seal/specs") == []

    def test_a_move_not_yet_committed_is_read_from_the_files(
        self, tmp_path, monkeypatch
    ):
        """Under `--worktree` an untracked file has no blob git can name, so
        the moved file's bytes are hashed to pair it."""
        d, _old = two_declarations(tmp_path)
        os.rename(d / "seal/specs/1788000000-old", d / "seal/specs/1788000000-moved")
        monkeypatch.setattr(chain, "WORKTREE", True)
        _paths, renamed = chain.changed(str(d), "main")
        assert renamed == {
            "seal/specs/1788000000-old/routing.md",
            "seal/specs/1788000000-moved/routing.md",
        }

    def test_a_deletion_beside_a_similar_addition_is_not_read_as_a_rename(
        self, tmp_path
    ):
        """Two declarations from one template differ in a row or two, which
        git's rename detection pairs. The check reads declarations, not file
        identity, so the deletion is seen."""
        d, old = two_declarations(tmp_path)
        git(d, "rm", "-q", "seal/specs/1788000000-old/routing.md")
        write(
            d,
            "seal/specs/1791999999-new/routing.md",
            old.replace("feature/x", "feature/y"),
        )
        commit(d, "one leaves, one arrives")
        paths, renamed = chain.changed(str(d), "main")
        assert renamed == set()
        assert chain.changed_routing(paths, renamed, "seal/specs") == [
            "seal/specs/1788000000-old/routing.md",
            "seal/specs/1791999999-new/routing.md",
        ]


# --- carried_by ---------------------------------------------------------------

RELEASE = "release/v9.9.9"
GITHUB = {"GIT_COMMITTER_NAME": "GitHub", "GIT_COMMITTER_EMAIL": "noreply@github.com"}


def squash(d, source, subject, committer=None):
    """Squash `source` onto the checked-out branch as GitHub's merge button
    does: one commit, committed by GitHub, its subject ending with the pull
    request's number. `committer` replaces GitHub's identity."""
    git(d, "merge", "--squash", "-q", source)
    subprocess.run(
        ["git", "-C", str(d), "commit", "-qm", subject],
        check=True,
        capture_output=True,
        env={**os.environ, **(committer or GITHUB)},
    )
    return git(d, "rev-parse", "HEAD")


def released(root, subject="feat: a work item (#7)", committer=None, keep=False):
    """`release/v9.9.9` cut from `main` with `feature/x` squashed into it and
    the feature branch deleted, so the item's records name commits HEAD does
    not descend from — what a release pull request into `main` carries."""
    git(root, "switch", "-q", "-c", RELEASE, "main")
    squash(root, "feature/x", subject, committer)
    if not keep:
        git(root, "branch", "-q", "-D", "feature/x")


@pytest.mark.rule("judged-where-carried")
class TestCarriedBy:
    def test_a_declaration_only_a_squash_merge_touched_is_that_pull_requests(
        self, branch, monkeypatch
    ):
        root, _code = branch
        monkeypatch.setattr(chain, "WORKTREE", False)
        released(root)
        rel = f"{ITEM}/routing.md"
        sha, subject = chain.carried_by(str(root), "main", rel)
        assert sha == git(root, "rev-parse", "HEAD")
        assert subject == "feat: a work item (#7)"
        # Under `--worktree` an edit not yet committed is this branch's own.
        monkeypatch.setattr(chain, "WORKTREE", True)
        assert chain.carried_by(str(root), "main", rel) is not None
        write(root, rel, (root / rel).read_text(encoding="utf-8") + "\nA note.\n")
        assert chain.carried_by(str(root), "main", rel) is None

    def test_the_items_own_commits_a_persons_squash_and_an_unnumbered_one_are_not(
        self, branch, monkeypatch
    ):
        """The item's own branch, a squash a person committed with a subject
        naming an issue the way this repository's commits do, GitHub's commit
        whose subject does not end with a pull request number, and a path no
        commit touched each leave the declaration this pull request's."""
        root, _code = branch
        monkeypatch.setattr(chain, "WORKTREE", False)
        rel = f"{ITEM}/routing.md"
        assert chain.carried_by(str(root), "main", rel) is None
        released(root, committer={"GIT_COMMITTER_EMAIL": "t@t"}, keep=True)
        assert chain.carried_by(str(root), "main", rel) is None
        git(root, "reset", "-q", "--hard", "main")
        squash(root, "feature/x", "feat: a work item (#7), edited")
        assert chain.carried_by(str(root), "main", rel) is None
        assert chain.carried_by(str(root), "main", "seal/specs/none/routing.md") is None


# --- grammar ------------------------------------------------------------------

DOC = ROOT / "docs" / "the-review-record.md"
TEMPLATE = ROOT / "templates" / "sdd-round.md"


def doc_with(tmp_path, old, new):
    """The grammar document with `old`, which stands once, replaced by `new`,
    written to a path of its own."""
    text = DOC.read_text(encoding="utf-8")
    assert text.count(old) == 1, old
    path = tmp_path / "the-review-record.md"
    path.write_text(text.replace(old, new), encoding="utf-8")
    return path


def row_of(key):
    """The table row of `key` as the document writes it, its line end
    included."""
    return next(
        ln + "\n"
        for ln in DOC.read_text(encoding="utf-8").splitlines()
        if ln.startswith(f"| `{key}` |")
    )


def readings(rows):
    """`rows` as plain values, so two loads of one table compare equal."""
    return {
        k: (r.shape.pattern if r.shape else None, r.where, r.many, r.refused)
        for k, r in rows.items()
    }


class TestGrammar:
    def test_the_table_loads_and_every_line_matches_its_row_whole(
        self, monkeypatch, tmp_path
    ):
        """S4 (T2): the table in `docs/the-review-record.md` *The round
        record* is what the check reads. Its rows are the nine labels, the
        finding heading, the two sections and the three old spellings, and
        the module's grammar is the document's, read again here. Every line
        `templates/sdd-round.md` writes of a row matches it whole, and the
        same line with a word after it is refused wherever the row's shape
        ends in fixed words — `verdict: fixed abc1234 and more` among them,
        through the reader end to end. Two refusals arrive by construction:
        a severity other than `must` or `should`, and a finding with no
        `answer:` line. And a row changed in the document changes what the
        readers accept, so no constant stands beside the table.

        Protects: a fourth statement of the grammar drifting from the
        table, and a partial match letting a shape through, which #923 met
        three times. No other case loads the table or reads a line through
        a changed one."""
        assert set(chain.GRAMMAR) == {
            "target:",
            "original:",
            "severity:",
            "location:",
            "evidence:",
            "verdict:",
            "regression:",
            "reopens:",
            "answer:",
            "confirms:",
            "### <n>. <symptom>",
            "## Findings",
            "## Confirmations",
        }, chain.GRAMMAR
        # S10 of #1000: the old spellings are a table of their own, and no
        # cell of either table holds a dash.
        assert chain.OLD_SPELLINGS == {
            "Target SHA:": "target:",
            "refixes:": "regression:",
            "fix of a fix:": "regression:",
        }, chain.OLD_SPELLINGS
        rows, old = chain.grammar(str(DOC), reader)
        assert readings(rows) == readings(chain.GRAMMAR)
        assert old == chain.OLD_SPELLINGS
        cells = [c for r in readings(rows).values() for c in r] + [*old.items()]
        assert not [c for c in cells if chain.DASH in str(c)], cells

        lines = reader.readable(TEMPLATE.read_text(encoding="utf-8"))
        # A finding carries one of `regression:` and `reopens:`, and the
        # template's finding writes the first; the second's example is its
        # comment's `round-<N>#<n>`. The `original:` line is owed only in a
        # migration repository, so the template writes it in a comment, and
        # that comment's line is the one read here (#988).
        raw = TEMPLATE.read_text(encoding="utf-8").splitlines()
        written_by_comment = {
            "reopens:": ["reopens: round-1#2"],
            "original:": [ln for ln in raw if ln.startswith("original: ")],
        }
        for key in chain.LABELS:
            row = chain.GRAMMAR[key]
            written = [ln for ln in lines if chain.label_of(ln) == key]
            written = written or written_by_comment.get(key, [])
            assert written, f"the template writes no `{key}` line"
            for ln in written:
                assert row.shape.fullmatch(ln), ln
                trailing = row.shape.fullmatch(f"{ln} and more")
                assert bool(trailing) == (key == "answer:"), ln
        headings = [ln for ln in lines if ln.startswith("### ")]
        assert headings and all(chain.finding_number(h) == 1 for h in headings)
        for key in chain.SECTION_ROWS:
            assert len(chain.sections_of(reader, lines, key)) == 1, key
        longer = record("abc1234", [finding(1, "open")]).replace(
            "## Findings", "## Findings so far"
        )
        assert chain.findings(reader, reader.readable(longer), "r.md") == (
            [],
            [("r.md", 0, chain.NO_FINDINGS)],
        )

        text = record(
            "abc1234",
            [
                finding(1, "fixed abc1234 and more"),
                finding(2, "rejected", severity="anything at all"),
                finding(3, "rejected").replace("answer: \n", ""),
                finding(4, "rejected"),
            ],
        ).replace(
            "target: abc1234 against main", "target: abc1234 against main and more"
        )
        lines = reader.readable(text)
        found, errors = chain.record_findings(reader, text, "r.md")
        assert [f.number for f in found] == [4], errors
        said = {line: why for _rel, line, why in errors}
        verdict = lines.index("verdict: fixed abc1234 and more") + 1
        assert "reads `verdict: fixed abc1234 and more`" in said[verdict], said
        assert "a verdict is `open`, `fixed <commit>`" in said[verdict], said
        severity = lines.index("severity: anything at all") + 1
        assert "a severity is `must` or `should`" in said[severity], said
        third = lines.index("### 3. the parser drops a row") + 1
        assert "no `answer:` line" in said[third], said
        target = lines.index("target: abc1234 against main and more") + 1
        assert "`<sha> against <base>`" in said[target], said
        assert len(errors) == 4, errors
        assert chain.verdict_of("fixed abc1234 and more") is None

        could = record("abc1234", [finding(1, "rejected", severity="could")])
        assert chain.record_findings(reader, could, "r.md")[1] != []
        wider = doc_with(
            tmp_path,
            "`severity: (?:must\\|should)`",
            "`severity: (?:must\\|should\\|could)`",
        )
        monkeypatch.setattr(chain, "GRAMMAR", chain.grammar(str(wider), reader)[0])
        assert chain.record_findings(reader, could, "r.md")[1] == []

    def test_the_warden_and_the_review_skill_name_every_line_a_finding_needs(self):
        """S8 (#985): `agents/warden.md` step 7 and `skills/code-review/SKILL.md`
        *The record* each list the lines a finding carries, and each names
        every row the table places in a finding as `one`, read from the table.

        Protects: a row added to the table and missed in either list, which
        tells the warden to write a finding the check then refuses at the
        pull request. `evidence:` is the row #985 added."""
        needed = [
            key
            for key, row in chain.GRAMMAR.items()
            if row.where == chain.IN_FINDING and row.many == chain.ONE
        ]
        assert "evidence:" in needed, needed
        warden = " ".join((ROOT / "agents" / "warden.md").read_text("utf-8").split())
        step = warden.split("7. Write the record", 1)[1].split("## Never", 1)[0]
        skill = " ".join(
            (ROOT / "skills" / "code-review" / "SKILL.md").read_text("utf-8").split()
        )
        record = skill.split("## The record ", 1)[1]
        record = record.split("Each finding carries one line of each row", 1)[1]
        record = record.split("The check refuses a finding missing any.", 1)[0]
        for where, text in (
            ("warden.md step 7", step),
            ("`skills/code-review/SKILL.md` *The record*", record),
        ):
            missing = [key for key in needed if f"`{key}" not in text]
            assert missing == [], f"{where} does not name {missing}"

    @pytest.mark.parametrize(
        "old, new, said",
        [
            (
                "## The round record\n",
                "## The round records\n",
                "0 `## The round record`",
            ),
            ("| How many |", "| Count |", "holds no table headed"),
            ("|---|---|---|---|---|\n| `target:`", "| `target:`", "separator row"),
            (" | a severity is `must` or `should` |", " |", "4 cells"),
            ("| `severity:` |", "| severity: |", "not one code span"),
            ("| `severity:` |", "| `severity:` `x` |", "not one code span"),
            ("(?:must\\|should)`", "(?:must\\|should`", "does not compile"),
            (
                "| a finding | one | a severity",
                "| a section | one | a severity",
                "cannot read",
            ),
            (
                "| a finding | one | a severity",
                "| a finding | two | a severity",
                "cannot read",
            ),
            (row_of("reopens:"), "", "no `reopens:` row"),
            ("`target: (?P<commit>", "`target: (?P<sha>", "no `(?P<commit>…)`"),
            # S12 of #1000: the old-spellings table the loader cannot read.
            ("| Old spelling | Means |", "| Old | Means |", "no table headed"),
            (
                "| Old spelling | Means |",
                "| Old spelling | Meaning |",
                "no table headed",
            ),
            (
                "| `refixes:` | `regression:` |",
                "| refixes: | `regression:` |",
                "code span",
            ),
            (
                "| `refixes:` | `regression:` |",
                "| `refixes:` | `regression:` `x` |",
                "code span",
            ),
            (
                "| `refixes:` | `regression:` |",
                "| `refixes:` | `regressed:` |",
                "no label of the grammar table",
            ),
            (
                "| `refixes:` | `regression:` |",
                "| `refixes:` | `## Findings` |",
                "no label of the grammar table",
            ),
            (
                "| `refixes:` | `regression:` |",
                "| `answer:` | `regression:` |",
                "`answer:` is a label of the grammar table",
            ),
            (
                "| `refixes:` | `regression:` |",
                "| `refixes:` | `regression:` |\n| `refixes:` | `regression:` |",
                "a second `refixes:` old spelling",
            ),
            (
                "| `refixes:` | `regression:` |",
                "| `refixes` | `regression:` |",
                "an old spelling is a label",
            ),
            (
                row_of("answer:"),
                row_of("answer:") + "| `Answer:` | — | nowhere | none | x |\n",
                "not one code span",
            ),
            (
                row_of("answer:"),
                row_of("answer:") + "| `said:` | `said: .+` | nowhere | one | x |\n",
                "cannot read",
            ),
            ("`severity: (?:must", "`sev: (?:must", "cannot read"),
            (row_of("severity:"), row_of("severity:") * 2, "a second `severity:` row"),
            (
                row_of("answer:"),
                row_of("answer:")
                + "| `## Probes` | `## Probes` | the record | one | x |\n",
                "reads nothing from",
            ),
            (
                "| a finding | one | a verdict is",
                "| a finding | any | a verdict is",
                "`verdict:` row's `How many` is `any`, and the check can honour "
                "only `one`",
            ),
            (
                "| a finding | one | a verdict is",
                "| a finding | at most one | a verdict is",
                "`How many` is `at most one`, and the check can honour only `one`",
            ),
            (
                "| a finding | one | a location is",
                "| a finding | at most one | a location is",
                "`location:` row's `How many` is `at most one`",
            ),
            (
                "| outside every finding | one | it names",
                "| outside every finding | any | it names",
                "`target:` row's `How many` is `any`",
            ),
            (
                "| a finding | at most one | a reference is",
                "| a finding | any | a reference is",
                "`regression:` row's `How many` is `any`, and the check can "
                "honour only `one` or `at most one`",
            ),
            (
                "| a finding | at most one | a reopened close",
                "| a finding | any | a reopened close",
                "`reopens:` row's `How many` is `any`",
            ),
            (
                "| outside every finding | at most one | it names the migration",
                "| outside every finding | one | it names the migration",
                "`original:` row's `How many` is `one`, and the check can honour "
                "only `at most one`",
            ),
            (
                "| a finding | one | a verdict is",
                "| outside every finding | one | a verdict is",
                '`verdict:` row stands "outside every finding", and the check '
                'reads it only where the table says "a finding"',
            ),
            (
                "| outside every finding | one | it names",
                "| a finding | one | it names",
                '`target:` row stands "a finding"',
            ),
            (
                "| `## Confirmations` | any | it is",
                "| a finding | any | it is",
                '`confirms:` row stands "a finding"',
            ),
        ],
    )
    def test_a_document_the_check_cannot_read_is_exit_2_naming_it(
        self, tmp_path, old, new, said
    ):
        """S4 (T2): a table the check cannot read stops it and is never a
        pass. Each way to break it — no section, no header, no separator, a
        row of the wrong width, a `Line` that is no code span, a shape that
        does not compile, a `Where` or `How many` the table does not use, a
        row the check reads missing or naming no part it reads, an
        old-spellings table that is missing, holds a cell that is no code
        span, means no label, spells a label, or names a spelling twice
        (S12 of #1000), a label whose shape does not open with
        it, a row twice, a heading row the check reads nothing from, and a
        row the check reads a meaning from standing where its reader does not
        look or allowing a `How many` that reader cannot keep — is refused
        naming the document. Run as a command beside such a document, the
        check exits 2 with that sentence and no traceback, and beside no
        document at all the same; imported, it raises the error for the
        importer to decide.

        Protects: a `docs/` rewrite (#941) moving the table out from under
        the check while it reads every record as holding nothing, and one
        loosening a count the reader cannot keep: `verdict:` at `any`, read
        as its last line, let a finding holding `open` then `deferred #5`
        pass as deferred; and one moving a read row: `verdict:` outside every
        finding left `finding_of` no verdict to decide on, and `target:` in a
        finding raised `KeyError` in `round_of`, a traceback where the check
        owes exit 2. No other case hands the loader a document it cannot
        read."""
        path = doc_with(tmp_path, old, new)
        with pytest.raises(chain.GrammarError) as refused:
            chain.grammar(str(path), reader)
        assert str(refused.value).startswith(str(path)), refused.value
        assert said in str(refused.value), refused.value
        missing = tmp_path / "no-such-document.md"
        with pytest.raises(chain.GrammarError, match="cannot be read"):
            chain.grammar(str(missing), reader)

        tree = tmp_path / "tree"
        script = tree / "skills" / "code-review" / "scripts" / "chain_check.py"
        script.parent.mkdir(parents=True)
        script.write_text(CHAIN.read_text(encoding="utf-8"), encoding="utf-8")
        (tree / "skills" / "verify" / "scripts").mkdir(parents=True)
        (tree / "skills" / "verify" / "scripts" / "unverified_check.py").write_text(
            READER.read_text(encoding="utf-8"), encoding="utf-8"
        )
        (tree / "docs").mkdir()
        target = tree / "docs" / "the-review-record.md"
        named = os.path.join(str(script.parent), "..", "..", "..", "docs", target.name)
        for present in (True, False):
            if present:
                target.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
            else:
                target.unlink()
            done = subprocess.run(
                [
                    sys.executable,
                    str(script),
                    "--baseline",
                    "HEAD",
                    "--root",
                    str(tmp_path),
                ],
                capture_output=True,
                encoding="utf-8",
                errors="replace",
            )
            assert done.returncode == 2, (present, done.returncode, done.stderr)
            assert "Traceback" not in done.stderr, done.stderr
            assert named in done.stderr, done.stderr
            assert "grammar would not load" in done.stderr, done.stderr
            assert (said if present else "cannot be read") in done.stderr, done.stderr
        with pytest.raises(ValueError, match="cannot be read"):
            load(script, "chain_check_imported_beside_no_table")


# --- verdict_of ---------------------------------------------------------------


class TestVerdictOf:
    def test_the_four_values_read_and_nothing_else_does(self):
        """S3 (T25): a `verdict:` value is one of four shapes, read as it is
        written against the grammar table's `verdict:` row whole. Anything
        else is None, which the arm refuses by name."""
        sha = "1a2b3c4d" * 5
        for value, read in (
            ("open", (chain.OPEN, None)),
            ("fixed abc1234", (chain.FIXED, "abc1234")),
            (f"fixed {sha}", (chain.FIXED, sha)),
            ("rejected", (chain.REJECTED, None)),
            ("deferred #12", (chain.DEFERRED, "#12")),
            ("deferred the frame", (chain.DEFERRED, "the frame")),
        ):
            assert chain.verdict_of(value) == read, value
        for value in (
            "Fixed abc1234",
            "fixed",
            "fixed abc1234.",
            "fixed abc123",
            f"fixed {sha}0",
            "fixed ABC1234",
            "fixed abc1234 · fix pass: done",
            "deferred",
            "deferred ",
            "confirmed",
            "**fixed** abc1234",
            "open — see below",
            "Open",
            " rejected",
            "answered",
            "Rejected",
            "",
        ):
            assert chain.verdict_of(value) is None, value


# --- deferred_home and issue_of -----------------------------------------------


class TestDeferredHome:
    def test_the_home_after_the_word_is_read(self):
        assert chain.deferred_home("deferred #12") == "#12"
        assert chain.issue_of(chain.deferred_home("deferred #12")) == 12
        assert chain.deferred_home("deferred the frame") == "the frame"

    def test_no_home_and_prose_name_no_issue(self):
        assert chain.deferred_home("deferred") is None
        assert chain.deferred_home("deferredness #12") is None
        assert chain.deferred_home("fixed abc1234") is None
        assert chain.issue_of(chain.deferred_home("deferred to #664")) is None
        assert chain.issue_of(chain.deferred_home("deferred #12.")) is None


# --- location_of --------------------------------------------------------------


class TestLocationOf:
    @pytest.mark.rule("location-touched-by-fix")
    def test_one_or_more_backticked_coordinates_read_and_nothing_else_does(self):
        """S22 (T33): a `location:` value is one or more backticked `path`,
        `path:line` or `path:first-last` items joined by `, `, read against
        the grammar table's `location:` row whole and then as the paths they
        name. Anything else is None, which the arm refuses: the `path#unit`
        coordinate #923 leaked among them."""
        for value, paths in (
            ("`a.py`", ["a.py"]),
            ("`a.py:12`", ["a.py"]),
            ("`a.py:12-14`", ["a.py"]),
            ("`docs/x/`", ["docs/x/"]),
            ("`a.py:1`, `docs/b.md:3-4`", ["a.py", "docs/b.md"]),
            ("`a.py:1`, `b.py`, `c/d.md:9`", ["a.py", "b.py", "c/d.md"]),
        ):
            assert chain.location_of(value) == paths, value
        for value in (
            "`:617`",
            "`a.py:1`, `:617`",
            "a.py:12",
            "https://example.com/a",
            "`https://example.com/a`",
            "**`a.py:1`**",
            "_`a.py:1`_",
            "`a.py:1`,`b.py`",
            "`a.py:1` and `b.py`",
            "`a.py:1`, ",
            "`a.py:x`",
            "`a.py:1-`",
            "`/abs/a.py`",
            "`a.py`.",
            "`a b.py`",
            "`a.py#unit`",
            "`a.py#unit:3`",
            "`a.py:1`, `b.py#unit`",
            "",
        ):
            assert chain.location_of(value) is None, value


# --- reference_of -------------------------------------------------------------


class TestReferenceOf:
    def test_a_round_and_a_finding_read_and_nothing_else_does(self):
        """S23 (T35): a reference is `round-<N>#<n>`, or `round-<N>` for a
        round's fix pass, in that spelling and no other: the grammar table's
        `regression:` row, read whole."""
        for value, read in (
            ("round-2#3", (2, 3)),
            ("round-2", (2, None)),
            ("round-12#10", (12, 10)),
        ):
            assert chain.reference_of(value) == read, value
        for value in (
            "round 2's 3",
            "Round-2#3",
            "ROUND-2#3",
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
        ):
            assert chain.reference_of(value) is None, value


# --- a record's target --------------------------------------------------------


def target_of(text):
    """`(the commit round_of reads off the record's target line, its
    errors)`."""
    read, errors = chain.round_of(reader, text, "r.md", 1)
    return read.target, errors


class TestRecordTarget:
    def test_the_one_target_line_reads_its_commit(self):
        """S4: a record's reviewed commit is its one `target:` line, reading
        `<sha> against <base>` or, for a verifying round,
        `<sha>, fixes <a>..<b>`; the commit is the first word."""
        sha = "1a2b3c4d" * 5
        for value, read in (
            ("abc1234 against main", "abc1234"),
            (f"{sha} against origin/release/v0.22.0", sha),
            ("abc1234, fixes 1111111..abc1234", "abc1234"),
        ):
            text = record("x").replace("target: x against main", f"target: {value}")
            assert target_of(text) == (read, []), value

    @pytest.mark.rule("round-record-read-by-label")
    def test_no_line_two_lines_or_a_value_it_cannot_read_is_refused(self):
        """S4: no `target:` line — the old `| Target SHA |` table row among
        the ways to have none — two of them, or a value outside the two
        shapes is refused by its line, and no commit is read."""
        table = record("x").replace(
            "target: x against main",
            "| Field | Value |\n|---|---|\n| Target SHA | abc1234 against main |",
        )
        assert target_of(table) == (None, [("r.md", 0, chain.NO_TARGET)])
        two = record("abc1234").replace(
            "## Findings", "target: abc1234 against main\n\n## Findings"
        )
        lines = reader.readable(two)
        second = [i + 1 for i, ln in enumerate(lines) if ln.startswith("target:")][1]
        sha, errors = target_of(two)
        assert sha is None and [line for _rel, line, _why in errors] == [second]
        assert "2 `target:` lines" in errors[0][2], errors
        for value in (
            "abc1234",
            "abc123 against main",
            "ABC1234 against main",
            "abc1234 against",
            "abc1234 against main.",
            "`abc1234` against main",
            "abc1234, fixes 111..abc1234",
            "abc1234 fixes 1111111..abc1234",
            "abc1234 against main · a verifying round",
            "",
        ):
            text = record("x").replace("target: x against main", f"target: {value}")
            lines = reader.readable(text)
            at = next(i + 1 for i, ln in enumerate(lines) if ln.startswith("target:"))
            sha, errors = target_of(text)
            assert sha is None, value
            assert [(rel, line) for rel, line, _why in errors] == [("r.md", at)], value
            assert "`<sha> against <base>`" in errors[0][2], value


# --- findings -----------------------------------------------------------------


class TestFindings:
    def test_each_finding_is_read_by_its_labelled_lines(self):
        """A finding's `### ` heading names it and its number; its one
        `verdict:` line decides it, its one `location:` line names its paths
        and its `regression:` line, where it stands, the earlier finding; a
        severity, an answer and a confirmation decide nothing."""
        text = record(
            "abc1234",
            [
                finding(1, "open"),
                finding(2, "fixed abc1234", severity="should", regression="round-1#4"),
                finding(
                    3,
                    "deferred #12",
                    severity="should",
                    location="`a.py:3`, `docs/b.md`",
                    regression="round-1",
                ),
            ],
            confirmations=confirm("round-1#2"),
        )
        lines = reader.readable(text)
        found, errors = chain.findings(reader, lines, "r.md")
        assert errors == []
        assert [
            (f.line, f.heading, f.number, f.verdict, f.paths, f.regression)
            for f in found
        ] == [
            (
                lines.index("verdict: open") + 1,
                "### 1. the parser drops a row",
                1,
                (chain.OPEN, None),
                ["f.txt"],
                None,
            ),
            (
                lines.index("verdict: fixed abc1234") + 1,
                "### 2. the parser drops a row",
                2,
                (chain.FIXED, "abc1234"),
                ["f.txt"],
                (1, 4),
            ),
            (
                lines.index("verdict: deferred #12") + 1,
                "### 3. the parser drops a row",
                3,
                (chain.DEFERRED, "#12"),
                ["a.py", "docs/b.md"],
                (1, None),
            ),
        ]
        assert found[1].regression_line == lines.index("regression: round-1#4") + 1
        empty = reader.readable(record("abc1234"))
        assert chain.findings(reader, empty, "r.md") == ([], [])

    @pytest.mark.rule("round-record-read-by-label")
    def test_what_the_check_cannot_read_is_refused_by_name(self):
        """S3, S11, S22 (T26, T33): what the reader cannot read is an error
        naming the path, the line and the finding's heading, never a pass — a
        finding with no `verdict:` line, with two, with its only one inside
        the fix block; a value outside the four; a labelled line above the
        first finding or under another section; a finding with no
        `location:` line, two, or one the check cannot read, whatever its
        verdict; two `regression:` lines, or one it cannot read; no
        `## Findings`, or two."""
        sections = [
            finding(1, "rejected").replace("verdict: rejected\n", ""),
            finding(2, "rejected").replace(
                "verdict: rejected\n", "verdict: rejected\nverdict: open\n"
            ),
            finding(3, "rejected")
            .replace("verdict: rejected\n", "")
            .replace("x = 1\n", "verdict: rejected\n"),
            finding(4, "deferred #9").replace("location: `f.txt:1`\n", ""),
            finding(5, "confirmed"),
            finding(6, "deferred #9", location="f.txt:1"),
            finding(7, "rejected").replace(
                "location: `f.txt:1`\n", "location: `f.txt:1`\nlocation: `g.txt`\n"
            ),
            finding(8, "rejected", regression="round 1's 3"),
            finding(9, "rejected", regression="round-1#3").replace(
                "regression: round-1#3\n",
                "regression: round-1#3\nregression: round-1#4\n",
            ),
            finding(10, "rejected"),
        ]
        text = record(
            "abc1234",
            sections,
            confirmations=confirm("none") + "\nlocation: `f.txt:1`\n",
        ).replace("## Findings\n\n", "## Findings\n\nverdict: rejected\n\n")
        lines = reader.readable(text)
        found, errors = chain.findings(reader, lines, "r.md")
        assert [f.heading for f in found] == ["### 10. the parser drops a row"]
        heads = [i + 1 for i, ln in enumerate(lines) if ln.startswith("### ")]

        def at(prefix, k=0):
            return [i + 1 for i, ln in enumerate(lines) if ln.startswith(prefix)][k]

        assert [(rel, line) for rel, line, _why in errors] == [
            ("r.md", at("verdict: ")),
            ("r.md", heads[0]),
            ("r.md", at("verdict: open")),
            ("r.md", heads[2]),
            ("r.md", heads[3]),
            ("r.md", at("verdict: confirmed")),
            ("r.md", at("location: f.txt:1")),
            ("r.md", at("location: `g.txt`")),
            ("r.md", at("regression: round 1's 3")),
            ("r.md", at("regression: round-1#4")),
            ("r.md", at("location: ", -1)),
        ], errors
        said = [why for _rel, _line, why in errors]
        assert "outside a finding" in said[0] and "outside a finding" in said[-1]
        assert "`verdict:`" in said[0] and "`location:`" in said[-1]
        for why, n in zip(said[1:10], (1, 2, 3, 4, 5, 6, 7, 8, 9), strict=True):
            assert f"### {n}. the parser drops a row" in why, why
        assert "2 `verdict:` lines" in said[2]
        assert "no `verdict:` line" in said[1] and "no `verdict:` line" in said[3]
        assert "no `location:` line" in said[4]
        assert "`verdict: confirmed`" in said[5]
        assert "`fixed <commit>`" in said[5] and "`deferred <home>`" in said[5]
        assert "`location: f.txt:1`" in said[6] and "`path:line`" in said[6]
        assert "2 `location:` lines" in said[7]
        assert "`regression: round 1's 3`" in said[8] and "`round-<N>#<n>`" in said[8]
        assert "2 `regression:` lines" in said[9]
        assert chain.findings(
            reader, reader.readable("# r\n\n## Probes\n"), "r.md"
        ) == (
            [],
            [("r.md", 0, chain.NO_FINDINGS)],
        )
        two = reader.readable(record("abc1234") + "\n## Findings\n")
        second = [i + 1 for i, ln in enumerate(two) if ln == "## Findings"][1]
        _found, errors = chain.findings(reader, two, "r.md")
        assert [(line, why) for _rel, line, why in errors] == [
            (second, chain.TWO_FINDINGS)
        ]

    def test_a_label_in_another_spelling_is_refused_by_line(self):
        """S24 (T32): a line whose first word, case-folded and stripped of
        emphasis, is one of the grammar table's nine labels or one of the
        old spellings the old-spellings table names, `fix of a fix`,
        `refixes` and `Target SHA`, and which is not the exact lowercase
        form, is refused
        at its line naming the label the check reads — never skipped as
        prose. A finding carrying one is not read past it, so a finding with
        both spellings does not pass on the lowercase one."""
        for spelling, label in (
            ("Verdict: open", "`verdict:`"),
            ("**verdict:** open", "`verdict:`"),
            ("VERDICT: open", "`verdict:`"),
            ("verdict : open", "`verdict:`"),
            ("_verdict_: open", "`verdict:`"),
            ("Fix of a fix: `open_findings`", "`regression:`"),
            ("`fix of a fix`: the unit", "`regression:`"),
            ("fix of a fix: the unit", "`regression:`"),
            ("refixes: round-1#1", "`regression:`"),
            ("Refixes: round-1#1", "`regression:`"),
            ("Regression: round-1#1", "`regression:`"),
            ("Reopens: round-1#1", "`reopens:`"),
            ("**reopens:** round-1#1", "`reopens:`"),
            ("Severity: must", "`severity:`"),
            ("Location: `f.txt:1`", "`location:`"),
            ("Evidence: read `a.py:1`", "`evidence:`"),
            ("**evidence:** read `a.py:1`", "`evidence:`"),
            ("evidence : read `a.py:1`", "`evidence:`"),
            ("Answer: done", "`answer:`"),
            ("  answer : done", "`answer:`"),
            ("Confirms: round-1#1", "`confirms:`"),
            ("**confirms:** none", "`confirms:`"),
            ("Target SHA: abc1234 against main", "`target:`"),
            ("Target: abc1234 against main", "`target:`"),
        ):
            text = record(
                "abc1234",
                [
                    finding(1, "rejected").replace("answer: \n", f"{spelling}\n"),
                    finding(2, "rejected"),
                ],
            )
            lines = reader.readable(text)
            found, errors = chain.findings(reader, lines, "r.md")
            assert [f.number for f in found] == [2], spelling
            assert [(rel, line) for rel, line, _why in errors] == [
                ("r.md", lines.index(spelling) + 1)
            ], spelling
            why = errors[0][2]
            assert "### 1. the parser drops a row" in why, why
            assert label in why and "another spelling" in why, why
        outside = record("abc1234", [finding(1, "rejected")]).replace(
            "## Not judged", "Verdict: rejected\n\n## Not judged"
        )
        lines = reader.readable(outside)
        found, errors = chain.findings(reader, lines, "r.md")
        assert [f.number for f in found] == [1]
        assert [(line, "`verdict:`" in why) for _rel, line, why in errors] == [
            (lines.index("Verdict: rejected") + 1, True)
        ]
        exact = record("abc1234", [finding(1, "rejected")])
        assert chain.findings(reader, reader.readable(exact), "r.md")[1] == []
        for prose in ("Answers: none", "Verdicts read below.", "Severity matters."):
            text = record("abc1234", [finding(1, "rejected")]).replace(
                "Why it matters.", prose
            )
            assert chain.findings(reader, reader.readable(text), "r.md")[1] == []

    @pytest.mark.rule("round-record-read-by-label")
    def test_a_reopens_line_names_one_finding_and_never_beside_a_regression_line(
        self,
    ):
        """S23, S24 (T42): a `reopens:` line is read into its finding with its
        line, naming the earlier finding as `round-<N>#<n>`. A reopened close
        is a finding's, so `reopens: round-1` is refused; so is a second
        `reopens:` line, and a finding holding a `reopens:` and a
        `regression:` line, at the later of the two, the refusal naming
        which line each case takes. A refused finding is left out of the
        list."""
        text = record(
            "abc1234",
            [
                finding(1, "open", reopens="round-1#2"),
                finding(2, "open", reopens="round-1"),
                finding(3, "open", reopens="round-1#2").replace(
                    "reopens: round-1#2\n",
                    "reopens: round-1#2\nreopens: round-1#3\n",
                ),
                finding(4, "open", regression="round-1#2", reopens="round-1#3"),
                finding(5, "open").replace(
                    "verdict: open\n",
                    "reopens: round-1#4\nverdict: open\nregression: round-1\n",
                ),
                finding(6, "open"),
            ],
            n=2,
        )
        lines = reader.readable(text)
        found, errors = chain.findings(reader, lines, "r.md")
        assert [(f.number, f.reopens, f.regression) for f in found] == [
            (1, (1, 2), None),
            (6, None, None),
        ], errors
        assert found[0].reopens_line == lines.index("reopens: round-1#2") + 1
        assert found[1].reopens_line is None
        fourth = lines.index("### 4. the parser drops a row")
        assert [(rel, line) for rel, line, _why in errors] == [
            ("r.md", lines.index("reopens: round-1") + 1),
            ("r.md", lines.index("reopens: round-1#3") + 1),
            ("r.md", lines.index("reopens: round-1#3", fourth) + 1),
            ("r.md", lines.index("regression: round-1") + 1),
        ], errors
        said = [why for _rel, _line, why in errors]
        for why, n in zip(said, (2, 3, 4, 5), strict=True):
            assert f"### {n}. the parser drops a row" in why, why
        assert "`reopens: round-1`" in said[0] and "`round-<N>#<n>`" in said[0]
        assert "2 `reopens:` lines" in said[1]
        for why in said[2:]:
            assert "`regression:`" in why and "`reopens:`" in why, why
            assert "a fix pass's own commit made the defect" in why, why
            assert "does not hold" in why, why

    def test_a_reference_label_with_nothing_after_it_is_refused(self):
        """S24: a bare `reopens:` or `regression:` line is the exact form,
        and its reader refuses the empty value at its line; a bare
        `regression:` beside a `reopens:` line is refused as a finding
        holding both."""
        for bare in ("reopens:", "regression:"):
            text = record(
                "abc1234",
                [
                    finding(1, "open").replace(
                        "verdict: open\n", f"verdict: open\n{bare}\n"
                    )
                ],
                n=2,
            )
            lines = reader.readable(text)
            found, errors = chain.findings(reader, lines, "r.md")
            assert found == [], bare
            assert [line for _r, line, _w in errors] == [lines.index(bare) + 1], errors
            assert f"`{bare}" in errors[0][2], errors
        both = record(
            "abc1234",
            [
                finding(1, "open", reopens="round-1#1").replace(
                    "verdict: open\n", "verdict: open\nregression:\n"
                )
            ],
            n=2,
        )
        found, errors = chain.findings(reader, reader.readable(both), "r.md")
        assert found == [], errors
        assert any("`reopens:` line" in why for _r, _l, why in errors), errors

    def test_an_evidence_line_missing_twice_or_malformed_is_refused(self):
        """S1, S3, S4 (#985): a finding carries one `evidence:` line, matched
        whole against its row. A finding with none is refused at its heading,
        one with two at the second, and each value the row does not hold at
        its line with the row's `Refused as`: a `read` coordinate with no
        line or no backticks, an `executed` command with no backticks, a
        word other than the two, nothing after the label, and a word after
        the last backtick. A refused finding is left out of the list, and
        the record's other findings still read.

        Protects: a finding whose claim names nothing it rests on passing
        the check, the trait #971's two `wrong` findings shared."""
        malformed = (
            "read `a.py`",
            "read a.py:1",
            "executed pytest",
            "ran `x`",
            None,
            "executed `x` and more",
        )
        sections = [
            finding(1, "open", evidence=None),
            finding(2, "open").replace(
                "evidence: read `f.txt:1`\n",
                "evidence: read `f.txt:1`\nevidence: executed `git grep -n x`\n",
            ),
            *(
                finding(n, "open").replace(
                    "evidence: read `f.txt:1`",
                    f"evidence: {value}" if value else "evidence:",
                )
                for n, value in enumerate(malformed, 3)
            ),
            finding(9, "open"),
        ]
        lines = reader.readable(record("abc1234", sections))
        found, errors = chain.findings(reader, lines, "r.md")
        assert [f.number for f in found] == [9], errors
        heads = [i + 1 for i, ln in enumerate(lines) if ln.startswith("### ")]
        said = [i + 1 for i, ln in enumerate(lines) if ln.startswith("evidence:")]
        assert [(rel, line) for rel, line, _why in errors] == [
            ("r.md", heads[0]),
            ("r.md", said[1]),
            *(("r.md", line) for line in said[2:8]),
        ], errors
        why = [w for _rel, _line, w in errors]
        shape = "`executed` and each command run, or `read` and each `path:line`"
        assert "no `evidence:` line: a finding carries one" in why[0], why[0]
        assert shape in why[0], why[0]
        assert "2 `evidence:` lines; a finding carries one" in why[1], why[1]
        for n, w in enumerate(why[2:], 3):
            assert f"### {n}. the parser drops a row" in w, w
            assert "which the check cannot read" in w and shape in w, w

    def test_both_evidence_forms_and_their_lists_read(self):
        """S5 (#985): `executed` with one or more backticked commands, and
        `read` with one or more backticked `path:line` or `path:first-last`
        coordinates, each list joined by `, `, match the row whole, and the
        finding carrying one is read and decided by its `verdict:` as
        before. The line decides nothing. A backtick ends a command on the
        line, and the record document names the spelling for a command that
        holds one, `$(printf '\\140')`, which the row reads.

        Protects: the row refusing a line a warden writes as the grammar
        says, which would stop every round at the pull request, and a
        warden whose search holds a backtick left with no way to name it
        but a different command or a `read` line."""
        stand_in = "$(printf '\\140')"
        said = f"with `{stand_in}` in place of the character"
        assert said in " ".join(DOC.read_text(encoding="utf-8").split()), said
        values = (
            "executed `git grep -n x -- tests`",
            "executed `a`, `b`",
            "read `a.py:3`",
            "read `a.py:3-9`, `docs/b.md:12`",
            f'executed `grep -n "{stand_in}evidence:" docs/x.md`',
        )
        row = chain.GRAMMAR["evidence:"]
        for value in values:
            assert row.shape.fullmatch(f"evidence: {value}"), value
        text = record(
            "abc1234",
            [finding(n, "rejected", evidence=v) for n, v in enumerate(values, 1)],
        )
        found, errors = chain.findings(reader, reader.readable(text), "r.md")
        assert errors == []
        assert [(f.number, f.verdict) for f in found] == [
            (n, (chain.REJECTED, None)) for n in range(1, 6)
        ]

    def test_a_target_or_confirms_line_out_of_its_place_is_refused(self):
        """A `target:` or `confirms:` line inside a finding, and a
        `confirms:` line outside `## Confirmations`, is refused at its line:
        the check reads each in one place, and a line it would not read is
        never passed as prose."""
        inside = record(
            "abc1234",
            [
                finding(1, "rejected").replace(
                    "answer: \n", "target: abc1234 against main\n"
                ),
                finding(2, "rejected").replace("answer: \n", "confirms: none\n"),
                finding(3, "rejected"),
            ],
        ).replace("## Probes", "confirms: none\n\n## Probes")
        lines = reader.readable(inside)
        found, errors = chain.findings(reader, lines, "r.md")
        assert [f.number for f in found] == [3]
        at = [i + 1 for i, ln in enumerate(lines) if ln.startswith(("target:", "conf"))]
        assert [(rel, line) for rel, line, _why in errors] == [
            ("r.md", line) for line in at[1:]
        ], errors
        said = [why for _rel, _line, why in errors]
        assert "### 1." in said[0] and "`target:`" in said[0], said
        assert "### 2." in said[1] and "`confirms:`" in said[1], said
        assert "`confirms:`" in said[2] and chain.CONFIRMATIONS_HEADING in said[2]

    def test_the_template_is_the_record_the_check_reads(self):
        """S1 (T29, T38): `templates/sdd-round.md` is a record the check reads
        — one `target:` line and no table above the findings; one finding at
        `open`, located at one coordinate, resting on one `evidence:` line
        (#985), naming the regression `round-1#1`;
        a `verdict:` written inside its fix block not read as a line;
        `## Confirmations` holding its two example entries, `confirms:
        round-1#2` read and `confirms: none`; its comments naming the
        `reopens:` line beside `regression:`, and the `original:` line a
        migration repository's round owes (#988), each read as no line; and
        no emoji anywhere in it."""
        text = (ROOT / "templates" / "sdd-round.md").read_text(encoding="utf-8")
        lines = reader.readable(text)
        found, errors = chain.record_findings(reader, text, "t")
        assert errors == []
        assert [(f.verdict, f.paths, f.regression, f.reopens) for f in found] == [
            ((chain.OPEN, None), ["path"], (1, 1), None)
        ]
        said = [ln for ln in lines if chain.label_of(ln) == "evidence:"]
        assert len(said) == 1, said
        comments = text.split(chain.FINDINGS_HEADING)[1].split("### 1. ")[0]
        assert "`reopens:`" in comments and "  reopens:  " in comments, comments
        assert not any(ln.startswith(chain.REOPENS_ROW) for ln in lines)
        above = text.split(chain.FINDINGS_HEADING)[0]
        assert "\noriginal: " in above and "`seal/parity.md`" in above, above
        assert not any(ln.startswith(chain.ORIGINAL_ROW) for ln in lines)
        assert found[0].heading.startswith("### 1. ") and found[0].number == 1
        confirmed, errors = chain.confirmations(reader, lines, "t")
        assert errors == []
        assert [ref for _line, ref in confirmed] == [(1, 2)]
        assert [ln for ln in lines if ln.startswith("confirms:")] == [
            "confirms: round-1#2",
            "confirms: none",
        ]
        head = text.split(chain.FINDINGS_HEADING)[0]
        assert chain.table_rows(reader, reader.readable(head)) == []
        assert chain.round_of(reader, text, "t", 1)[0].target == "1a2b3c4"
        fence = text.index("```", text.index("### 1. "))
        line_end = text.index("\n", fence) + 1
        fenced = text[:line_end] + "verdict: rejected\n" + text[line_end:]
        found, errors = chain.findings(reader, reader.readable(fenced), "t")
        assert errors == [] and [f.verdict for f in found] == [(chain.OPEN, None)]
        marks = [c for c in text if EMOJI.match(c)]
        assert marks == [], marks

    @pytest.mark.rule("round-record-read-by-label")
    def test_a_heading_with_no_number_or_a_number_twice_is_refused(self):
        """A finding is named across rounds by its heading's number, so a
        heading with none, or a number a second heading also carries, is a
        finding no `round-<N>#<n>` names alone: both are refused at the
        heading, and the record's other findings still read."""
        text = record(
            "abc1234",
            [
                finding(1, "fixed abc1234"),
                finding(1, "fixed abc1234", title="a second one"),
                finding(2, "deferred #9").replace("### 2. ", "### "),
                finding(3, "open"),
            ],
        )
        lines = reader.readable(text)
        found, errors = chain.findings(reader, lines, "r.md")
        assert [f.number for f in found] == [1, 3]
        assert [(line, why.split(" — ")[0]) for _r, line, why in errors] == [
            (lines.index("### 1. a second one") + 1, "### 1. a second one"),
            (
                lines.index("### the parser drops a row") + 1,
                "### the parser drops a row",
            ),
        ]
        assert "a second finding numbered 1" in errors[0][2]
        assert "no number" in errors[1][2]


# --- record_findings ----------------------------------------------------------


class TestRecordFindings:
    def test_a_record_whose_regions_close_reads_as_findings_reads_it(self):
        text = record("abc1234", [finding(1, "open"), finding(2, "rejected")])
        found, errors = chain.record_findings(reader, text, "r.md")
        assert errors == []
        assert found == chain.findings(reader, reader.readable(text), "r.md")[0]

    @pytest.mark.rule("round-record-read-by-label")
    def test_a_fence_or_comment_that_never_closes_is_refused_by_its_opener(self):
        """A fence or a comment that never closes hides every line after it,
        so the findings below it would vanish and the record would pass. The
        record is refused at the opener's line instead, and what the reader
        could still see is read as well."""
        hidden = finding(2, "open")
        # A `~~~` fence, so the backtick fence of the finding below it is
        # content and cannot close it.
        for opener, why in (("~~~python\n", "fence"), ("<!-- a note\n", "comment")):
            text = record(
                "abc1234",
                [
                    finding(1, "rejected").replace("answer: \n", "answer: \n" + opener),
                    hidden,
                ],
            )
            found, errors = chain.record_findings(reader, text, "r.md")
            lines = text.splitlines()
            second = lines.index("### 2. the parser drops a row")
            line = 1 + max(
                i for i, ln in enumerate(lines[:second]) if ln == opener.rstrip("\n")
            )
            assert [(rel, n) for rel, n, _why in errors] == [("r.md", line)], errors
            assert why in errors[0][2] and "never closes" in errors[0][2]
            assert [f.heading for f in found] == ["### 1. the parser drops a row"]

    def test_an_opener_quoted_in_a_code_span_is_no_comment(self):
        """Round 1 of #1000, finding 2: a finding quoting the comment opener
        in a code span is a correct record, read whole. Seen red against the
        scan that read the opener: refused at its line, the finding below
        it hidden."""
        text = record(
            "abc1234",
            [
                finding(1, "rejected").replace(
                    "answer: \n", "answer: the `<!--` opener is quoted\n"
                ),
                finding(2, "open"),
            ],
        )
        found, errors = chain.record_findings(reader, text, "r.md")
        assert errors == [] and [f.number for f in found] == [1, 2], errors


# --- confirmations ------------------------------------------------------------


class TestConfirmations:
    def test_each_confirms_line_reads_as_a_reference_or_none(self):
        """S23: each entry of `## Confirmations` is a `confirms:` line at the
        start of a line, reading `round-<N>#<n>`, read with its line, or
        `none`, and the prose after it is read for nothing. A record with
        nothing to confirm may leave the section out."""
        text = record(
            "abc1234",
            confirmations=confirm("round-1#2") + confirm("none") + confirm("round-3#1"),
            n=4,
        )
        lines = reader.readable(text)
        found, errors = chain.confirmations(reader, lines, "r.md")
        assert errors == []
        assert found == [
            (lines.index("confirms: round-1#2") + 1, (1, 2)),
            (lines.index("confirms: round-3#1") + 1, (3, 1)),
        ]
        left_out = record("abc1234").replace("## Confirmations\n", "")
        assert chain.CONFIRMATIONS_HEADING not in left_out
        assert chain.confirmations(reader, reader.readable(left_out), "r.md") == (
            [],
            [],
        )

    @pytest.mark.parametrize(
        "old, new, said",
        [
            (
                "| the record | at most one | each entry is",
                "| the record | one | each entry is",
                "no `## Confirmations` section",
            ),
            (
                row_of("confirms:"),
                row_of("confirms:")
                + "| `signed:` | `signed: .+` | `## Confirmations` | one | x |\n",
                "no `signed:` line: `## Confirmations` carries one",
            ),
        ],
    )
    def test_a_section_left_out_is_counted_where_the_table_says_one(
        self, monkeypatch, tmp_path, old, new, said
    ):
        """Round 2's finding 1 of #964: `## Confirmations` may be left out,
        and its reader counted nothing in a section that was absent. So a
        table giving the section, or any row placed in it, `one` loaded, and
        a record leaving the section out passed without what the table asks
        for. The reader now counts the section and each row placed in it
        against no lines where it is absent, so `one` is kept for every row
        there, the ones the check reads nothing from among them.

        Protects: a `docs/` rewrite (#941) adding a row to
        `## Confirmations` at `one`, or making the section `one`, and every
        record that leaves the section out passing anyway. The loader cases
        refuse only the rows the check reads a meaning from; no other case
        reads a record without the section against such a table."""
        left_out = record("abc1234", [finding(1, "open")]).replace(
            "## Confirmations\n", ""
        )
        assert chain.CONFIRMATIONS_HEADING not in left_out
        assert chain.round_of(reader, left_out, "r.md", 1)[1] == []
        table, _old = chain.grammar(str(doc_with(tmp_path, old, new)), reader)
        monkeypatch.setattr(chain, "GRAMMAR", table)
        errors = chain.round_of(reader, left_out, "r.md", 1)[1]
        assert [(rel, line) for rel, line, _why in errors] == [("r.md", 0)], errors
        assert said in errors[0][2], errors
        signed = "signed: the warden\n\n" * ("signed" in new)
        kept = record("abc1234", [finding(1, "open")], confirm("none") + signed)
        monkeypatch.setattr(chain, "LABELS", (*chain.LABELS, "signed:"))
        assert chain.round_of(reader, kept, "r.md", 1)[1] == []

    @pytest.mark.rule("round-record-read-by-label")
    def test_a_line_or_a_table_the_check_cannot_read_is_refused_by_line(self):
        """S23 (T36): a `confirms:` value the grammar table's `confirms:` row
        does not match whole, `round-<N>#<n>` or `none` — prose, another
        case, a bare `#3`, a round with no finding, emphasis, nothing, a
        reference with words after it — is refused by its line; so is a
        table row in the section, the old shape, and a second
        `## Confirmations` section."""
        bad = (
            "round 1's 3",
            "Round-1#3",
            "#3",
            "round-1",
            "**none**",
            "None",
            "round-1#2 holds",
            "",
        )
        text = record(
            "abc1234",
            confirmations="".join(confirm(cell) for cell in bad) + confirm("none"),
            n=2,
        )
        lines = reader.readable(text)
        found, errors = chain.confirmations(reader, lines, "r.md")
        assert found == []
        at = [
            i + 1
            for i, ln in enumerate(lines)
            if ln.startswith("confirms:") and ln != "confirms: none"
        ]
        assert [(rel, line) for rel, line, _why in errors] == [
            ("r.md", line) for line in at
        ], errors
        for (_rel, _line, why), cell in zip(errors, bad, strict=True):
            assert f"`confirms: {cell}`" in why, why
            assert "`round-<N>#<n>` or `none`" in why, why
        table = record(
            "abc1234",
            confirmations="| Confirms | What holds |\n|---|---|\n| round-1#2 | x |\n",
            n=2,
        )
        lines = reader.readable(table)
        found, errors = chain.confirmations(reader, lines, "r.md")
        first = lines.index("| Confirms | What holds |") + 1
        assert found == []
        assert [line for _rel, line, _why in errors] == [first, first + 1, first + 2]
        assert all("`confirms:`" in why for _rel, _line, why in errors), errors
        two = reader.readable(record("abc1234") + "\n## Confirmations\n")
        second = [i + 1 for i, ln in enumerate(two) if ln == "## Confirmations"][1]
        assert chain.confirmations(reader, two, "r.md")[1] == [
            ("r.md", second, chain.TWO_CONFIRMATIONS)
        ]


# --- channel ------------------------------------------------------------------


class TestChannel:
    def test_every_fixed_or_rejected_finding_is_confirmed_or_named_a_regression(
        self,
    ):
        """S23 (T36, read through the grammar table's reference rows): every
        finding of round N at `fixed <commit>` or
        `rejected` is named in round N+1, by a `confirms:` line or by a
        `regression:` line here, and by a `reopens:` line in T43's case; a
        `deferred` one owes nothing, and a `regression:` line naming the round
        alone covers no finding. One left unnamed is refused at its own
        heading, in round N's record."""
        one = record(
            "abc1234",
            [
                finding(1, "fixed abc1234"),
                finding(2, "rejected"),
                finding(3, "deferred #9"),
                finding(4, "fixed abc1234", title="the fourth"),
                finding(5, "rejected", title="the fifth"),
            ],
        )
        two = record(
            "abc1234",
            [
                finding(1, "deferred the frame", regression="round-1#2"),
                finding(2, "deferred the frame", regression="round-1"),
            ],
            confirmations=confirm("round-1#1") + confirm("none"),
            n=2,
        )
        rounds, errors = rounds_of(one, two)
        assert errors == []
        problems = chain.channel(rounds)
        lines = reader.readable(one)
        assert [(rel, line) for rel, line, _why in problems] == [
            ("round-1.md", lines.index("### 4. the fourth") + 1),
            ("round-1.md", lines.index("### 5. the fifth") + 1),
        ], problems
        said = [why for _rel, _line, why in problems]
        assert "`round-1#4`" in said[0] and "### 4. the fourth" in said[0]
        assert "`round-1#5`" in said[1] and "### 5. the fifth" in said[1]
        assert all("round-2.md" in why for why in said), said
        assert all("names it on no" in why for why in said), said
        covered = two.replace(
            confirm("none"), confirm("round-1#4") + confirm("round-1#5")
        )
        assert chain.channel(rounds_of(one, covered)[0]) == []
        deferred = record("abc1234", [finding(1, "deferred #9")])
        empty = record("abc1234", n=2)
        assert chain.channel(rounds_of(deferred, empty)[0]) == []

    def test_a_reopens_line_answers_the_earlier_finding_as_the_other_two_do(self):
        """S23 (T43): a `fixed` and a `rejected` finding of round 1 named only
        by round 2's `reopens:` lines owe nothing more. A `reopens:` reference
        to a record the item has not got, to a finding the record does not
        hold, or standing in round 1 is refused by its line; and the refusal
        of a finding no line names names all three labels."""
        one = record(
            "abc1234",
            [
                finding(1, "fixed abc1234"),
                finding(2, "rejected"),
                finding(3, "rejected"),
            ],
        )
        two = record(
            "abc1234",
            [
                finding(1, "open", reopens="round-1#1"),
                finding(2, "open", reopens="round-1#2"),
            ],
            n=2,
        )
        rounds, errors = rounds_of(one, two)
        assert errors == []
        problems = chain.channel(rounds)
        lines_one = reader.readable(one)
        assert [(rel, line) for rel, line, _why in problems] == [
            ("round-1.md", lines_one.index("### 3. the parser drops a row") + 1),
        ], problems
        why = problems[0][2]
        assert "`round-1#3`" in why and "round-2.md" in why, why
        for label in ("`confirms:`", "`reopens:`", "`regression:`"):
            assert label in why, why
        covered = two.replace(
            "\n## Confirmations",
            "\n" + finding(3, "open", reopens="round-1#3") + "\n## Confirmations",
        )
        rounds, errors = rounds_of(one, covered)
        assert errors == [] and len(rounds[1].findings) == 3
        assert chain.channel(rounds) == []
        first = record("abc1234", [finding(1, "deferred #9", reopens="round-1#1")])
        dangling = record(
            "abc1234",
            [
                finding(1, "deferred #9", reopens="round-3#1"),
                finding(2, "deferred #9", reopens="round-1#7"),
            ],
            n=2,
        )
        rounds, errors = rounds_of(first, dangling)
        assert errors == []
        problems = chain.channel(rounds)
        lines_first, lines_dangling = reader.readable(first), reader.readable(dangling)
        assert [(rel, line) for rel, line, _why in problems] == [
            ("round-1.md", lines_first.index("reopens: round-1#1") + 1),
            ("round-2.md", lines_dangling.index("reopens: round-3#1") + 1),
            ("round-2.md", lines_dangling.index("reopens: round-1#7") + 1),
        ], problems
        said = [why for _rel, _line, why in problems]
        assert "the first record" in said[0], said
        assert "`round-3#1`" in said[1] and "not an earlier record" in said[1]
        assert "`round-1#7`" in said[2] and "holds no finding 7" in said[2]

    @pytest.mark.rule("round-record-read-by-label")
    def test_a_reference_the_check_cannot_read_or_naming_no_finding_is_refused(self):
        """S23 (T36): a reference naming a record the item has not got, or
        no earlier one, or a finding number that record does not hold, is
        refused by its line, naming the round and the number; any reference
        in the first record is refused, and `none` there passes."""
        one = record(
            "abc1234",
            [finding(1, "deferred #9", regression="round-1#1")],
            confirmations=confirm("none") + confirm("round-1#1"),
        )
        two = record(
            "abc1234",
            [
                finding(1, "deferred #9", regression="round-3#1"),
                finding(2, "deferred #9", regression="round-2"),
            ],
            confirmations=confirm("round-1#7") + confirm("round-1#1"),
            n=2,
        )
        rounds, errors = rounds_of(one, two)
        assert errors == []
        problems = chain.channel(rounds)
        lines_one, lines_two = reader.readable(one), reader.readable(two)
        assert [(rel, line) for rel, line, _why in problems] == [
            ("round-1.md", lines_one.index("regression: round-1#1") + 1),
            ("round-1.md", lines_one.index("confirms: round-1#1") + 1),
            ("round-2.md", lines_two.index("regression: round-3#1") + 1),
            ("round-2.md", lines_two.index("regression: round-2") + 1),
            ("round-2.md", lines_two.index("confirms: round-1#7") + 1),
        ], problems
        said = [why for _rel, _line, why in problems]
        assert all("the first record" in why for why in said[:2]), said
        assert "`round-3#1`" in said[2] and "not an earlier record" in said[2]
        assert "`round-2`" in said[3] and "not an earlier record" in said[3]
        assert "`round-1#7`" in said[4] and "holds no finding 7" in said[4]
        assert (
            chain.channel(
                rounds_of(record("abc1234", confirmations=confirm("none")))[0]
            )
            == []
        )

    def test_the_last_records_fixed_or_rejected_finding_is_named(self):
        """S23 (T37): nothing after the last record has read its fixes or
        its answers, so each such finding is named with the words the
        `target:` rule prints; its `deferred` findings, and none, pass."""
        last = record(
            "abc1234",
            [
                finding(1, "fixed abc1234"),
                finding(2, "rejected"),
                finding(3, "deferred #9"),
                finding(4, "open"),
            ],
        )
        lines = reader.readable(last)
        problems = chain.channel(rounds_of(last)[0])
        assert [(rel, line) for rel, line, _why in problems] == [
            ("round-1.md", lines.index("verdict: fixed abc1234") + 1),
            ("round-1.md", lines.index("verdict: rejected") + 1),
        ], problems
        assert all(chain.VERIFYING_ROUND in why for _r, _l, why in problems)
        assert "### 1." in problems[0][2] and "### 2." in problems[1][2]
        quiet = record("abc1234", [finding(1, "deferred #9")])
        assert chain.channel(rounds_of(quiet)[0]) == []
        assert chain.channel(rounds_of(record("abc1234"))[0]) == []


# --- follows ------------------------------------------------------------------


@pytest.mark.rule("run-ends-with-verifying-round")
@pytest.mark.rule("last-record-at-head")
class TestFollows:
    def test_head_and_record_commits_after_it_pass(self, branch):
        root, code = branch
        assert chain.follows(str(root), code, "main", ITEM) is None

    def test_a_code_commit_after_it_and_an_unseen_commit_are_named(self, branch):
        root, code = branch
        write(root, "f.txt", "three\n")
        later = commit(root, "a fix nobody reviewed")
        found = chain.follows(str(root), code, "main", ITEM)
        assert found[0] == "after" and found[1] == later and found[2] == "f.txt"
        assert chain.follows(str(root), "0" * 40, "main", ITEM)[0] == "unseen"

    def test_another_items_records_and_a_commit_off_the_branch_are_named(self, branch):
        root, code = branch
        write(root, "seal/specs/1791999998-another-item/routing.md", "x\n")
        later = commit(root, "another work item's file")
        found = chain.follows(str(root), code, "main", ITEM)
        assert found[:2] == ("after", later)
        git(root, "switch", "-q", "main")
        write(root, "g.txt", "elsewhere\n")
        off = commit(root, "a commit the branch never had")
        git(root, "switch", "-q", "feature/x")
        assert chain.follows(str(root), off, "main", ITEM)[0] == "off"


# --- frame --------------------------------------------------------------------


class TestFrame:
    def declared(self):
        return {"planning": "framer", "review": "through the review chain"}

    def routing(self):
        return load(ROOT / "hooks" / "routing.py", "routing_for_chain_tests")

    def test_a_framed_item_with_a_reframe_by_the_framer_passes(self, branch):
        root, _code = branch
        write(
            root,
            f"{ITEM}/spec.md",
            SPEC + "Reframed 2026-10-16 by framer, after round 2.\n",
        )
        write(root, f"{ITEM}/plan.md", "# plan\n")
        commit(root, "frame")
        assert (
            chain.frame(reader, self.routing(), str(root), ITEM, self.declared()) == []
        )

    def test_a_missing_plan_and_a_reframe_by_another_party_are_named(self, branch):
        root, _code = branch
        write(
            root,
            f"{ITEM}/spec.md",
            SPEC + "Reframed 2026-10-16 by the session, after round 2.\n",
        )
        commit(root, "frame")
        problems = chain.frame(reader, self.routing(), str(root), ITEM, self.declared())
        assert any("plan.md" in p for p in problems)
        assert any("Reframed 2026-10-16 by the session" in p for p in problems)


# --- rule_changes_read --------------------------------------------------------

RULES = reader.rule_changes()
# The refusal's text before the parser's reason, pinned here so an edit to
# `chain.RULE_CHANGES_SAYS` meets a case.
SAYS = "`## Rule changes` does not parse, and `settle` applies nothing from this spec: "
CONTINUED = "- nothing\n  why: a reason\n  that continues two spaces in\n"
PROSE = "- add\n  file: docs/policy.md\n  to: A rule.\n\nA paragraph under the item.\n"
NOTHING = "- nothing\n  why: a reason\n"
CHANGE = (
    "- change\n  file: docs/policy.md\n  section: A section\n"
    "  from: old words.\n  to: new words.\n"
)


def template_comment():
    """What `templates/sdd-spec.md` holds under its `## Rule changes`: the
    comment a framer's skeleton commit carries."""
    text = (ROOT / "templates" / "sdd-spec.md").read_text(encoding="utf-8")
    section = text.split("\n## Rule changes\n", 1)[1].split("\n## Removes\n", 1)[0]
    assert section.strip().startswith("<!--") and section.strip().endswith("-->")
    return section


def spec_with(section):
    """A spec whose `## Rule changes` holds SECTION, or that has no such
    section where SECTION is None, ending with the framer's mark."""
    rules = "" if section is None else f"## Rule changes\n\n{section}\n"
    return f"# spec\n\nbody\n\n{rules}## Removes\n\nnone\n\n" + SPEC.split("\n\n")[-1]


def put_spec(root, text, committed=True):
    """Write the work item's `spec.md`; where COMMITTED, commit it and the
    closing records after it, so the spec is the one thing to refuse."""
    write(root, f"{ITEM}/spec.md", text)
    if committed:
        commit(root, "the spec")
        seal(root)


def refusal(root, text, item=ITEM):
    """The line the check prints for ITEM's spec reading TEXT outside CI,
    built from `rule_changes.parse`'s own error so no reason is spelt here."""
    ((line, reason),) = RULES.parse(text, reader.policy_root(str(root))).errors
    return f"{item}/spec.md:{line}  {chain.RULE_CHANGES_SAYS.format(reason=reason)}"


def spec_lines(out, item=ITEM):
    return [ln for ln in out.splitlines() if f"{item}/spec.md" in ln]


def reviewed_to_head(root):
    """A round 3 at HEAD, with nothing of its own, and the closing records
    after it: what the branch carries once its edit outside the work item's
    own directory was reviewed, so the spec read is the one refusal left."""
    head = git(root, "rev-parse", "HEAD")
    write(root, f"{ITEM}/rounds/round-3.md", record(head, n=3))
    commit(root, "the round at HEAD")
    seal(root)


def on_main(root, rel, text):
    """Commit TEXT at REL on `main` and merge `main` into `feature/x`."""
    git(root, "switch", "-q", "main")
    write(root, rel, text)
    commit(root, f"{rel} on the base")
    git(root, "switch", "-q", "feature/x")
    git(root, "merge", "-q", "--no-edit", "main")


@pytest.mark.rule("rule-changes-read-at-the-pull-request")
class TestRuleChangesRead:
    @pytest.mark.parametrize(
        "section",
        [lambda: CONTINUED, lambda: PROSE, template_comment],
        ids=["S1-continued-two-in", "S2-prose-under-items", "S3-the-template-comment"],
    )
    def test_a_section_the_parser_refuses_fails_a_ready_pull_request_at_its_line(
        self, branch, ready, capsys, section
    ):
        """S1, S2, S3: the one refusal names the spec, the line the parser
        names and the parser's reason. S3's section is the template's
        comment and nothing else, which a framer's skeleton commit holds."""
        root, _code = branch
        text = spec_with(section())
        put_spec(root, text)
        code, out = check(root, capsys)
        assert code == 1, out
        assert spec_lines(out) == [refusal(root, text)], out
        assert SAYS in spec_lines(out)[0]

    @pytest.mark.parametrize(
        "section", [NOTHING, CHANGE, None], ids=["no-change", "a-change", "none"]
    )
    def test_a_section_that_parses_or_no_section_passes(
        self, branch, ready, capsys, section
    ):
        """S4: the no-change block, a `change` item that parses, and a spec
        with no `## Rule changes`, which `settle` names and keeps."""
        root, _code = branch
        put_spec(root, spec_with(section))
        code, out = check(root, capsys)
        assert code == 0, out
        assert spec_lines(out) == [], out

    def test_a_draft_prints_the_refusal_as_a_notice(
        self, branch, draft, capsys, monkeypatch
    ):
        """S5: in CI a draft annotates the same line as a notice and passes."""
        root, _code = branch
        text = spec_with(CONTINUED)
        put_spec(root, text)
        monkeypatch.setenv("GITHUB_ACTIONS", "true")
        code, out = check(root, capsys)
        assert code == 0, out
        notices = [ln for ln in out.splitlines() if ln.startswith("::notice ")]
        assert any(f"file={ITEM}/spec.md," in ln for ln in notices), out
        where, said = refusal(root, text).split("  ", 1)
        path, line = where.rsplit(":", 1)
        assert f"::notice file={path},line={line}::{said}" in out.splitlines(), out

    def test_the_broad_run_keeps_it_a_refusal_and_fails_only_on_a_ready_one(
        self, branch, ready, capsys, monkeypatch
    ):
        """S6: `--sealing` turns the closing records' lines into notices and
        leaves this refusal one, so a ready pull request fails. Where no pull
        request is observed, as when the broad run goes before the pull
        request opens, the check prints it and exits 0."""
        root, _code = branch
        text = spec_with(CONTINUED)
        put_spec(root, text)
        code, out = check(root, capsys, chain.SEALING)
        assert code == 1, out
        assert spec_lines(out) == [refusal(root, text)], out
        monkeypatch.delenv("GITHUB_EVENT_PATH")
        code, out = check(root, capsys, chain.SEALING)
        assert code == 0, out
        assert chain.UNSEEN_SAYS in out
        assert spec_lines(out) == [refusal(root, text)], out

    def test_a_framer_drawn_frame_is_read_as_the_sessions_is(
        self, branch, ready, capsys
    ):
        """S7: the fixture declares `Planning | the session`, which S1 reads;
        under `Planning | framer`, with the frame arm satisfied, the spec is
        refused the same way."""
        root, _code = branch
        write(
            root,
            f"{ITEM}/routing.md",
            ROUTING.format(review="through the review chain", planning="framer"),
        )
        write(root, f"{ITEM}/plan.md", "# plan\n")
        text = spec_with(CONTINUED)
        put_spec(root, text)
        code, out = check(root, capsys)
        assert code == 1, out
        assert spec_lines(out) == [refusal(root, text)], out

    @pytest.mark.rule("judged-where-carried")
    def test_a_spec_another_pull_requests_squash_carried_is_not_read(
        self, branch, ready, capsys, monkeypatch
    ):
        """S8: the release pull request leaves the work item to the pull
        request that carried it, its spec with it; the head branch's own
        pull request reads the same spec."""
        root, _code = branch
        put_spec(root, spec_with(CONTINUED))
        released(root)
        monkeypatch.setenv("GITHUB_HEAD_REF", RELEASE)
        code, out = check(root, capsys)
        assert code == 0, out
        assert spec_lines(out) == [], out
        monkeypatch.setenv("GITHUB_HEAD_REF", "feature/x")
        _code, out = check(root, capsys)
        assert len(spec_lines(out)) == 1, out

    @pytest.mark.rule("judged-where-carried")
    def test_a_carried_spec_stays_unread_where_the_release_declares_its_own(
        self, branch, ready, capsys, monkeypatch
    ):
        """S8, for the specs the diff carries: a release pull request that
        declares a work item of its own reaches the edited specs, and still
        leaves another work item's spec a squash carried to that squash's
        pull request."""
        root, _code = branch
        write(root, f"{MERGED_ITEM}/spec.md", spec_with(CONTINUED))
        commit(root, "another work item's spec")
        reviewed_to_head(root)
        released(root)
        own = "seal/specs/1792000000-the-release"
        write(
            root,
            f"{own}/routing.md",
            ROUTING.format(review="straight to the PR", planning="the session").replace(
                "feature/x", RELEASE
            ),
        )
        commit(root, "the release's own work item")
        monkeypatch.setenv("GITHUB_HEAD_REF", RELEASE)
        code, out = check(root, capsys)
        assert code == 1 and f"{own}/broad-gate.md" in out, out
        assert spec_lines(out, MERGED_ITEM) == [], out

    def test_the_working_tree_is_read_under_worktree_and_head_otherwise(
        self, branch, ready, capsys
    ):
        """S9: a spec written and not committed is refused under `--worktree`;
        CI reads HEAD, which does not carry it."""
        root, _code = branch
        text = spec_with(CONTINUED)
        put_spec(root, text, committed=False)
        code, out = check(root, capsys, "--worktree")
        assert code == 1, out
        assert spec_lines(out) == [refusal(root, text)], out
        code, out = check(root, capsys)
        assert code == 0, out
        assert spec_lines(out) == [], out

    def test_a_reader_that_will_not_load_is_exit_2_naming_it(
        self, branch, ready, capsys, monkeypatch
    ):
        """S10: the check cannot run, which is not a pass, and stderr names
        the reader and what it raised. A work item with no `spec.md` has
        nothing to read and never reaches the reader."""
        root, _code = branch

        def will_not_load():
            raise ImportError("a planted failure")

        monkeypatch.setattr(chain.SHARED_READER, "rule_changes", will_not_load)
        code, out = check(root, capsys)
        assert code == 0, out
        put_spec(root, spec_with(NOTHING))
        code = chain.main(["--baseline", "main", "--root", str(root)])
        err = capsys.readouterr().err
        assert code == 2, err
        assert (
            "chain-check: the rule-changes reader would not load (a planted failure)"
            in err
        )

    def test_another_work_items_spec_the_branch_adds_is_read(
        self, branch, ready, capsys
    ):
        """S12: a declared work item's commit adds a spec to another work
        item, whose `routing.md` is not in the diff, as #941's squash did to
        114 of them."""
        root, _code = branch
        text = spec_with(CONTINUED)
        write(root, f"{MERGED_ITEM}/spec.md", text)
        commit(root, "another work item's spec")
        reviewed_to_head(root)
        code, out = check(root, capsys)
        assert code == 1, out
        assert spec_lines(out, MERGED_ITEM) == [refusal(root, text, MERGED_ITEM)], out

    def test_another_work_items_spec_the_branch_changes_is_read(
        self, branch, ready, capsys
    ):
        """S13: a spec that parses on the base, edited on the branch into a
        section the reader refuses."""
        root, _code = branch
        rel = f"{MERGED_ITEM}/spec.md"
        on_main(root, rel, spec_with(NOTHING))
        text = spec_with(CONTINUED)
        write(root, rel, text)
        commit(root, "another work item's section, edited")
        reviewed_to_head(root)
        code, out = check(root, capsys)
        assert code == 1, out
        assert spec_lines(out, MERGED_ITEM) == [refusal(root, text, MERGED_ITEM)], out

    @pytest.mark.rule("two-review-answers")
    def test_another_work_items_spec_is_read_straight_to_the_pr(
        self, branch, ready, capsys
    ):
        """S14: under `straight to the PR` no round is owed, and the spec is
        still read."""
        root, _code = branch
        write(
            root,
            f"{ITEM}/routing.md",
            ROUTING.format(review="straight to the PR", planning="the session"),
        )
        git(root, "rm", "-rq", f"{ITEM}/rounds")
        text = spec_with(CONTINUED)
        write(root, f"{MERGED_ITEM}/spec.md", text)
        commit(root, "direct, and another work item's spec")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1, out
        assert spec_lines(out, MERGED_ITEM) == [refusal(root, text, MERGED_ITEM)], out

    def test_a_pull_request_that_declares_nothing_reads_no_spec(
        self, branch, ready, capsys
    ):
        """S15: the promise in `hygiene.yml` and `CONTRIBUTING.md` holds."""
        root, _code = branch
        git(root, "rm", "-rq", ITEM)
        write(root, f"{MERGED_ITEM}/spec.md", spec_with(CONTINUED))
        commit(root, "no work item, and a spec")
        code, out = check(root, capsys)
        assert code == 0, out
        assert "declared neither way" in out
        assert spec_lines(out, MERGED_ITEM) == [], out

    def test_a_spec_only_moved_is_not_read(self, branch, ready, capsys):
        """S16: a move with the bytes unchanged writes no section, so it is
        read at the pull request that wrote it, as a moved declaration is."""
        root, _code = branch
        old, new = "seal/specs/1788000001-old", "seal/specs/1788000001-moved"
        on_main(root, f"{old}/spec.md", spec_with(CONTINUED))
        git(root, "mv", old, new)
        commit(root, "moved")
        reviewed_to_head(root)
        code, out = check(root, capsys)
        assert code == 0, out
        assert spec_lines(out, old) == [] and spec_lines(out, new) == [], out

    def test_only_a_work_items_own_spec_file_is_read_from_the_diff(
        self, branch, ready, capsys
    ):
        """S12's set holds `<id>/spec.md` exactly. Another file the branch
        changes beside a spec it leaves alone, and a `spec.md` one directory
        down, write no section `settle` reads."""
        root, _code = branch
        on_main(root, f"{MERGED_ITEM}/spec.md", spec_with(CONTINUED))
        write(root, f"{MERGED_ITEM}/plan.md", "# plan\n")
        write(root, f"{MERGED_ITEM}/notes/spec.md", spec_with(CONTINUED))
        commit(root, "beside another work item's spec, and below it")
        reviewed_to_head(root)
        code, out = check(root, capsys)
        assert code == 0, out
        assert spec_lines(out, MERGED_ITEM) == [], out
        assert spec_lines(out, f"{MERGED_ITEM}/notes") == [], out

    def test_a_reader_that_will_not_load_for_an_edited_spec_is_exit_2(
        self, branch, ready, capsys, monkeypatch
    ):
        """S10, for the specs the diff carries: the judged work item has no
        spec, so the edited spec is the first to reach the reader."""
        root, _code = branch
        write(root, f"{MERGED_ITEM}/spec.md", spec_with(NOTHING))
        commit(root, "another work item's spec")
        reviewed_to_head(root)

        def will_not_load():
            raise ImportError("a planted failure")

        monkeypatch.setattr(chain.SHARED_READER, "rule_changes", will_not_load)
        code = chain.main(["--baseline", "main", "--root", str(root)])
        err = capsys.readouterr().err
        assert code == 2, err
        assert "the rule-changes reader would not load (a planted failure)" in err


# --- originals_of: the parity arm at the pull request (#988) -------------------

BASELINE = "0123456789abcdef0123456789abcdef01234567"
PARITY = "seal/parity.md"
routing_module = load(chain.ROUTING, "specseal_routing_for_chain_tests")


def parity_file(sha):
    """`templates/parity.md` with its `Baseline commit` placeholder replaced
    by SHA, or left standing where SHA is None."""
    text = (ROOT / "templates" / "parity.md").read_text(encoding="utf-8")
    assert text.count("`<SHA>`") == 1
    return text if sha is None else text.replace("`<SHA>`", f"`{sha}`")


def with_original(text, said):
    """A round record with `original: SAID` under its `target:` line."""
    assert text.count(" against main\n") == 1
    return text.replace(" against main\n", f" against main\noriginal: {said}\n")


def migrating(root, originals, sha=BASELINE):
    """`main` declares a migration whose baseline is SHA, merged into
    `feature/x`; each round record N gains `original: <ORIGINALS[N-1]>`,
    none where that is None, and the closing records name HEAD."""
    on_main(root, PARITY, parity_file(sha))
    for n, said in enumerate(originals, 1):
        if said is not None:
            rel = f"{ITEM}/rounds/round-{n}.md"
            write(root, rel, with_original((root / rel).read_text("utf-8"), said))
    if any(said is not None for said in originals):
        commit(root, "the rounds compared with the original")
    seal(root)


def original_lines(out):
    """The lines the check prints about a round record or the config."""
    where = (f"{ITEM}/rounds/", f"{PARITY}:")
    return [ln for ln in out.splitlines() if ln.startswith(where)]


@pytest.mark.rule("parity-at-the-pull-request")
class TestOriginals:
    def test_a_record_with_no_original_line_fails_a_ready_pull_request(
        self, branch, ready, capsys, monkeypatch
    ):
        """S4: in a repository declaring `seal/parity.md`, a chain-declared
        pull request changing code fails while a round record holds no
        `original:` line, each record named with the baseline it owes, and
        a draft prints the same lines and exits 0."""
        root, _code = branch
        migrating(root, (None, None))
        code, out = check(root, capsys)
        assert code == 1, out
        says = chain.NO_ORIGINAL.format(config=PARITY, sha=BASELINE)
        # What the person reads: the line owed, and who writes it after what.
        for words in (
            f"no `original:` line: `{PARITY}` declares a migration",
            f"each round record carries `original: {BASELINE}`",
            "written by the warden once it compared the round's target with "
            "the original through `legacy-parity`",
        ):
            assert words in says, says
        assert original_lines(out) == [
            f"{ITEM}/rounds/round-{n}.md:0  {says}" for n in (1, 2)
        ], out
        event = pathlib.Path(os.environ["GITHUB_EVENT_PATH"])
        event.write_text(json.dumps({"pull_request": {"draft": True}}), "utf-8")
        code, out = check(root, capsys)
        assert code == 0, out
        assert len(original_lines(out)) == 2, out

    @pytest.mark.parametrize(
        "originals, sha",
        [
            ((BASELINE[:8], BASELINE), BASELINE),
            ((BASELINE, BASELINE[:12]), BASELINE[:7]),
        ],
        ids=["short-in-the-record", "short-in-the-config"],
    )
    def test_a_record_naming_the_baseline_by_either_prefix_passes(
        self, branch, ready, capsys, originals, sha
    ):
        """S5: an `original:` commit that is a prefix of the `Baseline
        commit` row's SHA, or that SHA a prefix of it, is the baseline."""
        root, _code = branch
        migrating(root, originals, sha)
        code, out = check(root, capsys)
        assert code == 0, out
        assert original_lines(out) == [], out

    def test_a_record_naming_another_commit_fails_naming_both(
        self, branch, ready, capsys
    ):
        """S6: an `original:` line naming another commit is refused at its
        line, naming the record and both commits."""
        root, _code = branch
        other = "fedcba9876543210"
        migrating(root, (BASELINE, other))
        code, out = check(root, capsys)
        assert code == 1, out
        rel = f"{ITEM}/rounds/round-2.md"
        line = reader.readable((root / rel).read_text("utf-8")).index(
            f"original: {other}"
        )
        says = chain.OTHER_ORIGINAL.format(said=other, sha=BASELINE)
        assert original_lines(out) == [f"{rel}:{line + 1}  {says}"], out
        assert other in says and BASELINE in says

    def test_a_config_whose_baseline_holds_no_commit_fails_naming_it(
        self, branch, ready, capsys
    ):
        """S10: a migration config whose `Baseline commit` row still holds
        the template's placeholder fails a ready pull request naming
        `seal/parity.md`, and no record is compared with nothing."""
        root, _code = branch
        migrating(root, (BASELINE, BASELINE), sha=None)
        code, out = check(root, capsys)
        assert code == 1, out
        (line,) = original_lines(out)
        assert line.startswith(f"{PARITY}:0  "), line
        assert "`Baseline commit`" in line and "`<SHA>`" in line, line

    def test_a_change_confined_to_the_document_roots_owes_no_line(self, branch):
        """S7 and S11: the paths decide through `gate.touches_code`, read
        from `hooks/gate.py`: a change confined to `docs/` and `seal/` owes
        no line, one path outside them owes it, and paths git could not list
        owe it too, as the parity arm reads them at the commit."""
        root, _code = branch
        migrating(root, (None, None))
        inside = ["docs/a.md", f"{ITEM}/rounds/round-1.md"]

        def owed(paths):
            return chain.originals_of(reader, routing_module, str(root), paths, [ITEM])

        assert owed(inside) == []
        assert [p for p, _n, _w in owed([*inside, "f.txt"])] == [
            f"{ITEM}/rounds/round-1.md",
            f"{ITEM}/rounds/round-2.md",
        ]
        assert owed(None) == owed([*inside, "f.txt"])

    @pytest.mark.parametrize(
        "where, said",
        [
            ("inside", "a `original:` line inside a finding"),
            ("twice", "2 `original:` lines; a round record carries one at most"),
            ("spelt", "a label in another spelling"),
        ],
    )
    def test_a_line_the_table_refuses_is_refused_at_its_line_and_only_so(
        self, where, said
    ):
        """S9: an `original:` line inside a finding, a second one, and one
        spelt `Original:` are refused at the line by the grammar table's
        row, and `original_of` adds no second refusal saying the record has
        none."""
        text = record("abc1234", [finding(1, "rejected")])
        if where == "inside":
            text = text.replace("answer: \n", f"answer: \noriginal: {BASELINE}\n")
        elif where == "twice":
            text = with_original(with_original(text, BASELINE), BASELINE)
        else:
            text = with_original(text, BASELINE).replace("original:", "Original:")
        lines = reader.readable(text)
        at = next(
            i + 1 for i, ln in enumerate(lines) if ln.lower().startswith("original:")
        )
        _round, errors = chain.round_of(reader, text, "r.md", 1)
        assert [(line, said in why) for _r, line, why in errors] == [
            (at + (where == "twice"), True)
        ], errors
        assert chain.original_of(reader, text, "r.md", BASELINE, PARITY) == []

    def test_the_baseline_is_the_first_code_span_of_its_one_row(self):
        """The `Baseline commit` reader in `hooks/config.py`: the SHA in the
        first code span of the one row, else no SHA and why, naming a
        placeholder, a second row, no row and no table."""
        config = chain.parity_readers()[0]
        row = "| Baseline commit | `<SHA>`, the commit the original's coordinates refer to |"
        text = parity_file(BASELINE)
        assert config.baseline_commit(text) == (BASELINE, None)
        assert config.baseline_commit(parity_file(BASELINE[:7])) == (BASELINE[:7], None)
        for bad, why in (
            (parity_file(None), "`<SHA>`"),
            (parity_file(BASELINE.upper()), BASELINE.upper()),
            (
                text.replace(row.replace("<SHA>", BASELINE) + "\n", ""),
                "no `Baseline commit` row",
            ),
            (
                text.replace(
                    "| Policy root |",
                    row.replace("<SHA>", BASELINE) + "\n| Policy root |",
                ),
                "2 `Baseline commit` rows",
            ),
            ("# Migration config\n", "holds no `| Field | Value |` table"),
        ):
            sha, said = config.baseline_commit(bad)
            assert sha is None and why in said, (said, bad)
        # No table is said as no table, not as a table with no such row.
        _sha, said = config.baseline_commit("# Migration config\n")
        assert "Baseline commit" not in said, said

    def test_the_readers_load_where_only_the_check_was_loaded(self):
        """`parity_readers` loads `hooks/config.py` before `hooks/gate.py`,
        whose `import optin` needs `hooks/` on `sys.path`: a fresh
        interpreter that loaded the check alone, and no routing reader,
        still loads both."""
        code = (
            "import importlib.util, sys\n"
            f"s = importlib.util.spec_from_file_location('c', {str(CHAIN)!r})\n"
            "m = importlib.util.module_from_spec(s)\n"
            "s.loader.exec_module(m)\n"
            "config, gate = m.parity_readers()\n"
            "print(gate.touches_code(['f.txt']), config.BASELINE_ROW)\n"
        )
        done = subprocess.run(
            [sys.executable, "-I", "-c", code],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )
        assert done.returncode == 0, done.stderr
        assert done.stdout.strip() == "True Baseline commit", done.stdout

    def test_readers_that_will_not_load_are_exit_2_naming_them(
        self, branch, ready, capsys, monkeypatch
    ):
        """A `hooks/` reader the arm needs that will not load ends the run at
        exit 2 with the reason, never a pass."""
        root, _code = branch
        migrating(root, (None, None))

        def will_not_load():
            raise ImportError("a planted failure")

        monkeypatch.setattr(chain, "parity_readers", will_not_load)
        code = chain.main(["--baseline", "main", "--root", str(root)])
        err = capsys.readouterr().err
        assert code == 2, err
        assert "the parity readers would not load (a planted failure)" in err


# --- main: the arms over a pull request ---------------------------------------


@pytest.mark.rule("routing-read-first")
class TestMain:
    @pytest.mark.rule("old-table-shape-refused")
    def test_a_reviewed_branch_passes_a_ready_pull_request(self, branch, ready, capsys):
        """S11: the merged item's old-shape record, a finding open in it, is
        never opened — the check judges only what this pull request carries."""
        root, _code = branch
        code, out = check(root, capsys)
        assert code == 0, out
        assert MERGED_ITEM not in out

    @pytest.mark.rule("round-record-read-by-label")
    def test_an_open_finding_fails_a_ready_pull_request(self, branch, ready, capsys):
        """S3 (T27): the `verdict:` lines decide, the line and the finding's
        heading are named, and a draft prints the same line and passes. A
        finding's `severity:` decides nothing."""
        root, code_sha = branch
        rel = f"{ITEM}/rounds/round-1.md"
        write(root, rel, record(code_sha, [finding(1, "open")]))
        commit(root, "the record, still open")
        code, out = check(root, capsys)
        assert code == 1
        line = next(ln for ln in out.splitlines() if "### 1." in ln)
        number = reader.readable(record(code_sha, [finding(1, "open")])).index(
            "verdict: open"
        )
        assert line.startswith(f"{rel}:{number + 1}"), line
        assert "### 1. the parser drops a row" in line
        assert (
            "reads `verdict: open`: the fix pass answers it with another verdict, "
            "and a verdict is `open`, `fixed <commit>`, `rejected` or `deferred <home>`"
        ) in line
        event = pathlib.Path(os.environ["GITHUB_EVENT_PATH"])
        event.write_text(
            json.dumps({"pull_request": {"draft": True}}), encoding="utf-8"
        )
        code, out = check(root, capsys)
        assert code == 0
        assert any("### 1." in ln and "verdict: open" in ln for ln in out.splitlines())
        event.write_text(
            json.dumps({"pull_request": {"draft": False}}), encoding="utf-8"
        )
        write(root, rel, record(code_sha, [finding(1, "rejected")]))
        commit(root, "the record, rejected at the most severe severity")
        seal(root)
        code, out = check(root, capsys)
        assert code == 0, out

    @pytest.mark.rule("round-record-read-by-label")
    def test_a_fixed_commit_head_does_not_descend_from_is_refused(
        self, branch, ready, capsys
    ):
        """S3 (T28): `fixed <commit>` names a commit on this branch. One this
        repository cannot resolve, and one on another branch, are refused by
        the finding's line and heading; the fixture's own code commit is not."""
        root, code_sha = branch
        git(root, "switch", "-q", "main")
        write(root, "g.txt", "elsewhere\n")
        off = commit(root, "a commit the branch never had")
        git(root, "switch", "-q", "feature/x")
        rel = f"{ITEM}/rounds/round-1.md"
        sections = [
            finding(1, "fixed 0000000"),
            finding(2, f"fixed {off[:8]}"),
            finding(3, f"fixed {code_sha[:8]}"),
        ]
        write(root, rel, record(code_sha, sections))
        commit(root, "the record, three fixes")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1
        named = [
            ln
            for ln in out.splitlines()
            if ln.startswith(f"{rel}:") and "does not descend" in ln
        ]
        assert len(named) == 2, out
        assert "### 1." in named[0] and "`0000000`" in named[0]
        assert "### 2." in named[1] and f"`{off[:8]}`" in named[1]
        assert all("HEAD does not descend from" in ln for ln in named), named

    @pytest.mark.rule("round-record-read-by-label")
    @pytest.mark.rule("fix-pass-two-lines")
    @pytest.mark.rule("location-touched-by-fix")
    def test_a_fixed_commit_that_touches_nothing_of_the_finding_is_refused(
        self, branch, ready, capsys
    ):
        """S22 (T34): a `fixed <commit>` on the branch must change a path the
        finding's `location:` names, or one under it. A commit touching
        another path is refused naming the finding, the commit and what it
        touched; one touching one of two named paths, a file under a named
        directory, or a path the fix pass appended to the line passes, and so
        does the root commit, whose paths are read too. A path sharing a
        named directory's prefix is not under it."""
        root, code_sha = branch
        base = git(root, "rev-list", "--max-parents=0", "HEAD")
        made = {}
        for name, path in (
            ("g", "g.txt"),
            ("dir", "docs/x/y.md"),
            ("h", "h.txt"),
            ("near", "docs/xy.md"),
        ):
            write(root, path, f"{name}\n")
            made[name] = commit(root, f"touch {path}")[:8]
        rel = f"{ITEM}/rounds/round-1.md"
        sections = [
            finding(1, f"fixed {made['g']}"),
            finding(2, f"fixed {made['g']}", location="`f.txt:1`, `g.txt:3`"),
            finding(3, f"fixed {made['dir']}", location="`docs/x/`"),
            finding(4, f"fixed {made['dir']}", location="`docs/x`"),
            finding(5, f"fixed {made['h']}", location="`f.txt:1`, `h.txt`"),
            finding(6, f"fixed {base[:8]}", location="`f.txt`"),
            finding(7, f"fixed {made['near']}", location="`docs/x`"),
        ]
        write(root, rel, record(code_sha, sections))
        commit(root, "the record, seven fixes")
        write(
            root,
            f"{ITEM}/rounds/round-2.md",
            record(
                made["near"],
                confirmations="".join(confirm(f"round-1#{n}") for n in range(1, 8)),
                n=2,
            ),
        )
        commit(root, "the verifying round")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1
        named = [ln for ln in out.splitlines() if ln.startswith(f"{rel}:")]
        assert len(named) == 2, out
        assert "### 1." in named[0] and f"`{made['g']}`" in named[0], named
        assert "`g.txt`" in named[0] and "`f.txt`" in named[0], named
        assert "### 7." in named[1] and "`docs/xy.md`" in named[1], named
        assert all("touches no path" in ln for ln in named), named

    @pytest.mark.rule("run-ends-with-verifying-round")
    @pytest.mark.rule("last-record-at-head")
    def test_the_last_records_fixed_or_rejected_finding_owes_a_verifying_round(
        self, branch, ready, capsys
    ):
        """S23 (T37): on a ready pull request a `fixed` or `rejected` finding
        in the last record fails as *a verifying round is owed*, since no
        round after it read the fix or the answer; a draft prints it and
        passes, and a last record of `deferred` findings, or of none, passes."""
        root, code_sha = branch
        git(root, "rm", "-q", f"{ITEM}/rounds/round-2.md")
        commit(root, "no verifying round")
        seal(root)
        rel = f"{ITEM}/rounds/round-1.md"
        code, out = check(root, capsys)
        assert code == 1
        line = next(ln for ln in out.splitlines() if ln.startswith(f"{rel}:"))
        assert "### 1." in line and chain.VERIFYING_ROUND in line, line
        event = pathlib.Path(os.environ["GITHUB_EVENT_PATH"])
        event.write_text(
            json.dumps({"pull_request": {"draft": True}}), encoding="utf-8"
        )
        code, out = check(root, capsys)
        assert code == 0 and chain.VERIFYING_ROUND in out
        event.write_text(
            json.dumps({"pull_request": {"draft": False}}), encoding="utf-8"
        )
        for found, closes in (
            ([finding(1, "rejected")], False),
            ([finding(1, "deferred #9")], True),
            ([], True),
        ):
            write(root, rel, record(code_sha, found))
            commit(root, "the last record, again")
            seal(root)
            code, out = check(root, capsys)
            assert (code == 0) is closes, out
            assert (chain.VERIFYING_ROUND in out) is not closes, out

    @pytest.mark.rule("last-record-at-head")
    def test_the_last_record_is_at_head_or_only_record_commits_follow(
        self, branch, ready, capsys
    ):
        """S4 (T12): a record commit after the last record passes; a code
        commit after it fails naming the commit and the verifying round."""
        root, _code = branch
        write(root, f"{ITEM}/overview.md", "# overview\n")
        commit(root, "a record commit")
        seal(root)
        code, out = check(root, capsys)
        assert code == 0, out
        write(root, "f.txt", "three\n")
        later = commit(root, "a fix after the last round")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1
        assert later[:8] in out and "a verifying round is owed" in out

    def test_a_chain_with_no_record_fails_ready_and_prints_on_a_draft(
        self, tmp_path, monkeypatch, capsys, branch
    ):
        root, _code = branch
        git(root, "rm", "-rq", f"{ITEM}/rounds")
        commit(root, "no record")
        event = tmp_path / "e.json"
        event.write_text(
            json.dumps({"pull_request": {"draft": False}}), encoding="utf-8"
        )
        monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
        code, out = check(root, capsys)
        assert code == 1 and "holds no `round-N.md`" in out
        event.write_text(
            json.dumps({"pull_request": {"draft": True}}), encoding="utf-8"
        )
        code, out = check(root, capsys)
        assert code == 0 and "holds no `round-N.md`" in out

    @pytest.mark.rule("old-table-shape-refused")
    def test_an_old_shape_record_under_the_declared_item_is_refused(
        self, branch, ready, capsys
    ):
        """S11: nothing reads the old table. A record of that shape under the
        item this pull request declares has no `## Findings`, and is refused
        by name rather than read as a record with nothing open."""
        root, code_sha = branch
        rel = f"{ITEM}/rounds/round-1.md"
        write(root, rel, OLD_RECORD.replace("0000000", code_sha))
        commit(root, "an old-shape record")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1
        assert f"{rel}:0" in out and chain.NO_FINDINGS in out

    def test_an_unclosed_fence_hiding_an_open_finding_fails_a_ready_pull_request(
        self, branch, ready, capsys
    ):
        """A fence the warden never closed hides the open finding below it;
        the check names the fence's opener rather than passing the record."""
        root, code_sha = branch
        rel = f"{ITEM}/rounds/round-1.md"
        text = record(
            code_sha,
            [
                finding(1, "rejected").replace("answer: \n", "~~~python\n"),
                finding(2, "open"),
            ],
        )
        write(root, rel, text)
        commit(root, "a record with a fence left open")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1, out
        opener = text.splitlines().index("~~~python")
        assert f"{rel}:{opener + 1}" in out, out

    def test_a_broad_gate_file_naming_another_commit_fails_a_ready_pull_request(
        self, branch, ready, capsys
    ):
        """S5 (T15): the newest run must be HEAD or have only records after
        it; a stale run fails naming the file, and `--sealing` prints it."""
        root, _code = branch
        rel = f"{ITEM}/broad-gate.md"
        write(root, rel, gate_file("1" * 40))
        commit(root, "a run this repository cannot see")
        code, out = check(root, capsys)
        assert code == 1
        assert any(ln.startswith(f"{rel}:") for ln in out.splitlines())
        code, out = check(root, capsys, "--sealing")
        assert code == 0 and rel in out

    @pytest.mark.rule("two-review-answers")
    def test_a_straight_to_the_pr_item_owes_the_sealers_two_files(
        self, branch, ready, capsys
    ):
        root, _code = branch
        write(
            root,
            f"{ITEM}/routing.md",
            ROUTING.format(review="straight to the PR", planning="the session"),
        )
        git(
            root,
            "rm",
            "-rq",
            f"{ITEM}/rounds",
            f"{ITEM}/broad-gate.md",
            f"{ITEM}/guarantee.md",
        )
        commit(root, "direct, and no run")
        code, out = check(root, capsys)
        assert code == 1 and "broad-gate.md" in out and "guarantee.md" in out
        seal(root)
        code, out = check(root, capsys)
        assert code == 0, out

    def test_an_unreadable_declaration_fails_and_none_passes(
        self, branch, ready, capsys
    ):
        root, _code = branch
        write(root, f"{ITEM}/routing.md", "# nothing to read\n")
        commit(root, "garbled")
        code, out = check(root, capsys)
        assert code == 1 and "not a readable declaration" in out
        git(root, "rm", "-rq", ITEM)
        commit(root, "no work item")
        code, out = check(root, capsys)
        assert code == 0 and "declared neither way" in out

    @pytest.mark.rule("judged-where-carried")
    def test_a_release_pull_request_leaves_a_squashed_item_to_its_own_pull_request(
        self, branch, ready, capsys, monkeypatch
    ):
        """Q7: a pull request into `main` from the release branch carries every
        item squashed into it, whose records name commits the squash orphaned.
        Each was judged at the pull request that carried it, so the release
        pull request passes and names each item it left with its squash."""
        root, _code = branch
        released(root)
        monkeypatch.setenv("GITHUB_HEAD_REF", RELEASE)
        code, out = check(root, capsys)
        assert code == 0, out
        line = next(ln for ln in out.splitlines() if f"{ITEM}/routing.md" in ln)
        assert "judged at its own pull request" in line and "(#7)" in line
        assert "does not descend from" not in out
        # A declaration naming the head branch is judged however it arrived.
        monkeypatch.setenv("GITHUB_HEAD_REF", "feature/x")
        code, out = check(root, capsys)
        assert code == 1 and "does not descend from" in out
        assert "judged at its own pull request" not in out

    @pytest.mark.rule("judged-where-carried")
    def test_an_item_the_release_pull_requests_own_commit_changes_is_judged(
        self, branch, ready, capsys, monkeypatch
    ):
        """Q7: a commit made on the release branch itself is the release pull
        request's own, so the declaration it changed is judged there."""
        root, _code = branch
        released(root)
        monkeypatch.setenv("GITHUB_HEAD_REF", RELEASE)
        rel = f"{ITEM}/routing.md"
        write(root, rel, (root / rel).read_text(encoding="utf-8") + "\nA note.\n")
        commit(root, "a change on the release branch itself (#8)")
        code, out = check(root, capsys)
        assert code == 1
        assert "does not descend from" in out
        assert "judged at its own pull request" not in out

    def test_a_baseline_that_does_not_resolve_is_exit_2(self, branch, capsys):
        root, _code = branch
        code = chain.main(["--baseline", "no-such-ref", "--root", str(root)])
        assert code == 2
        assert "does not resolve" in capsys.readouterr().err


# --- retired ------------------------------------------------------------------

OLD_ITEM = "seal/specs/1788000000-an-earlier-item"


def remove_an_earlier_item(root, applied, whole=True):
    """Declare an earlier work item on `main`, bring it into the branch, and
    remove its directory there, or only its declaration, with or without its
    rule change applied."""
    git(root, "switch", "-q", "main")
    # Close enough to the branch's own declaration for git's rename detection
    # to pair the two, which `changed` reads without.
    write(
        root,
        f"{OLD_ITEM}/routing.md",
        ROUTING.format(review="straight to the PR", planning="the session"),
    )
    write(
        root,
        f"{OLD_ITEM}/spec.md",
        "# a spec\n\n## Rule changes\n\n- add\n  file: docs/policy.md\n  to: A rule.\n",
    )
    commit(root, "an earlier item, declared")
    git(root, "switch", "-q", "feature/x")
    git(root, "merge", "-q", "--no-edit", "main")
    git(root, "rm", "-rq", OLD_ITEM if whole else f"{OLD_ITEM}/routing.md")
    if applied:
        write(root, "docs/policy.md", "A rule.\n")
    commit(root, "the earlier item leaves")


class TestRetired:
    @pytest.mark.rule("a-declaration-removed")
    def test_a_declaration_a_settle_removed_is_not_one_this_branch_made(
        self, branch, draft, capsys
    ):
        """A `routing.md` that `settle --apply` removed is a deletion in the
        diff, and the work item it declared was reviewed at its own pull
        request; `docs/` holding its rule change is what tells it from a
        deletion."""
        root, _code = branch
        remove_an_earlier_item(root, applied=True)
        _code, out = check(root, capsys)
        assert "retired: a settle" in out and "1788000000-an-earlier-item" in out
        assert "does not carry this file at HEAD" not in out

    @pytest.mark.rule("a-declaration-removed")
    def test_a_declaration_deleted_with_nothing_absorbing_it_is_refused(
        self, branch, draft, capsys
    ):
        root, _code = branch
        remove_an_earlier_item(root, applied=False)
        _code, out = check(root, capsys)
        assert "does not carry this file at HEAD" in out
        assert "retired:" not in out

    def test_a_declaration_removed_from_a_directory_that_stays_is_refused(
        self, branch, draft, capsys
    ):
        """A settle takes the whole directory, so a `routing.md` deleted
        beside a `spec.md` that stays is a deletion, its rule applied or not."""
        root, _code = branch
        remove_an_earlier_item(root, applied=True, whole=False)
        _code, out = check(root, capsys)
        assert "does not carry this file at HEAD" in out
        assert "retired:" not in out

    def test_a_rule_change_only_the_working_tree_holds_is_not_read(
        self, branch, draft, capsys
    ):
        """CI reads HEAD, so a rule change written and not committed applies
        nothing there."""
        root, _code = branch
        remove_an_earlier_item(root, applied=False)
        write(root, "docs/policy.md", "A rule.\n")
        _code, out = check(root, capsys)
        assert "does not carry this file at HEAD" in out
        assert "retired:" not in out
