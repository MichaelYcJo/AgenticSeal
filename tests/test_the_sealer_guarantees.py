"""The sealer's `guarantee.md`: its template, what `chain_check.py` reads of
it, and the definition that writes it.

`templates/sdd-guarantee.md` is the file the sealer fills, and
`chain_check.py#guarantee` is the arm that reads it at the pull request: a
ready pull request passes only where the file names HEAD and its verdict
reads `sound`. Each group holds a case on good input and one on bad.
"""

import importlib.util
import json
import pathlib
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
        "| Broad gate | sealed |\n\n"
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
    write(d, f"{ITEM}/guarantee.md", guarantee(audited, "sound"))
    commit(d, "the sealer's two files")
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": False}}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
    monkeypatch.delenv("GITHUB_HEAD_REF", raising=False)
    return d, audited


def check(root, capsys, *extra):
    code = chain.main(["--baseline", "main", "--root", str(root), *extra])
    return code, capsys.readouterr().out


# --- the template ---------------------------------------------------------------


class TestTemplate:
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

    def test_the_unfilled_template_is_no_guarantee(self):
        text = TEMPLATE.read_text(encoding="utf-8")
        assert chain.target_of(reader, text) is None
        verdicts = chain.verdicts_of(reader, text)
        assert len(verdicts) == 1 and verdicts[0][1] != chain.SOUND

    def test_the_claims_table_takes_a_row_per_act_of_step_3_and_lists_none(self):
        """T22: the sealer's acts are listed once, in `agents/sealer.md` step
        3. The comment over `## Claims re-run` points there and names no act,
        so a duty added to the definition has a row here without a second
        list to keep in step."""
        comment = between(TEMPLATE, "## Claims re-run", "| Claim |")
        assert "One row per act of `agents/sealer.md` step 3, whatever the act" in (
            comment
        )
        assert "`does not hold — <what came back>`" in comment
        for act in ("`fixed <commit>`", "sampled", "removal", "🔴"):
            assert act not in comment, act


# --- verdicts_of ---------------------------------------------------------------


class TestVerdictsOf:
    def test_each_verdict_is_read_through_emphasis(self):
        for said, word in (
            ("sound", "sound"),
            ("**sound**", "sound"),
            ("not sound — the body claims a README change", "not sound"),
            ("undecidable — does #12 ask for the flag?", "undecidable"),
        ):
            found = chain.verdicts_of(reader, guarantee("abc1234", said))
            assert [chain.verdict_word(v) for _n, v in found] == [word], said
        assert chain.verdict_word("sound, but the README is stale") != chain.SOUND

    def test_a_verdict_in_a_comment_is_not_read_and_two_lines_are_two(self):
        text = guarantee("abc1234", "sound").replace(
            "Verdict: sound", "<!-- Verdict: sound -->\nVerdict: sound\nVerdict: not"
        )
        found = chain.verdicts_of(reader, text)
        assert [v for _n, v in found] == ["sound", "not"]


# --- guarantee: the arm --------------------------------------------------------


class TestGuarantee:
    def test_a_sound_verdict_at_head_passes(self, item):
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
        write(root, rel, guarantee(head, "sound") + "Verdict: sound\n")
        commit(root, "two verdicts")
        [(_p, _n, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        assert "2 `Verdict:` lines" in why
        git(root, "rm", "-q", rel)
        commit(root, "no guarantee")
        [(_p, _n, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        assert "git carries no guarantee file" in why


# --- main: the arm at the pull request -----------------------------------------


def test_a_verdict_other_than_sound_fails_a_ready_pull_request(item, capsys):
    """S8 (T16): `not sound` and `undecidable` fail a ready pull request
    naming the file and the verdict; a draft prints the same line and
    passes; `--sealing`, the broad gate's own run, prints it."""
    root, sha = item
    code, out = check(root, capsys)
    assert code == 0, out
    rel = f"{ITEM}/guarantee.md"
    for verdict in ("not sound — the body claims a README change", "undecidable — Q?"):
        write(root, rel, guarantee(sha, verdict))
        commit(root, f"the sealer says {verdict}")
        code, out = check(root, capsys)
        assert code == 1, out
        line = next(ln for ln in out.splitlines() if ln.startswith(f"{rel}:"))
        assert verdict.split(" — ")[0] in line and "`sound`" in line
        code, out = check(root, capsys, "--sealing")
        assert code == 0 and rel in out
    event = root.parent / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": True}}), encoding="utf-8")
    code, out = check(root, capsys)
    assert code == 0 and rel in out


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
        assert "broad-gate --base <base> --record <item>" in text
        assert "judges nothing" not in text

    def test_the_sealer_quotes_what_only_the_gate_can_tell(self):
        """The moved base, the copy of the gate that ran, the outputs
        directory and the stamp's command are lines a reader learns from
        nowhere else, and the scratch log carries the work item's id so two
        sealers of one session never share it."""
        text = " ".join(SEALER.read_text(encoding="utf-8").split())
        assert "<scratchpad>/<work-item-id>/broad-gate.log" in text
        assert "where resolving the base moved it" in text.lower()
        assert "the tree's copy of the gate" in text
        assert "`outputs kept under broad-gate-<random>/`" in text
        assert "`seal-stamp --from <path>`" in text

    def test_the_sealer_reads_every_red_and_yellow_row_not_only_fixed_ones(self):
        """The check reads a row's word and not its mark, so a 🔴 or 🟡 row
        closed `confirmed` passes it. `docs/the-review-record.md` names the
        sealer as where such a row is caught, and on the last round nobody
        else reads it; this holds the sentence that tells the sealer to."""
        text = " ".join(SEALER.read_text(encoding="utf-8").split())
        assert "Read every 🔴 and 🟡 row of every record" in text
        assert (
            "closed `confirmed` or `❓ out of verified scope` passes it and "
            "answers nothing"
        ) in text
        assert (
            "unless a later round's row answers it, the verdict is `not sound`"
        ) in text

    def test_the_sealer_names_such_a_row_in_the_claims_table(self):
        """T21: a 🔴 or 🟡 row closed by another kind's word is written into
        `guarantee.md`'s `## Claims re-run`, so the file has a place for it;
        its `Result` is the later round's row that answers it, or
        `does not hold`."""
        step = between(
            SEALER,
            "3. **A claim against the fact.**",
            "4. **The parties against each other.**",
        )
        assert "Read every 🔴 and 🟡 row of every record" in step
        assert "each one as a row of `## Claims re-run`" in step
        assert (
            "its `Result` the later round's row that answers it or `does not hold`"
        ) in step


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
