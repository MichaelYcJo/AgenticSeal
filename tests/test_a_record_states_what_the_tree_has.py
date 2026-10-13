"""evidence-check's records arm: what a live work item's records say is there.

A ledger row is a claim about the tree that something reads. A record --
`spec.md`, `plan.md`, `overview.md`, `rounds/round-N.md`, `phases/phase-N.md`
-- states the same kind of thing and nothing reads it (#190). This file holds
the boundary that decides whose records are read, the identifier arm, the
stamp arm, and the escape hatch.

**No fixture here runs git, and no fixture here may.** The checker calls git
for nothing outside `--migrate` (`README.md` §*A row carries no line number
and no commit*), so a fixture that needed an index would be pinning behaviour
the checker is not allowed to have. The boundary is the presence of a file
and the arms resolve content, the way `test_a_row_points_by_content.py` does.
"""

import importlib.util
import ntpath
import os
import subprocess
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "skills", "evidence-check", "scripts", "evidence_check.py")


def module():
    spec = importlib.util.spec_from_file_location("specseal_evidence_check", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run(args, cwd):
    return subprocess.run(
        [sys.executable, SCRIPT, *args],
        cwd=str(cwd),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


def home(tmp_path):
    """A `seal/` root with `specs/` and `ledger/` under it."""
    h = tmp_path / "seal"
    (h / "specs").mkdir(parents=True)
    (h / "ledger").mkdir(parents=True)
    return h


def work_item(h, item, fragment=True, **files):
    """A work item directory, with or without its ledger fragment.

    `fragment=False` is a work item that has shipped: the release folded its
    rows into the gathered ledger and removed the file.
    """
    d = h / "specs" / item
    d.mkdir(parents=True, exist_ok=True)
    for name, text in files.items():
        path = d / name.replace("__", "/")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    if fragment:
        (h / "ledger" / f"{item}.md").write_text(
            "| Clause | Coordinate | Grounds | Checked |\n|---|---|---|---|\n",
            encoding="utf-8",
        )
    return d


# --- the boundary: has this work item shipped -------------------------------


def test_a_work_item_with_a_ledger_fragment_has_not_shipped(tmp_path):
    h = home(tmp_path)
    work_item(h, "1780000000-live", **{"spec.md": "# live\n"})
    assert set(module().unshipped(str(h))) == {"1780000000-live"}


def test_a_work_item_whose_fragment_was_folded_away_has_shipped(tmp_path):
    h = home(tmp_path)
    work_item(h, "1780000000-shipped", fragment=False, **{"spec.md": "# shipped\n"})
    assert module().unshipped(str(h)) == {}


def test_the_boundary_reads_the_fragments_beside_the_specs(tmp_path):
    """Two work items, one folded — only the unfolded one is live.

    The pair, not either alone: a reader that returned everything and a
    reader that returned nothing both pass a single-arm case.
    """
    h = home(tmp_path)
    work_item(h, "1780000000-live", **{"spec.md": "# a\n"})
    work_item(h, "1770000000-shipped", fragment=False, **{"spec.md": "# b\n"})
    assert set(module().unshipped(str(h))) == {"1780000000-live"}


def test_a_fragment_whose_records_are_not_here_is_not_a_work_item(tmp_path):
    """`seal export` carries the records out and leaves the fragment.

    An arm that reads records has nothing to say about a work item that has
    none in this tree, and returning the id would make every caller check the
    directory again.
    """
    h = home(tmp_path)
    (h / "ledger" / "1780000000-carried-out.md").write_text("rows\n", encoding="utf-8")
    assert module().unshipped(str(h)) == {}


def test_a_directory_in_the_fragment_folder_is_not_a_fragment(tmp_path):
    h = home(tmp_path)
    work_item(h, "1780000000-live", fragment=False, **{"spec.md": "# a\n"})
    (h / "ledger" / "1780000000-live.md").mkdir()
    assert module().unshipped(str(h)) == {}


def test_a_root_with_no_fragment_folder_reads_as_nothing_live(tmp_path):
    """A repository that has never written a fragment, not a crash."""
    h = tmp_path / "seal"
    (h / "specs").mkdir(parents=True)
    assert module().unshipped(str(h)) == {}


def test_the_records_read_are_every_md_in_the_work_item(tmp_path):
    """The whole SDD set, not the round records alone.

    #190's three instances landed in a `plan.md`, an `overview.md` and a
    ledger row; nothing here reads a file name to decide.
    """
    h = home(tmp_path)
    d = work_item(
        h,
        "1780000000-live",
        **{
            "spec.md": "# a\n",
            "overview.md": "# b\n",
            "rounds__round-1.md": "# c\n",
            "phases__phase-1.md": "# d\n",
            "notes.txt": "not a record\n",
        },
    )
    found = {
        os.path.relpath(p, str(d)).replace(os.sep, "/")
        for p in module().record_files(str(d))[0]
    }
    assert found == {
        "spec.md",
        "overview.md",
        "rounds/round-1.md",
        "phases/phase-1.md",
    }


def test_the_walk_does_not_descend_into_a_cache(tmp_path):
    """A `__pycache__` under a work item is not a record.

    The same reason the name corpus skips one: build output carries copies of
    names the tree no longer has.
    """
    h = home(tmp_path)
    d = work_item(h, "1780000000-live", **{"spec.md": "# a\n"})
    (d / "__pycache__").mkdir()
    (d / "__pycache__" / "stale.md").write_text("# stale\n", encoding="utf-8")
    found = [os.path.basename(p) for p in module().record_files(str(d))[0]]
    assert found == ["spec.md"]


def test_a_repository_with_no_records_reads_as_nothing_to_check(tmp_path):
    (tmp_path / "seal").mkdir()
    r = run(["."], tmp_path)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "no evidence ledgers found" in r.stdout


# --- the identifier arm: a name the tree does not have ----------------------


def tree(tmp_path, **files):
    """Files outside `seal/`, which is what the name corpus is built from."""
    for name, text in files.items():
        path = tmp_path / name.replace("__", "/")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def refusals(tmp_path):
    findings, read, _stamps = module().check_records(
        str(tmp_path), str(tmp_path / "seal")
    )
    return [(status, coord, detail) for status, coord, detail in findings], read


def test_a_live_record_naming_a_unit_the_tree_lacks_is_refused(tmp_path):
    h = home(tmp_path)
    tree(tmp_path, **{"mod.py": "def kept_helper():\n    return 1\n"})
    work_item(
        h,
        "1780000000-live",
        **{"rounds__round-2.md": "# r\n\nthe alias `gone_helper` has one call site\n"},
    )
    found, read = refusals(tmp_path)
    assert read == 1
    assert len(found) == 1
    status, coord, detail = found[0]
    assert status == "NOT-IN-TREE"
    assert coord.endswith("rounds/round-2.md:3")
    assert "`gone_helper`" in detail


def test_the_refusal_names_the_file_the_line_and_the_name(tmp_path):
    """All three, because a class is enumerated from a coordinate.

    A refusal that named the file alone would send the reader through a
    record looking for which of its backticks moved.
    """
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"plan.md": "# p\n\n\n\nphase 2 builds `gone_helper` here\n"},
    )
    found, _ = refusals(tmp_path)
    coord, detail = found[0][1], found[0][2]
    assert coord.replace(os.sep, "/").endswith("1780000000-live/plan.md:5")
    assert "`gone_helper`" in detail


def test_a_shipped_work_items_record_is_left_alone(tmp_path):
    """129 occurrences sit in this repository's shipped records and they are
    history — a plan proposing a helper built under another name is a correct
    record of what was decided then."""
    h = home(tmp_path)
    work_item(
        h,
        "1770000000-shipped",
        fragment=False,
        **{"plan.md": "# p\n\nbuild `gone_helper`\n"},
    )
    assert refusals(tmp_path) == ([], 0)


def test_a_name_the_tree_carries_passes(tmp_path):
    h = home(tmp_path)
    tree(tmp_path, **{"mod.py": "def kept_helper():\n    return 1\n"})
    work_item(h, "1780000000-live", **{"plan.md": "# p\n\n`kept_helper` stays\n"})
    assert refusals(tmp_path) == ([], 1)


def test_a_file_name_is_a_name_the_tree_carries(tmp_path):
    """A record naming `test_foo` is naming a module as often as a function."""
    h = home(tmp_path)
    tree(tmp_path, **{"tests__test_the_thing.py": "x = 1\n"})
    work_item(
        h, "1780000000-live", **{"plan.md": "# p\n\n`test_the_thing` covers it\n"}
    )
    assert refusals(tmp_path) == ([], 1)


def test_a_single_word_name_is_not_read_as_a_claim(tmp_path):
    """`cmp`, `rpartition`, `Starred` — a shell command, a str method and an
    ast node. Nineteen such names sit in this repository's records and not one
    is a claim about a unit, so the pattern is narrowed rather than the
    exemption widened."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"plan.md": "# p\n\nthe reviewer ran `cmp` and read `rpartition`\n"},
    )
    assert refusals(tmp_path) == ([], 0)


def test_the_marker_exempts_the_line(tmp_path):
    """The escape hatch a reviewer already writes beside a proposed name."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"rounds__round-1.md": "# r\n\n`gone_helper` — NAME NOT IN TREE\n"},
    )
    assert refusals(tmp_path) == ([], 0)


def test_the_marker_exempts_the_line_and_not_the_name(tmp_path):
    """Marked on one line, the same name is still a claim on the next.

    The exemption is a marker on the LINE for the reason `plan.md` gives: a
    list inside the checker gets widened by whoever is annoyed, and a name
    exempted once would be exempt everywhere it is claimed afterwards.
    """
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{
            "rounds__round-1.md": (
                "# r\n\n`gone_helper` — NAME NOT IN TREE\n\n"
                "and `gone_helper` is what the module calls\n"
            )
        },
    )
    found, _ = refusals(tmp_path)
    assert len(found) == 1
    assert found[0][1].endswith(":5")


def test_a_cache_in_the_tree_does_not_supply_a_name(tmp_path):
    """A compiled module carries its own identifiers in its constants pool,
    so a corpus that reads one answers "still there" for a name the tree lost
    at the last commit."""
    h = home(tmp_path)
    cache = tmp_path / "__pycache__"
    cache.mkdir()
    (cache / "mod.cpython-312.pyc").write_text("gone_helper\n", encoding="utf-8")
    work_item(h, "1780000000-live", **{"plan.md": "# p\n\n`gone_helper`\n"})
    found, _ = refusals(tmp_path)
    assert len(found) == 1


def test_a_binary_file_does_not_supply_a_name(tmp_path):
    """A compiled artefact outside a cache directory is still not the tree.

    Decoded with `errors="replace"`, a `.pyc`, an archive or an image yields
    token-shaped runs from its own bytes, and a name that turns up there is a
    name nobody wrote. The failure that guard prevents is a false PASS, which
    is the expensive direction: the record keeps a claim that is not true.
    """
    h = home(tmp_path)
    (tmp_path / "assets").mkdir()
    (tmp_path / "assets" / "thing.bin").write_bytes(b"\x00\x01gone_helper\x00")
    work_item(h, "1780000000-live", **{"plan.md": "# p\n\n`gone_helper`\n"})
    found, _ = refusals(tmp_path)
    assert len(found) == 1


def test_the_records_own_directory_is_not_its_own_corpus(tmp_path):
    """A name that only another work item's record carries is still a name
    the tree does not have."""
    h = home(tmp_path)
    work_item(
        h, "1770000000-shipped", fragment=False, **{"plan.md": "# p\n\n`gone_helper`\n"}
    )
    work_item(h, "1780000000-live", **{"plan.md": "# p\n\n`gone_helper`\n"})
    found, _ = refusals(tmp_path)
    assert len(found) == 1
    assert "1780000000-live" in found[0][1]


def test_a_work_items_own_ledger_fragment_is_not_part_of_the_corpus(tmp_path):
    """A fragment is the work item writing about itself, same branch and same
    lifetime as the records beside it.

    Found while writing this work item's own rows: naming four units in the
    fragment put them in the corpus and silenced four refusals in its own
    `phase-2.md`. A work item could clear the check on its records by naming
    the unit in its own ledger file.
    """
    h = home(tmp_path)
    work_item(h, "1780000000-live", **{"plan.md": "# p\n\n`gone_helper` is gone\n"})
    (h / "ledger" / "1780000000-live.md").write_text(
        "| Clause | Coordinate |\n|---|---|\n| R1 · `gone_helper` went | x |\n",
        encoding="utf-8",
    )
    found, _ = refusals(tmp_path)
    assert len(found) == 1
    assert "`gone_helper`" in found[0][2]


def test_the_gathered_ledger_is_part_of_the_corpus(tmp_path):
    """`seal/ledger.md` keeps a renamed unit's old name beside the new one on
    purpose, so a reader coming from an older record can follow it. Excluding
    the whole of `seal/` refuses five such occurrences in this repository."""
    h = home(tmp_path)
    (h / "ledger.md").write_text(
        "| Clause | Coordinate |\n|---|---|\n"
        "| R1 · renamed from `gone_helper` | `mod.py#kept@deadbeef` |\n",
        encoding="utf-8",
    )
    work_item(h, "1780000000-live", **{"plan.md": "# p\n\n`gone_helper` was renamed\n"})
    assert refusals(tmp_path)[0] == []


def test_a_refusal_fails_the_run(tmp_path):
    h = home(tmp_path)
    (h / "ledger" / "1780000000-live.md").write_text("rows\n", encoding="utf-8")
    work_item(h, "1780000000-live", **{"plan.md": "# p\n\n`gone_helper`\n"})
    r = run(["."], tmp_path)
    assert r.returncode == 2, r.stdout + r.stderr
    assert "NOT-IN-TREE" in r.stdout
    assert "1 refused" in r.stdout


def test_the_records_arm_runs_even_when_a_narrowing_finds_no_ledger(tmp_path):
    """`--ledger` narrows the LEDGERS read; it says nothing about records, and
    a narrowing that matched none must not silence the other arm."""
    h = home(tmp_path)
    work_item(h, "1780000000-live", **{"plan.md": "# p\n\n`gone_helper`\n"})
    r = run(["--ledger", "nothing/here/*.md", "."], tmp_path)
    assert r.returncode == 2, r.stdout + r.stderr
    assert "NOT-IN-TREE" in r.stdout


# --- the corpus reaches a local-mode root (round 1, 🟡 4) -------------------


def test_the_gathered_ledger_is_in_the_corpus_in_local_mode_too(tmp_path):
    """Identical bytes answered exit 0 shared and exit 2 local.

    In local mode `seal/` sits under the git common directory, which every
    walk here prunes with `.git` — so `seal/ledger.md`, which is IN the
    corpus by design, was dropped for no reason but where the root happens to
    sit.
    """
    (tmp_path / "mod.py").write_text(
        "def kept_helper():\n    return 1\n", encoding="utf-8"
    )
    local = tmp_path / ".git" / "seal"
    (local / "specs").mkdir(parents=True)
    (local / "ledger").mkdir(parents=True)
    work_item(local, "1780000000-live", **{"plan.md": "# p\n\n`renamed_helper`\n"})
    (local / "ledger.md").write_text(
        "| S1 | `mod.py#renamed_helper@00000000` | read | 2026-09-07 |\n",
        encoding="utf-8",
    )
    findings, read, _stamps = module().check_records(str(tmp_path), str(local))
    assert (findings, read) == ([], 1)


# --- the stamp arm: an anchor a record wrote down ---------------------------

SERVICE = "def handler(x):\n    return x + 1\n"
# `handler`'s body, hashed the way the checker hashes it. Pinned rather than
# computed, so a fixture cannot agree with a broken hasher.
GOOD = "9207ed06"


def test_a_stamp_the_tree_contradicts_is_named(tmp_path):
    """#190's own worked example: an `overview.md` naming an anchor stamp the
    tree no longer holds."""
    h = home(tmp_path)
    tree(tmp_path, **{"src__service.py": "def handler(x):\n    return x + 2\n"})
    work_item(
        h,
        "1780000000-live",
        **{"overview.md": f"# o\n\nstamped `src/service.py#handler@{GOOD}`\n"},
    )
    findings, _names, stamps = module().check_records(
        str(tmp_path), str(tmp_path / "seal")
    )
    assert stamps == 1
    assert len(findings) == 1
    status, coord, detail = findings[0]
    assert status == "DRIFTED"
    assert coord.endswith("overview.md:3")
    assert "src/service.py#handler" in detail


def test_a_stamp_naming_a_file_the_tree_lacks_is_broken(tmp_path):
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"plan.md": "# p\n\nthe fixture `mod.py#helper@deadbeef`\n"},
    )
    findings, _names, _stamps = module().check_records(
        str(tmp_path), str(tmp_path / "seal")
    )
    assert [f[0] for f in findings] == ["BROKEN"]
    assert findings[0][1].endswith("plan.md:3")


def test_a_stamp_the_tree_still_holds_passes(tmp_path):
    h = home(tmp_path)
    tree(tmp_path, **{"src__service.py": SERVICE})
    work_item(
        h,
        "1780000000-live",
        **{"overview.md": f"# o\n\n`src/service.py#handler@{GOOD}`\n"},
    )
    findings, _names, stamps = module().check_records(
        str(tmp_path), str(tmp_path / "seal")
    )
    assert (findings, stamps) == ([], 1)


def test_the_marker_exempts_a_stamp_line_too(tmp_path):
    """One marker, named in one place. `plan.md` and a round record in this
    repository both carry the fixture stamp `mod.py#helper@deadbeef`, which is
    exactly the shape the marker exists for."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"plan.md": "# p\n\n`mod.py#helper@deadbeef` — NAME NOT IN TREE\n"},
    )
    assert module().check_records(str(tmp_path), str(tmp_path / "seal")) == ([], 0, 0)


def test_a_shipped_work_items_stamp_is_left_alone(tmp_path):
    h = home(tmp_path)
    work_item(
        h,
        "1770000000-shipped",
        fragment=False,
        **{"overview.md": f"# o\n\n`src/service.py#handler@{GOOD}`\n"},
    )
    assert module().check_records(str(tmp_path), str(tmp_path / "seal")) == ([], 0, 0)


def test_a_location_column_is_not_an_unmigrated_coordinate(tmp_path):
    """`path:line` is what the round template prescribes for a Location cell.

    `old_format_rows` reads every table row for that shape and tells the
    author to run the migrator, which is right for a ledger and wrong for a
    record — so the records arm calls `check_text` and not `check_ledger`.
    """
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{
            "rounds__round-1.md": (
                "# r\n\n| # | Finding | Location |\n|---|---|---|\n"
                "| 1 | the guard | `hooks/review-history-guard.py:130` |\n"
            )
        },
    )
    assert module().check_records(str(tmp_path), str(tmp_path / "seal")) == ([], 0, 0)


def test_two_lines_stamping_one_unit_are_two_claims(tmp_path):
    """A record repeating a stale stamp is stale twice, and a reader who has
    to open one line has to open the other."""
    h = home(tmp_path)
    tree(tmp_path, **{"src__service.py": "def handler(x):\n    return x + 2\n"})
    work_item(
        h,
        "1780000000-live",
        **{
            "overview.md": (
                f"# o\n\n`src/service.py#handler@{GOOD}`\n\n"
                f"and again `src/service.py#handler@{GOOD}`\n"
            )
        },
    )
    findings, _names, stamps = module().check_records(
        str(tmp_path), str(tmp_path / "seal")
    )
    assert stamps == 2
    assert [f[1].rsplit(":", 1)[1] for f in findings] == ["3", "5"]


def test_a_records_drift_does_not_fail_the_run_and_a_broken_anchor_does(tmp_path):
    """A live work item's branch is editing the units its records stamp, so a
    run that failed on drift would be red by construction — the state the
    ledger CI job's own comment refuses. A name or an anchor that does not
    resolve has no mid-flight excuse."""
    h = home(tmp_path)
    (h / "ledger" / "1780000000-live.md").write_text("rows\n", encoding="utf-8")
    tree(tmp_path, **{"src__service.py": "def handler(x):\n    return x + 2\n"})
    d = work_item(
        h,
        "1780000000-live",
        **{"overview.md": f"# o\n\n`src/service.py#handler@{GOOD}`\n"},
    )
    drift = run(["."], tmp_path)
    assert drift.returncode == 1, drift.stdout + drift.stderr
    assert "0 refused · 1 drifted" in drift.stdout

    strict = run(["--strict", "."], tmp_path)
    assert strict.returncode == 2, strict.stdout + strict.stderr

    (d / "overview.md").write_text(
        "# o\n\n`src/gone.py#handler@deadbeef`\n", encoding="utf-8"
    )
    broken = run(["."], tmp_path)
    assert broken.returncode == 2, broken.stdout + broken.stderr
    assert "1 refused · 0 drifted" in broken.stdout


# --- a quotation is not a claim (round 1, 🟡 11) -----------------------------


def test_a_fenced_name_is_a_quotation_and_not_a_claim(tmp_path):
    """`## Paste-ready fixes` is fences of code the tree does not have yet —
    that is what a paste-ready fix IS. Refusing one asks the writer to mark
    up a block they copied verbatim, and a marker inside a fence changes the
    fix somebody pastes."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{
            "rounds__round-1.md": "# r\n\n## Paste-ready fixes\n\n"
            "```python\ndef gone_helper():\n    return `gone_helper`\n```\n"
        },
    )
    assert refusals(tmp_path) == ([], 0)


def test_a_name_after_the_fence_closes_is_a_claim_again(tmp_path):
    """The pair: a reader that switched the arm off at the first fence would
    pass the case above and read nothing after it."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{
            "rounds__round-1.md": "# r\n\n```python\n`inside_a_fence`\n```\n\n"
            "and then `gone_helper` in prose\n"
        },
    )
    found, read = refusals(tmp_path)
    assert read == 1
    assert [s for s, _, _ in found] == ["NOT-IN-TREE"], found
    assert "`gone_helper`" in found[0][2]


def test_an_html_comment_is_an_aside_and_not_a_claim(tmp_path):
    """A template's comments describe fields rather than assert units, and
    the records are bootstrapped from templates that carry them."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"plan.md": "# p\n\n<!-- `gone_helper` — what this field holds -->\n"},
    )
    assert refusals(tmp_path) == ([], 0)


def test_a_multi_line_html_comment_is_an_aside_to_its_end(tmp_path):
    """An aside was an aside only on the line that OPENS it, so a comment
    spanning lines had every continuation line read as a claim (round 2,
    🟡 2). `templates/` writes comments that way, so the false refusal
    landed on a record using a template exactly as the template is written.
    """
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{
            "plan.md": "# p\n\n<!-- what this field holds, and\n"
            "     why `gone_helper` is the example -->\n"
        },
    )
    assert refusals(tmp_path) == ([], 0)


def test_a_name_after_a_multi_line_comment_closes_is_a_claim_again(tmp_path):
    """The pair for the case above, and the same pair the fence already has:
    a reader that switched the arm off at the first `<!--` would pass it and
    read nothing after the comment either."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{
            "plan.md": "# p\n\n<!-- what this field holds, and\n"
            "     why `inside_a_comment` is the example -->\n\n"
            "and then `gone_helper` in prose\n"
        },
    )
    found, read = refusals(tmp_path)
    assert read == 1, (found, read)
    assert [s for s, _, _ in found] == ["NOT-IN-TREE"], found
    assert "`gone_helper`" in found[0][2]


def test_a_fence_the_record_never_closes_does_not_silence_what_follows(tmp_path):
    """A fence the record never closes took every claim under it, in silence
    (round 2, 🟡 3). An unclosed fence is a malformed record, not a licence
    to read nothing, so the lines it holds are read rather than dropped."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{
            "rounds__round-1.md": "# r\n\n```python\ndef f():\n    pass\n\n"
            "and then `gone_helper` in prose\n"
        },
    )
    found, read = refusals(tmp_path)
    assert read == 1, (found, read)
    assert [s for s, _, _ in found] == ["NOT-IN-TREE"], found
    assert "`gone_helper`" in found[0][2]


def test_a_comment_the_record_never_closes_does_not_silence_what_follows(tmp_path):
    """The pair of the case above, one region over (#217). A comment with no
    `-->` set the aside and nothing ever cleared it, so every remaining line
    of the record was dropped and the arm said nothing — exit 0, `0 names
    read`, on a file whose author made a mistake. The fence half had already
    been given the answer: an unclosed region is a malformed record, not a
    licence to read nothing, so its lines are held and read at the end."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"plan.md": "# p\n\n<!-- note\n\nand then `gone_helper` in prose\n"},
    )
    found, read = refusals(tmp_path)
    assert read == 1, (found, read)
    assert [s for s, _, _ in found] == ["NOT-IN-TREE"], found
    assert "`gone_helper`" in found[0][2]


def test_the_marker_exempts_a_line_a_never_closed_comment_held(tmp_path):
    """The marker exempts the LINE, and a line an unclosed comment held is
    still a line — the same rule the fence's held lines already have. The
    marker is written bare here, because a `<!-- … -->` on the held line
    would close the comment and the line would never be held at all."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"plan.md": "# p\n\n<!-- note\n\n`gone_helper` — NAME NOT IN TREE\n"},
    )
    assert refusals(tmp_path) == ([], 0)


def test_a_closed_comment_lets_go_of_the_lines_it_held(tmp_path):
    """A comment that DOES close is an aside to its end, middle lines
    included: what the region held while it was open is dropped at the
    `-->`, exactly as a closed fence clears `held`. Without that, a
    three-line template comment would have its middle line read as a claim
    at the end of the file — round 2's 🟡 2 of #190, one region over."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{
            "plan.md": "# p\n\n<!-- what this field holds,\n"
            "     why `gone_helper` is the example,\n"
            "     and where it goes -->\n"
        },
    )
    assert refusals(tmp_path) == ([], 0)


def test_a_tilde_fence_does_not_close_a_backtick_fence(tmp_path):
    """The two markers shared one flag, so a `~~~` line quoted INSIDE a
    ```-fence closed it and everything after was read as prose. The opener
    is remembered, so only its own marker closes it."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{
            "rounds__round-1.md": "# r\n\n```python\n~~~\n`gone_helper`\n```\n\n"
            "prose after the fence\n"
        },
    )
    assert refusals(tmp_path) == ([], 0)


def test_the_marker_exempts_a_line_a_never_closed_fence_held(tmp_path):
    """The marker exempts the LINE, and a line an unclosed fence held is
    still a line. Re-reading held lines past the marker would refuse a name
    the writer had already said the tree does not have."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{
            "rounds__round-1.md": "# r\n\n```python\n"
            "`gone_helper`  <!-- NAME NOT IN TREE -->\n"
        },
    )
    assert refusals(tmp_path) == ([], 0)


def test_a_fenced_stamp_is_a_quotation_too(tmp_path):
    """One reader for both arms: a stamp in a fence is a quoted anchor
    exactly as a name in one is a quoted name."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"plan.md": "# p\n\n```\nrow `mod.py#helper@deadbeef`\n```\n"},
    )
    assert refusals(tmp_path) == ([], 0)


# --- a closer is a position (#220), and the fence rule is the shared one --


def test_a_claim_after_a_closing_delimiter_is_read(tmp_path):
    """S10, #220's first shape. The whole line holding `-->` used to be
    skipped, so a name written after the closer was never read. What follows
    a closer is read by the line's own rules. Seen red against `c52e8350`:
    no name read, exit 0."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"plan.md": "# p\n\n<!-- note\nend --> `gone_helper` is used\n"},
    )
    found, read = refusals(tmp_path)
    assert read == 1, (found, read)
    assert [s for s, _, _ in found] == ["NOT-IN-TREE"], found
    assert "`gone_helper`" in found[0][2]


def test_a_comment_reopened_on_its_closing_line_is_an_aside_again(tmp_path):
    """S11, #220's second shape. A remainder that BEGINS with `<!--` opens an
    aside again, so the name inside the reopened comment is not a claim.
    Seen red against `c52e8350`, which ended the aside at the whole closing
    line and then read the reopened comment's name as prose."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"plan.md": "# p\n\n<!-- a\nb --> <!-- c\n`gone_helper`\n-->\n"},
    )
    assert refusals(tmp_path) == ([], 0)


def test_a_claim_after_a_one_line_comment_is_read(tmp_path):
    """The same position rule on one line: a comment that opens at the start
    and closes on the line hands its remainder back as text. The comment's
    own name stays an aside."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"plan.md": "# p\n\n<!-- `inside_a_note` --> then `gone_helper`\n"},
    )
    found, read = refusals(tmp_path)
    assert read == 1, (found, read)
    assert "`gone_helper`" in found[0][2]


def test_a_shorter_fence_does_not_close_a_longer_one(tmp_path):
    """S12. A ```` ```` ```` block quoting a ```` ``` ```` block is one
    quotation: the inner delimiter is shorter than the opener, so it closes
    nothing (CommonMark 4.5, and the shared rule `fence_rule` asks). Seen red
    against `c52e8350`, whose three-character mark closed the outer block on
    the inner ```` ```markdown ```` and read the quoted name as prose."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{
            "rounds__round-1.md": "# r\n\n````\n```markdown\n`gone_helper`\n```\n"
            "````\n\nprose after the fence\n"
        },
    )
    assert refusals(tmp_path) == ([], 0)


def test_a_mid_line_comment_is_read_with_its_text(tmp_path):
    """`questions.md` Q1 of work item 1790260566, pinned at its default: a
    comment that opens part-way along text is NOT an aside, so a name in it
    is read — a false refusal a person sees and answers with the marker.
    Reading it as an aside needs a positional scanner with code-span state,
    and `skills/evidence-check/SKILL.md` §*What counts as a claim* says so."""
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"plan.md": "# p\n\n| a row | text <!-- `gone_helper` --> |\n"},
    )
    found, read = refusals(tmp_path)
    assert read == 1, (found, read)
    assert [s for s, _, _ in found] == ["NOT-IN-TREE"], found


# --- the boundary says what it did not read (round 1, 🟡 6) ------------------


def test_a_work_item_with_no_fragment_is_counted_as_unread(tmp_path):
    h = home(tmp_path)
    work_item(h, "1780000000-live", **{"spec.md": "# a\n"})
    work_item(h, "1770000000-shipped", fragment=False, **{"spec.md": "# b\n"})
    assert module().unread_items(str(h)) == ["1770000000-shipped"]


def test_the_run_says_how_many_work_items_it_did_not_read(tmp_path):
    """`0 names read` and exit 0 is the same output for *every record is
    clean* and *no record was opened*, and this arm's own work item sat in
    the second state through five of its six phases."""
    h = home(tmp_path)
    work_item(h, "1780000000-unwritten", fragment=False, **{"spec.md": "# a\n"})
    got = run(["."], tmp_path)
    assert got.returncode == 0, got.stdout + got.stderr
    assert "0 work items read · 1 unread · 0 names read" in got.stdout, got.stdout


def test_a_fragment_named_only_md_is_not_a_work_item(tmp_path):
    """`seal/ledger/.md` leaves the id empty, `os.path.join(specs, "")` is
    `specs/` itself and `isdir` says yes — so the whole records tree became
    one live work item and every shipped record in it was read."""
    h = home(tmp_path)
    work_item(
        h, "1770000000-shipped", fragment=False, **{"plan.md": "# `gone_helper`\n"}
    )
    (h / "ledger" / ".md").write_text("rows\n", encoding="utf-8")
    assert module().unshipped(str(h)) == {}
    assert refusals(tmp_path) == ([], 0)


# --- what `main` hands the arm ----------------------------------------------


def test_an_external_anchor_in_a_record_is_exit_0_as_it_is_in_a_ledger(tmp_path):
    """`EXTERNAL` is what a coordinate reads in a repository that has
    DECLARED cross-repo intent, and `SKILL.md` documents it at exit 0.
    Counting it as a refusal made a migration repository's records fail for
    the state its parity config exists to allow."""
    h = home(tmp_path)
    (h / "parity.md").write_text("| Original | somewhere |\n", encoding="utf-8")
    work_item(
        h,
        "1780000000-live",
        **{"overview.md": "# o\n\n`legacy/mod.py#handler@deadbeef`\n"},
    )
    findings, _names, stamps = module().check_records(str(tmp_path), str(h))
    assert stamps == 1
    assert [s for s, _, _ in findings] == ["EXTERNAL"], findings
    got = run(["."], tmp_path)
    assert got.returncode == 0, got.stdout + got.stderr
    assert "0 refused · 0 drifted · 1 external" in got.stdout, got.stdout


def test_two_stamps_of_one_unit_on_one_line_are_two_stamps(tmp_path):
    """`check_text` dedupes a repeated anchor, so counting what it RETURNS
    counted findings: one line stamping a unit twice read as one stamp, and
    the number beside a refusal was never the number of stamps."""
    h = home(tmp_path)
    tree(tmp_path, **{"src__service.py": SERVICE})
    work_item(
        h,
        "1780000000-live",
        **{
            "overview.md": f"# o\n\n`src/service.py#handler@{GOOD}` twice: "
            f"`src/service.py#handler@{GOOD}`\n"
        },
    )
    findings, _names, stamps = module().check_records(str(tmp_path), str(h))
    assert (findings, stamps) == ([], 2)


# --- the corpus guards, each with an observer (round 1, 🟡 7) ----------------


def test_a_deleted_name_surviving_in_the_git_directory_is_not_a_name(tmp_path):
    """`.git` is where every deleted version of every file lives, so a walk
    that read it would answer *the tree still has this* for a name the tree
    lost. Constructed without `git init`, so `SKIP_DIRS` is what refuses it
    rather than the index."""
    h = home(tmp_path)
    tree(tmp_path, **{".git__objects__pack__loose.txt": "gone_helper\n"})
    work_item(h, "1780000000-live", **{"plan.md": "# p\n\n`gone_helper`\n"})
    found, _read = refusals(tmp_path)
    assert [s for s, _, _ in found] == ["NOT-IN-TREE"], found


def test_a_broken_stamps_hint_does_not_point_into_a_vendored_package(tmp_path):
    """The scan looks for where a unit WENT, and a cache or a vendored
    package is the one place it cannot have gone. A hint reading `same name
    at .venv/lib/site-packages/pkg/a.py` sends the reader somewhere the
    repository does not own, and it is what made `SKIP_DIRS`' own comment —
    *directories no walk in this file descends* — false."""
    h = home(tmp_path)
    tree(tmp_path, **{".venv__lib__pkg__service.py": "def handler(x):\n    return x\n"})
    work_item(
        h,
        "1780000000-live",
        **{"overview.md": "# o\n\n`src/service.py#handler@deadbeef`\n"},
    )
    findings, _names, _stamps = module().check_records(str(tmp_path), str(h))
    assert [s for s, _, _ in findings] == ["BROKEN"], findings
    assert ".venv" not in findings[0][2], findings[0][2]


def test_a_file_over_the_size_cap_supplies_no_name(tmp_path):
    """A minified bundle or a lockfile is megabytes of tokens that name
    nothing anyone claims. Without the cap the run pays for reading them on
    every invocation, and the guard had no observer."""
    h = home(tmp_path)
    big = tmp_path / "bundle.min.js"
    big.write_text(
        "x" * (module().NAME_FILE_CAP + 1) + "\ngone_helper\n", encoding="utf-8"
    )
    work_item(h, "1780000000-live", **{"plan.md": "# p\n\n`gone_helper`\n"})
    found, _read = refusals(tmp_path)
    assert [s for s, _, _ in found] == ["NOT-IN-TREE"], found


def test_the_corpus_does_not_fold_case(tmp_path):
    """`Gone_Helper` and `gone_helper` are two identifiers in every language
    this reads, and a corpus that folded case would answer for one when the
    tree carries the other."""
    h = home(tmp_path)
    tree(tmp_path, **{"mod.py": "def gone_helper():\n    return 1\n"})
    work_item(h, "1780000000-live", **{"plan.md": "# p\n\n`Gone_Helper`\n"})
    found, _read = refusals(tmp_path)
    assert [s for s, _, _ in found] == ["NOT-IN-TREE"], found
    assert "`Gone_Helper`" in found[0][2]


def test_a_record_that_cannot_be_read_is_named(tmp_path, monkeypatch):
    """The status had no case at all. Constructed by refusing the read rather
    than by `chmod 000`, which is nothing to root and sets only a read-only
    flag on Windows — `test_gates_do_not_fail_open.py` makes the same choice
    for the same reason."""
    mod = module()
    h = home(tmp_path)
    work_item(h, "1780000000-live", **{"plan.md": "# p\n"})
    monkeypatch.setattr(mod, "read", lambda path: None)
    findings, names, stamps = mod.check_records(str(tmp_path), str(h))
    assert (names, stamps) == (0, 0)
    assert [s for s, _, _ in findings] == [mod.UNREADABLE_STATUS], findings
    assert findings[0][2] == "the record could not be read"


def refuses_scandir(mod, monkeypatch, tail):
    """`os.scandir` raising for one directory, and answering for the rest.

    Not `chmod 000`, which is nothing to root and sets only a read-only flag
    on Windows — `test_gates_do_not_fail_open.py` makes the same call, and a
    defence resting on a platform guarantee is not verified until the
    guarantee is gone.
    """
    real = os.scandir

    def refuses(path=".", *args, **kwargs):
        if str(path).replace(os.sep, "/").endswith(tail):
            raise PermissionError(13, "Permission denied", str(path))
        return real(path, *args, **kwargs)

    monkeypatch.setattr(mod.os, "scandir", refuses)


def test_a_records_directory_that_cannot_be_listed_is_named(tmp_path, monkeypatch):
    """`os.walk` swallows a directory it cannot list, so a work item whose
    `rounds/` is unreadable contributed no records and the run said nothing —
    exit 0, where an unreadable FILE is `UNREADABLE` and exit 2 (round 2,
    🟡 4)."""
    mod = module()
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"plan.md": "# p\n", "rounds__round-1.md": "# r\n\n`gone_helper`\n"},
    )
    refuses_scandir(mod, monkeypatch, "1780000000-live/rounds")
    findings, _names, _stamps = mod.check_records(str(tmp_path), str(h))
    assert [s for s, _, _ in findings] == [mod.UNREADABLE_STATUS], findings
    assert findings[0][2] == "the records directory could not be listed"
    assert findings[0][1].endswith("rounds"), findings


def test_a_ledger_fragment_directory_that_cannot_be_listed_is_named(
    tmp_path, monkeypatch
):
    """The same cause one directory up, and it silences the WHOLE arm rather
    than one work item: `unshipped` answered `{}` for a `ledger/` it could
    not list, so `check_records` returned nothing and the run exited 0."""
    mod = module()
    h = home(tmp_path)
    work_item(h, "1780000000-live", **{"plan.md": "# p\n\n`gone_helper`\n"})
    real = os.listdir

    def refuses(path=".", *args, **kwargs):
        if str(path).replace(os.sep, "/").endswith("seal/ledger"):
            raise PermissionError(13, "Permission denied", str(path))
        return real(path, *args, **kwargs)

    monkeypatch.setattr(mod.os, "listdir", refuses)
    findings, names, stamps = mod.check_records(str(tmp_path), str(h))
    assert (names, stamps) == (0, 0)
    assert [s for s, _, _ in findings] == [mod.UNREADABLE_STATUS], findings
    assert findings[0][2] == "the ledger fragments directory could not be listed"


def test_a_missing_ledger_folder_is_still_an_empty_answer(tmp_path):
    """The pair: `unshipped` distinguishes a directory that is ABSENT from
    one it cannot list, and only the second is a refusal. A root with no
    `ledger/` at all is a repository that has not started, not a broken one.
    """
    (tmp_path / "seal" / "specs").mkdir(parents=True)
    assert module().unshipped(str(tmp_path / "seal")) == {}
    assert module().check_records(str(tmp_path), str(tmp_path / "seal")) == ([], 0, 0)


def test_the_same_anchor_answers_the_same_in_both_arms_under_default_repo(tmp_path):
    """`--default-repo` reaches the records arm, the way it reaches the ledger.

    Both arms resolve an anchor through `check_text`, so a coordinate that
    grades `OK` in `seal/ledger.md` has to grade `OK` in a record stating the
    same thing. `main` handed the records arm `maps` and not `default_repo`
    (round 1, 🔴 1), so the identical anchor read `1 ok` from the ledger and
    `BROKEN` from the record — exit 2, with the cross-repo look-alike scan
    switched back on, which is a migration repository's CI failing on every
    invocation.
    """
    root = tmp_path / "repo"
    root.mkdir()
    original = tmp_path / "original"
    (original / "src").mkdir(parents=True)
    (original / "src" / "service.py").write_text(SERVICE, encoding="utf-8")
    h = home(root)
    anchor = f"src/service.py#handler@{GOOD}"
    work_item(h, "1780000000-live", **{"overview.md": f"# o\n\n`{anchor}`\n"})
    (h / "ledger" / "1780000000-live.md").write_text(
        f"| S1 | `{anchor}` | read | 2026-09-07 |\n", encoding="utf-8"
    )
    got = run([".", "--default-repo", str(original)], root)
    assert got.returncode == 0, got.stdout + got.stderr
    assert "1 ok · 0 drifted · 0 broken" in got.stdout, got.stdout
    assert "1 stamp read · 0 refused" in got.stdout, got.stdout
    assert "BROKEN" not in got.stdout, got.stdout


# --- seal/follow-up.md is read (#508) ----------------------------------------
#
# The permanent list of schedulable items names units, is addressed to a
# person, and is read months after it was written. Until #508 nothing read
# it: a row named a case in no file and was caught by grepping.


def follow_up(h, text):
    (h / "follow-up.md").write_text(text, encoding="utf-8")


FOLLOW_UP_ROW = (
    "# Follow-up\n\n| Item | Who |\n|---|---|\n| `invented_unit_name` | x |\n"
)


def test_a_follow_up_row_naming_a_unit_the_tree_lacks_is_refused(tmp_path):
    """F1 and F2. The file carries the name, and that is not evidence: it is
    out of the corpus, or the row would vouch for itself."""
    h = home(tmp_path)
    work_item(h, "1780000000-live", **{"plan.md": "# p\n"})
    follow_up(h, FOLLOW_UP_ROW)
    found, read = refusals(tmp_path)
    assert read == 1, found
    assert [(s, c.replace(os.sep, "/")) for s, c, _ in found] == [
        ("NOT-IN-TREE", "seal/follow-up.md:5")
    ], found
    for flags in ([], ["--strict"]):
        got = run([*flags, "."], tmp_path)
        assert got.returncode == 2, got.stdout + got.stderr
        assert "seal/follow-up.md:5" in got.stdout, got.stdout


def test_a_follow_up_name_another_file_carries_passes(tmp_path):
    """F2's other direction: out of the corpus is the follow-up file alone."""
    h = home(tmp_path)
    tree(tmp_path, **{"mod.py": "def invented_unit_name():\n    return 1\n"})
    follow_up(h, FOLLOW_UP_ROW)
    assert refusals(tmp_path) == ([], 1)


def test_the_follow_up_is_read_with_no_work_item_live(tmp_path):
    """F3. The file is permanent and its rows are live until removed, so the
    shipped boundary does not reach it: no `seal/ledger/` at all, and it is
    still read."""
    h = tmp_path / "seal"
    h.mkdir()
    follow_up(h, FOLLOW_UP_ROW)
    found, read = refusals(tmp_path)
    assert (read, [s for s, _, _ in found]) == (1, ["NOT-IN-TREE"]), found


def test_no_follow_up_is_nothing_to_read(tmp_path):
    """F4, first half: absent is the one quiet answer."""
    h = home(tmp_path)
    work_item(h, "1780000000-live", **{"plan.md": "# p\n\n`kept_helper`\n"})
    tree(tmp_path, **{"mod.py": "kept_helper = 1\n"})
    assert refusals(tmp_path) == ([], 1)


def test_a_follow_up_that_cannot_be_read_is_named(tmp_path):
    """F4, second half: a directory under the file's name is there and cannot
    be read, which is `UNREADABLE` and exit 2, the way a record is."""
    h = home(tmp_path)
    (h / "follow-up.md").mkdir()
    found, _read = refusals(tmp_path)
    assert [(s, c.replace(os.sep, "/")) for s, c, _ in found] == [
        ("UNREADABLE", "seal/follow-up.md")
    ], found
    got = run(["."], tmp_path)
    assert got.returncode == 2, got.stdout + got.stderr
    assert "seal/follow-up.md unreadable" in got.stdout, got.stdout


@pytest.mark.parametrize(
    "text, refused",
    [
        ("`invented_unit_name` NAME NOT IN TREE\n", False),
        ("```\n`invented_unit_name`\n```\n", False),
        ("<!-- `invented_unit_name` -->\n", False),
        ("<!--\n`invented_unit_name`\n-->\n", False),
        ("```\n`invented_unit_name`\n", True),
        ("<!-- open\n`invented_unit_name`\n", True),
    ],
    ids=[
        "marker",
        "closed-fence",
        "comment",
        "multi-line-comment",
        "unclosed-fence",
        "unclosed-comment",
    ],
)
def test_the_follow_up_is_read_by_the_records_own_claim_rules(tmp_path, text, refused):
    """F5. One reader for a record and the follow-up file, so the two cannot
    come to disagree about what a claim is."""
    h = home(tmp_path)
    follow_up(h, "# Follow-up\n\n" + text)
    found, _read = refusals(tmp_path)
    assert bool(found) is refused, found


def test_the_follow_up_is_read_and_left_out_of_the_corpus_in_local_mode(tmp_path):
    """F6. In local mode `seal/` sits under the git common directory; the
    file there is read, and it is out of the corpus, with shared mode's
    answers."""
    local = tmp_path / ".git" / "seal"
    local.mkdir(parents=True)
    follow_up(local, FOLLOW_UP_ROW)
    findings, read, _stamps = module().check_records(str(tmp_path), str(local))
    assert (read, [s for s, _, _ in findings]) == (1, ["NOT-IN-TREE"]), findings
    assert "follow-up.md:5" in findings[0][1], findings


def test_a_refusal_names_every_place_the_corpus_leaves_out(tmp_path):
    """F7. A reader told *nothing outside X carries this name* looks outside
    X, and naming two places of three sent them to the one that does."""
    h = home(tmp_path)
    work_item(h, "1780000000-live", **{"plan.md": "# p\n\n`gone_helper`\n"})
    found, _read = refusals(tmp_path)
    assert (
        found[0][2]
        .replace(os.sep, "/")
        .startswith(
            "`gone_helper` — nothing outside seal/specs, seal/ledger and "
            "seal/follow-up.md carries this name. Correct the record, or write "
            "NAME NOT IN TREE on the line where the record means a name the tree "
            "does not have"
        )
    ), found


def test_the_summary_line_says_whether_the_follow_up_was_read(tmp_path):
    """F7. `0 refused` says the same thing for *read and clean* and *never
    opened*, so the line says which, and the heading names the file."""
    h = home(tmp_path)
    got = run(["."], tmp_path)
    assert got.returncode == 0, got.stdout + got.stderr
    assert module().RECORDS_HEADING in got.stdout, got.stdout
    assert "seal/follow-up.md" in module().RECORDS_HEADING
    assert "0 external · no seal/follow-up.md\n" in got.stdout, got.stdout
    follow_up(h, "# Follow-up\n")
    got = run(["."], tmp_path)
    assert got.returncode == 0, got.stdout + got.stderr
    assert "0 external · seal/follow-up.md read\n" in got.stdout, got.stdout


# --- a name written as `path#name` is checked (#508) --------------------------
#
# `RECORD_NAME_RE` needs the whole backticked span to be an identifier, so a
# name written the way a coordinate is written was skipped inside the very
# records that were read.

MOD = (
    "class Kept:\n"
    "    def open(self):\n"
    "        return kept_helper()\n"
    "\n"
    "\n"
    "def kept_helper():\n"
    "    return 1\n"
)


def coordinate_refusals(tmp_path, line, where="record"):
    """(findings, names read, stamps read) for one line in a live record or
    in `seal/follow-up.md`, over a tree holding `src/mod.py` and nothing
    else."""
    h = home(tmp_path)
    tree(tmp_path, **{"src__mod.py": MOD})
    if where == "record":
        work_item(h, "1780000000-live", **{"plan.md": f"# p\n\n{line}\n"})
    else:
        work_item(h, "1780000000-live", **{"plan.md": "# p\n"})
        follow_up(h, f"# Follow-up\n\n{line}\n")
    return module().check_records(str(tmp_path), str(h))


@pytest.mark.parametrize("where", ["record", "follow-up"])
@pytest.mark.parametrize(
    "span, missing",
    [
        ("src/mod.py#invented_unit_name", "invented_unit_name"),
        ("src/mod.py#invented_unit_name()", "invented_unit_name"),
        ("src/mod.py#Kept.invented_method", "invented_method"),
    ],
    ids=["name", "call", "dotted"],
)
def test_a_coordinate_form_name_the_named_file_lacks_is_refused(
    tmp_path, where, span, missing
):
    """P1 and P7: refused, the detail naming the path and the segment, and
    the span counted in `names read`."""
    findings, names, stamps = coordinate_refusals(tmp_path, f"see `{span}`", where)
    assert (names, stamps) == (1, 0), findings
    assert [s for s, _, _ in findings] == ["NOT-IN-TREE"], findings
    assert findings[0][1].endswith(":3"), findings
    assert findings[0][2].startswith(
        f"`{span.rstrip('()')}` — `{missing}` is not a token of src/mod.py, "
        "the file the path names. Correct the record, or write NAME NOT IN "
        "TREE on the line"
    ), findings


def test_a_coordinate_form_name_the_named_file_carries_passes(tmp_path):
    """P2, the passing direction, dotted and called forms included."""
    line = "`src/mod.py#kept_helper` and `src/mod.py#Kept.open()`"
    assert coordinate_refusals(tmp_path, line) == ([], 2, 0)


def test_a_name_only_another_file_carries_is_refused_under_the_path(tmp_path):
    """P2: #508's own instance was a case named under a file that has no such
    case. Another file carrying the name is not evidence for this one."""
    tree(tmp_path, **{"src__other.py": "def elsewhere_only():\n    return 2\n"})
    findings, names, _ = coordinate_refusals(tmp_path, "`src/mod.py#elsewhere_only`")
    assert names == 1
    assert [s for s, _, _ in findings] == ["NOT-IN-TREE"], findings


def test_a_one_word_name_under_a_resolving_path_is_a_claim(tmp_path):
    """P3: the path is what makes the span a claim, so the underscore
    narrowing that keeps a single backticked word out does not apply."""
    findings, names, _ = coordinate_refusals(tmp_path, "`src/mod.py#Zork`")
    assert names == 1
    assert [s for s, _, _ in findings] == ["NOT-IN-TREE"], findings


@pytest.mark.parametrize(
    "path",
    ["mod.py", "src/gone.py", "../out.py"],
    ids=["bare-file-name", "missing-file", "escapes-the-root"],
)
def test_an_unresolved_path_reads_its_name_as_a_bare_name(tmp_path, path):
    """P4: the name half is read exactly as the same name written bare, the
    compound rule against the whole corpus. A one-word name is not read."""
    findings, names, _ = coordinate_refusals(
        tmp_path, f"`{path}#invented_unit_name` and `{path}#Zork`"
    )
    assert names == 1, findings
    assert [s for s, _, _ in findings] == ["NOT-IN-TREE"], findings
    assert findings[0][2].startswith(
        f"`{path}#invented_unit_name` — {path} resolves to no file here, so "
        "`invented_unit_name` is read as a bare name, and nothing outside "
    ), findings


def test_an_unresolved_path_with_a_name_the_corpus_carries_passes(tmp_path):
    """P4, the passing direction: a bare file name with a name some file has."""
    assert coordinate_refusals(tmp_path, "`mod.py#kept_helper`") == ([], 1, 0)


def test_a_stamped_span_is_a_stamp_and_not_a_name(tmp_path):
    """P5: `@hash` makes the span the stamp half's, and it is counted once."""
    findings, names, stamps = coordinate_refusals(
        tmp_path, "`src/mod.py#kept_helper@00000000`"
    )
    assert (names, stamps) == (0, 1), findings
    assert [s for s, _, _ in findings] == ["DRIFTED"], findings


@pytest.mark.parametrize(
    "text",
    [
        "`src/mod.py#invented_unit_name` NAME NOT IN TREE",
        "```\n`src/mod.py#invented_unit_name`\n```",
        "<!-- `src/mod.py#invented_unit_name` -->",
    ],
    ids=["marker", "closed-fence", "comment"],
)
def test_the_coordinate_form_takes_the_claim_rules(tmp_path, text):
    """P6: the same lines `claim_lines` reads, and no others."""
    assert coordinate_refusals(tmp_path, text)[0] == []


def test_a_cross_repo_name_is_not_read_where_its_stamp_is_external(tmp_path):
    """Round 1 of 1790635414, 🟡 2. In a repository that declared another
    checkout, a path under a top-level directory this tree does not have is
    `EXTERNAL` to the stamp half at exit 0, and the name half must not refuse
    it. A missing file under a directory the tree does have is still read."""
    h = home(tmp_path)
    (h / "parity.md").write_text("# parity\n", encoding="utf-8")
    tree(tmp_path, **{"src__mod.py": MOD})
    work_item(
        h,
        "1780000000-live",
        **{
            "plan.md": "# p\n\n"
            "Ports `legacy/src/service.py#get_user_by_id`.\n"
            "Stamped `legacy/src/service.py#get_user_by_id@abcdef12`.\n"
            "And `src/gone.py#invented_unit_name`.\n"
        },
    )
    findings, names, stamps = module().check_records(str(tmp_path), str(h))
    assert (names, stamps) == (1, 1), findings
    assert [(s, c.replace(os.sep, "/")[-9:]) for s, c, _ in findings] == [
        ("NOT-IN-TREE", "plan.md:5"),
        ("EXTERNAL", "plan.md:4"),
    ], findings


def test_a_heading_fragment_and_a_line_anchor_are_not_refused(tmp_path):
    """Round 1 of 1790635414, 🟡 3. After a `.md` path the fragment is
    GitHub's heading anchor, which lower-cases the heading's words; a
    `#L120` line anchor names no unit. A word the file does not carry after
    the same path is still refused."""
    tree(tmp_path, **{"README.md": "# Tool\n\n## Install\n\nRun it.\n"})
    findings, names, _ = coordinate_refusals(
        tmp_path,
        "Setup is in `README.md#install`, entry at `src/mod.py#L1`, "
        "and `README.md#uninstall`.",
    )
    assert names == 2, findings
    assert [s for s, _, _ in findings] == ["NOT-IN-TREE"], findings
    assert "`uninstall`" in findings[0][2], findings


def test_a_heading_anchor_github_strips_punctuation_from_is_not_refused(tmp_path):
    """Round 2 of 1790635414, 🟡 7. GitHub's anchor drops every character of a
    heading but letters, digits, `_`, `-` and spaces, so `## Don't` is
    `#dont`, a code-span heading `evidence_check.py` is `#evidence_checkpy`
    and `## v1.2` is `#v12`: none is a word of the file, lower-cased or not.
    An invented anchor is still refused, and so is the anchor of a `#` line
    inside a fence, which GitHub does not read as a heading."""
    tree(
        tmp_path,
        **{
            "README.md": "# Tool\n\n## Don't\n\n## `evidence_check.py`\n\n## v1.2\n\n"
            "```\n# Fenced's\n```\n"
        },
    )
    findings, names, _ = coordinate_refusals(
        tmp_path,
        "See `README.md#dont`, `README.md#evidence_checkpy`, `README.md#v12`, "
        "`README.md#fenceds` and `README.md#uninstall`.",
    )
    assert names == 5, findings
    assert [d.split(" — ")[0] for _, _, d in findings] == [
        "`README.md#fenceds`",
        "`README.md#uninstall`",
    ], findings


def test_a_heading_github_renders_before_it_slugs_is_not_refused(tmp_path):
    """Round 3 of 1790635414, 🟡 9. GitHub slugs a heading's rendered text
    and anchors a setext heading and one inside a blockquote, so each of
    these is a real anchor of the file: a setext `Don't`, a quoted `Won't`,
    an emphasised `Note`, a linked code span, a word glued to an inline tag
    and an entity, none of them a word of the file lower-cased. An invented
    anchor is still refused."""
    tree(
        tmp_path,
        **{
            "README.md": "# Tool\n\nDon't\n-----\n\n> ## Won't\n\n## _Note_\n\n"
            "## [`evidence_check.py`](a.py)\n\n## Press<kbd>Esc</kbd>\n\n"
            "## Isn&#39;t\n"
        },
    )
    findings, names, _ = coordinate_refusals(
        tmp_path,
        "See `README.md#dont`, `README.md#wont`, `README.md#note`, "
        "`README.md#evidence_checkpy`, `README.md#pressesc`, `README.md#isnt` "
        "and `README.md#uninstall`.",
    )
    assert names == 7, findings
    assert [d.split(" — ")[0] for _, _, d in findings] == ["`README.md#uninstall`"], (
        findings
    )


# --- this repository's own records ------------------------------------------


def test_this_repositorys_own_records_state_nothing_the_tree_lacks():
    """The measurement #190 was opened for, run against the tree itself.

    Four occurrences of one name in work item `1788749195`'s round records —
    the instance that work item's own round 3 found by READING, three weeks of
    records later. This is what a check names at the commit that writes it.

    **What the tree LACKS is the bar, which is the arm's own grading and not
    everything the arm prints.** `main` counts a refusal as anything that is
    neither DRIFTED nor EXTERNAL, and the comment beside it gives the reason:
    a live work item's branch is editing the very units its records stamp, so
    failing on drift is red by construction. Asserting the whole list made
    this case stricter than the tool it measures, and #84 is where that came
    due — one record quoting the hash `COVERED` held before the same branch
    changed it, beside the new hash, which is the record doing its job. The
    `ledger` CI job rendered that as a warning and this case failed the same
    tree on all three platforms. A name the tree does not carry stays fatal
    here, and so does a broken anchor: both count refused, above and in
    `main`.
    """
    findings, _names, _stamps = module().check_records(ROOT, os.path.join(ROOT, "seal"))
    refused = [f for f in findings if f[0] not in ("DRIFTED", "EXTERNAL")]
    assert refused == [], "\n".join(f"{c}  {d}" for _s, c, d in refused)


def test_a_built_coordinate_prints_with_forward_slashes_on_windows():
    """The records arm builds every path it prints, so it normalises them.

    `display_name` returns the caller's own spelling, which is right for a
    `--ledger` pattern and wrong for a coordinate this arm built out of
    `os.walk` and `os.path.join`: on Windows that carries `\\`, while the
    ledger arm's rows carry `/` because they were read from a file, and the
    same coordinate then reads two ways depending on which arm printed it.

    **Seen red the only way this one can be**: the Windows leg of CI was red
    on `assert coord.endswith("rounds/round-2.md:3")` from the commit that
    added this arm through three review rounds and two fix passes, because
    every round and every broad gate ran on macOS where the replacement is a
    no-op. `ntpath` is what removes that guarantee from a POSIX machine
    (`agent-contract` §13); with the `.replace` deleted this case returns
    `seal\\specs\\1780000000-live\\rounds\\round-2.md` and fails.
    """
    built = module().built_name
    assert (
        built(
            r"C:\proj\seal\specs\1780000000-live\rounds\round-2.md",
            r"C:\proj",
            flavour=ntpath,
        )
        == "seal/specs/1780000000-live/rounds/round-2.md"
    )
    # A path the root does not cover comes back whole, and still with `/`:
    # length is what a miss costs, never a separator a reader cannot paste.
    assert built(r"D:\other\seal\specs\x\plan.md", r"C:\proj", flavour=ntpath) == (
        "D:/other/seal/specs/x/plan.md"
    )


# --- a frame's `## Removes` section, read as claims of absence (#835) ---------

REMOVES_HEAD = (
    "# frame\n\n## Removes\n\n"
    "| Removes | Coordinate | Where it lands, or why it can go |\n"
    "|---|---|---|\n"
)
REMOVES_TAIL = "\n## Open questions\n\nnone\n"


def frame(tmp_path, rows, item="1780000000-live"):
    """A live work item whose `spec.md` carries a `## Removes` section of ROWS
    (whole lines), and the arm's findings over it."""
    h = home(tmp_path)
    work_item(h, item, **{"spec.md": REMOVES_HEAD + rows + REMOVES_TAIL})
    found, _ = refusals(tmp_path)
    return found


def test_a_named_removal_that_still_stands_is_standing(tmp_path):
    """S1. A row whose coordinate resolves at HEAD names a removal that has
    not happened."""
    tree(tmp_path, **{"mod.py": "def old_reader():\n    return 1\n"})
    found = frame(tmp_path, "| the old reader | `mod.py#old_reader` | gone |\n")
    assert [(s, c.replace(os.sep, "/")[-9:]) for s, c, _ in found] == [
        ("STANDING", "spec.md:7")
    ]
    assert found[0][2] == (
        "`mod.py#old_reader` still resolves at 1-2, so the removal this row "
        "names has not happened — take it out of the tree, or correct the row"
    )


def test_a_standing_removal_fails_the_run_like_a_stated_name_the_tree_lacks(
    tmp_path,
):
    """S1. Graded as NOT-IN-TREE is: exit 2 under either reading."""
    tree(tmp_path, **{"mod.py": "def old_reader():\n    return 1\n"})
    frame(tmp_path, "| the old reader | `mod.py#old_reader` | gone |\n")
    r = run(["."], tmp_path)
    assert r.returncode == 2, r.stdout + r.stderr
    assert "STANDING" in r.stdout and "1 refused" in r.stdout


@pytest.mark.parametrize(
    "coordinate",
    [
        "mod.py#old_reader",
        "gone.py#anything",
        'notes.md#"## Gone heading"',
        'mod.py#kept>"return 2"',
    ],
)
def test_a_removal_that_happened_is_no_finding(tmp_path, coordinate):
    """S2. A unit gone from its file, a file gone, a heading gone, and a
    quoted line gone from a unit that stays: each is the claim holding."""
    tree(
        tmp_path,
        **{
            "mod.py": "def kept():\n    return 1\n",
            "notes.md": "# n\n\n## Kept\n\ntext\n",
        },
    )
    assert frame(tmp_path, f"| x | `{coordinate}` | y |\n") == []


@pytest.mark.parametrize("coordinate", ['notes.md#"## Kept"', 'mod.py#kept>"return 1"'])
def test_a_heading_or_a_quoted_line_still_there_is_standing(tmp_path, coordinate):
    """S1 for the two locators that are not a unit name."""
    tree(
        tmp_path,
        **{
            "mod.py": "def kept():\n    return 1\n",
            "notes.md": "# n\n\n## Kept\n\ntext\n",
        },
    )
    found = frame(tmp_path, f"| x | `{coordinate}` | y |\n")
    assert [s for s, _c, _d in found] == ["STANDING"]


def test_a_name_in_a_removes_row_is_not_read_by_the_name_half(tmp_path):
    """S2. Elsewhere in a record `mod.py#gone_helper` is a stated name the
    tree lacks; in the section it is the claim that it is gone."""
    tree(tmp_path, **{"mod.py": "def kept():\n    return 1\n"})
    rows = "| `gone_helper` | `mod.py#gone_helper` | `other_gone_name` |\n"
    assert frame(tmp_path, rows) == []
    (tmp_path / "seal" / "specs" / "1780000000-live" / "plan.md").write_text(
        "# p\n\n`mod.py#gone_helper`\n", encoding="utf-8"
    )
    found, _ = refusals(tmp_path)
    assert [s for s, _c, _d in found] == ["NOT-IN-TREE"]


@pytest.mark.parametrize(
    ("line", "refused"),
    [("nothing — the work only adds a check", False), ("nothing", True)],
)
def test_the_nothing_line_names_its_reason(tmp_path, line, refused):
    """S3."""
    h = home(tmp_path)
    work_item(h, "1780000000-live", **{"spec.md": f"# f\n\n## Removes\n\n{line}\n"})
    found, _ = refusals(tmp_path)
    if refused:
        assert [(s, d) for s, _c, d in found] == [
            (
                "REFUSED",
                "`nothing` — a `nothing` line names its reason: `nothing — <why>`",
            )
        ]
    else:
        assert found == []


def removes_config(tmp_path, value):
    (tmp_path / "seal").mkdir(exist_ok=True)
    (tmp_path / "seal" / "config.md").write_text(
        f"| Item | Value |\n|---|---|\n| Removes from | {value} |\n",
        encoding="utf-8",
    )


@pytest.mark.parametrize(
    ("cutoff", "item", "spec", "why"),
    [
        ("1780000000", "1780000000-bound", "# f\n\nno section\n", "has no"),
        (
            "1780000000",
            "1780000001-bound",
            "# f\n\n## Removes\n\n## Next\n",
            "has an empty",
        ),
        ("1780000000", "1770000000-older", "# f\n\nno section\n", None),
        (None, "1780000000-unbound", "# f\n\nno section\n", None),
    ],
    ids=["bound, absent", "bound, empty", "below the cutoff", "no row"],
)
def test_presence_is_required_at_or_above_the_cutoff(tmp_path, cutoff, item, spec, why):
    """S4, one root per branch."""
    h = home(tmp_path)
    if cutoff is not None:
        removes_config(tmp_path, cutoff)
    work_item(h, item, **{"spec.md": spec})
    found, _ = refusals(tmp_path)
    if why is None:
        assert found == []
        return
    assert len(found) == 1
    status, coord, detail = found[0]
    assert status == "REFUSED"
    assert coord.replace(os.sep, "/").endswith(f"{item}/spec.md")
    assert detail == (
        f"{why} `## Removes` section, and `Removes from` in seal/config.md binds "
        "this work item — name what the work removes, in the ledger's grammar "
        "without a hash, or write `nothing — <why>`"
    )


def test_a_section_below_the_cutoff_is_still_read_where_present(tmp_path):
    """S4. Not required is not unread."""
    tree(tmp_path, **{"mod.py": "def old_reader():\n    return 1\n"})
    removes_config(tmp_path, "1790000000")
    found = frame(tmp_path, "| r | `mod.py#old_reader` | gone |\n")
    assert [s for s, _c, _d in found] == ["STANDING"]


@pytest.mark.parametrize(
    ("cell", "detail"),
    [
        (
            '<path#unit, or path#"heading">',
            '`<path#unit, or path#"heading">` is not a coordinate — write '
            '`path#unit`, `path#"## heading"` or `path#"a quoted line"`',
        ),
        (
            "`tests/test_x.py::test_y`",
            "`tests/test_x.py::test_y` is a test's node id, which names a test "
            'and no unit — write `path#unit`, `path#"## heading"` or '
            '`path#"a quoted line"`',
        ),
    ],
    ids=["the template's placeholder", "a node id"],
)
def test_a_cell_that_is_no_coordinate_is_refused_naming_the_row(tmp_path, cell, detail):
    """S5."""
    found = frame(tmp_path, f"| x | {cell} | y |\n")
    assert [(s, c.replace(os.sep, "/")[-9:], d) for s, c, d in found] == [
        ("REFUSED", "spec.md:7", detail)
    ]


def test_a_bare_symbol_no_rule_bounds_is_refused_never_read_as_gone(tmp_path):
    """S5. `f.ts#bar` would read as a removal that happened if `resolve_unit`'s
    empty places were taken at their word; its `refused` sentence is the
    answer, and it is `unbounded`'s, pinned in
    `tests/test_a_unit_the_extractor_cannot_bound_is_refused.py`."""
    tree(tmp_path, **{"f.ts": "function bar() {}\n"})
    found = frame(tmp_path, "| x | `f.ts#bar` | y |\n")
    unbounded = module().unbounded("f.ts", None, "")
    assert [(s, d) for s, _c, d in found] == [("REFUSED", f"`f.ts#bar` — {unbounded}")]


def test_a_coordinate_that_does_not_read_is_refused_never_read_as_gone(tmp_path):
    """S5, round 1 of #835 (🟡 2). `place` refuses a path out of the tree,
    and a directory will not read; neither is a removal that happened, so
    each is refused naming the row. A file the tree does not have is still
    the claim holding."""
    root = tmp_path / "r"
    tree(root, **{"pkg__sub.d__x.py": "def g():\n    return 1\n"})
    (tmp_path / "outside.py").write_text("def f():\n    return 1\n", encoding="utf-8")
    h = home(root)
    rows = (
        "| x | `../outside.py#f` | y |\n"
        "| x | `pkg/sub.d#g` | y |\n"
        "| x | `pkg/gone.py#g` | y |\n"
    )
    work_item(h, "1780000000-live", **{"spec.md": REMOVES_HEAD + rows + REMOVES_TAIL})
    found, _ = refusals(root)
    assert [(s, d) for s, _c, d in found] == [
        (
            "REFUSED",
            "`../outside.py#f` — the path escapes the repository, so nothing it "
            "names can be read as gone — write a path inside the tree",
        ),
        (
            "REFUSED",
            "`pkg/sub.d#g` — the path is there and will not read as a file, so "
            "nothing in it can be read as gone",
        ),
    ]


def test_a_removal_is_read_in_this_tree_never_in_another_checkout(tmp_path):
    """S1/S2, round 2 of #835. A row is a claim about HEAD: one the original
    still holds is a removal that happened here, and one in a mapped checkout
    is refused rather than read as gone."""
    root = tmp_path / "r"
    tree(root, **{"kept.py": "def k():\n    return 1\n"})
    orig = tmp_path / "orig"
    tree(orig, **{"old.py": "def k():\n    return 1\n"})
    h = home(root)
    rows = "| x | `old.py#k` | y |\n| x | `legacy/a.py#k` | y |\n"
    work_item(h, "1780000000-live", **{"spec.md": REMOVES_HEAD + rows + REMOVES_TAIL})
    found, _read, _stamps = module().check_records(
        str(root), str(root / "seal"), {"legacy": str(tmp_path / "absent")}, str(orig)
    )
    assert [(s, d) for s, _c, d in found] == [
        (
            "REFUSED",
            "`legacy/a.py#k` — the path names another checkout through `--map`, "
            "and a frame names what its work removes from this tree — write the "
            "path in this tree, as `./legacy/a.py` where this tree's own "
            "directory carries the map's name",
        )
    ]


@pytest.mark.parametrize(
    ("coordinate", "status"),
    [
        ("kept.py/#k", "REFUSED"),
        ("kept.py/.#k", "REFUSED"),
        ("sub//kept.py#k", "REFUSED"),
        ("./legacy/kept.py#k", "STANDING"),
    ],
)
def test_a_path_spelled_another_way_is_refused_never_read_as_gone(
    tmp_path, coordinate, status
):
    """Round 3 of #835, ⬜ 2 and ⬜ 1, as the broad gate left them. A trailing
    `/` or `/.`, or an empty segment, names a file by a spelling the read does
    not use, and a lexical fold would name another file through a symlink
    (#163), so it is refused rather than read as gone. A leading `./` is the
    spelling the `--map` refusal names, and it reads the row in this tree."""
    tree(
        tmp_path,
        **{
            "kept.py": "def k():\n    return 1\n",
            "legacy__kept.py": "def k():\n    return 1\n",
        },
    )
    h = home(tmp_path)
    rows = f"| x | `{coordinate}` | y |\n"
    work_item(h, "1780000000-live", **{"spec.md": REMOVES_HEAD + rows + REMOVES_TAIL})
    found, _read, _stamps = module().check_records(
        str(tmp_path), str(tmp_path / "seal"), {"legacy": str(tmp_path / "absent")}
    )
    assert [s for s, _c, _d in found] == [status]
    if status == "REFUSED":
        assert found[0][2] == (
            f"`{coordinate}` — the path carries an empty or `.` segment, so it "
            "names the file by a spelling the tree does not use — write the "
            "path as the tree spells it"
        )


def test_a_path_through_dot_dot_is_refused_never_read_as_gone(tmp_path):
    """Round 2 of #835, ⬜ 2. `missing/../kept.py` stays inside the tree by
    name, and the read goes through `missing`, so it would read as gone while
    `kept.py` holds the unit; a path through `..` is refused instead."""
    tree(tmp_path, **{"kept.py": "def k():\n    return 1\n"})
    found = frame(tmp_path, "| x | `missing/../kept.py#k` | y |\n")
    assert [(s, d) for s, _c, d in found] == [
        (
            "REFUSED",
            "`missing/../kept.py#k` — the path walks through `..`, so whether it "
            "names a file depends on the directories it passes — write the path "
            "as the tree spells it",
        )
    ]


@pytest.mark.parametrize(
    "wrap",
    [("```\n", "```\n"), ("<!--\n", "-->\n")],
    ids=["a fence", "an html comment"],
)
def test_a_quoted_section_is_not_read(tmp_path, wrap):
    """S7. A section inside a fence or a comment is an example."""
    tree(tmp_path, **{"mod.py": "def old_reader():\n    return 1\n"})
    h = home(tmp_path)
    opener, closer = wrap
    section = REMOVES_HEAD.split("\n", 2)[2] + "| r | `mod.py#old_reader` | gone |\n"
    work_item(
        h, "1780000000-live", **{"spec.md": "# f\n\n" + opener + section + closer}
    )
    found, _ = refusals(tmp_path)
    assert found == []


def test_the_section_is_read_only_in_a_frame(tmp_path):
    """A `## Removes` heading in another record is that record's prose; the
    frame's own file is the one place the section is a claim."""
    tree(tmp_path, **{"mod.py": "def old_reader():\n    return 1\n"})
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"plan.md": REMOVES_HEAD + "| r | `mod.py#old_reader` | gone |\n"},
    )
    found, _ = refusals(tmp_path)
    assert found == []


# --- a line under `## Removes` that is neither a row nor a `nothing` line (#905)

REMOVES_TABLE = (
    "| Removes | Coordinate | Where it lands, or why it can go |\n"
    "|---|---|---|\n"
    "| x | `gone.py#x` | y |\n"
)


def off_shape(line):
    """The refusal of an off-shape LINE under `## Removes`, whole (§14)."""
    return (
        f"`{line}` — a line under `## Removes` is a table row or "
        "`nothing — <why>`; prose about the rows goes under a sub-heading "
        "after the table, such as `### Why these rows`"
    )


@pytest.mark.parametrize("required", [False, True], ids=["unrequired", "required"])
@pytest.mark.parametrize(
    ("body", "number", "line"),
    [
        (
            REMOVES_TABLE + "- `mod.py#old_reader` goes too\n",
            8,
            "- `mod.py#old_reader` goes too",
        ),
        (
            REMOVES_TABLE + "The reader above goes because nothing calls it.\n",
            8,
            "The reader above goes because nothing calls it.",
        ),
        (
            REMOVES_TABLE + "Nothing — the rest of the work only adds a check\n",
            8,
            "Nothing — the rest of the work only adds a check",
        ),
        (
            "nothing — the work only adds a check and\nkeeps every reader it had\n",
            6,
            "keeps every reader it had",
        ),
    ],
    ids=["a bullet", "a prose line", "a capitalised Nothing", "a wrapped reason"],
)
def test_an_off_shape_line_under_removes_is_refused_naming_it(
    tmp_path, required, body, number, line
):
    """S1 of #905. A line the section's two shapes do not cover is refused at
    its line, naming it, beside a row or a `nothing` line, whether or not a
    cutoff binds the frame — never dropped unread, which is what made the
    four `unknown refused` words false. The run exits 2."""
    tree(tmp_path, **{"mod.py": "def old_reader():\n    return 1\n"})
    h = home(tmp_path)
    if required:
        removes_config(tmp_path, "1780000000")
    work_item(
        h,
        "1780000000-live",
        **{"spec.md": "# frame\n\n## Removes\n\n" + body + REMOVES_TAIL},
    )
    found, _ = refusals(tmp_path)
    assert [(s, c.replace(os.sep, "/").rsplit("/", 1)[-1], d) for s, c, d in found] == [
        ("REFUSED", f"spec.md:{number}", off_shape(line))
    ]
    r = run(["."], tmp_path)
    assert r.returncode == 2, r.stdout + r.stderr


def test_the_shapes_that_belong_under_removes_are_not_refused(tmp_path):
    """S2 of #905. The header and rule rows, a blank line, an HTML comment
    over two lines and a fenced block are no off-shape line."""
    body = (
        REMOVES_TABLE
        + "\n<!-- why the row above can go:\n     nothing reads it -->\n\n"
        + "```\n- a quoted bullet\n```\n"
    )
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"spec.md": "# frame\n\n## Removes\n\n" + body + REMOVES_TAIL},
    )
    found, _ = refusals(tmp_path)
    assert found == []


def test_a_required_section_holding_only_an_off_shape_line_is_refused_twice(tmp_path):
    """S3 of #905. The section is empty in today's words, and the line is
    refused naming it: neither finding stands in for the other."""
    h = home(tmp_path)
    removes_config(tmp_path, "1780000000")
    item = "1780000000-bound"
    work_item(
        h, item, **{"spec.md": "# frame\n\n## Removes\n\n- `mod.py#old_reader` goes\n"}
    )
    found, _ = refusals(tmp_path)
    assert [(s, c.replace(os.sep, "/").rsplit("/", 1)[-1], d) for s, c, d in found] == [
        (
            "REFUSED",
            "spec.md",
            "has an empty `## Removes` section, and `Removes from` in "
            "seal/config.md binds this work item — name what the work removes, "
            "in the ledger's grammar without a hash, or write `nothing — <why>`",
        ),
        ("REFUSED", "spec.md:5", off_shape("- `mod.py#old_reader` goes")),
    ]


@pytest.mark.parametrize("sub", ["### Why these rows", "### Removes"])
def test_a_heading_of_any_level_ends_the_section(tmp_path, sub):
    """M1 of #905. Prose about the rows goes under a sub-heading, which ends
    the section — a level-3 heading reading `Removes` opens none — so the
    prose is no off-shape line, and the name half reads it as it reads any
    record line: a removed unit named there is a stated name the tree
    lacks, unless the line carries the marker."""
    body = REMOVES_TABLE + f"\n{sub}\n\nThe `gone_helper` went with its caller.\n"
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"spec.md": "# frame\n\n## Removes\n\n" + body + REMOVES_TAIL},
    )
    found, _ = refusals(tmp_path)
    assert [(s, c.replace(os.sep, "/").rsplit("/", 1)[-1]) for s, c, _d in found] == [
        ("NOT-IN-TREE", "spec.md:11")
    ]


def strayed(line):
    """The refusal of a table row LINE under a sub-heading of `## Removes`."""
    return (
        f"`{line}` — a table row under a sub-heading of `## Removes` is not "
        "read as a removal; move it into the table above the sub-heading, or "
        "write it as prose"
    )


STANDING_ROW = "| y | `mod.py#old_reader` | z |"
GONE_ROW = "| y | `mod.py#gone_reader` | z |"


@pytest.mark.parametrize("required", [False, True], ids=["unrequired", "required"])
@pytest.mark.parametrize(
    ("tail", "number", "row"),
    [
        (STANDING_ROW + "\n", 11, STANDING_ROW),
        (REMOVES_HEAD.split("\n", 4)[4] + STANDING_ROW + "\n", 13, STANDING_ROW),
        ("Prose.\n\n### Phase 3\n\n" + STANDING_ROW + "\n", 15, STANDING_ROW),
        (GONE_ROW + "\n", 11, GONE_ROW),
    ],
    ids=[
        "a row alone",
        "a whole second table",
        "a row under a second sub-heading",
        "a row naming a unit that is gone",
    ],
)
def test_a_table_row_under_a_sub_heading_of_removes_is_refused(
    tmp_path, required, tail, number, row
):
    """Round 1 of #905, 🟡 1. The section ends at any heading so prose has a
    home, and a table row under that sub-heading — or under a later one,
    before the next level-2 heading — is refused naming it, never read by
    the name half alone, where a unit that still stands passes. A second
    table's header — the row its rule row follows — and that rule row are
    not refused; its body row is, once: the name half does not also read a
    gone name on it."""
    tree(tmp_path, **{"mod.py": "def old_reader():\n    return 1\n"})
    h = home(tmp_path)
    if required:
        removes_config(tmp_path, "1780000000")
    body = REMOVES_TABLE + "\n### Phase 2\n\n" + tail
    work_item(
        h,
        "1780000000-live",
        **{"spec.md": "# frame\n\n## Removes\n\n" + body + REMOVES_TAIL},
    )
    found, _ = refusals(tmp_path)
    assert [(s, c.replace(os.sep, "/").rsplit("/", 1)[-1], d) for s, c, d in found] == [
        ("REFUSED", f"spec.md:{number}", strayed(row))
    ]


@pytest.mark.parametrize(
    ("body", "expected"),
    [
        (
            REMOVES_TABLE + "- `mod.py#old_reader` goes too NAME NOT IN TREE\n",
            ("REFUSED", "spec.md:8"),
        ),
        (
            REMOVES_TABLE.replace(
                "`gone.py#x` | y", "`mod.py#old_reader` | y NAME NOT IN TREE"
            ),
            ("STANDING", "spec.md:7"),
        ),
    ],
    ids=["a marked bullet", "a marked row"],
)
def test_the_marker_exempts_no_line_of_the_removes_section(tmp_path, body, expected):
    """Round 1 of #905, 🟡 2. The marker exempts a line from the name half,
    and the section is not the name half's: a marked line under `## Removes`
    is read by the section's shapes like any other."""
    tree(tmp_path, **{"mod.py": "def old_reader():\n    return 1\n"})
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"spec.md": "# frame\n\n## Removes\n\n" + body + REMOVES_TAIL},
    )
    found, _ = refusals(tmp_path)
    assert [(s, c.replace(os.sep, "/").rsplit("/", 1)[-1]) for s, c, _d in found] == [
        expected
    ]


@pytest.mark.parametrize(
    ("body", "expected"),
    [
        (
            REMOVES_TABLE
            + "\n### Why these rows\n\n| Before | After |\n|---|---|\n| a | b |\n",
            [("REFUSED", "spec.md:13")],
        ),
        (
            REMOVES_TABLE + "\n### Phase 2\n\n| Removes | `mod.py#old_reader` | z |\n",
            [("REFUSED", "spec.md:11")],
        ),
        (
            REMOVES_TABLE.replace(
                "| x | `gone.py#x` |", "| Removes | `mod.py#old_reader` |"
            ),
            [("STANDING", "spec.md:7")],
        ),
    ],
    ids=[
        "a foreign table's header",
        "a row reading Removes under the sub-heading",
        "a row reading Removes in the section",
    ],
)
def test_a_header_is_the_row_a_rule_row_follows(tmp_path, body, expected):
    """Round 2 of #905, 🟡 1. A header is known by the rule row under it,
    never by its first cell: a foreign table's header names no removal, and
    a body row whose first cell reads `Removes` is still a row."""
    tree(tmp_path, **{"mod.py": "def old_reader():\n    return 1\n"})
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"spec.md": "# frame\n\n## Removes\n\n" + body + REMOVES_TAIL},
    )
    found, _ = refusals(tmp_path)
    assert [
        (s, c.replace(os.sep, "/").rsplit("/", 1)[-1]) for s, c, _d in found
    ] == expected


def test_a_table_in_the_next_section_is_no_strayed_row(tmp_path):
    """Round 2 of #905, 🟡 2. A table row under a sub-heading of `## Removes`
    is refused up to the next heading of level 2 or above and no further: a
    table in the frame's next section is read as the rest of the frame is."""
    tree(tmp_path, **{"mod.py": "def old_reader():\n    return 1\n"})
    h = home(tmp_path)
    body = (
        REMOVES_TABLE
        + "\n### Why these rows\n\nProse.\n\n## Data & interfaces\n\n"
        + "| Unit | Why |\n|---|---|\n| `mod.py#old_reader` | z |\n"
    )
    work_item(
        h,
        "1780000000-live",
        **{"spec.md": "# frame\n\n## Removes\n\n" + body + REMOVES_TAIL},
    )
    found, _ = refusals(tmp_path)
    assert found == []
