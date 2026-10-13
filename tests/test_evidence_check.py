"""evidence-check: ledger discovery, the CLI surface, and the exit codes.

The verdict machinery itself lives in `test_a_row_points_by_content.py`. What
is here is everything around it — which files are read, how several are
aggregated, and what a CI step sees.

**No fixture in this file runs git.** It used to need a repository with real
commits, because a row's baseline was a commit and drift was a diff. A
coordinate that names content needs only the file, which is the shortest
statement of what the redesign removed.
"""

import os
import subprocess
import sys

import config_shapes
import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "skills", "evidence-check", "scripts", "evidence_check.py")

SERVICE = "def handler(x):\n    return x + 1\n\n\ndef other():\n    return 0\n"
# `handler`'s body, hashed the way the checker hashes it.
GOOD = "9207ed06"


def run(args, cwd):
    return subprocess.run(
        [sys.executable, SCRIPT, *args],
        cwd=str(cwd),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


def usable_bash():
    """Whether `bash` here actually executes what it is handed.

    The precondition this file's guard tests assume, stated and checked
    rather than assumed: on Windows, `bash` on PATH can resolve to the WSL
    stub in System32, which fails every command with its own exit code no
    matter what was asked — so every assertion expecting the guarded 1
    passed for that wrong reason, and only the one expecting 0 could fail.
    The step under test runs on the ubuntu leg of real CI, so a skip here
    costs the guard nothing it is ever asked to do.
    """
    try:
        r = subprocess.run(["bash", "-c", "exit 7"], capture_output=True, timeout=30)
    except OSError:
        return False
    return r.returncode == 7


def step(args, cwd):
    """The exit code of the CI step `evidence-ci` prints, guard included."""
    quoted = " ".join(f"'{a}'" for a in args)
    # `sys.executable`, not `python3`: the name does not exist on Windows.
    # Forward slashes, not `os.sep`: inside bash's single quotes a backslash
    # is literal, so `C:\...\python.exe` never resolves to the interpreter,
    # the command exits before the guard runs, and every case expecting the
    # guarded 1 passed for that wrong reason while the one expecting 0
    # failed. Both spellings name the same file to Windows Python.
    exe = sys.executable.replace("\\", "/")
    script = SCRIPT.replace("\\", "/")
    return subprocess.run(
        [
            "bash",
            "-e",
            "-c",
            f"'{exe}' '{script}' {quoted} || [ $? -eq 1 ]",
        ],
        cwd=str(cwd),
        capture_output=True,
        encoding="utf-8",
    ).returncode


@pytest.fixture
def proj(tmp_path):
    d = tmp_path / "proj"
    (d / "src").mkdir(parents=True)
    (d / "src" / "service.py").write_text(SERVICE, encoding="utf-8")
    return d


def ledger(proj, body, at="seal/ledger.md"):
    path = proj / at
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("# map\n\n" + body, encoding="utf-8")
    return path


def test_the_hash_in_this_files_fixtures_is_the_real_one(proj):
    """Pinned rather than computed, so a fixture cannot agree with a broken
    hash function by using it to build its own expectation."""
    import importlib.util

    spec = importlib.util.spec_from_file_location("ec", SCRIPT)
    ec = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ec)
    assert ec.content_hash(SERVICE.splitlines()[0:2]) == GOOD


def test_a_matching_row_is_ok_and_exits_zero(proj):
    ledger(proj, f"| POL-1 | `src/service.py#handler@{GOOD}` |\n")
    r = run(["."], proj)
    assert "1 ok" in r.stdout and r.returncode == 0, r.stdout


def test_drift_exits_one_and_strict_exits_two(proj):
    ledger(proj, "| POL-1 | `src/service.py#handler@00000000` |\n")
    assert run(["."], proj).returncode == 1
    assert run(["--strict", "."], proj).returncode == 2


def test_a_broken_coordinate_exits_two(proj):
    ledger(proj, "| POL-1 | `src/service.py#gone@00000000` |\n")
    r = run(["."], proj)
    assert "BROKEN" in r.stdout and r.returncode == 2, r.stdout


def test_a_deleted_root_level_file_is_broken_not_external(proj):
    """`main.py#f` with the file deleted used to classify as EXTERNAL — first
    path element missing meant "other repo" — and EXTERNAL never fails the
    build. A root-level coordinate has no cross-repo prefix, so a missing file
    there is a broken citation."""
    ledger(proj, "| POL-1 | `src/service.py#handler@00000000` |\n")
    (proj / "src" / "service.py").unlink()
    r = run(["."], proj)
    assert r.returncode == 2 and "BROKEN" in r.stdout and "EXTERNAL" not in r.stdout


def test_duplicate_coordinates_are_counted_once(proj):
    ledger(
        proj,
        f"| POL-1 | `src/service.py#handler@{GOOD}` |\n"
        f"| POL-2 | `src/service.py#handler@{GOOD}` |\n",
    )
    assert "1 ok" in run(["."], proj).stdout


def test_map_resolves_a_prefixed_cross_repo_path(proj, tmp_path):
    other = tmp_path / "legacy"
    (other / "src").mkdir(parents=True)
    (other / "src" / "service.py").write_text(SERVICE, encoding="utf-8")
    ledger(proj, f"| POL-1 | `legacy/src/service.py#handler@{GOOD}` |\n")
    # EXTERNAL needs declared cross-repo intent since round 4's 🔴 3; a
    # parity config is one of the three declarations.
    (proj / "seal" / "parity.md").write_text("# parity\n", encoding="utf-8")
    assert "1 external" in run(["."], proj).stdout
    r = run(["--map", f"legacy={other}", "."], proj)
    assert "1 ok" in r.stdout and r.returncode == 0, r.stdout


def test_a_missing_prefix_without_cross_repo_intent_is_broken(proj):
    """EXTERNAL is a claim about ANOTHER repository, and only a declaration —
    `seal/parity.md`, `--map`, `--default-repo` — says this project has
    one. Without intent, a deleted or renamed directory turned its rows
    EXTERNAL and the build stayed green (round 4, 🔴 3)."""
    ledger(proj, "| POL-1 | `legacy/src/old.py#handler@00000000` |\n")
    r = run(["."], proj)
    assert "EXTERNAL" not in r.stdout and "BROKEN" in r.stdout, r.stdout
    assert r.returncode == 2, r.stdout


def test_migrate_reads_map_and_default_repo(proj, tmp_path):
    """`--migrate` ignored both, so a legacy-parity ledger could never
    migrate and the OLD-FORMAT prescription line was circular for exactly
    those repositories (round 4, 🟡 9)."""
    other = tmp_path / "legacy"
    (other / "src").mkdir(parents=True)
    (other / "src" / "old.py").write_text(SERVICE, encoding="utf-8")
    orig = tmp_path / "orig"
    (orig / "apps").mkdir(parents=True)
    (orig / "apps" / "svc.py").write_text(SERVICE, encoding="utf-8")
    ledger(
        proj,
        "| POL-1 | `legacy/src/old.py:1-2` | 2026-08-31 |\n"
        "| POL-2 | `apps/svc.py:1-2` | 2026-08-31 |\n",
    )
    r = run(
        ["--migrate", "--map", f"legacy={other}", "--default-repo", str(orig), "."],
        proj,
    )
    assert "2 rows migrated" in r.stdout, r.stdout
    text = (proj / "seal" / "ledger.md").read_text(encoding="utf-8")
    assert f"legacy/src/old.py#handler@{GOOD}" in text, text
    assert f"apps/svc.py#handler@{GOOD}" in text, text


def test_default_repo_resolves_an_unprefixed_cross_repo_path(proj, tmp_path):
    """A migration ledger states coordinates against the ORIGINAL repo with no
    prefix. The property is resolution: found in the other checkout rather than
    reported EXTERNAL or BROKEN."""
    orig = tmp_path / "orig"
    (orig / "apps").mkdir(parents=True)
    (orig / "apps" / "svc.py").write_text(SERVICE, encoding="utf-8")
    ledger(proj, f"| POL-9 | `apps/svc.py#handler@{GOOD}` |\n")
    r = run(["--default-repo", str(orig), "."], proj)
    assert "1 ok" in r.stdout and r.returncode == 0, r.stdout


def test_no_ledger_at_all_is_a_no_op(proj):
    r = run(["."], proj)
    assert "no evidence ledgers found" in r.stdout and r.returncode == 0


@pytest.mark.parametrize(
    "at",
    ["seal/ledger.md", "seal/ledger/core.md", "docs/policies/demo/_evidence.md"],
)
def test_the_checker_finds_the_ledger_with_no_arguments(proj, at):
    """The current home, the per-work-item fragment, and the pre-0.10 address."""
    ledger(proj, "| POL-1 | `src/service.py#gone@00000000` |\n", at=at)
    r = run(["."], proj)
    assert "no evidence ledgers found" not in r.stdout, r.stdout
    assert "src/service.py#gone" in r.stdout, r.stdout
    assert r.returncode == 2


def test_a_custom_ledger_glob_is_read_instead(proj):
    ledger(proj, "| POL-1 | `src/service.py#gone@00000000` |\n")
    (proj / "SPEC.md").write_text(
        f"| POL-1 | `src/service.py#handler@{GOOD}` |\n", encoding="utf-8"
    )
    r = run(["--ledger", "SPEC.md", "."], proj)
    assert "SPEC.md" in r.stdout and "1 ok" in r.stdout and r.returncode == 0


def test_several_ledgers_aggregate_and_the_worst_one_decides(proj):
    ledger(proj, f"| POL-1 | `src/service.py#handler@{GOOD}` |\n")
    ledger(proj, "| POL-9 | `src/service.py#gone@00000000` |\n", at="seal/ledger/b.md")
    r = run(["."], proj)
    assert "1 ok" in r.stdout and "1 broken" in r.stdout
    assert r.returncode == 2, "a broken coordinate in the second ledger must fail"


def test_a_coordinate_in_a_dot_directory_resolves(proj):
    """A leading dot is allowed: `.github/...` was read as `github/...` and
    reported EXTERNAL, so the plugin could not cite its own directory."""
    (proj / ".github").mkdir()
    (proj / ".github" / "svc.py").write_text(SERVICE, encoding="utf-8")
    ledger(proj, f"| POL-1 | `.github/svc.py#handler@{GOOD}` |\n")
    r = run(["."], proj)
    assert "1 ok" in r.stdout and r.returncode == 0, r.stdout


def test_letting_drift_warn_takes_both_halves(proj):
    """`evidence-ci` twice described a softer mode that does not exist.

    Drift fails a `bash -e` step either way; the guard only lets it through
    once `--strict` is gone too, and a broken coordinate still fails through
    that same guard. A malformed coordinate follows the flag the way drift
    does (work item 1790381328), so the guard lets it through as well, which
    is what `evidence-ci`'s step 4 now says."""
    if not usable_bash():
        pytest.skip("no usable bash — the step under test runs on ubuntu CI")
    ledger(proj, "| POL-1 | `src/service.py#handler@00000000` |\n")
    assert run(["."], proj).returncode == 1, "drift already fails without --strict"
    assert run(["--strict", "."], proj).returncode == 2
    assert step(["--strict", "."], proj) == 1, "the guard cannot swallow exit 2"
    assert step(["."], proj) == 0, "both halves together let drift warn"

    ledger(proj, "| POL-1 | `src/service.py#gone@00000000` |\n")
    assert step(["."], proj) == 1, "the guard must not swallow a broken coordinate"

    ledger(proj, "| POL-1 | `src/service.py#handler@0` |\n")
    assert step(["."], proj) == 0, "the guard lets a malformed coordinate warn"
    assert step(["--strict", "."], proj) == 1, "--strict still refuses it"


def test_the_ci_skill_prints_the_step_that_matches_that_behavior():
    """The executed fact above is worth what the sentence beside it says."""
    with open(
        os.path.join(ROOT, "skills", "evidence-ci", "SKILL.md"), encoding="utf-8"
    ) as f:
        text = f.read()
    snippet = text.split("```yaml")[1].split("```")[0]
    assert "|| [ $? -eq 1 ]" in snippet, "the step lost the guard"
    assert "--strict" not in snippet, (
        "the printed step keeps --strict, whose exit 2 the guard cannot swallow"
    )
    assert "drop `--strict`" in text, "the prose stopped naming the other half"


# --- Q2 (#80): which `seal/` the defaults are joined under -------------------
#
# No git runs here either: a `.git` DIRECTORY at the root is the common git
# directory, and `hooks/optin.py` answers that case without a process.


def local_root(proj):
    """`.git/seal/` and nothing at `<root>/seal/` — a local-mode repository
    as the checker sees it."""
    home = proj / ".git" / "seal"
    home.mkdir(parents=True)
    assert not (proj / "seal").exists()
    return home


def test_the_plugins_copy_resolves_the_root_under_the_git_directory(proj):
    """Q2 (a). The plugin's copy sits beside `hooks/optin.py` and asks it
    where `seal/` is; the defaults were joined under ROOT, so a local-mode
    ledger was "no evidence ledgers found", exit 0 — a green run that
    examined nothing."""
    local_root(proj)
    ledger(
        proj, "| POL-1 | `src/service.py#gone@00000000` |\n", at=".git/seal/ledger.md"
    )
    r = run(["."], proj)
    assert "no evidence ledgers found" not in r.stdout, r.stdout
    assert "src/service.py#gone" in r.stdout, r.stdout
    assert r.returncode == 2


def test_the_plugins_copy_reads_the_parity_config_under_the_resolved_root(proj):
    """The other join: `seal/parity.md` is the declaration that lets an
    unplaceable prefixed row read EXTERNAL instead of BROKEN, and it was
    looked for under ROOT only."""
    local_root(proj)
    (proj / ".git" / "seal" / "parity.md").write_text("# parity\n", encoding="utf-8")
    ledger(
        proj,
        "| POL-1 | `legacy/src/old.py#handler@00000000` |\n",
        at=".git/seal/ledger.md",
    )
    r = run(["."], proj)
    assert "EXTERNAL" in r.stdout and "BROKEN" not in r.stdout, r.stdout
    assert r.returncode == 0, r.stdout


def test_the_tree_root_still_wins_for_the_plugins_copy(proj):
    """S1's order, through the checker: `<root>/seal/` first."""
    local_root(proj)
    ledger(
        proj, "| POL-1 | `src/service.py#gone@00000000` |\n", at=".git/seal/ledger.md"
    )
    ledger(proj, f"| POL-1 | `src/service.py#handler@{GOOD}` |\n")
    r = run(["."], proj)
    assert "total: 1 ok" in r.stdout and ".git" not in r.stdout, r.stdout
    assert r.returncode == 0


def vendored_copy(tmp_path):
    """The checker as `evidence-ci` vendors it: alone in `tools/`, with no
    `hooks/` and no `SKILL.md` beside it."""
    tools = tmp_path / "elsewhere" / "tools"
    tools.mkdir(parents=True)
    dst = tools / "evidence_check.py"
    dst.write_bytes(open(SCRIPT, "rb").read())
    return dst


def test_a_copy_with_no_hooks_beside_it_reads_the_tree_root_only(proj, tmp_path):
    """Q2 (a)'s other half. The vendored copy cannot import `hooks/optin.py`,
    and it runs in CI, which is shared mode: it reads `<root>/seal/` as it
    always did. A local-mode ledger is invisible to it, and says so."""
    copy = vendored_copy(tmp_path)
    local_root(proj)
    ledger(
        proj, "| POL-1 | `src/service.py#gone@00000000` |\n", at=".git/seal/ledger.md"
    )
    r = subprocess.run(
        [sys.executable, str(copy), "."],
        cwd=str(proj),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    assert "no evidence ledgers found" in r.stdout and r.returncode == 0, r.stdout

    ledger(proj, f"| POL-1 | `src/service.py#handler@{GOOD}` |\n")
    r = subprocess.run(
        [sys.executable, str(copy), "."],
        cwd=str(proj),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    assert "1 ok" in r.stdout and r.returncode == 0, r.stdout


def test_a_copy_under_a_plugin_tree_without_a_skill_beside_it_is_still_vendored(
    proj, tmp_path
):
    """`seal_home`'s `os.path.isfile(skill)` conjunct, which stood recorded as
    unreachable and is not.

    The rider here said the state that separates the two conjuncts is a
    vendored copy inside a tree that HAS a plugin above it, and that nothing
    constructs it. This constructs it. The copy sits three directories under a
    tree carrying `hooks/optin.py`, so the FIRST conjunct passes; there is no
    `SKILL.md` one level up, so the second is the only thing left to say this
    is not the plugin's own copy.

    Against a local-mode repository the two answers differ — `<root>/seal/`
    with the conjunct, `<git-common-dir>/seal/` without it — so dropping it
    makes a vendored copy read a root it must not read. That is a wrong
    ANSWER rather than merely an unheld line, and the mutation that survived
    every evidence suite dies here.
    """
    tree = tmp_path / "tree"
    (tree / "hooks").mkdir(parents=True)
    (tree / "hooks" / "optin.py").write_bytes(
        open(os.path.join(ROOT, "hooks", "optin.py"), "rb").read()
    )
    scripts = tree / "a" / "b" / "scripts"
    scripts.mkdir(parents=True)
    copy = scripts / "evidence_check.py"
    copy.write_bytes(open(SCRIPT, "rb").read())
    assert (tree / "hooks" / "optin.py").is_file(), "the first conjunct must pass"
    assert not (tree / "a" / "b" / "SKILL.md").exists(), (
        "a SKILL.md here would let the first conjunct decide and the case "
        "would prove nothing"
    )

    local_root(proj)
    ledger(
        proj, f"| POL-1 | `src/service.py#handler@{GOOD}` |\n", at=".git/seal/ledger.md"
    )
    r = subprocess.run(
        [sys.executable, str(copy), "."],
        cwd=str(proj),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    assert "no evidence ledgers found" in r.stdout, (
        "a vendored copy read the local-mode root: the `SKILL.md` conjunct is "
        f"what keeps it on `<root>/seal/`\n{r.stdout}"
    )
    assert r.returncode == 0, r.stdout


def test_the_ledger_flag_overrides_the_resolver_either_way(proj):
    """`--ledger` is unchanged: a pattern given by hand is joined under ROOT,
    whatever the resolver would have said."""
    local_root(proj)
    ledger(
        proj, "| POL-1 | `src/service.py#gone@00000000` |\n", at=".git/seal/ledger.md"
    )
    (proj / "SPEC.md").write_text(
        f"| POL-1 | `src/service.py#handler@{GOOD}` |\n", encoding="utf-8"
    )
    r = run(["--ledger", "SPEC.md", "."], proj)
    assert "SPEC.md" in r.stdout and "1 ok" in r.stdout and r.returncode == 0
    assert "gone" not in r.stdout, "the resolved default was read beside --ledger"


# --- #444: a row inside a closed fence is an example, not a claim ----------

FENCED_EXAMPLE = (
    "A row looks like this:\n\n"
    "```markdown\n"
    "| X | `nosuchfile.py#nothing@deadbeef` | read | 2026-01-01 | |\n"
    "| Y | `src/service.py#handler@00000000` | old `src/service.py:1-2` 2026-01-01 abcdef1 | |\n"
    "```\n\n"
)


def test_a_fenced_example_row_is_not_checked(proj):
    """S1, #444's reproduction. A ledger that explains its own row format
    shows an example row in a fenced block, and nobody wrote that row. Seen
    red against `c52e8350`: `BROKEN  nosuchfile.py#nothing  file not found`
    and exit 2 — the broad gate failing over an example."""
    ledger(proj, FENCED_EXAMPLE + f"| POL-1 | `src/service.py#handler@{GOOD}` |\n")
    r = run(["--strict", "."], proj)
    assert "nosuchfile" not in r.stdout, r.stdout
    assert "OLD-FORMAT" not in r.stdout, r.stdout
    assert "1 ok · 0 drifted · 0 broken" in r.stdout and r.returncode == 0, r.stdout


def test_the_writers_leave_a_fenced_example_byte_for_byte(proj):
    """S2. `--reverify` rewrites a hash by position and `--migrate` rewrites an
    old `path:line` row, and neither may touch an example: a person's example
    that `--reverify` rewrote would stop showing the shape it was written to
    show. Seen red against `c52e8350`: `--reverify` rewrote the fenced
    `00000000` and `--migrate` rewrote the fenced `src/service.py:1-2`."""
    path = ledger(
        proj,
        FENCED_EXAMPLE
        + "| POL-1 | `src/service.py#handler@00000000` |\n"
        + "| POL-2 | old `src/service.py:1-2` 2026-01-01 |\n",
    )
    fenced = FENCED_EXAMPLE
    r = run(["--reverify", "."], proj)
    assert r.returncode == 0, r.stdout
    after = path.read_text(encoding="utf-8")
    assert fenced in after, after
    assert f"`src/service.py#handler@{GOOD}` |\n| POL-2" in after, after
    r = run(["--migrate", "."], proj)
    after = path.read_text(encoding="utf-8")
    assert fenced in after, after
    assert "| POL-2 | old `src/service.py#handler@" in after, after


def test_an_unclosed_fence_still_holds_its_rows(proj):
    """S3, which pins the direction rather than a change: only a block that
    closes is certainly a quotation. A fence the author never closed runs to
    the end of the file, and reading nothing from there on would pass a
    broken row in silence. Passes before and after #444."""
    ledger(
        proj,
        "```markdown\nan example the author never closed\n\n"
        "| POL-1 | `src/gone.py#handler@00000000` |\n",
    )
    r = run(["."], proj)
    assert "BROKEN   src/gone.py#handler" in r.stdout and r.returncode == 2, r.stdout


def test_a_vendored_copy_skips_a_fenced_example_too(proj, tmp_path):
    """The copy `evidence-ci` puts alone in `tools/` has no shared reader
    beside it, so it asks its own pair of delimiter functions. The verdict
    must be the plugin's."""
    copy = vendored_copy(tmp_path)
    ledger(proj, FENCED_EXAMPLE + f"| POL-1 | `src/service.py#handler@{GOOD}` |\n")
    r = subprocess.run(
        [sys.executable, str(copy), "--strict", "."],
        cwd=str(proj),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    assert "nosuchfile" not in r.stdout and r.returncode == 0, r.stdout


def test_the_vendored_fence_rule_agrees_with_the_shared_one():
    """The vendored pair is a second copy of `unverified_check.py`'s
    delimiter rule, kept for the one reason `hooks/blocks.py#FENCE` keeps its
    own: the copy cannot load the reader. This holds the two in step over the
    shape table the config reader's agreement case walks, opener and closer
    alike."""
    import importlib.util

    from test_unverified_rows_close import FENCE_SHAPES, uc

    spec = importlib.util.spec_from_file_location("ec_vendored_rule", SCRIPT)
    ec = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ec)
    assert ec.fence_rule()[0].__module__ == "specseal_unverified_reader", (
        "the plugin's copy must ask the shared reader, not its vendored pair"
    )
    lines = {line for shape in FENCE_SHAPES for line in shape}
    for line in lines:
        assert ec.vendored_fence_opener(line) == uc.fence_opener(line), line
        for opener in {uc.fence_opener(o) for o in lines} - {None}:
            assert ec.vendored_fence_closes(line, opener) == uc.fence_closes(
                line, opener
            ), (line, opener)


def test_the_vendored_cell_rule_agrees_with_the_shared_one():
    """The `MALFORMED` arm (#299) reads a ledger row's `Code grounds` cell,
    so the checker splits table rows, and a copy `evidence-ci` vendors alone
    cannot load the shared reader's `split_row` any more than its fence rule.
    The plugin's copy asks the shared reader; this holds the vendored split
    in step with it over the shapes a ledger row takes."""
    import importlib.util

    from test_unverified_rows_close import uc

    spec = importlib.util.spec_from_file_location("ec_vendored_cells", SCRIPT)
    ec = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ec)
    assert ec.cell_rule().__module__ == "specseal_unverified_reader", (
        "the plugin's copy must ask the shared reader, not its vendored split"
    )
    for line in (
        "| a | b |",
        "|a|b",
        "  | indented | row |  ",
        "| a \\| b | c |",
        '| `x.py#"p \\| q"@00000000` | c |',
        "| ends on an escape \\|",
        "| | | |",
        "|---|:-:|",
        "|",
        "not a row",
        "",
    ):
        assert ec.vendored_split_row(line) == uc.split_row(line), line


# The config table's own shapes, for S4 of #867 and S7 of #871: every shape
# the vendored twin can meet in a CI checkout's `seal/config.md` that it can
# judge line by line, the walker's refusal shapes from
# `tests/config_shapes.py` among them. **No fence and no comment inside the
# table**, on purpose: the twin carries no block state, and where it lacks
# it the rule is a direction, not equality —
# `test_the_vendored_config_rule_refuses_where_it_lacks_block_state` holds
# that over the shapes that carry one. Shape 1's comment is a single line
# directly above the header, which both readers refuse by the line alone.
_HEAD = "# Repository config\n\n| Item | Value |\n|---|---|\n"
CONFIG_SHAPES = {
    "plain": _HEAD + "| Mode | shared |\n| Broad gate | bin/test -q |\n",
    "a doubled row": _HEAD + "| Mode | shared |\n| Mode | local |\n",
    "an empty value": _HEAD + "| Mode |  |\n| Broad gate | x |\n",
    "an escaped pipe": _HEAD + "| Broad gate | a \\| b |\n| Mode | shared |\n",
    "a stray separator": _HEAD + "| Mode | shared |\n|---|---|\n| Broad gate | x |\n",
    "a second header": _HEAD
    + "| Mode | shared |\n| Item | Value |\n|---|---|\n| Broad gate | x |\n",
    "no header": "| Mode | shared |\n| Broad gate | x |\n",
    "rows above the header": "| Mode | local |\n\n" + _HEAD + "| Mode | shared |\n",
    "an empty item": _HEAD + "|| x |\n| Mode | shared |\n",
    "a three-column row": _HEAD
    + "| Mode | shared |\n| a | b | c |\n| Broad gate | x |\n",
    "prose under the table": _HEAD
    + "| Mode | shared |\n\nsome prose\n| Broad gate | x |\n",
    "a line before the first row": _HEAD + "| not a row\n| Mode | shared |\n",
    "crlf": (_HEAD + "| Mode | shared |\n| Broad gate | x |\n").replace("\n", "\r\n"),
    "no table": "# nothing here\n",
    # #871: planted after a mutation dropping the twin's list-item check
    # survived every other shape — GFM reads this header into the item.
    "a header indented under a list item": "- a note\n\n | Item | Value |\n"
    "|---|---|\n| Mode | shared |\n",
    # The shape every config `seal mode` writes, `seal.py#NEW_CONFIG`: a
    # closed comment above the header, a blank line between, and this
    # repository's own config, which carries the same comment.
    "the config seal mode writes": "# Repository config\n\n"
    + config_shapes.OPEN
    + " What this repository says about itself. This file was\n"
    + "created by `seal mode`. "
    + config_shapes.CLOSE
    + "\n\n| Item | Value |\n|---|---|\n| Mode | shared |\n",
    # A fence and a one-line comment that close above the header hide
    # nothing from GFM; each was planted after a mutation of the twin's
    # closing check survived the shapes above.
    "a closed fence above the header": "# c\n\n```\nan example\n```\n\n"
    "| Item | Value |\n|---|---|\n| Mode | shared |\n",
    "a one-line comment above the header": "# c\n\n"
    + config_shapes.OPEN
    + " a note "
    + config_shapes.CLOSE
    + "\n\n| Item | Value |\n|---|---|\n| Mode | shared |\n",
    # #871 round 2, yellow 8: an item written again below the line the walk
    # stopped at has no value, in the twin as in the plugin.
    "an item written again below the stop": _HEAD
    + "| Mode | shared |\n| a | b | c |\n| Mode | local |\n",
    "a cutoff written again below the stop": _HEAD
    + "| Ledger frozen from | 100 |\n| a | b | c |\n| Ledger frozen from | 200 |\n",
    "this repository's own config": open(
        os.path.join(ROOT, "seal", "config.md"), encoding="utf-8"
    ).read(),
    **{
        f"shape {n}": config_shapes.SHAPES[n]
        for n in (1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    },
}
# The shapes where the twin lacks the block state the plugin's walker has:
# a comment inside the table, and a fence or a comment above the header
# that hides an example table from the plugin.
LACKS_BLOCK_STATE = {
    "shape 5, a comment inside the table": config_shapes.SHAPES[5],
    "a fenced example above the live table": (
        "# c\n\n```markdown\n\n| Item | Value |\n|---|---|\n| Mode | local |\n"
        "```\n\n| Item | Value |\n|---|---|\n| Mode | shared |\n"
    ),
    "a commented old table above the live one": (
        "# c\n\n" + config_shapes.OPEN + "\n\n| Item | Value |\n|---|---|\n"
        "| Mode | local |\n" + config_shapes.CLOSE + "\n\n"
        "| Item | Value |\n|---|---|\n| Mode | shared |\n"
    ),
    "a fence directly under the last row": (
        _HEAD + "| Mode | shared |\n```\n| Broad gate | x |\n```\n"
    ),
    # #871 round 2: the twin ends a line where GFM does and the walker reads
    # `str.splitlines` pieces, and a fence below the table can hide a heading
    # from the walker that the twin sees. Each was seen red against
    # 4dfb3d0d: the twin read `Mode` or answered no `Broad gate` row where
    # the plugin refused.
    "a row holding a line separator": _HEAD + "| Mode | shared |\n",
    "a row piece after a line separator below the table": (
        _HEAD + "| Mode | shared |\n\nx | Broad gate | y |\n"
    ),
    "a heading inside a fence below the table": (
        _HEAD + "| Mode | shared |\n\n```\n# x\n```\n| Broad gate | y |\n"
    ),
    # Planted after a mutation dropping the comment from the blocks the twin
    # follows below the table survived the shapes above.
    "a heading inside a comment below the table": (
        _HEAD
        + "| Mode | shared |\n\n"
        + config_shapes.OPEN
        + "\n# x\n"
        + config_shapes.CLOSE
        + "\n| Broad gate | y |\n"
    ),
}


def _checker(name):
    import importlib.util

    spec = importlib.util.spec_from_file_location(name, SCRIPT)
    ec = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ec)
    return ec


@pytest.mark.parametrize("name", sorted(CONFIG_SHAPES))
def test_the_vendored_config_rule_agrees_with_the_shared_one(name):
    """S4 of #867. A copy `evidence-ci` vendors alone cannot load
    `hooks/config.py`, so it carries twins of the table walk and the value
    rule; this holds both equal to the plugin's reader over the config
    table's own shapes, item by item. The twin's table walk had no case at
    all (inventory row E46 said it had one, and none existed), and it read a
    stray separator, a second header and an empty item differently: seen red
    against 5623d728's `vendored_config_rows` on those three shapes.

    **Since #871 both sides are the walker's**: the twin returns
    `(rows, refusals)` on the walker's table grammar, and the rows, the
    refusals and the per-item answer are held equal to `config_table` and
    `config_value`. Seen red against the stop rule's twin on every refusal
    shape: it returned rows and no refusal."""
    from conftest import load_hook_module

    config = load_hook_module("config.py", "specseal_config_for_the_twin")
    ec = _checker("ec_vendored_config")
    assert os.path.realpath(
        ec.config_rule()[1].__code__.co_filename
    ) == os.path.realpath(config.config_table.__code__.co_filename), (
        "the plugin's copy must ask hooks/config.py, not its vendored twin"
    )
    text = CONFIG_SHAPES[name]
    rows, refusals = config.config_table(text)
    twin_rows, twin_refusals = ec.vendored_config_rows(text)
    assert [(i, v) for _n, i, v in twin_rows] == [(i, v) for _n, i, v in rows], name
    assert twin_refusals == refusals, name
    for item in ("Mode", "Broad gate", "Ledger frozen from", "x", ""):
        assert ec.vendored_config_value(text, item) == config.config_value(
            text, item
        ), (name, item)


@pytest.mark.parametrize("name", sorted(LACKS_BLOCK_STATE))
def test_the_vendored_config_rule_refuses_where_it_lacks_block_state(name):
    """S7 of #871, the stated direction. Where the plugin's walker reads a
    line by block state the twin does not carry, the twin may refuse what
    the plugin reads and never reads what the plugin refuses: every item is
    the plugin's answer or a refusal, a value is never one the plugin does
    not give, and on each of these shapes the twin refuses something. Seen
    red against the stop rule's twin, which read the fenced example's
    `Mode local` where the plugin reads `shared`."""
    from conftest import load_hook_module

    config = load_hook_module("config.py", "specseal_config_for_the_twin_direction")
    ec = _checker("ec_vendored_config_direction")
    text = LACKS_BLOCK_STATE[name]
    assert ec.vendored_config_rows(text)[1], name
    for item in ("Mode", "Broad gate", "Ledger frozen from"):
        twin = ec.vendored_config_value(text, item)
        plugin = config.config_value(text, item)
        assert twin == plugin or (twin[0] is None and twin[1] is not None), (
            name,
            item,
            twin,
            plugin,
        )


def test_the_vendored_table_grammar_is_the_walkers():
    """S7 of #871: each pattern of the twin's line grammar is the walker's,
    byte for byte, so the two read a line alike wherever the twin reads one."""
    from conftest import load_hook_module

    config = load_hook_module("config.py", "specseal_config_for_the_twin_grammar")
    ec = _checker("ec_vendored_config_grammar")
    for twin, walker in (
        (ec.VENDORED_TABLE_ROW, config.TABLE_ROW),
        (ec.VENDORED_CELL_PIPE, config.CELL_PIPE),
        (ec.VENDORED_EVEN_ESCAPED_PIPE, config.EVEN_ESCAPED_PIPE),
        (ec.VENDORED_DELIMITER_ROW, config.DELIMITER_ROW),
        (ec.VENDORED_ATX_HEADING, config.ATX_HEADING),
        (ec.VENDORED_LIST_ITEM, config.LIST_ITEM),
        (ec.VENDORED_FIRST_CELL, config.FIRST_CELL),
        (ec.VENDORED_THEMATIC_BREAK, config.THEMATIC_BREAK),
    ):
        assert (twin.pattern, twin.flags) == (walker.pattern, walker.flags)
    assert ec.VENDORED_CONFIG_HEADER == config.CONFIG_TABLE
    # The characters the twin splits a GFM line at, to read it as the
    # walker's pieces: every one `str.splitlines` ends a line at, LF and CR
    # aside, and no other.
    import sys

    cuts = {
        chr(c)
        for c in range(sys.maxunicode + 1)
        if len(f"a{chr(c)}b".splitlines()) == 2 and chr(c) not in "\r\n"
    }
    assert {
        chr(c)
        for c in range(sys.maxunicode + 1)
        if ec.VENDORED_PIECE_BREAK.match(chr(c))
    } == cuts
    # The HTML blocks no blank line ends, kinds 1-5, which the twin follows
    # to their close above the header as the walker does.
    assert [
        (s.pattern, s.flags, e.pattern, e.flags) for s, e in ec.VENDORED_RAW_HTML
    ] == [(s.pattern, s.flags, e.pattern, e.flags) for s, e in config.HTML_KINDS[:5]]


def test_the_twin_names_an_example_table_inside_a_closed_block():
    """#871 round 2, yellow 11. A header inside a fence or a comment that
    closes below it is an example the twin cannot tell from the live table:
    its sentence says so, never that the block is unclosed, and a block that
    is never closed keeps its own sentence. Seen red against 4dfb3d0d, which
    said "never closed" for both closed blocks."""
    ec = _checker("ec_vendored_example_table")
    for name in (
        "a fenced example above the live table",
        "a commented old table above the live one",
    ):
        said = ec.vendored_config_rows(LACKS_BLOCK_STATE[name])[1]
        assert said and "closes below it" in said[0], (name, said)
        assert "never closed" not in said[0], (name, said)
    unclosed = "# c\n\n```\n\n| Item | Value |\n|---|---|\n| Mode | shared |\n"
    said = ec.vendored_config_rows(unclosed)[1]
    assert said and "close the fence above the table" in said[0], said
    comment = (
        "# c\n\n" + config_shapes.OPEN + "\n\n| Item | Value |\n|---|---|\n"
        "| Mode | shared |\n"
    )
    said = ec.vendored_config_rows(comment)[1]
    assert said and "never closed" in said[0], said


@pytest.mark.parametrize(
    "line",
    ["```", "~~~", "- item", "1. item", "> quoted", "    code", "\tcode", "<div>"]
    + ["***", "---", config_shapes.OPEN + " c " + config_shapes.CLOSE],
)
def test_the_twin_does_not_call_a_block_line_a_row(line):
    """#871 round 2, yellow 12. The walker ends the table at each of these
    lines (cmark-gfm measured by the round's reviewer for the fence, list,
    quote, code and HTML lines), so the twin's refusal names what it cannot
    judge and the blank line that clears it. Seen red against 4dfb3d0d,
    which said GFM reads the line as one of the table's rows, or called
    `---` a delimiter row out of place."""
    ec = _checker("ec_vendored_block_line")
    said = ec.vendored_config_rows(_HEAD + "| Mode | shared |\n" + line + "\n")[1]
    assert said and "leave a blank line above it" in said[0], said
    assert "reads as one of its rows" not in said[0], said
    assert "out of place" not in said[0], said


@pytest.mark.parametrize("shape", ["absent", "readable", "directory", "undecodable"])
def test_the_vendored_config_file_reader_agrees_with_the_shared_one(tmp_path, shape):
    """S4's file half: the twin of `hooks/config.py#config_text` tells an
    absent file from one that is there and will not read, in the reader's
    own sentence, so a vendored `--reverify` refuses exactly where the
    plugin's does."""
    from conftest import load_hook_module

    config = load_hook_module("config.py", "specseal_config_for_the_file_twin")
    ec = _checker("ec_vendored_config_file")
    path = tmp_path / "config.md"
    if shape == "readable":
        path.write_text(CONFIG_SHAPES["plain"], encoding="utf-8")
    elif shape == "directory":
        path.mkdir()
    elif shape == "undecodable":
        path.write_bytes(b"| Item | Value |\n|---|---|\n| Mode | \xff |\n")
    assert ec.vendored_config_text(str(tmp_path)) == config.config_text(str(tmp_path))


def test_the_vendored_heading_rule_agrees_with_the_shared_one():
    """#867. The checker reads a markdown heading by
    `unverified_check.py#heading_level` where it is the plugin's copy, and
    by its twin where `evidence-ci` vendored it alone; this holds the twin to
    the rule over the heading's shapes, each with and without a line end."""
    from test_unverified_rows_close import uc

    ec = _checker("ec_vendored_headings")
    assert ec.heading_rule().__module__ == "specseal_unverified_reader", (
        "the plugin's copy must ask the shared reader, not its vendored twin"
    )
    for line in (
        "## B",
        "   ## B",
        "    ## B",
        "\t## B",
        "#",
        "######",
        "####### seven",
        "#\tx",
        "#hello",
        "#120) wrapped",
        "## closed ##",
        " # one space",
        "",
        "plain",
        "> # quoted",
    ):
        for end in ("", "\n", "\r\n"):
            assert ec.vendored_heading_level(line + end) == uc.heading_level(
                line + end
            ), repr(line + end)
