"""The sealer's `guarantee.md`: its template, what `chain_check.py` reads of
it, and the definition that writes it.

`templates/sdd-guarantee.md` is the file the sealer fills, and
`chain_check.py#guarantee` is the arm that reads it at the pull request: a
ready pull request passes only where the file names HEAD and its verdict
reads `sealed`. Each group holds a case on good input and one on bad.
"""

import importlib.util
import json
import pathlib
import re
import subprocess

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHAIN = ROOT / "skills" / "code-review" / "scripts" / "chain_check.py"
READER = ROOT / "skills" / "verify" / "scripts" / "unverified_check.py"
TEMPLATE = ROOT / "templates" / "sdd-guarantee.md"
SEALER = ROOT / "agents" / "sealer.md"
DOCUMENT = ROOT / "docs" / "the-review-record.md"
ITEM = "seal/specs/1791999990-a-guaranteed-item"


def between(path, start, end):
    """The text of `path` from `start` to `end`, whitespace collapsed."""
    text = " ".join(path.read_text(encoding="utf-8").split())
    head = text.index(start)
    return text[head : text.index(end, head)]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


chain = load(CHAIN, "chain_check_for_the_guarantee")
reader = load(READER, "unverified_reader_for_the_guarantee")


def git(d, *args):
    return subprocess.run(
        ["git", "-C", str(d), *args],
        check=True,
        capture_output=True,
        encoding="utf-8",
    ).stdout.strip()


def write(d, rel, text):
    p = pathlib.Path(d) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def commit(d, message):
    git(d, "add", "-A")
    git(d, "commit", "-qm", message)
    return git(d, "rev-parse", "HEAD")


def guarantee(sha, verdict):
    return (
        "# 1791999990-a-guaranteed-item — guarantee\n\n"
        "| Field | Value |\n|---|---|\n"
        f"| Target SHA | {sha} against main |\n"
        f"| Broad gate | {sha} against main, as `broad-gate.md` names it |\n\n"
        "## Claims re-run\n\n"
        "| Claim | Source | Command | Result |\n|---|---|---|---|\n\n"
        "## The parties\n\n"
        "| Party | Says | Agrees with | Disagrees with |\n|---|---|---|---|\n\n"
        f"Verdict: {verdict}\n"
    )


ROUTING = """# routing

| Axis | Answer |
|---|---|
| Review | straight to the PR |
| Destination | open the pull request |
| Planning | the session |
| Branch | feature/g |
"""


@pytest.fixture
def item(tmp_path, monkeypatch):
    """A branch that went straight to the pull request and was sealed: the
    code, then `broad-gate.md` and `guarantee.md` naming that commit, judged
    as a ready pull request. Returns `(root, the audited commit)`."""
    d = tmp_path / "g"
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "t@t")
    git(d, "config", "user.name", "t")
    write(d, "f.txt", "one\n")
    commit(d, "base")
    git(d, "switch", "-q", "-c", "feature/g")
    write(d, f"{ITEM}/routing.md", ROUTING)
    write(d, "f.txt", "two\n")
    audited = commit(d, "the work")
    write(
        d,
        f"{ITEM}/broad-gate.md",
        f"| Field | Value |\n|---|---|\n| Broad gate | {audited} against main |\n",
    )
    write(d, f"{ITEM}/guarantee.md", guarantee(audited, "sealed"))
    commit(d, "the closing records")
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": False}}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
    monkeypatch.delenv("GITHUB_HEAD_REF", raising=False)
    # Under Actions the check prints `::error` annotations; these cases read
    # the plain line it prints everywhere else.
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    return d, audited


def check(root, capsys, *extra):
    code = chain.main(["--baseline", "main", "--root", str(root), *extra])
    return code, capsys.readouterr().out


# --- the template ---------------------------------------------------------------


def sealer_verdict_patterns():
    """Every `pattern:` a sealer eval grader matches a verdict line with, as
    `evals/scripts/rule_cases.py` generated it."""
    found = []
    for path in sorted(
        (ROOT / "evals" / "behaviour" / "sealer").glob("*/graders/*.md")
    ):
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("pattern: '^Verdict:"):
                found.append(line[len("pattern: '") : -1])
    return found


class TestTemplate:
    def test_no_sealer_grader_matches_a_line_of_the_template(self):
        """Round 2 of #1000, finding 2: a sealer that keeps the template's
        comment must not pass a verdict grader by it, so no line of the
        template opens with a verdict a grader reads. Seen red against the
        comment that listed the three shapes at the start of their lines."""
        patterns = sealer_verdict_patterns()
        assert len(patterns) >= 9, patterns
        text = TEMPLATE.read_text(encoding="utf-8")
        hits = [p for p in patterns if re.search(p, text, re.M)]
        assert hits == [], hits

    def test_the_template_carries_the_fields_sections_and_verdict_line(self):
        text = TEMPLATE.read_text(encoding="utf-8")
        lines = reader.readable(text)
        rows = chain.table_rows(reader, lines)
        assert [c[0].strip() for c in rows[:4]] == [
            "Field",
            "---",
            "Target SHA",
            "Broad gate",
        ]
        assert reader.sections(lines, "## Claims re-run")
        assert reader.sections(lines, "## The parties")
        assert ["Claim", "Source", "Command", "Result"] in [
            [c.strip() for c in r] for r in rows
        ]
        assert ["Party", "Says", "Agrees with", "Disagrees with"] in [
            [c.strip() for c in r] for r in rows
        ]
        # T4, S9 of #969: `sealed` has one meaning in this file. The cell
        # quotes the run `broad-gate.md` names; it never says `sealed`, which
        # a reader would take for the sealer's verdict.
        cell = next(c[1] for c in rows if c[0].strip() == "Broad gate")
        assert "sealed" not in cell, cell
        assert "`broad-gate.md` names" in cell, cell

    def test_the_target_row_keeps_an_earlier_run(self):
        """T3, S5 of #969. A re-run at a new HEAD keeps the earlier verdict on
        the `Target SHA` row as `; earlier run: <sha> <word>`, the form
        `broad-gate.md` already uses, and the definition re-runs only what a
        commit since touched. Protects: a full re-audit for a records-only
        commit, and an earlier verdict lost when the file is rewritten."""
        text = TEMPLATE.read_text(encoding="utf-8")
        rows = chain.table_rows(reader, reader.readable(text))
        cell = next(c[1] for c in rows if c[0].strip() == "Target SHA")
        assert "; earlier run: <sha> <word>" in cell, cell
        rule = between(SEALER, "**The guarantee covers HEAD", " check: ")
        assert "; earlier run: <sha> <word>" in rule, rule
        assert "re-runs only the claims whose coordinates a commit since" in rule

    def test_the_unfilled_template_is_no_guarantee(self):
        text = TEMPLATE.read_text(encoding="utf-8")
        assert chain.target_of(reader, text) is None
        verdicts = chain.verdicts_of(reader, text)
        assert len(verdicts) == 1 and verdicts[0][1] != chain.SEALED

    def test_the_claims_table_takes_a_row_per_act_of_step_3_and_lists_none(self):
        """T22: the sealer's acts are listed once, in `agents/sealer.md` step
        3. The comment over `## Claims re-run` points there and names no act,
        so a duty added to the definition has a row here without a second
        list to keep in step."""
        comment = between(TEMPLATE, "## Claims re-run", "| Claim |")
        assert "One row per act of `agents/sealer.md` step 3, whatever the act" in (
            comment
        )
        assert "`does not hold: <what came back>`" in comment
        for act in ("`fixed <commit>`", "sampled", "removal", "🔴"):
            assert act not in comment, act


# --- verdicts_of ---------------------------------------------------------------


class TestVerdictsOf:
    def test_each_verdict_is_read_in_its_shape(self):
        """S5 of #1000: the line is `Verdict: sealed`, `Verdict: withheld
        reason: <…>` or `Verdict: undecided question: <…>`, read whole.
        Protects: `withheld` with its reason left off read as `sealed`, and a
        `sealed` with a rider passing."""
        for said, word in (
            ("sealed", "sealed"),
            ("withheld reason: the body claims a README change", "withheld"),
            ("undecided question: does #12 ask for the flag?", "undecided"),
        ):
            found = chain.verdicts_of(reader, guarantee("abc1234", said))
            assert [chain.verdict_word(v) for _n, v in found] == [word], said
        assert chain.verdict_word("Verdict: sealed, but the README is stale") is None
        assert chain.verdict_word("Verdict: withheld") is None

    def test_a_verdict_in_a_comment_is_not_read_and_two_lines_are_two(self):
        text = guarantee("abc1234", "sealed").replace(
            "Verdict: sealed",
            "<!-- Verdict: sealed -->\nVerdict: sealed\n**Verdict:** with",
        )
        found = chain.verdicts_of(reader, text)
        assert [v for _n, v in found] == ["Verdict: sealed", "**Verdict:** with"]

    def test_the_verdict_patterns_are_linear_in_the_line(self):
        """#941's round 3 met a pattern that backtracked exponentially; the
        verdict line's patterns and the earlier run's repeat, so a long line
        of their repeated characters is read inside the bound, which is far
        above the linear time (under 0.1 s) and far below a backtracking
        one (no end), so a loaded runner does not fail it."""
        import time

        start = time.monotonic()
        for line in (
            "Verdict: withheld reason: " + "x " * 50000,
            "*_ " * 30000 + "verdict",
            "Verdict: undecided question:" + " " * 100000,
        ):
            chain.verdict_word(line)
            chain.verdicts_of(reader, line)
        chain.earlier_verdicts("; earlier run: aaa1111 against " + "x" * 100000)
        chain.earlier_verdicts("; earlier run: aaa1111" + " against x" * 30000)
        chain.earlier_verdicts("aaa1111 against " + "x" * 100000 + ";")
        chain.earlier_verdicts("earlier" + " " * 100000)
        chain.earlier_verdicts(" " * 100000 + "earlier runs" + " " * 100000)
        assert time.monotonic() - start < 5.0


# S6 of #1000: lines that mean the verdict and are not one of its three
# shapes. Each is refused at its line, and none reads as `sealed`.
NEAR_MISSES = (
    "Verdict: withheld — x",
    "Verdict: withheld - x",
    "Verdict: withheld",
    "Verdict: withheld reason:",
    "Verdict: withheld reason:x",
    "Verdict: withheld reason:  x",
    "Verdict: Sealed",
    "Verdict: **sealed**",
    "**Verdict:** sealed",
    "verdict: sealed",
    "Verdict: sealed reason: x",
    "Verdict: undecided reason: x",
    # Round 1 of #1000, finding 3: an indent is a code block at four spaces.
    "    Verdict: sealed",
    "\tVerdict: sealed",
)


@pytest.mark.rule("ready-needs-sealed")
@pytest.mark.parametrize("line", NEAR_MISSES)
def test_a_near_miss_of_the_verdict_is_refused_at_its_line(item, line):
    """S6 of #1000. Seen red against the reader that stripped emphasis and
    read a value by its prefix: `Sealed`, `**sealed**` and `**Verdict:**
    sealed` passed as `sealed`, and the rest were refused naming no shape,
    or not read at all."""
    root, sha = item
    rel = f"{ITEM}/guarantee.md"
    text = guarantee(sha, "sealed").replace("Verdict: sealed", line)
    write(root, rel, text)
    commit(root, f"the sealer wrote {line}")
    found = chain.verdicts_of(reader, text)
    assert len(found) == 1 and chain.verdict_word(found[0][1]) != chain.SEALED
    [(path, number, why)] = chain.guarantee(reader, str(root), ITEM, "main")
    assert (path, number) == (rel, text.splitlines().index(line) + 1), why
    for shape in (
        "`Verdict: sealed`",
        "`Verdict: withheld reason: <reason>`",
        "`Verdict: undecided question: <question>`",
    ):
        assert shape in why, why


# --- earlier_verdicts ----------------------------------------------------------


class TestEarlierVerdicts:
    """#975: the stamp is drawn once per work item, held by the `Target SHA`
    row's own `; earlier run: <sha> <word>` chain rather than a count kept
    beside the tree. One reader of that chain, beside the check's other
    readers of the same row."""

    def test_each_earlier_run_is_read_with_its_verdict_word(self):
        """S9 of #1000: an entry is `<sha> <word>`, with `against <base>`
        after the SHA where it names one."""
        cell = (
            "ccc3333 against main; earlier run: bbb2222 against main sealed; "
            "earlier run: aaa1111 withheld"
        )
        assert chain.earlier_verdicts(cell) == [
            ("bbb2222", chain.SEALED),
            ("aaa1111", chain.WITHHELD),
        ]

    def test_a_first_run_has_none(self):
        assert chain.earlier_verdicts("aaa1111 against main") == []
        assert chain.earlier_verdicts("") == []
        assert chain.earlier_verdicts(None) == []

    @pytest.mark.parametrize(
        "entry",
        [
            "; earlier run: aaa1111 withheld — x",
            "; earlier run: aaa1111 Sealed",
            "; earlier run: `bbb2222` against main **sealed**",
            "; earlier run: an earlier one, sealed",
            # Round 1 of #1000, finding 4: a misspelt separator.
            ";  earlier run: bbb2222 sealed",
            "; Earlier run: bbb2222 sealed",
            "; earlier run bbb2222 sealed",
            "; earlier runs: bbb2222 sealed",
            ", earlier run: bbb2222 sealed",
            # Round 2 of #1000, finding 3: the row has one shape, so no
            # spelling of the separator passes unread.
            "; earlier-run: bbb2222 sealed",
            "; earlier_run: bbb2222 sealed",
            "; earlierrun: bbb2222 sealed",
            # Any other text after the target, such as a second word of base.
            " @ 4a6e24f6",
            " (resolved as origin/main)",
        ],
    )
    def test_text_after_the_target_that_is_no_earlier_run_reads_no_word(self, entry):
        """S9 of #1000, and round 1's finding 4 and round 2's finding 3: the
        `Target SHA` value is `<sha> against <base>`, then each earlier run
        as exactly `; earlier run: <sha> <word>`, and any other text after
        the target comes back quoted with no word, for the arm to refuse.
        Seen red against the reader that read the word by its prefix and
        through emphasis, and against the one that looked for the separator
        in some spellings: a hyphen, an underscore and the joined word gave
        no entry at all."""
        cell = f"ccc3333 against main{entry}"
        assert chain.earlier_verdicts(cell) == [(entry.strip(), None)]

    @pytest.mark.parametrize(
        "entry",
        [
            "; earlier run: aaa1111 withheld — x",
            "; earlier run: aaa1111 Sealed",
            "; Earlier run: aaa1111 sealed",
            "; earlier-run: aaa1111 sealed",
        ],
    )
    def test_the_arm_refuses_an_entry_at_the_target_row(self, item, entry):
        """S9 of #1000: the guarantee arm refuses it at the `Target SHA`
        row's line, naming the entry and the shape it reads."""
        root, sha = item
        rel = f"{ITEM}/guarantee.md"
        text = guarantee(sha, "sealed").replace(
            f"| Target SHA | {sha} against main |",
            f"| Target SHA | {sha} against main{entry} |",
        )
        write(root, rel, text)
        commit(root, "an earlier run with a rider")
        [(path, number, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        row = next(n for n, ln in enumerate(text.splitlines(), 1) if "Target SHA" in ln)
        assert (path, number) == (rel, row), why
        assert f"`{entry.strip()}`" in why, why
        assert "`<sha> against <base>`" in why and "<sha> <word>`" in why, why


# --- guarantee: the arm --------------------------------------------------------


@pytest.mark.rule("ready-needs-sealed")
class TestGuarantee:
    def test_a_sealed_verdict_at_head_passes(self, item):
        root, _sha = item
        assert chain.guarantee(reader, str(root), ITEM, "main") == []

    def test_absent_unfilled_and_behind_head_are_named(self, item):
        root, _sha = item
        rel = f"{ITEM}/guarantee.md"
        write(root, f"{ITEM}/overview.md", "# an edit the sealer never read\n")
        later = commit(root, "a record after the guarantee")
        [(path, _line, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        assert path == rel and later[:8] in why
        write(root, rel, TEMPLATE.read_text(encoding="utf-8"))
        commit(root, "the template, unfilled")
        problems = chain.guarantee(reader, str(root), ITEM, "main")
        assert any("no SHA" in why for _p, _n, why in problems)
        head = git(root, "rev-parse", "HEAD")
        write(root, rel, guarantee(head, "sealed") + "Verdict: sealed\n")
        commit(root, "two verdicts")
        [(_p, _n, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        assert "2 `Verdict:` lines" in why
        write(root, rel, guarantee(head, "sealed").replace("Verdict: sealed\n", ""))
        commit(root, "no verdict")
        assert chain.guarantee(reader, str(root), ITEM, "main") == [
            (rel, 0, "0 `Verdict:` lines; the guarantee carries one")
        ]
        hidden = guarantee(head, "sealed").replace(
            "## The parties", "<!-- a note\n\n## The parties"
        )
        write(root, rel, hidden)
        commit(root, "a comment nobody closed")
        opener = hidden.splitlines().index("<!-- a note") + 1
        problems = chain.guarantee(reader, str(root), ITEM, "main")
        assert [(p, n) for p, n, _why in problems] == [(rel, opener), (rel, 0)]
        assert "never closes" in problems[0][2], problems
        git(root, "rm", "-q", rel)
        commit(root, "no guarantee")
        [(_p, _n, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        assert "git carries no guarantee file" in why

    def test_an_opener_quoted_in_a_code_span_hides_no_verdict(self, item):
        """Round 1 of #1000, finding 2: a claims cell quoting the comment
        opener in a code span, as two merged guarantees do, leaves the
        verdict line below it read. Seen red against the scan that read the
        opener: 0 `Verdict:` lines."""
        root, sha = item
        rel = f"{ITEM}/guarantee.md"
        text = guarantee(sha, "sealed").replace(
            "|---|---|---|---|\n\n## The parties",
            "|---|---|---|---|\n| markers | `x.md:1` | `git grep '<!-- specs/'` "
            "| holds |\n\n## The parties",
        )
        write(root, rel, text)
        commit(root, "a claim quoting the opener")
        assert chain.guarantee(reader, str(root), ITEM, "main") == []


def test_every_committed_guarantee_shows_its_one_verdict_line():
    """Round 1 of #1000, finding 2: each `guarantee.md` under `seal/specs/`
    gives the reader exactly the one `Verdict:` line it holds. Seen red at
    565dfa24, where two gave none."""
    found = {
        p.parent.name: len(chain.verdicts_of(reader, p.read_text(encoding="utf-8")))
        for p in (ROOT / "seal" / "specs").glob("*/guarantee.md")
    }
    assert {name: n for name, n in found.items() if n != 1} == {}, found


# --- main: the arm at the pull request -----------------------------------------


@pytest.mark.rule("ready-needs-sealed")
def test_a_verdict_other_than_sealed_fails_a_ready_pull_request(item, capsys):
    """T8, S8 of #969: `withheld` and `undecided` fail a ready pull request
    naming the file and the verdict; a draft prints the same line and
    passes; `--sealing`, the broad gate's own run, prints it."""
    root, sha = item
    code, out = check(root, capsys)
    assert code == 0, out
    rel = f"{ITEM}/guarantee.md"
    for verdict in (
        "withheld reason: the body claims a README change",
        "undecided question: Q?",
    ):
        write(root, rel, guarantee(sha, verdict))
        commit(root, f"the sealer says {verdict}")
        code, out = check(root, capsys)
        assert code == 1, out
        line = next(ln for ln in out.splitlines() if ln.startswith(f"{rel}:"))
        assert f"`Verdict: {verdict}`" in line and "needs `sealed`" in line, line
        code, out = check(root, capsys, "--sealing")
        assert code == 0 and rel in out
    event = root.parent / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": True}}), encoding="utf-8")
    code, out = check(root, capsys)
    assert code == 0 and rel in out


@pytest.mark.rule("ready-needs-sealed")
def test_the_old_words_are_refused_by_line(item, capsys):
    """T8, S8 of #969: a `guarantee.md` written before the words changed,
    reading `sound`, `not sound` or `undecidable`, fails a ready pull request
    on its `Verdict:` line, and the line says the word changed and what to
    do: spawn the sealer again at HEAD where `broad-gate.md` names a run at
    HEAD or one followed only by the work item's records, and otherwise run
    the broad gate first (round 1 of #969, finding 4). The line asserts
    nothing about the record it did not read (round 2, finding 2): the same
    pass's `broad_gate` line may say the record is behind HEAD. Protects: two
    spellings in one tree, where the check takes `sound` for the new
    `sealed`, or refuses it with a line nobody can place."""
    root, sha = item
    rel = f"{ITEM}/guarantee.md"
    for old in ("sound", "not sound — the body claims a README change", "undecidable"):
        text = guarantee(sha, old)
        number = text.splitlines().index(f"Verdict: {old}") + 1
        write(root, rel, text)
        commit(root, f"the sealer said {old} before the words changed")
        code, out = check(root, capsys)
        assert code == 1, out
        line = next(ln for ln in out.splitlines() if ln.startswith(f"{rel}:"))
        assert line.split()[0] == f"{rel}:{number}", line
        word = old.split(" — ")[0]
        assert f"`{word}` is a word the verdict no longer uses" in line, line
        # S8 of #1000: the three shapes, and no dash form.
        assert (
            "`Verdict: sealed`, `Verdict: withheld reason: <reason>` or "
            "`Verdict: undecided question: <question>`"
        ) in line, line
        assert chain.DASH not in line.split("no longer uses", 1)[1], line
        assert (
            "Where `broad-gate.md` names a run at HEAD, or one followed only "
            "by the work item's records, spawn the sealer again at HEAD, which "
            "writes the new word"
        ) in line, line
        assert (
            "otherwise run `broad-gate --base <base> --record <item>` and "
            "commit `broad-gate.md` first"
        ) in line, line
        assert "still stands" not in line, line


# --- the definition that writes it ---------------------------------------------


class TestDefinition:
    def test_the_sealer_runs_on_opus_with_the_contract_alone(self):
        head = SEALER.read_text(encoding="utf-8").split("---")[1]
        assert "\nmodel: opus\n" in head
        assert "skills:\n  - agent-contract\n" in head
        assert head.count("\n  - ") == 1

    def test_the_sealer_writes_the_guarantee_from_the_template(self):
        text = " ".join(SEALER.read_text(encoding="utf-8").split())
        assert "templates/sdd-guarantee.md" in text
        assert "judges nothing" not in text

    def test_step_1_reads_the_record_and_runs_nothing(self):
        """T2, S1 of #969. Step 1 reads `broad-gate.md` and the commits after
        the run it names, and refuses with `withheld reason: no broad run at HEAD`
        where the record is absent or followed by a path outside the work
        item's records; no step of the definition runs `broad-gate --base`.

        Protects: the sealer re-running a suite the orchestrator just ran
        (the 240K-token second run #957 measured), and a sealer that runs
        nothing and still writes a verdict over a run that never happened.
        Its conduct is the `shape-runs-no-broad-gate` and `truth-no-gate`
        graders' (`evals/behaviour/sealer/rule-sealer-no-gate/`); this holds
        the words the spawn reads."""
        step = " ".join(
            between(SEALER, "1. **Read the gate's record.**", "2. **").split()
        )
        assert "`broad-gate.md`" in step, step
        assert "log --no-merges --name-only <named>..HEAD ^<base>" in step, step
        assert "`chain_check.py#follows`" in step, step
        assert "`Verdict: withheld reason: no broad run at HEAD`" in step, step
        assert "Absent" in step and "any other path" in step, step
        assert "not an ancestor of HEAD" in step, step
        assert "the plain branch name the prompt names" not in step, step
        # Round 2 of #969, finding 1: the base arrives as a plain branch name,
        # a local ref, and a worktree with only `origin/<base>` gives step 1's
        # `^<base>` exit 128. It is resolved once, as the gate resolves it, and
        # every `<base>` after it is that ref's commit. Round 3, findings 1
        # and 2: the at-base clone carries no remote-tracking ref, so the
        # ref names nothing there; and a base resolving to nothing is the
        # orchestrator's input to repair, so `withheld`, not `undecided`.
        intro = " ".join(
            between(SEALER, "You work in the clone", "## Order of work").split()
        )
        assert "`broad_gate.py#resolve_base`" in intro, intro
        assert (
            "take the first of `<name>@{upstream}`, `origin/<name>` and "
            "`<name>` that `git -C <root> rev-parse --verify --quiet` answers, "
            "and every `<base>` below is the commit it prints"
        ) in intro, intro
        assert (
            "`Verdict: withheld reason: the base <name> resolves to no commit here`"
        ) in intro, intro
        order = between(SEALER, "## Order of work", "## Never")
        assert "broad-gate --base" not in order, (
            "a step of the sealer's definition runs the broad gate"
        )
        never = " ".join(between(SEALER, "## Never", "## Rules").split())
        assert "the typecheck or `broad-gate`" in never, never

    def test_the_sealer_is_spawned_before_the_pull_request_and_reads_its_body_from_a_file(
        self,
    ):
        """S8 of #943. The pull request opens once the sealer has sealed, so
        no pull request exists when the sealer runs: the description no
        longer spawns it per ready pull request, and the body it audits is
        the file the prompt names, the one the pull request then opens
        with."""
        text = SEALER.read_text(encoding="utf-8")
        head = " ".join(text.split("---")[1].split())
        assert "once per ready pull request" not in head, head
        assert "before the pull request opens" in head, head
        intro = " ".join(
            between(SEALER, "You work in the clone", "## Order of work").split()
        )
        assert "a file holding the pull request body" in intro, intro
        # Round 1 of #943, finding 1: on the stated limit's path the sealer
        # runs again with the pull request already open.
        assert "or is given it where already open" in intro, intro
        assert "gh pr view" not in text, "the sealer still reads an open pull request"

    def test_the_guarantee_rule_exempts_only_the_closing_records(self):
        """Round 1 of #969, finding 1. `chain_check.py#guarantee` lets only
        `broad-gate.md` and `guarantee.md` follow the commit the guarantee
        names (`follows(..., only=CLOSING_RECORDS)`); a sealer told that any
        record of the work item may follow keeps an earlier verdict over a
        changelog or phase record it never read, and the check refuses it."""
        rule = " ".join(
            between(SEALER, "**The guarantee covers HEAD", " check: ").split()
        )
        assert (
            "other than one touching only the closing records, `broad-gate.md` "
            "and `guarantee.md`, owes a new audit"
        ) in rule, rule
        assert "work item's records" not in rule, rule

    def test_the_orchestration_quotes_what_only_the_gate_can_tell(self):
        """Moved by #969 from the sealer with the run. The moved base, the
        copy of the gate that ran and the outputs directory are lines a reader
        learns from nowhere else, and the orchestrator who runs the gate is
        the one who quotes them; the sealer, which sees no gate output, no
        longer carries the instruction."""
        text = " ".join(
            (ROOT / "skills" / "code-review" / "orchestration.md")
            .read_text(encoding="utf-8")
            .split()
        )
        assert "where resolving the base moved it" in text.lower()
        assert "the tree's copy of the gate" in text
        assert "`outputs kept under broad-gate-<random>/`" in text
        sealer = " ".join(SEALER.read_text(encoding="utf-8").split())
        assert "outputs kept under" not in sealer

    def test_step_3_holds_two_acts_and_reads_no_location(self):
        """T40 (S22): step 3 is the one list of the sealer's acts, and it holds
        two — the sample of the smith's claims re-run, and the removals
        confirmed absent. Whether a `fixed` commit touches its finding's
        `location:` is the check's to read, so no act of step 3 reads it."""
        step = between(SEALER, "3. **A claim against the fact.**", "4. **")
        assert "Choose a sample of the smith's `executed`" in step, step
        assert "For every `## Removes` row of `spec.md`" in step, step
        assert "two acts" in step.lower(), step
        assert step.count("For every") == 1, step
        for word in ("touches", "Location", "location", "fixed <commit>"):
            assert word not in step, word


# --- the document that states the guarantee ------------------------------------


class TestDocument:
    def test_the_guarantee_section_points_at_step_3_and_lists_no_act(self):
        """T23: `docs/the-review-record.md` §*The guarantee* points at the
        definition's steps 3 and 4 for the acts and lists none of them. The
        record's vocabulary in §*The round record* keeps `fixed <commit>`,
        and is outside the slice read here."""
        section = between(DOCUMENT, "## The guarantee", "## The run")
        assert "`agents/sealer.md` step 3" in section
        assert "step 4" in section
        assert "one row of `## Claims re-run` or `## The parties`" in section
        for act in ("`fixed <commit>`", "re-runs a sample", "stands in the tree"):
            assert act not in section, act
