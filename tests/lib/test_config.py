"""`lib/config.py`, the shared reader of `seal/config.json`, one class per
function its cases reach.

#1454 moved the settings out of a markdown table, so the cases that pinned
the walker's refusals of the `| Item | Value |` table as a settings reader
left with that reader. The walker moved to `lib/tables.py`, and its own
cases are in `tests/lib/test_tables.py`. The cases of the pact's `| Signer |` table and
of the header 0.18.x wrote left with their reader too, and the pact's
signers are read from a `Pact signers` key.

#942's phase 6 placed here the reference-root reader's cases from
`tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`, the policy root's
from `tests/text/test_a_document_has_room_for_the_next_fold.py`, the remote
normaliser's from `tests/text/test_the_records_can_be_carried_out_and_in.py`, the
`Baseline commit` reader's from `tests/skills/test_chain_check.py`, the row reader's
from `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`,
the reader's cases of
`tests/test_the_mode_question_is_asked_once.py`, whose writer's cases are in
`tests/skills/test_seal.py`, the pact readers' of `tests/behaviour/test_a_signer_declares_its_pact.py`, and the
cases `tests/skills/test_pact_check.py` left for this module that run `seal
pact` over the pact's world in `tests/conftest.py`; one of them stands, and
the rest left with the `| Signer |` table's reader. Each case keeps
its body; a name its old file defined for it is defined here, and a fixture
or text two files read is `tests/conftest.py`'s.
"""

import importlib.util
import json
import os
import subprocess

import pytest
from conftest import (
    BASELINE,
    MOBILE_URL,
    ORDERS,
    PACT_URL,
    ROOT,
    SIGNER_URL,
    URL,
    V2,
    census_case,
    clause,
    load_lib_module,
    load_module,
    local_home,
    mark_root,
    opt_in_shared,
    parity_file,
    signer_config,
    write,
    write_config,
    write_unreadable,
)
from conftest import config_json as table

TARGET = "lib/config.py"

config = load_lib_module("config.py", "config_under_test")


# The sentence a pact no `Pact signers` key signs is refused in, pinned whole
# (contract rule 14).
NO_SIGNER = (
    "no `Pact signers` key names a signer, and a pact nobody signs is not a "
    "pact — write the origin remote URL of every other signer into that key, "
    "separated by `;`"
)

# `seal.py`, which re-exports `normalise_remote`: the normaliser's cases ask
# it by that name, through the `seal` fixture below.
SCRIPT = os.path.join(ROOT, "skills", "implement", "scripts", "seal.py")

# The `Baseline commit` case asks the reader `chain_check.py` loads for the
# parity arm, as the command reaches it.
chain = load_module(
    os.path.join(ROOT, "skills", "code-review", "scripts", "chain_check.py"),
    "chain_check_for_config",
)


@pytest.fixture
def seal():
    spec = importlib.util.spec_from_file_location("agentic_seal", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Test_reference_roots:
    def test_accepts_a_row_naming_its_prefixes_with_or_without_a_slash(self, tmp_path):
        """Present: the prefixes it names, normalised, and nothing else."""
        home = str(tmp_path / "seal")
        write_config(
            home,
            table(
                ("Reference specs", "specs/, docs/adr ,./design/, specs, tools\\notes")
            ),
        )
        roots = config.reference_roots(home, "seal")
        assert roots == ("specs", "docs/adr", "design", "tools/notes"), roots
        for rel in (
            "specs/x/design.md",
            "docs/adr/0001.md",
            "design/a.md",
            "specs",
            "./specs/x.md",
            "tools/notes/n.md",
        ):
            assert config.under_reference_root(rel, roots, "seal"), rel
        for rel in ("docs/adrs/0001.md", "docs/specs/x.md", "src/specs.py", "spec/x"):
            assert not config.under_reference_root(rel, roots, "seal"), rel

    def test_no_row_means_every_specs_directory_outside_the_root(
        self, tmp_path, monkeypatch
    ):
        """Absent, empty or unreadable: the ticket's default, at any depth."""
        home = str(tmp_path / "seal")
        for body in (None, table(("Mode", "shared")), table(("Reference specs", ""))):
            if body is not None:
                write_config(home, body)
            roots = config.reference_roots(home, "seal")
            assert roots is None, (body, roots)
            for rel in (
                "specs/x/design.md",
                "docs/specs/y.md",
                "a/b/specs/c/d.md",
                "specs\\x\\design.md",
            ):
                assert config.under_reference_root(rel, roots, "seal"), rel
            for rel in (
                "seal/threads/1790000000-x/design.md",
                "docs/design.md",
                "specsheet/a",
            ):
                assert not config.under_reference_root(rel, roots, "seal"), rel
        # No root at either place is no reference root at all: the repository has
        # not opted in, and the 0.3.x `specs/` the checks still read was the
        # plugin's own. Never a `config.json` found relative to wherever the
        # process happens to stand, either.
        stray = tmp_path / "elsewhere"
        write_config(str(stray), table(("Reference specs", "docs/adr")))
        monkeypatch.chdir(stray)
        assert config.reference_roots("", "") == ()
        assert not config.under_reference_root("specs/x/design.md", (), "")

    def test_refuses_a_row_written_twice_or_a_file_that_will_not_read(self, tmp_path):
        """#867. A `Reference specs` key written twice has no value, by
        `lib/config.py#config_value`'s rule; the reader used to take the
        first. A file that is there and will not read is the default too, as it
        was, and the reader no longer opens the file itself to find out. Seen red
        against the first-wins reader: `('docs/adr',)`."""
        home = str(tmp_path / "seal")
        write_config(
            home, table(("Reference specs", "docs/adr"), ("Reference specs", "none"))
        )
        assert config.reference_roots(home, "seal") is None
        os.remove(os.path.join(home, "config.json"))
        os.mkdir(os.path.join(home, "config.json"))
        assert config.reference_roots(home, "seal") is None

    def test_none_declares_no_reference_root(self, tmp_path):
        home = str(tmp_path / "seal")
        write_config(home, table(("Reference specs", "None")))
        roots = config.reference_roots(home, "seal")
        assert roots == (), roots
        assert not config.under_reference_root("specs/x/design.md", roots, "seal")

    @pytest.mark.parametrize("name", ["seal", "agentic-seal"])
    def test_the_plugins_own_root_is_never_a_reference_root(self, tmp_path, name):
        """A reference root is outside the root by definition; a prefix naming
        the root, by the name its caller reads from `lib/optin.py`, or
        anything under it is dropped, and the default never reaches its
        `threads/` either. Beside a root named `agentic-seal`, the project's
        own `seal/` is outside it, so a `specs/` under it is a reference
        root."""
        home = str(tmp_path / name)
        write_config(home, table(("Reference specs", f"{name}/threads, {name}, specs")))
        roots = config.reference_roots(home, name)
        assert roots == ("specs",), roots
        assert not config.under_reference_root(
            f"{name}/threads/1790000000-x/design.md", roots, name
        )
        assert not config.under_reference_root(
            f"{name}/threads/1790000000-x/design.md", None, name
        )
        assert config.under_reference_root("seal/vendor/specs/x.md", None, name) == (
            name != "seal"
        )

    def test_local_mode_reads_the_key_under_the_git_directory(self, tmp_path):
        """In local mode the root sits under the common git directory and nothing
        of it is in the tree, so its name in the tree is "", with no key every
        tree `specs` is a reference root, a `seal/vendor/specs/` among them,
        and a key there is read like any other."""
        repo = tmp_path / "repo"
        repo.mkdir()
        subprocess.run(["git", "-C", str(repo), "init", "-q"], check=True)
        optin = load_lib_module("optin.py", "optin_for_reference_roots")
        common = optin.git_common_dir(str(repo))
        home = os.path.join(common, "seal")
        mark_root(home)
        assert optin.home_at(str(repo), common) == home, "the fixture is not local mode"
        assert config.reference_roots(home, "") is None
        assert config.under_reference_root("specs/x/design.md", None, "")
        assert config.under_reference_root("seal/vendor/specs/x.md", None, "")
        write_config(home, table(("Reference specs", "docs/adr, seal/vendor/specs")))
        assert config.reference_roots(home, "") == ("docs/adr", "seal/vendor/specs")


class Test_normalise_remote:
    @pytest.mark.parametrize(
        "left,right",
        [
            ("git@example.com:org/repo.git", "https://example.com/org/repo"),
            ("ssh://git@example.com/org/repo.git", "https://example.com/org/repo/"),
            ("HTTPS://Example.com/Org/Repo.git", "https://example.com/org/repo"),
        ],
    )
    def test_accepts_remote_urls_that_reduce_to_one_host_and_path(
        self, seal, left, right
    ):
        assert seal.normalise_remote(left) == seal.normalise_remote(right)

    def test_a_port_is_not_read_as_an_scp_separator(self, seal):
        """The colon becomes `/` only where there was no scheme. Otherwise
        `https://example.com:8443/x` reduces to `example.com/8443/x`, and two
        ports of one host stop comparing equal to themselves."""
        assert seal.normalise_remote("https://example.com:8443/org/repo") == (
            "example.com:8443/org/repo"
        )

    def test_refuses_to_reduce_two_different_repositories_to_one(self, seal):
        """The direction the normalisation must not be wrong in."""
        assert seal.normalise_remote(
            "git@example.com:org/a.git"
        ) != seal.normalise_remote("git@example.com:org/b.git")
        assert seal.normalise_remote("git@example.com:org/a") != seal.normalise_remote(
            "git@other.example:org/a"
        )


class Test_config_pairs:
    def test_accepts_the_object_as_its_members_in_file_order(self, config, tmp_path):
        """S1. A value holding a pipe is a JSON string like any other, so it
        reads with the pipe plain: the escape a markdown cell needed is gone
        with the cell."""
        write_config(tmp_path, table(("Mode", "shared"), ("Broad gate", "a | b")))
        pairs, refusal = config.config_pairs(str(tmp_path))
        assert refusal is None
        assert list(pairs) == [("Mode", "shared"), ("Broad gate", "a | b")]
        assert config.declared_value(str(tmp_path), "Broad gate") == ("a | b", None)

    def test_accepts_a_byte_order_mark(self, config, tmp_path):
        """S2. An editor that writes a byte order mark has not made the file
        unreadable. Seen red against a `utf-8` decode: the parser refused the
        mark as an unexpected character."""
        path = tmp_path / "config.json"
        path.write_bytes(b"\xef\xbb\xbf" + table(("Mode", "local")).encode("utf-8"))
        assert config.declared_mode(str(tmp_path)) == ("mode", "local")

    def test_refuses_an_empty_home_whatever_the_working_directory_holds(
        self, config, monkeypatch, tmp_path
    ):
        """An empty home is no root, so no file is read, not even the
        `config.json` the working directory holds."""
        write_config(tmp_path, table(("Mode", "shared")))
        monkeypatch.chdir(tmp_path)
        assert config.config_pairs("") == (None, None)

    @pytest.mark.parametrize(
        "text, said",
        [
            ("| Item | Value |\n|---|---|\n| Mode | shared |\n", "does not parse"),
            ('{"Mode": "shared",}\n', "does not parse"),
            ("", "does not parse"),
            ('["Mode", "shared"]\n', "holds a JSON array where"),
            ('"shared"\n', "holds a JSON string where"),
            ("null\n", "holds a JSON null where"),
        ],
        ids=["a table", "a trailing comma", "empty", "an array", "a string", "null"],
    )
    def test_refuses_a_file_that_is_not_one_object_for_every_key(
        self, config, tmp_path, text, said
    ):
        """S2. A file that will not parse, or whose top level is not an object,
        holds no key anybody can read, so every key is that one refusal and
        none reads as absent. The sentence opens with the path, which the
        commands print after their own prefix."""
        write_config(tmp_path, text)
        path = str(tmp_path / "config.json")
        pairs, refusal = config.config_pairs(str(tmp_path))
        assert pairs is None and refusal.startswith(path + " "), refusal
        assert said in refusal, refusal
        assert config.declared_value(str(tmp_path), "Record language") == (
            None,
            refusal,
        )
        assert config.declared_mode(str(tmp_path)) == ("refused", refusal)

    def test_reads_a_config_md_standing_alone_as_no_file(self, config, tmp_path):
        """S3. A root an earlier release wrote holds `config.md` and no
        `config.json`. No reader opens that table, so the root declares
        nothing, as a root holding no file does: no key, and no refusal
        naming the old file or a command that converts it. Seen red against
        the reader that refused the root naming `seal mode`."""
        (tmp_path / "config.md").write_text(
            "# Repository config\n\n| Item | Value |\n|---|---|\n| Mode | shared |\n",
            encoding="utf-8",
        )
        assert config.config_pairs(str(tmp_path)) == (None, None)
        assert config.declared_mode(str(tmp_path)) == ("none", "")


class Test_unreadable_config:
    def test_accepts_a_decode_error_in_its_own_words(self, config):
        exc = UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid start byte")
        said = config.unreadable_config(os.path.join("seal", "config.json"), exc)
        assert f"({exc})" in said, said

    def test_refuses_the_error_numbers_wording_and_names_the_reason_alone(self, config):
        """An `OSError` is named by its reason, `Permission denied`, and not by
        the `[Errno 13] …: path` its own text wraps the reason in."""
        path = os.path.join("seal", "config.json")
        said = config.unreadable_config(path, OSError(13, "Permission denied", path))
        assert "(Permission denied)" in said, said
        assert "Errno" not in said, said


class Test_config_value:
    def test_accepts_one_row_as_its_value_and_no_row_as_none(self, config):
        """The two answers beside the refusal, so a reader of `config_value` can
        tell an empty key from no key: `""` is a key somebody left empty, and
        None is no key at all."""
        pairs = [("Mode", "shared"), ("Broad gate", "")]
        assert config.config_value(pairs, "Mode") == ("shared", None)
        assert config.config_value(pairs, "Broad gate") == ("", None)
        assert config.config_value(pairs, "Ledger frozen from") == (None, None)
        assert config.config_value(None, "Mode") == (None, None)

    def test_an_item_spelt_otherwise_names_no_item(self, config):
        """A key is spelt as `templates/setup/config.md` spells it, case
        included, so a `Policy Root` key names nothing and `Policy root` reads
        as absent, which is what that file's paragraph on absent keys says."""
        pairs = [("Policy Root", "elsewhere")]
        assert config.config_value(pairs, "Policy root") == (None, None)

    @pytest.mark.parametrize(
        "value, kind",
        [
            (1, "number"),
            (True, "boolean"),
            (None, "null"),
            (["a"], "array"),
            ({"a": "b"}, "object"),
        ],
    )
    def test_refuses_a_value_that_is_not_a_string_for_that_key_alone(
        self, config, tmp_path, value, kind
    ):
        """S2. Every key's grammar is a string's, so a value of another JSON
        type is no value: it is refused for its key, naming the type, and
        every other key reads. Seen red against a reader that handed the
        parsed value on."""
        write_config(tmp_path, table(("Broad gate", value), ("Mode", "shared")))
        assert config.declared_value(str(tmp_path), "Broad gate") == (
            None,
            f"`Broad gate` holds a JSON {kind}, and its value is a string",
        )
        assert config.declared_mode(str(tmp_path)) == ("mode", "shared")


class Test_declared_mode:
    def test_accepts_the_row_from_the_root_the_folder_is_at(self, config, repo):
        """The reader answers for whichever root exists, so a local-mode
        repository is not read as one that declared nothing."""
        home = local_home(repo)
        write_config(home, table(("Mode", "local")))
        assert config.declared_mode(str(home)) == ("mode", "local")

    @pytest.mark.parametrize(
        "text, expected",
        [
            (None, ("none", "")),
            (table(("Record language", "Korean")), ("none", "")),
            (table(("Mode", "")), ("none", "")),
            ("{}\n", ("none", "")),
            (table(("Mode", "SHARED")), ("mode", "shared")),
            (table(("Mode", "whatever")), ("unknown", "whatever")),
        ],
    )
    def test_the_four_spellings_of_undeclared_are_one_answer(
        self, config, repo, text, expected
    ):
        """The same four `seal.py#declared` already had, because it is the same
        reader — moved, not rewritten. A key that names no mode is told apart from
        no key, because a claim nobody can act on is not the same as no claim."""
        home = opt_in_shared(repo)
        if text is not None:
            write_config(home, text)
        assert config.declared_mode(str(home)) == expected

    @pytest.mark.parametrize(
        "rows",
        [
            [("Mode", "shared"), ("Mode", "local")],
            [("Mode", "local"), ("Mode", "local")],
            [("Mode", "shared"), ("Record language", "Korean"), ("Mode", "")],
        ],
        ids=["two values", "the same value twice", "one value and an empty key"],
    )
    def test_refuses_a_mode_row_written_twice(self, config, repo, rows):
        """S1 of #867, the reader's half, and S2 of #1454. The reader took the
        first row and the checker took the last, so a person editing the one
        they could see might be editing the one that does not answer; a JSON
        parser keeps the last. A key written twice has no value -- not its
        first and not its last -- and the refusal names the key and how many
        times it is written, while every other key reads. Seen red against a
        reader over `json.loads`' dict: `('mode', 'local')` for the first
        shape."""
        home = opt_in_shared(repo)
        write_config(home, table(*rows, ("Broad gate", "bin/test")))
        kind, said = config.declared_mode(str(home))
        assert kind == "refused", (kind, said)
        assert said == "`Mode` appears 2 times — one value"
        assert config.declared_value(str(home), "Broad gate") == ("bin/test", None)

    def test_an_absent_config_and_an_unreadable_one_are_two_states(self, config, repo):
        """S3 of #867, the reader's half. No file declares nothing; a file that is
        there and will not read is refused with a sentence naming the path. The
        reader tells the two apart once, so no caller opens the file again to
        find out."""
        home = opt_in_shared(repo)
        assert config.config_pairs(str(home)) == (None, None)
        assert config.declared_value(str(home), "Mode") == (None, None)
        for shape in ("directory", "undecodable"):
            path = write_unreadable(home, shape)
            text, said = config.config_pairs(str(home))
            assert text is None and said.startswith(path + " is there and cannot"), said
            assert config.declared_value(str(home), "Mode") == (None, said)
            assert config.declared_mode(str(home)) == ("refused", said)
            if shape == "directory":
                os.rmdir(path)
            else:
                os.remove(path)


class Test_pact_declaration:
    def test_accepts_one_pact_normalised(self):
        """S1. One URL: the URL as written, and normalised."""
        pacts, refusals = config.pact_declaration(
            [("Mode", "shared"), ("Pact", "git@example.com:org/Orders-API.git")]
        )
        assert refusals == []
        assert pacts == [
            ("git@example.com:org/Orders-API.git", "example.com/org/orders-api")
        ]

    def test_two_pacts_come_back_in_order(self):
        """S2. `;` separates the pacts a signer signs, and the order is the
        key's."""
        pacts, refusals = config.pact_declaration(
            [
                (
                    "Pact",
                    "https://example.com/org/orders-api ; git@example.com:org/billing.git",
                ),
            ]
        )
        assert refusals == []
        assert [n for _, n in pacts] == [
            "example.com/org/orders-api",
            "example.com/org/billing",
        ]

    def test_accepts_two_pacts_whose_urls_end_in_one_segment(self):
        """S10 of #913: an anchor names the pact by its URL, so two pacts
        ending in one segment are two pacts and nothing is refused."""
        value = "git@example.com:org/api.git;https://example.com/other/api"
        assert config.pact_declaration([("Pact", value)]) == (
            [
                ("git@example.com:org/api.git", "example.com/org/api"),
                ("https://example.com/other/api", "example.com/other/api"),
            ],
            [],
        )

    def test_no_row_and_an_empty_row_hold_no_pact(self):
        """Absent means no pact is held elsewhere, and so do an empty value and
        no file."""
        for pairs in ([("Mode", "shared")], [("Pact", "")], [], None):
            assert config.pact_declaration(pairs) == ([], []), pairs

    @pytest.mark.parametrize(
        "rows",
        [
            [("Pact notify", "sometimes")],
            [("Pact notify", "never"), ("Pact notify", "always")],
        ],
        ids=["a value outside the old vocabulary", "written twice"],
    )
    def test_a_pact_notify_row_an_earlier_release_read_is_ignored(self, rows):
        """`templates/setup/config.md` *Pact*: a `Pact notify` key left in the
        config is read by nobody, with a `Pact` key or without one, so neither
        a value outside the vocabulary it once had nor the key written twice is
        refused. Seen red by `seal mutate` against a reader that refused the
        row (phase 8 of 1791940762)."""
        assert config.pact_declaration([("Pact", URL), *rows]) == (ORDERS, [])
        assert config.pact_declaration(rows) == ([], [])

    def test_refuses_a_row_that_will_not_parse_and_never_reads_it_as_absent(self):
        """Each way an entry fails is a sentence naming it, so a signer that
        wrote a row is never read as one that wrote none."""
        cases = {
            "orders-api": "is not a remote URL",
            "git@example.com:org/a.git;;git@example.com:org/b.git": "holds an empty entry",
            "git@example.com:org/a.git git@example.com:org/b.git": "holds a space",
            "git@example.com:org/api.git;https://example.com/org/api": "are one repository",
        }
        for value, said in cases.items():
            _, refusals = config.pact_declaration([("Pact", value)])
            assert len(refusals) == 1 and said in refusals[0], (value, refusals)
        # A `Pact` key written twice has no value, in the one sentence every
        # config key is refused in (#867): its first is not the answer, so it
        # lists no pact. Seen red against the first-wins reader, which listed `a`.
        pacts, refusals = config.pact_declaration(
            [
                ("Pact", "git@example.com:org/a.git"),
                ("Pact", "git@example.com:org/b.git"),
            ]
        )
        assert pacts == []
        assert refusals == ["`Pact` appears 2 times — one value"]


class Test_declared_pacts:
    def test_an_unreadable_config_is_no_declaration(self, tmp_path):
        """`declared_pacts` is what `seal pact` reads a signer's key
        through. No file is no key; a file that is there and will not read is
        None, which the caller refuses, because a written key read as absent is
        the silence the reader exists to end."""
        assert config.declared_pacts(str(tmp_path / "missing")) == ([], [])
        home = tmp_path / "seal"
        (home / "config.json").mkdir(parents=True)
        assert config.declared_pacts(str(home)) is None
        (home / "config.json").rmdir()
        (home / "config.json").write_text(table(("Pact", URL)), encoding="utf-8")
        pacts, refusals = config.declared_pacts(str(home))
        assert pacts == ORDERS and refusals == []

    def test_refuses_a_signer_config_that_will_not_parse_with_exit_2(self, world):
        """S2 at `seal pact`: a signer's config that will not parse is refused
        as `UNREADABLE`, in the reader's sentence after the path the command
        shows, and the run exits 2. Seen red against the sentence the command
        printed before #1454, `could not be read`, which named no cause."""
        write(world.web, "seal/config.json", '{"Pact": "x",}\n')
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 2, out
        assert f"UNREADABLE {SIGNER_URL} " in out, out
        assert "seal/config.json — does not parse as JSON" in out, out

    @pytest.mark.parametrize(
        "rows",
        [
            [("Pact notify", "sometimes")],
            [("Pact notify", "never"), ("Pact notify", "always")],
        ],
        ids=["a value outside the old vocabulary", "written twice"],
    )
    def test_accepts_a_pact_notify_row_an_earlier_release_read_as_nothing(
        self, world, rows
    ):
        """`templates/setup/config.md` *Pact*: a `Pact notify` key left in a
        signer's config is read by nobody."""
        write(world.web, "seal/config.json", signer_config(("Pact", PACT_URL), *rows))
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 0, out
        assert "REFUSED" not in out and "`Pact notify`" not in out, out


class Test_signer_declaration:
    def test_accepts_every_signer_the_key_lists_in_its_order(self):
        """S7. The pact's repository lists every other signer in its `Pact
        signers` key, separated by `;` as `Pact` separates pacts. Two
        signers ending in one segment are two repositories, because nobody
        cites a signer by name. Seen red against a reader of the `| Signer |`
        table, which had no such name."""
        signers, refusals = config.signer_declaration(
            [
                ("Mode", "shared"),
                (
                    "Pact signers",
                    "git@example.com:org/orders-web.git; https://example.com/other/orders-web",
                ),
            ]
        )
        assert refusals == []
        assert signers == [
            ("git@example.com:org/orders-web.git", "example.com/org/orders-web"),
            ("https://example.com/other/orders-web", "example.com/other/orders-web"),
        ]

    @pytest.mark.parametrize(
        "pairs",
        [None, [], [("Mode", "shared")], [("Pact signers", "")], [("Pact", URL)]],
        ids=["no file", "no key", "no such key", "an empty key", "a Pact key alone"],
    )
    def test_refuses_a_pact_no_key_signs_naming_the_key(self, pairs):
        """A pact nobody signs is not a pact, so an absent or empty key is a
        refusal naming it, not the no-pact answer `pact_declaration` gives
        an absent `Pact` key, and a `Pact` key is no answer about signers."""
        assert config.signer_declaration(pairs) == ([], [NO_SIGNER])

    @pytest.mark.parametrize(
        "value, read, said",
        [
            (
                f"{SIGNER_URL}; orders-mobile",
                [SIGNER_URL],
                "`orders-mobile` is not a remote URL — it reduces to no host and "
                "path, so no repository can be found by it",
            ),
            (
                f"{SIGNER_URL};;{MOBILE_URL}",
                [SIGNER_URL, MOBILE_URL],
                f"the `Pact signers` value `{SIGNER_URL};;{MOBILE_URL}` holds an "
                "empty entry — one remote URL between each `;`",
            ),
            (
                f"{SIGNER_URL} {MOBILE_URL}",
                [],
                f"`{SIGNER_URL} {MOBILE_URL}` holds a space — one remote URL per entry",
            ),
            (
                f"{SIGNER_URL}; git@example.com:org/orders-web.git",
                [SIGNER_URL],
                f"`git@example.com:org/orders-web.git` and `{SIGNER_URL}` are one "
                "repository",
            ),
        ],
        ids=["not a url", "an empty entry", "a space", "one repository twice"],
    )
    def test_refuses_each_entry_that_will_not_read_and_reads_the_rest(
        self, value, read, said
    ):
        """Each entry is read by `remote_entries`, in the sentences the
        `Pact` key prints, and an entry that will not read is refused rather
        than dropped."""
        signers, refusals = config.signer_declaration([("Pact signers", value)])
        assert refusals == [said], refusals
        assert [written for written, _n in signers] == read, signers

    def test_refuses_a_key_written_twice_or_holding_no_string(self):
        """By `config_value`'s rule and in its sentences (#867): neither key
        lists a signer."""
        assert config.signer_declaration(
            [("Pact signers", SIGNER_URL), ("Pact signers", MOBILE_URL)]
        ) == ([], ["`Pact signers` appears 2 times — one value"])
        assert config.signer_declaration([("Pact signers", [SIGNER_URL])]) == (
            [],
            ["`Pact signers` holds a JSON array, and its value is a string"],
        )


def parity_members(text):
    """The `(key, value)` members of the migration config TEXT, in order."""
    return json.loads(text, object_pairs_hook=list)


class Test_baseline_commit:
    @pytest.mark.parametrize("sha", [BASELINE, BASELINE[:7]])
    def test_accepts_the_sha_its_one_key_holds_alone(self, sha):
        """S6: the `Baseline commit` reader the parity arm loads through
        `chain_check.py#parity_readers` gives the SHA of `parity.json`'s
        one `Baseline commit` key, whole or abbreviated."""
        reads = chain.parity_readers()[0]
        assert reads.baseline_commit(parity_file(sha)) == (sha, None)

    def test_reads_past_a_byte_order_mark_an_editor_wrote(self):
        """S2's byte order mark, for `parity.json` as for `config.json`:
        the parity arm reads the file as `utf-8`, so the mark reaches the
        parser, and a mark an editor wrote is no refusal of every ready pull
        request. Seen red before the fix: "does not parse as JSON
        (Unexpected UTF-8 BOM ...)"."""
        assert config.baseline_commit(chr(0xFEFF) + parity_file(BASELINE)) == (
            BASELINE,
            None,
        )

    @pytest.mark.parametrize(
        "text, why",
        [
            (parity_file(None), "`<SHA>`"),
            (parity_file(BASELINE.upper()), BASELINE.upper()),
            (parity_file(BASELINE[:6]), BASELINE[:6]),
            (parity_file(f"`{BASELINE}`"), f"`{BASELINE}`"),
            (parity_file(f"{BASELINE}, read 2026-11-09"), "read 2026-11-09"),
            (
                table(
                    *[
                        (k, v)
                        for k, v in parity_members(parity_file(BASELINE))
                        if k != "Baseline commit"
                    ]
                ),
                "holds no `Baseline commit` key",
            ),
            (
                table(
                    ("Baseline commit", BASELINE),
                    *parity_members(parity_file(BASELINE)),
                ),
                "`Baseline commit` appears 2 times",
            ),
            (table(("Baseline commit", 123)), "holds a JSON number"),
            (
                "| Field | Value |\n|---|---|\n| Baseline commit | `0123456` |\n",
                "does not parse as JSON",
            ),
            ("[]\n", "holds a JSON array"),
        ],
        ids=[
            "the placeholder",
            "upper case",
            "six digits",
            "a code span",
            "a SHA and a date",
            "no such key",
            "the key twice",
            "a number",
            "an earlier release's table",
            "an array",
        ],
    )
    def test_refuses_a_config_that_names_no_sha_and_says_why(self, text, why):
        """S6: a `Baseline commit` that is not 7 to 40 lowercase hex digits
        and nothing else, an absent key, a key written twice, a value that
        is not a string, and a file that is not one JSON object each give
        no SHA and a why naming it, which reads after the file's name."""
        sha, said = config.baseline_commit(text)
        assert sha is None and why in said, (said, text)
        assert not said.startswith(("seal/", "parity")), said


class Test_module:
    @pytest.mark.parametrize(
        "value, root",
        [
            ("policy", "policy"),
            ("./policy/", "policy"),
            ("", "docs"),
            ("/etc", "docs"),
            ("../elsewhere", "docs"),
        ],
    )
    def test_the_policy_root_row_reads_as_docs_unless_it_names_a_directory_inside(
        self, tmp_path, value, root
    ):
        """`lib/config.py#policy_root`, the one reader every reader asks: an
        empty value and one that leaves the repository read as `docs`."""
        config = load_lib_module("config.py", "agentic_config_for_policy_root")
        (tmp_path / "config.json").write_text(
            table(("Policy root", value)), encoding="utf-8"
        )
        assert config.policy_root(str(tmp_path)) == root
        assert config.policy_root("") == "docs"


test_census = census_case(TARGET)
