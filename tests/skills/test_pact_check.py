"""`skills/verify/scripts/pact_check.py`, one class per function.

Rebuilt by #942's phase 5. The printed paths, the near-miss rule, the
anchor grammar, a clause's hash and an anchor's grade run in the process on
text, a grade against a stand-in history. The checkout search, the history
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
    LOCATOR,
    MOBILE_URL,
    PACT,
    PACT_URL,
    ROOT,
    SIGNER_URL,
    SPEC,
    V1,
    V2,
    V3,
    census_case,
    clause,
    grounding_row,
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

SIGNER = (SIGNER_URL, config.normalise_remote(SIGNER_URL), "orders-web")
SPEC_Y = "seal/threads/1790000001-y/frame/design.md"


def posix(path):
    """A path as `seal pact` prints one outside HOME: every separator `/`."""
    return str(path).replace(os.sep, "/")


class Test_module:
    @pytest.mark.parametrize(
        "anchor",
        [
            'pact:orders-api#"## Order response shape / ### Fields"@1a2b3c4d',
            "pact:orders-api/## Order response shape@1a2b3c4d",
            'pact:orders-api/"## Order response shape / ### Fields"',
            f"pact:orders-api{LOCATOR}@1a2b3c4d",
            f"pact:orders-api:{LOCATOR}@1a2b3c4d",
            f"pact:orders-api {LOCATOR}@1a2b3c4d",
            "pact:orders-api@1a2b3c4d",
            f"pact:orders-api.{LOCATOR}@1a2b3c4d",
            f"pact:orders-api-{LOCATOR}@1a2b3c4d",
            f"pact:orders-api_{LOCATOR}@1a2b3c4d",
            f"pact:orders-api./{LOCATOR}@1a2b3c4d",
            f"pact:orders-api-/{LOCATOR}@1a2b3c4d",
            f"pact:orders-api_/{LOCATOR}@1a2b3c4d",
            "pact:orders-api.@1a2b3c4d",
            "The clauses sit under pact:orders-api/ in that repository.",
        ],
        ids=[
            "hash for slash",
            "no quotes",
            "no hash",
            "no slash",
            "a colon for the slash",
            "a space for the slash",
            "no heading path",
            "a dot for the slash",
            "a hyphen for the slash",
            "an underscore for the slash",
            "a dot before the slash",
            "a hyphen before the slash",
            "an underscore before the slash",
            "a dot, no heading path",
            "half typed in prose",
        ],
    )
    def test_accepts_each_attempt_at_an_anchor_as_beginning_one(self, anchor):
        """The grammar's one rule: each of these begins an anchor naming the
        pact, or the pact and one mark, and does not complete one, so
        `check` refuses it."""
        assert not checker.PACT_ANCHOR_RE.search(anchor) or not any(
            m.group("name") == "orders-api"
            for m in checker.PACT_ANCHOR_RE.finditer(anchor)
        )
        begun = [m.group("name") for m in pc.PACT_MENTION_RE.finditer(anchor)]
        assert any(n == "orders-api" or pc.near_miss(n, "orders-api") for n in begun)

    @pytest.mark.parametrize(
        "body",
        [
            "This work item signs pact:orders-api, the order contract.",
            "This work item signs `pact:orders-api`.",
            'Cite each clause as `pact:orders-api/"<heading path>"@<hash>`.',
            "See pact:orders-api.",
        ],
        ids=[
            "prose",
            "code span",
            "the form with its placeholders",
            "a sentence's end",
        ],
    )
    def test_refuses_to_read_prose_naming_the_pact_as_an_attempt(self, body):
        assert not pc.PACT_MENTION_RE.search(body)

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
        assert hasattr(pc.load(pc.CHECKER, "evidence_loaded_again"), "PACT_ANCHOR_RE")

    def test_refuses_a_module_that_is_not_there_with_a_sentence(self, tmp_path, capsys):
        with pytest.raises(SystemExit) as stopped:
            pc.load(str(tmp_path / "gone.py"), "gone")
        assert stopped.value.code == 2
        err = capsys.readouterr().err
        assert "seal pact: cannot read " in err and "Nothing was read." in err, err


class Test_near_miss:
    @pytest.mark.parametrize("said", ["orders-api.", "orders-api-", "ORDERS-API_"])
    def test_accepts_the_name_and_one_mark_the_name_class_holds(self, said):
        assert pc.near_miss(said, "orders-api")

    @pytest.mark.parametrize(
        "said", ["orders-api", "orders-api.-", "orders-apix", "orders-ap."]
    )
    def test_refuses_the_name_itself_two_marks_or_another_character(self, said):
        assert not pc.near_miss(said, "orders-api")


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
        found, refusal = pc.path_map(config, str(world.home))
        assert refusal is None
        assert found == {
            "example.com/org/orders-web": os.path.expanduser("~/work/orders-web"),
            "example.com/org/b": "/x/b",
        }

    def test_accepts_no_map_as_an_empty_one(self, world):
        assert pc.path_map(config, str(world.home)) == ({}, None)

    def test_refuses_to_read_a_row_past_the_tables_end(self, world):
        write(
            world.home,
            ".claude/agentic/pact-paths.md",
            "| Remote | Path |\n|---|---|\n| https://example.com/org/a | /x/a |\n"
            "\nprose\n\n| https://example.com/org/b | /x/b |\n",
        )
        found, _ = pc.path_map(config, str(world.home))
        assert list(found) == ["example.com/org/a"]

    @pytest.mark.parametrize("shape", ["directory", "dangling link"])
    def test_refuses_a_map_that_is_there_and_will_not_read(self, world, shape):
        """Read as empty, every signer it names would be reported missing."""
        where = world.home / ".claude" / "agentic" / "pact-paths.md"
        where.parent.mkdir(parents=True)
        if shape == "directory":
            where.mkdir()
        else:
            symlink_or_skip(str(world.tmp / "gone"), where)
        found, refusal = pc.path_map(config, str(world.home))
        assert found == {}
        assert refusal == (
            "~/.claude/agentic/pact-paths.md is there and could not be read"
        )


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
        own = (PACT_URL, config.normalise_remote(PACT_URL), "orders-api")
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
        digest, why = pc.clause_hash(checker, text, '"## A"')
        assert why is None, why
        assert digest == checker.content_hash(checker.gfm_lines(text)[2:10])

    @pytest.mark.parametrize(
        "text, locator, why",
        [
            (
                pact(V2),
                '"Order response shape"',
                "names no heading path, and a pact clause is addressed by one",
            ),
            (
                pact(V2),
                '"## Order response shape / ### Gone"',
                "resolves to no clause in the pact",
            ),
            (
                pact(V2) + "\n## Order response shape\n\n### Fields\n\nagain\n",
                LOCATOR,
                "resolves to 2 clauses in the pact",
            ),
        ],
        ids=["no heading", "no clause", "two clauses"],
    )
    def test_refuses_a_locator_naming_no_one_clause(self, text, locator, why):
        assert pc.clause_hash(checker, text, locator) == (None, why)


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
        assert pc.grade(checker, pact(V2), history, LOCATOR, clause(V2)) == (
            pc.OK,
            "",
        )
        status, detail = pc.grade(checker, pact(V2), history, LOCATOR, clause(V1))
        assert status == pc.SUPERSEDED
        assert detail == (
            "the signer was built against a superseded clause, the one at "
            f"bbbbbbbb; it reads @{clause(V2)} now. Re-read it in the signer and "
            "re-anchor"
        )
        status, detail = pc.grade(checker, pact(V2), history, LOCATOR, clause(V3))
        assert status == pc.NOT_TAKEN
        assert detail.startswith(
            "the pact has not taken the signer's recorded change: this hash is "
            "the clause on side (at cccccccc), which HEAD does not hold."
        ), detail

    def test_refuses_a_hash_no_version_gave_and_a_path_naming_no_clause(self):
        history = _History(head=[(B, pact(V1))], other=[(C, pact(V3))])
        status, detail = pc.grade(checker, pact(V2), history, LOCATOR, "deadbeef")
        assert status == pc.UNMATCHED
        assert detail.endswith("Read both sides"), detail
        status, detail = pc.grade(
            checker, pact(V2), history, '"## Order response shape / ### Gone"', "x"
        )
        assert (status, detail) == (
            pc.BROKEN,
            "the heading path resolves to no clause in the pact: the clause was "
            "renamed or removed. Re-coordinate the signer",
        )


class Test_check:
    def test_accepts_a_signer_citing_the_current_clause(self, world):
        """S12: two specs cite the current hash, one of them in the pact's
        name as another case spells it, and an anchor of another pact and one
        shown in a fence are not read: exit 0 and the summary line."""
        world.cite(clause(V2))
        write(
            world.web,
            SPEC_Y,
            grounding_row(f"pact:ORDERS-API/{LOCATOR}@{clause(V2)}")
            + grounding_row(f"pact:billing/{LOCATOR}@deadbeef")
            + grounding_row(f"pact:orders-api-legacy-/{LOCATOR}@deadbeef")
            + f"```\npact:orders-api/{LOCATOR}@deadbeef\n```\n",
        )
        code, out = world.run()
        assert code == 0, out
        assert (
            f"READ {SIGNER_URL} {posix(world.web)} — 2 pact anchors naming `orders-api`"
        ) in out, out
        assert out.endswith(
            "seal pact: the pact `orders-api` — 1 of 1 signer read · 2 ok · 0 "
            "superseded · 0 not taken · 0 unmatched · 0 broken"
        ), out
        assert "heads its table" not in out and "does not parse" not in out, out

    @pytest.mark.parametrize(
        "fields, locator, code, line",
        [
            (V1, LOCATOR, 1, "SUPERSEDED {s} {spec}:1 {a} — the signer was built"),
            (V3, LOCATOR, 1, "NOT TAKEN {s} {spec}:1 {a} — the pact has not taken"),
            (None, LOCATOR, 1, "UNMATCHED {s} {spec}:1 {a} — no commit in this"),
            (
                V2,
                '"## Order response shape / ### Gone"',
                2,
                "BROKEN {s} {spec}:1 {a} — the heading path resolves to no clause",
            ),
        ],
        ids=["superseded", "not taken", "unmatched", "broken"],
    )
    def test_refuses_each_anchor_that_does_not_read_ok(
        self, world, fields, locator, code, line
    ):
        anchor = world.cite(clause(fields) if fields else "deadbeef", locator)
        got, out = world.run()
        assert got == code, out
        assert line.format(s=SIGNER_URL, spec=SPEC, a=anchor) in out, out

    def test_refuses_a_mismatch_under_local_mode_as_unmatched_and_says_why(self, world):
        common = git(world.api, "rev-parse", "--git-common-dir")
        local = os.path.join(str(world.api), common, "seal")
        os.makedirs(local)
        os.replace(str(world.api / PACT), os.path.join(local, "pact.md"))
        os.replace(
            str(world.api / "seal" / "README.md"), os.path.join(local, "README.md")
        )
        os.rmdir(str(world.api / "seal"))
        anchor = world.cite(clause(V1))
        code, out = world.run()
        assert code == 1, out
        assert f"UNMATCHED {SIGNER_URL} {SPEC}:1 {anchor}" in out, out
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
        assert "seal pact: the pact `orders-api` — 1 of 2 signers read · " in out, out

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
        "anchor",
        [
            'pact:orders-api#"## Order response shape / ### Fields"@1a2b3c4d',
            "pact:orders-api/## Order response shape@1a2b3c4d",
            'pact:orders-api/"## Order response shape / ### Fields"',
            f"pact:orders-api {LOCATOR}@1a2b3c4d",
            "pact:orders-api@1a2b3c4d",
            f"pact:orders-api.{LOCATOR}@1a2b3c4d",
            f"pact:orders-api-/{LOCATOR}@1a2b3c4d",
            "pact:orders-api.@1a2b3c4d",
        ],
        ids=[
            "hash for slash",
            "no quotes",
            "no hash",
            "a space for the slash",
            "no heading path",
            "a dot for the slash",
            "a hyphen before the slash",
            "a dot, no heading path",
        ],
    )
    def test_refuses_an_anchor_that_does_not_parse(self, world, anchor):
        """A mistyped citation is read by nobody else: not the signer's own
        check, not chain-check. Here it is named, with both remedies, and
        exit 2."""
        write(world.web, SPEC, grounding_row(anchor))
        code, out = world.run()
        assert code == 2, out
        assert f"REFUSED {SIGNER_URL} {SPEC}:1 — `" in out, out
        assert (
            'does not parse as `pact:orders-api/"<heading path>"@<hash>`, so '
            "nothing grades it. Quote the heading path and give it a hash, "
            "`@00000000` until the first report names the real one; or, where it "
            "shows the shape rather than citing a clause, put it in a fenced code "
            "block, which nothing reads"
        ) in out, out

    def test_accepts_the_pact_s_name_inside_a_graded_anchor_s_heading(self, world):
        """The anchor around it is graded, and the spelling inside it is not
        a second citation."""
        write(
            world.web,
            SPEC,
            grounding_row(
                'pact:orders-api/"## On pact:orders-api/old shapes"@deadbeef'
            ),
        )
        code, out = world.run()
        assert code == 2 and "BROKEN " in out, out
        assert "does not parse" not in out, out

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
        (world.home / ".claude" / "agentic" / "pact-paths.md").mkdir(parents=True)
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 2, out
        assert (
            "REFUSED ~/.claude/agentic/pact-paths.md — ~/.claude/agentic/"
            "pact-paths.md is there and could not be read"
        ) in out, out

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
        assert code == 2 and "has no origin remote" in out, out


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
