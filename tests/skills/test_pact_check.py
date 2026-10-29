"""`skills/verify/scripts/pact_check.py`, one class per function.

Rebuilt by #942's phase 5. The printed paths, a clause's hash and an
anchor's grade run in the process on text, a grade against a stand-in
history. The checkout search, the history
and `check` read a world built once for the module and copied for each case
that writes into it: the pact's repository, whose `seal/pact.md` carries one
clause committed as v1 and then v2 on `main` and v3 on a side branch HEAD does
not hold, and a signer beside it, which names the pact in its
`seal/config.md`. `HOME` is the world's own directory, so the machine-local
map is whatever a case writes there. Each copy is the reset. The world is
`tests/conftest.py`'s, because the seven cases phase 5 left here for
`hooks/lib/config.py`, which run `check` over a pact or a signer config the
table walker refuses, are in `tests/hooks/test_config.py` since #942's phase 6.
"""

import ntpath
import os
import shutil
import subprocess

import pytest
from conftest import (
    ANCHOR_LINE,
    CLAUSE_PATH,
    MOBILE_URL,
    PACT,
    PACT_URL,
    ROOT,
    SIGNER_URL,
    SPEC,
    V1,
    V2,
    V3,
    anchor_table,
    census_case,
    clause,
    init,
    load_module,
    old_header,
    pact,
    pact_check_modules,
    signer_config,
    symlink_or_skip,
    write,
)
from conftest import commit_everything_as_e as commit
from conftest import git_out as git

TARGET = "skills/verify/scripts/pact_check.py"

SCRIPT = os.path.join(ROOT, TARGET)
WRAPPER = os.path.join(ROOT, "bin", "seal")

# The module and its evidence reader, loaded once in `tests/conftest.py`, so
# the world's `check` runs and this file patches one module. The world, its
# texts and the `world` fixture are there too, since `tests/hooks/test_config.py`
# runs the pact walker's cases through them.
pc, checker = pact_check_modules()
config = pc.load(os.path.join(pc.HOOKS, "config.py"), "config_for_pact_tests")

SIGNER = (SIGNER_URL, config.normalise_remote(SIGNER_URL))
SPEC_Y = "seal/threads/1790000001-y/frame/design.md"
# A second pact a signer's `Pact` row declares beside this one.
BILLING = "git@example.com:org/billing.git"
# The machine-local map's header and delimiter row, as `seal pact`'s remedy
# line teaches a person to begin it.
MAP_TOP = "| Remote | Path |\n|---|---|\n"
MAP_REFUSED = "REFUSED ~/.claude/agentic/pact-paths.md — the map "
# The sentences `seal pact` refuses an anchor row and an inline anchor in,
# pinned whole (contract rule 14).
NOT_ONE_URL = (
    "the `Pact` cell is not one remote URL: it holds a space, a backtick or no "
    "host and path — write the origin URL of the pact's repository, bare, as "
    "the signer's `Pact` row writes it"
)
NO_HEADING = (
    "the `Clause` cell opens with no heading — write the clause's heading "
    "path, bare, such as `## Clause / ### Narrower`"
)
NOT_A_HASH = (
    "the `Hash` cell is not eight lowercase hex digits — write `00000000` "
    "until the first report names the real one"
)
UNDECLARED = (
    "the `Pact` cell names `{cell}`, a pact this signer's `seal/config.md` "
    "does not declare in its `Pact` row, so no `seal pact` grades the row — "
    "write the origin URL of a pact that row declares, or add `{cell}` to "
    "that row"
)
OUTSIDE_TABLE = (
    "the row names a pact this signer declares and a clause, and no anchor "
    "table holds it, so nothing grades it — write it as a row of a table "
    "headed exactly `| Pact | Clause | Hash |`"
)
INLINE = (
    "a `pact:` token is the inline pact anchor `seal pact` read through "
    "0.23.x, and nothing reads it now — write it as a row of a "
    "`| Pact | Clause | Hash |` table, `| <the origin URL of the pact's "
    "repository> | ## Clause / ### Narrower | <hash> |`; or, where the text "
    "shows the retired shape rather than citing a clause, put it in a fenced "
    "code block, which nothing reads"
)


def posix(path):
    """A path as `seal pact` prints one outside HOME: every separator `/`."""
    return str(path).replace(os.sep, "/")


class Test_module:
    def test_accepts_the_map_named_in_posix_form_under_windows_joins(
        self, monkeypatch, tmp_path
    ):
        """Loaded with Windows' `os.path.join`, as on a Windows runner, the
        module still names the map with `/`; reading the file stays native."""
        with monkeypatch.context() as patched:
            patched.setattr(os.path, "join", ntpath.join)
            windows = load_module(SCRIPT, "pact_check_with_windows_joins")
        _, why = windows.checkout(config, SIGNER, str(tmp_path / "nowhere"), {})
        assert "~/.claude/agentic/pact-paths.md" in why, why
        assert "\\" not in why, why

    def test_the_wrapper_runs_the_script_from_any_directory(self, world):
        """The command run as a person types it, from a directory that is
        not the pact's repository."""
        if os.name == "nt":
            pytest.skip("the POSIX wrapper; bin/seal.cmd is its Windows twin")
        world.cite(clause(V2))
        done = subprocess.run(
            ["sh", WRAPPER, "pact", str(world.api)],
            cwd=str(world.tmp),
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            env={**os.environ, "HOME": str(world.home)},
        )
        assert done.returncode == 0, done.stdout + done.stderr
        assert "1 ok" in done.stdout, done.stdout


class Test_shown:
    @pytest.mark.parametrize(
        "path, repo, home, want",
        [
            (
                r"C:\Users\x\work\orders-web\seal\config.md",
                r"C:\Users\x\work\orders-web",
                r"C:\Users\x",
                "seal/config.md",
            ),
            (
                r"C:\Users\x\.claude\agentic\pact-paths.md",
                None,
                r"C:\Users\x",
                "~/.claude/agentic/pact-paths.md",
            ),
            ("C:/Users/x/work/a\\b.md", r"C:\Users\x\work", None, "a/b.md"),
        ],
        ids=["inside its repository", "under home", "both separators"],
    )
    def test_accepts_a_path_under_its_repository_or_home_as_relative(
        self, path, repo, home, want
    ):
        """Windows paths through `ntpath`, so the POSIX guarantee is removed
        rather than relied on (contract rule 13)."""
        assert pc.shown(path, repo, home, flavour=ntpath) == want

    @pytest.mark.parametrize(
        "path, repo, home, want",
        [
            (r"D:\work\orders-web", None, r"C:\Users\x", "D:/work/orders-web"),
            (r"D:\Users\x\work", None, r"C:\Users\x", "D:/Users/x/work"),
            (r"Users\x\work", None, r"\Users\x", "Users/x/work"),
            (r"D:\data\xy\work", None, r"D:\data\x", "D:/data/xy/work"),
            (r"C:\Users\x\work", r"C:\Users\x\work", None, "C:/Users/x/work"),
        ],
        ids=[
            "another drive",
            "the same segments on another drive",
            "a relative path under a rooted home",
            "a longer segment is not under home",
            "the repository itself",
        ],
    )
    def test_refuses_to_shorten_a_path_under_neither_and_prints_it_whole(
        self, path, repo, home, want
    ):
        got = pc.shown(path, repo, home, flavour=ntpath)
        assert got == want
        assert "\\" not in got


class Test_load:
    def test_accepts_a_sibling_module_by_its_path(self):
        assert hasattr(pc.load(pc.CHECKER, "evidence_loaded_again"), "content_hash")

    def test_refuses_a_module_that_is_not_there_with_a_sentence(self, tmp_path, capsys):
        with pytest.raises(SystemExit) as stopped:
            pc.load(str(tmp_path / "gone.py"), "gone")
        assert stopped.value.code == 2
        err = capsys.readouterr().err
        assert "seal pact: cannot read " in err and "Nothing was read." in err, err


class Test_git:
    def test_accepts_a_command_git_answers_with_its_output(self, _template):
        api = _template / "work" / "orders-api"
        assert pc.git(str(api), "rev-parse", "--abbrev-ref", "HEAD") == "main\n"

    def test_refuses_a_command_git_refuses_and_a_directory_that_is_not_there(
        self, _template, tmp_path
    ):
        api = _template / "work" / "orders-api"
        assert pc.git(str(api), "rev-parse", "--verify", "no-such-ref") is None
        assert pc.git(str(tmp_path / "gone"), "status") is None


class Test_read:
    def test_accepts_a_file_as_its_text(self, tmp_path):
        write(tmp_path, "a.md", "text\n")
        assert pc.read(str(tmp_path / "a.md")) == "text\n"

    def test_refuses_a_directory_and_bytes_that_do_not_decode(self, tmp_path):
        (tmp_path / "d").mkdir()
        (tmp_path / "b.md").write_bytes(b"\xff\n")
        assert pc.read(str(tmp_path / "d")) is None
        assert pc.read(str(tmp_path / "b.md")) is None


class Test_origin:
    def test_accepts_the_origin_remote_as_written(self, _template):
        assert pc.origin(str(_template / "work" / "orders-api")) == PACT_URL

    def test_refuses_a_repository_with_no_origin_as_empty(self, tmp_path):
        d = tmp_path / "r"
        d.mkdir()
        git(d, "init", "-q")
        assert pc.origin(str(d)) == ""


class Test_path_map:
    def test_accepts_each_row_keyed_by_the_remote_normalised(self, world):
        world.map(
            ("git@example.com:org/orders-web.git", "~/work/orders-web"),
            ("https://example.com/org/b", "/x/b"),
        )
        found, refusals = pc.path_map(config, str(world.home))
        assert refusals == []
        assert found == {
            "example.com/org/orders-web": os.path.expanduser("~/work/orders-web"),
            "example.com/org/b": "/x/b",
        }

    def test_accepts_no_map_as_an_empty_one(self, world):
        assert pc.path_map(config, str(world.home)) == ({}, [])

    @pytest.mark.parametrize(
        "text, read, said",
        [
            (
                f"{MAP_TOP}| https://example.com/org/a | /x/a |\n"
                "\nprose\n\n| https://example.com/org/b | /x/b |\n",
                ["example.com/org/a"],
                "has a `Remote | Path` table that ends above "
                "`| https://example.com/org/b | /x/b |`, a row the walk never "
                "reaches — it and every row below it would go unread",
            ),
            (
                "# Checkouts\n\nhttps://example.com/org/a /x/a\n",
                [],
                "holds no `| Remote | Path |` table",
            ),
            (
                f"{MAP_TOP}| https://example.com/org/a | /x/a |\n"
                "| git@example.com:org/a.git | /y/a |\n"
                "| https://example.com/org/b | /x/b |\n",
                ["example.com/org/b"],
                "has rows at lines 3 and 4 naming one repository, "
                "`example.com/org/a`, so neither is read — keep one",
            ),
            (
                f"{MAP_TOP}| https://example.com/org/a |  |\n"
                "| https://example.com/org/b | /x/b |\n",
                ["example.com/org/b"],
                "has a row at line 3 with an empty cell — write the remote and "
                "the path of its checkout, or delete the row",
            ),
            (
                f"{MAP_TOP}| https://example.com/org/a | /x/a |\n"
                f"\n## Laptop\n\n{MAP_TOP}| https://example.com/org/b | /x/b |\n",
                ["example.com/org/a"],
                "holds a second `| Remote | Path |` header at line 7, and the "
                "walk reads the first table only — move its rows into the first "
                "table and delete the second header",
            ),
        ],
        ids=[
            "a row past the end",
            "no table",
            "one remote twice",
            "an empty cell",
            "a second header",
        ],
    )
    def test_refuses_each_line_it_does_not_read_and_reads_the_rest(
        self, world, text, read, said
    ):
        """S2 and S3. The rows the walk read are used, and every line it did
        not is a sentence. Seen red against `977b6613`, whose loop ended the
        map at the first line it did not read and said nothing."""
        write(world.home, ".claude/agentic/pact-paths.md", text)
        found, refusals = pc.path_map(config, str(world.home))
        assert list(found) == read
        assert refusals == [said]

    @pytest.mark.parametrize("shape", ["directory", "dangling link"])
    def test_refuses_a_map_that_is_there_and_will_not_read(self, world, shape):
        """Read as empty, every signer it names would be reported missing."""
        where = world.home / ".claude" / "agentic" / "pact-paths.md"
        where.parent.mkdir(parents=True)
        if shape == "directory":
            where.mkdir()
        else:
            symlink_or_skip(str(world.tmp / "gone"), where)
        found, refusals = pc.path_map(config, str(world.home))
        assert found == {}
        assert refusals == ["is there and could not be read"]


class Test_checkout:
    def test_accepts_the_map_s_checkout_and_the_one_sibling_with_the_origin(
        self, world
    ):
        moved = world.tmp / "elsewhere" / "orders-web"
        assert pc.checkout(config, SIGNER, str(world.api), {}) == (str(world.web), None)
        moved.parent.mkdir()
        world.web.rename(moved)
        mapped = {SIGNER[1]: str(moved)}
        assert pc.checkout(config, SIGNER, str(world.api), mapped) == (str(moved), None)

    def test_refuses_a_map_line_naming_no_directory_or_another_origin(self, world):
        gone = world.tmp / "gone"
        _, why = pc.checkout(config, SIGNER, str(world.api), {SIGNER[1]: str(gone)})
        assert why == f"the map names {posix(gone)}, which is not a directory here"
        other = world.tmp / "unrelated"
        init(other, "git@example.com:org/unrelated.git")
        _, why = pc.checkout(config, SIGNER, str(world.api), {SIGNER[1]: str(other)})
        assert why == (
            f"the map names {posix(other)}, whose origin is "
            "example.com/org/unrelated rather than example.com/org/orders-web"
        )

    def test_refuses_to_guess_between_two_siblings_with_the_origin(self, world):
        init(world.web.parent / "orders-web-2", SIGNER_URL)
        path, why = pc.checkout(config, SIGNER, str(world.api), {})
        assert path is None
        assert why.startswith("2 sibling directories have its origin (")
        assert "nothing here guesses which" in why, why

    def test_refuses_the_pact_s_own_repository_and_a_signer_nowhere(self, world):
        own = (PACT_URL, config.normalise_remote(PACT_URL))
        path, why = pc.checkout(config, own, str(world.api), {})
        assert path is None
        assert why == (
            "no checkout of it was found on this machine: add "
            f"`| {PACT_URL} | <the path of its checkout> |` to "
            "~/.claude/agentic/pact-paths.md"
        )


class Test_anchor_files:
    def test_accepts_every_work_item_s_spec_in_order(self, tmp_path):
        for rel in ("threads/2-b/frame/design.md", "threads/1-a/frame/design.md"):
            write(tmp_path, rel, "x\n")
        assert pc.anchor_files(str(tmp_path)) == [
            os.path.join(str(tmp_path), "threads", "1-a", "frame", "design.md"),
            os.path.join(str(tmp_path), "threads", "2-b", "frame", "design.md"),
        ]

    def test_refuses_a_work_item_s_other_records_and_a_spec_below_one(self, tmp_path):
        for rel in (
            "threads/1-a/frame/plan.md",
            "threads/1-a/trail/phases/design.md",
            "threads/1-a/design.md",
        ):
            write(tmp_path, rel, "x\n")
        assert pc.anchor_files(str(tmp_path)) == []


class Test_History:
    def test_accepts_heads_versions_newest_first_and_the_side_version_by_its_ref(
        self, _template
    ):
        history = pc.History(str(_template / "work" / "orders-api"), PACT)
        assert [history.text(s) for s in history.head()] == [pact(V2), pact(V1)]
        other = history.other()
        assert [history.text(s) for s in other] == [pact(V3)]
        assert history.ref_holding(other[0]) == "side"

    def test_accepts_a_version_a_merge_did_not_keep_and_one_only_a_tag_holds(
        self, world
    ):
        """Main held v2; a branch cut from v1 changed the clause, and the
        merge kept the branch's text, so v2 sits on the side git's default
        history simplification does not follow. A version on a tag alone is
        another ref's."""
        api = world.api
        git(api, "switch", "-qc", "early", "main~1")
        write(api, PACT, pact("id, total, tax"))
        commit(api, "the clause, changed from v1")
        git(api, "switch", "-q", "main")
        git(api, "merge", "-q", "--no-ff", "-s", "ours", "--no-commit", "early")
        write(api, PACT, pact("id, total, tax"))
        commit(api, "merge early, keeping its clause")
        git(api, "switch", "-q", "--detach", "main~1")
        write(api, PACT, pact("id"))
        tagged = commit(api, "a version on a tag")
        git(api, "tag", "t1")
        git(api, "switch", "-q", "main")
        history = pc.History(str(api), PACT)
        assert pact(V2) in [history.text(s) for s in history.head()]
        assert tagged in history.other()
        assert history.ref_holding(tagged) == "t1"

    def test_refuses_a_path_git_never_tracked_and_names_an_unheld_commit_by_sha(
        self, world
    ):
        history = pc.History(str(world.api), "seal/nothing.md")
        assert history.head() == [] and history.other() == []
        git(world.api, "switch", "-qc", "gone")
        write(world.api, "f.txt", "x\n")
        sha = commit(world.api, "a commit no ref will hold")
        git(world.api, "switch", "-q", "main")
        git(world.api, "branch", "-qD", "gone")
        assert history.text(sha) is None
        assert pc.History(str(world.api), PACT).ref_holding(sha) == sha[:8]


class Test_clause_hash:
    def test_accepts_a_clause_hashed_over_its_lines_as_written(self):
        """#867: a heading quoted inside a closed fence is no second clause,
        and the hash is over the clause's lines as written."""
        text = "# Pact\n\n## A\n\nterms\n\n```markdown\n## A\n```\n\n## B\n\nmore\n"
        digest, why = pc.clause_hash(checker, text, "## A")
        assert why is None, why
        assert digest == checker.content_hash(checker.gfm_lines(text)[2:10])

    @pytest.mark.parametrize(
        "text, clause_path, why",
        [
            (
                pact(V2),
                "Order response shape",
                "names no heading path, and a pact clause is addressed by one",
            ),
            (
                pact(V2),
                "## Order response shape / ### Gone",
                "resolves to no clause in the pact",
            ),
            (
                pact(V2) + "\n## Order response shape\n\n### Fields\n\nagain\n",
                CLAUSE_PATH,
                "resolves to 2 clauses in the pact",
            ),
        ],
        ids=["no heading", "no clause", "two clauses"],
    )
    def test_refuses_a_clause_path_naming_no_one_clause(self, text, clause_path, why):
        assert pc.clause_hash(checker, text, clause_path) == (None, why)


class _History:
    """A stand-in for `History`: HEAD's versions and another ref's, by sha."""

    def __init__(self, head=(), other=()):
        self._head, self._other = list(head), list(other)
        self.texts = {sha: text for sha, text in (*head, *other)}

    def head(self):
        return [sha for sha, _ in self._head]

    def other(self):
        return [sha for sha, _ in self._other]

    def text(self, sha):
        return self.texts[sha]

    def ref_holding(self, sha):
        return "side"


A, B, C = "a" * 40, "b" * 40, "c" * 40


class Test_grade:
    def test_accepts_the_current_hash_and_names_where_an_older_one_came_from(self):
        history = _History(head=[(A, None), (B, pact(V1))], other=[(C, pact(V3))])
        assert pc.grade(checker, pact(V2), history, CLAUSE_PATH, clause(V2)) == (
            pc.OK,
            "",
        )
        status, detail = pc.grade(checker, pact(V2), history, CLAUSE_PATH, clause(V1))
        assert status == pc.SUPERSEDED
        assert detail == (
            "the signer was built against a superseded clause, the one at "
            f"bbbbbbbb; its hash is {clause(V2)} now. Re-read it in the signer and "
            "re-anchor"
        )
        status, detail = pc.grade(checker, pact(V2), history, CLAUSE_PATH, clause(V3))
        assert status == pc.NOT_TAKEN
        assert detail.startswith(
            "the pact has not taken the signer's recorded change: this hash is "
            "the clause on side (at cccccccc), which HEAD does not hold."
        ), detail

    def test_refuses_a_hash_no_version_gave_and_a_path_naming_no_clause(self):
        history = _History(head=[(B, pact(V1))], other=[(C, pact(V3))])
        status, detail = pc.grade(checker, pact(V2), history, CLAUSE_PATH, "deadbeef")
        assert status == pc.UNMATCHED
        # The hash is printed bare, as the `Hash` cell takes it (round 1 of
        # #913, finding 2).
        assert detail == (
            "no commit in this repository gave the clause this hash, and its "
            f"hash is {clause(V2)} now: the version was squashed away or never "
            "existed. Read both sides"
        ), detail
        status, detail = pc.grade(
            checker, pact(V2), history, "## Order response shape / ### Gone", "x"
        )
        assert (status, detail) == (
            pc.BROKEN,
            "the heading path resolves to no clause in the pact: the clause was "
            "renamed or removed. Re-coordinate the signer",
        )


class Test_check:
    def test_accepts_a_signer_citing_the_current_clause(self, world):
        """S6, S7 and S9's passes: two frames cite the current hash, one
        naming the pact by another spelling of its URL. A row naming another
        pact the signer's `Pact` row declares is passed over whatever its
        other cells hold, and neither a table nor a `pact:` token inside a
        closed fence, nor `compact:`, nor the word and its colon with a space
        on either side of the colon (#1132, S7), nor a table
        naming the pact's remote beside no heading, nor a row that misses
        twice, nor a row four columns in, by spaces or by a tab, in a frame
        holding no anchor table, is read: below a blank line it is an
        indented code block, and right under a paragraph line it is the
        paragraph text the module docstring states as a limit. Exit 0, and
        the `READ` and summary lines name the pact by its URL (contract
        rule 14)."""
        legacy = "https://example.com/org/orders-api-legacy"
        write(
            world.web,
            "seal/config.md",
            signer_config(("Pact", f"{PACT_URL}; {BILLING}; {legacy}")),
        )
        world.cite(clause(V2))
        write(
            world.web,
            SPEC_Y,
            "## Grounding\n\n"
            + anchor_table(
                ("https://example.com/org/Orders-API/", CLAUSE_PATH, clause(V2)),
                (BILLING, CLAUSE_PATH, "deadbeef"),
                (legacy, "no heading", "x"),
            )
            + "\nThe compact:x note. Read the pact: it is short. A token with a"
            + " space beside its colon, pact: abc or pact :abc, is prose.\n\n```\n"
            + anchor_table((PACT_URL, CLAUSE_PATH, "x"))
            + 'pact:orders-api/"## A"@1a2b3c4d\n```\n\n'
            + f"| Repository | Role |\n|---|---|\n| {PACT_URL} | the pact |\n\n"
            # A row that misses twice, a near-miss header over a remote one
            # letter off, is no anchor's shape.
            + "| pact | clause | hash |\n|---|---|---|\n"
            + f"| git@example.com:org/ordres-api.git | {CLAUSE_PATH} | deadbeef |\n",
        )
        # A frame that cites no pact holds no anchor table, and says nothing;
        # a row in an indented code block, four spaces or a tab in, is no row,
        # and the same tab row right under a paragraph line is the stated
        # limit (round 2, finding 1).
        write(
            world.web,
            "seal/threads/1790000002-z/frame/design.md",
            f"# Z\n\nx\n\n    | {PACT_URL} | {CLAUSE_PATH} | deadbeef |\n"
            f"\n\t| {PACT_URL} | {CLAUSE_PATH} | deadbeef |\n"
            f"\n  \t| {PACT_URL} | {CLAUSE_PATH} | deadbeef |\n"
            f"\nx\n\t| {PACT_URL} | {CLAUSE_PATH} | deadbeef |\n",
        )
        code, out = world.run()
        assert code == 0, out
        assert (
            f"READ {SIGNER_URL} {posix(world.web)} — 2 pact anchors naming this pact"
        ) in out, out
        assert out.endswith(
            f"seal pact: the pact at {PACT_URL} — 1 of 1 signer read · 2 ok · 0 "
            "superseded · 0 not taken · 0 unmatched · 0 broken"
        ), out
        assert "heads its table" not in out and "REFUSED" not in out, out

    @pytest.mark.parametrize(
        "fields, clause_path, code, line",
        [
            (V1, CLAUSE_PATH, 1, "SUPERSEDED {s} {spec}:{n} `{c}` — the signer was"),
            (V3, CLAUSE_PATH, 1, "NOT TAKEN {s} {spec}:{n} `{c}` — the pact has not"),
            (None, CLAUSE_PATH, 1, "UNMATCHED {s} {spec}:{n} `{c}` — no commit in"),
            (
                V2,
                "## Order response shape / ### Gone",
                2,
                "BROKEN {s} {spec}:{n} `{c}` — the heading path resolves to no clause",
            ),
        ],
        ids=["superseded", "not taken", "unmatched", "broken"],
    )
    def test_refuses_each_anchor_that_does_not_read_ok(
        self, world, fields, clause_path, code, line
    ):
        """S6: each line that is not `OK` names the frame, the row's line and
        the clause path."""
        world.cite(clause(fields) if fields else "deadbeef", clause_path)
        got, out = world.run()
        assert got == code, out
        said = line.format(s=SIGNER_URL, spec=SPEC, n=ANCHOR_LINE, c=clause_path)
        assert said in out, out

    def test_refuses_a_mismatch_under_local_mode_as_unmatched_and_says_why(self, world):
        common = git(world.api, "rev-parse", "--git-common-dir")
        local = os.path.join(str(world.api), common, "seal")
        os.makedirs(local)
        os.replace(str(world.api / PACT), os.path.join(local, "pact.md"))
        os.replace(
            str(world.api / "seal" / "README.md"), os.path.join(local, "README.md")
        )
        os.rmdir(str(world.api / "seal"))
        world.cite(clause(V1))
        code, out = world.run()
        assert code == 1, out
        assert f"UNMATCHED {SIGNER_URL} {SPEC}:{ANCHOR_LINE} `{CLAUSE_PATH}`" in out, (
            out
        )
        assert out.endswith(
            "The pact sits under the git directory (local mode), so it has no "
            "history and every mismatch reads unmatched"
        ), out

    def test_accepts_a_signer_the_map_finds_where_no_sibling_is(self, world):
        moved = world.tmp / "elsewhere" / "orders-web"
        moved.parent.mkdir()
        world.web.rename(moved)
        code, out = world.run()
        assert code == 1, out
        assert (
            f"NOT FOUND {SIGNER_URL} — no checkout of it was found on this "
            f"machine: add `| {SIGNER_URL} | <the path of its checkout> |` to "
            "~/.claude/agentic/pact-paths.md"
        ) in out, out
        world.map(("git@example.com:org/orders-web.git", moved))
        world.web = moved
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 0, out

    def test_refuses_a_second_signer_not_found_and_counts_both(self, world):
        write(world.api, PACT, pact(V2, (SIGNER_URL, MOBILE_URL)))
        commit(world.api, "a second signer")
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 1, out
        assert f"NOT FOUND {MOBILE_URL} — " in out, out
        assert f"seal pact: the pact at {PACT_URL} — 1 of 2 signers read · " in out, out

    @pytest.mark.parametrize(
        "header", ["Signer", "Signatory"], ids=["Signer", "old_header"]
    )
    def test_refuses_a_pact_listing_its_own_repository_by_the_table_it_holds(
        self, world, header
    ):
        """Not `NOT FOUND`, which would send a person looking for a checkout
        of the repository they stand in; the sentence calls the table by the
        header the pact holds."""
        text = pact(V2, (SIGNER_URL, PACT_URL))
        write(world.api, PACT, text if header == "Signer" else old_header(text))
        commit(world.api, "the pact lists itself")
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 2, out
        assert (
            f"REFUSED {PACT_URL} seal/pact.md — the pact lists its own repository; "
            f"the `{header}` table lists every OTHER signer, so take this row out"
        ) in out, out
        assert "NOT FOUND" not in out, out

    def test_refuses_a_signer_row_the_table_walk_cannot_read(self, world):
        """The row with no closing pipe is refused at the pact, so a signer
        below it is never reported as clean by omission."""
        text = pact(V2).replace(
            f"| {SIGNER_URL} |\n", f"| {SIGNER_URL} |\n| {MOBILE_URL}\n"
        )
        write(world.api, PACT, text)
        commit(world.api, "a row with no closing pipe")
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 2, out
        assert (
            "REFUSED seal/pact.md — the pact has a `Signer` table that stops at "
            f"`| {MOBILE_URL}`"
        ) in out, out

    @pytest.mark.parametrize("side", ["no seal root", "no Pact row"])
    def test_refuses_a_relationship_recorded_on_one_side(self, world, side):
        if side == "no seal root":
            shutil.rmtree(world.web / "seal")
            where, said = posix(world.web), "it has no seal/ root to name this pact in"
        else:
            write(world.web, "seal/config.md", signer_config())
            where = "seal/config.md"
            said = f"its config names no `Pact` row for {PACT_URL}"
        code, out = world.run()
        assert code == 2, out
        assert (
            f"ONE-SIDED {SIGNER_URL} {where} — the pact lists it, and {said}: the "
            "relationship is recorded on one side only"
        ) in out, out

    @pytest.mark.parametrize(
        "row, said",
        [
            ((f"{PACT_URL} x", CLAUSE_PATH, "1a2b3c4d"), NOT_ONE_URL),
            ((f"`{PACT_URL}`", CLAUSE_PATH, "1a2b3c4d"), NOT_ONE_URL),
            (("orders-api", CLAUSE_PATH, "1a2b3c4d"), NOT_ONE_URL),
            ((PACT_URL, "Order response shape", "1a2b3c4d"), NO_HEADING),
            ((PACT_URL, f"`{CLAUSE_PATH}`", "1a2b3c4d"), NO_HEADING),
            ((PACT_URL, CLAUSE_PATH, "1A2B3C4D"), NOT_A_HASH),
            ((PACT_URL, CLAUSE_PATH, "1a2b3c"), NOT_A_HASH),
            (
                ("git@example.com:org/ordres-api.git", CLAUSE_PATH, "1a2b3c4d"),
                UNDECLARED.format(cell="git@example.com:org/ordres-api.git"),
            ),
            (
                ("git@git.example.com:org/orders-api.git", CLAUSE_PATH, "1a2b3c4d"),
                UNDECLARED.format(cell="git@git.example.com:org/orders-api.git"),
            ),
        ],
        ids=[
            "a space in the Pact cell",
            "a backtick in the Pact cell",
            "no host and path",
            "a clause path with no heading",
            "a clause path in backticks",
            "an uppercase hash",
            "a short hash",
            "a remote one letter off",
            "the pact's path on another host",
        ],
    )
    def test_refuses_a_row_it_cannot_grade_at_its_line(self, world, row, said):
        """S8: each shape is refused at the row's line, at exit 2. Seen red
        against `977b6613`, which read no anchor table and exited 0. A
        remote the signer's `Pact` row does not declare is graded by no
        `seal pact`, since another pact's reports the signer `ONE-SIDED`
        (#1132, S1); those two were seen red against `28edee12`, which
        passed the row over and exited 0."""
        write(world.web, SPEC, anchor_table(row))
        code, out = world.run()
        assert code == 2, out
        assert f"REFUSED {SIGNER_URL} {SPEC}:{ANCHOR_LINE} — {said}" in out, out

    @pytest.mark.parametrize(
        "text, line",
        [
            ('| `pact:orders-api/"## A"@1a2b3c4d` | the field list |\n', 1),
            ('# Grounding\n\nBuilt against pact:orders-api/"## A"@1a2b3c4d.\n', 3),
            ("| `PACT:abc` | the field list |\n", 1),
            ("# Grounding\n\nBuilt against PACT:abc.\n", 3),
            ("| Pact:abc | the field list |\n", 1),
            ("# Grounding\n\nBuilt against Pact:abc.\n", 3),
            ('| PACT:orders-api/"## A"@1a2b3c4d | the field list |\n', 1),
            ('# Grounding\n\nBuilt against PACT:orders-api/"## A"@1a2b3c4d.\n', 3),
        ],
        ids=[
            "in a table cell",
            "in prose",
            "upper case in a table cell",
            "upper case in prose",
            "capitalised in a table cell",
            "capitalised in prose",
            "an upper-case anchor in a table cell",
            "an upper-case anchor in prose",
        ],
    )
    def test_refuses_the_inline_anchor_naming_the_row_to_write(self, world, text, line):
        """S9 and `questions.md` Q1's default: the inline anchor is refused
        at its line, at exit 2, and the line names the row to write. Seen
        red against `977b6613`, which graded the token. The token is read in
        any case (#1132, S6); the six ids that spell it otherwise were seen
        red against `28edee12`, which read `pact:` alone and exited 0."""
        write(world.web, SPEC, text)
        code, out = world.run()
        assert code == 2, out
        assert f"REFUSED {SIGNER_URL} {SPEC}:{line} — {INLINE}" in out, out

    @pytest.mark.parametrize(
        "text, said",
        [
            (
                anchor_table((PACT_URL, CLAUSE_PATH, "1a2b3c4d"))
                + "\n## More\n\n"
                + anchor_table((PACT_URL, CLAUSE_PATH, "1a2b3c4d")),
                "the frame holds a second `| Pact | Clause | Hash |` header at "
                "line 7, and the walk reads the first table only — move its rows "
                "into the first table and delete the second header",
            ),
            (
                anchor_table((PACT_URL, CLAUSE_PATH, "1a2b3c4d"))
                + "\n"
                + anchor_table((PACT_URL, CLAUSE_PATH, "1a2b3c4d")),
                "the frame holds a second `| Pact | Clause | Hash |` header at "
                "line 5, and the walk reads the first table only — move its rows "
                "into the first table and delete the second header",
            ),
            (
                anchor_table((PACT_URL, CLAUSE_PATH, "1a2b3c4d")) + "| x | y |\n",
                "the frame has a `Pact | Clause | Hash` table that stops at "
                "`| x | y |`, which is not a 3-cell row written `| … | … | … |` — "
                "every row below it would go unread",
            ),
            (
                anchor_table((PACT_URL, CLAUSE_PATH, "1a2b3c4d"))
                + "\n| a | b |\n|---|\n",
                "the frame has a `Pact | Clause | Hash` table that ends above "
                "`| a | b |`, a row the walk never reaches — it and every row "
                "below it would go unread",
            ),
            (
                anchor_table((PACT_URL, CLAUSE_PATH, "1a2b3c4d"))
                + "\n| a | b |\n<!-- a note -->\n|---|---|\n",
                "the frame has a `Pact | Clause | Hash` table that ends above "
                "`| a | b |`, a row the walk never reaches — it and every row "
                "below it would go unread",
            ),
            (
                anchor_table((PACT_URL, CLAUSE_PATH, "1a2b3c4d"))
                + "\n| a | b |\n|---|---|\n| c | d |\n\n"
                + f"| {PACT_URL} | {CLAUSE_PATH} | 00000000 |\n",
                "the frame has a `Pact | Clause | Hash` table that ends above "
                f"`| {PACT_URL} | {CLAUSE_PATH} | 00000000 |`, a row the walk "
                "never reaches — it and every row below it would go unread",
            ),
            (
                anchor_table((PACT_URL, CLAUSE_PATH, "1a2b3c4d"))
                + "\n| a | b |\n|---|---|\n| c | d |\n<!-- a note -->\n"
                + f"| {PACT_URL} | {CLAUSE_PATH} | 00000000 |\n",
                "the frame has a `Pact | Clause | Hash` table that ends above "
                f"`| {PACT_URL} | {CLAUSE_PATH} | 00000000 |`, a row the walk "
                "never reaches — it and every row below it would go unread",
            ),
            (
                anchor_table((PACT_URL, CLAUSE_PATH, "1a2b3c4d"))
                + f"\n| {PACT_URL} | {CLAUSE_PATH} | 1a2b3c4d |\n",
                "the frame has a `Pact | Clause | Hash` table that ends above "
                f"`| {PACT_URL} | {CLAUSE_PATH} | 1a2b3c4d |`, a row the walk "
                "never reaches — it and every row below it would go unread",
            ),
        ],
        ids=[
            "a second table",
            "a second table under a blank line",
            "a row the walk stops at",
            "a row under a delimiter of another width",
            "a row whose delimiter a comment parts from it",
            "a row below another table",
            "a row a comment parts from another table",
            "a row under a blank line",
        ],
    )
    def test_refuses_an_anchor_row_nobody_reads(self, world, text, said):
        """A row the walk does not reach would read as a signer citing
        nothing, so the frame is refused at exit 2. A second anchor table is
        named as one wherever it stands. A line under the table that opens no
        table of its own, a header with a delimiter row of its width directly
        under it, is a row nobody reads, and so is a row below such a table
        and above the next heading (round 2 of #913, finding 2). The frame
        is refused once: the scan for a row no anchor table holds runs only
        where the walk refused nothing, so a row the walk's refusal names is
        not refused a second time (#1132, S5)."""
        write(world.web, SPEC, text)
        code, out = world.run()
        assert code == 2, out
        assert f"REFUSED {SIGNER_URL} {SPEC} — {said}" in out, out
        assert out.count(f"REFUSED {SIGNER_URL} {SPEC}") == 1, out

    @pytest.mark.parametrize(
        "text, line",
        [
            (
                "| pact | clause | hash |\n|---|---|---|\n"
                f"| {PACT_URL} | {CLAUSE_PATH} | 1a2b3c4d |\n",
                3,
            ),
            (
                "| Pact | Clause | Hashes |\n|---|---|---|\n"
                f"| {PACT_URL} | {CLAUSE_PATH} | 1a2b3c4d |\n",
                3,
            ),
            (
                "| **Pact** | Clause | Hash |\n|---|---|---|\n"
                f"| {PACT_URL} | {CLAUSE_PATH} | 1a2b3c4d |\n",
                3,
            ),
            (
                "| Clause | Pact | Hash |\n|---|---|---|\n"
                f"| {CLAUSE_PATH} | {PACT_URL} | 1a2b3c4d |\n",
                3,
            ),
            (
                "| Pact | Clause | Hash | Note |\n|---|---|---|---|\n"
                f"| {PACT_URL} | {CLAUSE_PATH} | 1a2b3c4d | x |\n",
                3,
            ),
            (
                "Pact | Clause | Hash\n---|---|---\n"
                f"{PACT_URL} | {CLAUSE_PATH} | 1a2b3c4d\n",
                3,
            ),
            (
                "| `Pact` | `Clause` | `Hash` |\n|---|---|---|\n"
                f"| {PACT_URL} | {CLAUSE_PATH} | 1a2b3c4d |\n",
                3,
            ),
            (
                "| Pact | Clauses | Hash |\n|---|---|---|\n"
                f"| {PACT_URL} | {CLAUSE_PATH} | 1a2b3c4d |\n",
                3,
            ),
            (f"# Grounding\n\n| {PACT_URL} | {CLAUSE_PATH} | 1a2b3c4d |\n", 3),
            (
                anchor_table((PACT_URL, CLAUSE_PATH, "1a2b3c4d"))
                + "\n## More\n\n| pact | clause | hash |\n|---|---|---|\n"
                + f"| {PACT_URL} | {CLAUSE_PATH} | 1a2b3c4d |\n",
                9,
            ),
            (
                "| pact | clause | hash |\n|---|---|---|\n"
                f"| {BILLING} | {CLAUSE_PATH} | 1a2b3c4d |\n",
                3,
            ),
        ],
        ids=[
            "a header in lower case",
            "a plural Hash header",
            "a header in emphasis",
            "a reordered header",
            "a header with a fourth column",
            "a table with no outer pipes",
            "a header in code spans",
            "a plural Clause header",
            "a row with no header",
            "a near miss below the anchor table",
            "a row naming another pact the signer declares",
        ],
    )
    def test_refuses_an_anchor_row_no_anchor_table_holds(self, world, text, line):
        """#1132, S3: a row naming a pact the signer declares in one cell and
        a heading path in another is refused at its own line, whatever
        header it stands under, or with none, because the walk reads the
        `| Pact | Clause | Hash |` header alone. Seen red against
        `28edee12`, where each frame printed nothing and the run exited 0.
        The signer declares a second pact, and a row naming it is refused
        too: no `seal pact` grades it (round 1, finding 2; seen red with the
        scan narrowed to this pact)."""
        write(
            world.web,
            "seal/config.md",
            signer_config(("Pact", f"{PACT_URL}; {BILLING}")),
        )
        write(world.web, SPEC, text)
        code, out = world.run()
        assert code == 2, out
        assert f"REFUSED {SIGNER_URL} {SPEC}:{line} — {OUTSIDE_TABLE}" in out, out

    @pytest.mark.parametrize(
        "between",
        ["\n", "\nThe clauses:\n", "***\n"],
        ids=["a blank line", "a sentence", "a thematic break"],
    )
    def test_accepts_an_anchor_table_above_another_table_in_its_section(
        self, world, between
    ):
        """Round 1 of #913, finding 1, and round 2's: under `## Grounding`
        the anchor table stands above the policy table
        `templates/records/sdd-design.md` writes, and GitHub renders two
        tables whatever stands between them. The anchor row is graded and
        nothing is refused. The blank-line shape was seen red at `29e1b040`;
        the sentence and the thematic break were seen red at `49bb6ba5`,
        which asked for a blank line above the other table's header."""
        write(
            world.web,
            SPEC,
            "# Feature\n\n## Grounding\n\n"
            + anchor_table((PACT_URL, CLAUSE_PATH, clause(V2)))
            + between
            + "| Policy clause | What it fixes for this work |\n|---|---|\n"
            + "| a | b |\n\n## Scope\n\nx\n",
        )
        code, out = world.run()
        assert code == 0, out
        assert "REFUSED" not in out and " 1 ok " in out, out

    @pytest.mark.parametrize("shape", ["directory", "undecodable"])
    def test_refuses_a_signer_config_that_will_not_read(self, world, shape):
        """Both unreadable shapes reach it as `UNREADABLE` at exit 2 through
        `hooks/lib/config.py#config_text`, named relative to the signer's
        checkout and in POSIX form."""
        cfg = world.web / "seal" / "config.md"
        text = cfg.read_bytes()
        cfg.unlink()
        if shape == "directory":
            cfg.mkdir()
        else:
            cfg.write_bytes(text + b"| Record language | \xff |\n")
        code, out = world.run()
        assert code == 2, out
        assert f"UNREADABLE {SIGNER_URL} seal/config.md — could not be read" in out, out

    def test_refuses_an_anchor_file_and_a_pact_that_will_not_read(self, world):
        (world.web / SPEC).mkdir(parents=True)
        code, out = world.run()
        assert code == 2, out
        assert f"UNREADABLE {SIGNER_URL} {SPEC} — could not be read" in out, out
        (world.api / PACT).unlink()
        (world.api / PACT).mkdir()
        code, out = world.run()
        assert code == 2, out
        assert out == "UNREADABLE seal/pact.md — the pact could not be read", out

    def test_refuses_a_map_that_will_not_read(self, world):
        """S4: the path is printed once, and the sentence reads after the
        words `the map` like every other refusal of the map."""
        (world.home / ".claude" / "agentic" / "pact-paths.md").mkdir(parents=True)
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 2, out
        assert f"{MAP_REFUSED}is there and could not be read" in out, out
        assert out.count("pact-paths.md") == 1, out

    def test_refuses_a_map_row_past_the_tables_end_and_reads_the_row_above(self, world):
        """S2. The signer the row above names is found and read, and the row
        below the paragraph is named at exit 2. Seen red against `977b6613`,
        which dropped that row with nothing printed and exited 0."""
        moved = world.tmp / "elsewhere" / "orders-web"
        moved.parent.mkdir()
        world.web.rename(moved)
        world.web = moved
        world.cite(clause(V2))
        write(
            world.home,
            ".claude/agentic/pact-paths.md",
            f"{MAP_TOP}| {SIGNER_URL} | {moved} |\n"
            "\nprose\n\n| https://example.com/org/b | /x/b |\n",
        )
        code, out = world.run()
        assert code == 2, out
        assert f"READ {SIGNER_URL} {posix(moved)} — 1 pact anchor" in out, out
        assert (
            f"{MAP_REFUSED}has a `Remote | Path` table that ends above "
            "`| https://example.com/org/b | /x/b |`, a row the walk never reaches"
        ) in out, out

    @pytest.mark.parametrize(
        "text, said",
        [
            (
                f"{MAP_TOP}\n{MAP_TOP}",
                "has a `Remote | Path` table that ends above `| Remote | Path |`",
            ),
        ],
        ids=["a second header the walk names"],
    )
    def test_refuses_each_map_line_it_does_not_read_at_exit_2(self, world, text, said):
        """S3: a second header the walk already refuses is named once, at
        exit 2. The other shapes are `Test_path_map`'s, and `check` prints
        each of them through the one loop the two cases above hold."""
        world.cite(clause(V2))
        write(world.home, ".claude/agentic/pact-paths.md", text)
        code, out = world.run()
        assert code == 2, out
        assert f"{MAP_REFUSED}{said}" in out, out
        assert out.count(MAP_REFUSED) == 1, out

    def test_refuses_a_root_outside_git_no_pact_and_no_origin(self, world):
        """Exit 2 for each way the pact's repository cannot be read."""
        code, out = world.run(root=world.tmp)
        assert code == 2 and out.endswith(
            "is not in a git repository — nothing was read"
        ), out
        code, out = world.run(root=world.web)
        assert code == 2 and "holds no seal/pact.md, so there is no pact" in out, out
        git(world.api, "remote", "remove", "origin")
        code, out = world.run()
        assert code == 2, out
        assert out.endswith(
            "has no origin remote, so no pact anchor can be matched to the pact "
            "— set `origin` and run it again"
        ), out


class Test_renamed:
    def test_accepts_the_header_0_18_wrote_with_one_line_naming_it(self, world):
        """S2 of #822: the pact headed `| Signatory |` reads identically, one
        line before its `READ` line names the file, both headers and the
        release, and the exit is the new header's."""
        world.cite(clause(V2))
        new_code, new_out = world.run()
        write(world.api, PACT, old_header(pact(V2)))
        commit(world.api, "the pact as 0.18.0 began it")
        code, out = world.run()
        rename = (
            "seal pact: seal/pact.md heads its table `| Signatory |`, the word "
            "before 0.19.0 — `| Signer |` is the header now; rename it when the "
            "file is next edited"
        )
        assert code == new_code == 0, (out, new_out)
        assert out.count(rename) == 1, out
        assert out.index(rename) < out.index(f"READ {SIGNER_URL}"), out
        assert out.replace(rename + " ", "") == new_out, (out, new_out)

    @pytest.mark.parametrize("header", [config.SIGNER_HEADER, None])
    def test_refuses_to_name_a_rename_for_the_header_now_or_none(self, header):
        said = []
        pc.renamed(config, PACT, header, config.SIGNER_HEADER, said.append)
        assert said == []


@pytest.fixture
def printed(monkeypatch):
    """What `main` prints. `check` binds `sys.stdout` as it stood when the
    module loaded, under pytest's collection, so its default is replaced."""
    import io

    out = io.StringIO()
    monkeypatch.setattr(pc.check, "__defaults__", (out, None))
    return out


class Test_main:
    def test_accepts_the_current_directory_as_the_pact_s_repository(
        self, world, monkeypatch, printed
    ):
        world.cite(clause(V2))
        monkeypatch.setenv("HOME", str(world.home))
        monkeypatch.setenv("USERPROFILE", str(world.home))
        monkeypatch.chdir(world.api)
        assert pc.main([]) == 0
        assert "1 ok" in printed.getvalue()

    def test_refuses_a_root_named_outside_any_repository(self, world, printed):
        assert pc.main([str(world.tmp)]) == 2
        assert "is not in a git repository" in printed.getvalue()


# For #923: it reads this module's source.


def test_no_line_formats_a_path_without_the_helper():
    """S6, the class: every `{…}` in an f-string of `pact_check.py` that names
    a path variable goes through `shown`. Restoring the old
    `{their_home}/{CONFIG_FILE}` puts one back, and this names it."""
    import ast

    with open(SCRIPT, encoding="utf-8") as handle:
        tree = ast.parse(handle.read())
    # `where` is not among them: every value it holds is built by `shown`
    # or is a literal `seal/...` label.
    paths = {
        "path",
        "repo",
        "root",
        "pact_path",
        "their_home",
        "their_repo",
        "file_path",
        "home",
        "home_dir",
        "h",
        "hits",
    }
    raw = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.JoinedStr):
            continue
        for part in node.values:
            if (
                isinstance(part, ast.FormattedValue)
                and isinstance(part.value, ast.Name)
                and part.value.id in paths
            ):
                raw.append((node.lineno, part.value.id))
    assert raw == [], raw


test_census = census_case(TARGET)
