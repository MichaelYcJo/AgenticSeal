"""`hooks/lib/core.py`: what the core hook prints, and how its first line reads.

A session receives the core, `skills/core/SKILL.md`, from the plugin's
`SessionStart` hook, under one first line naming the file printed, the
running plugin's version and the file's SHA-256 (#1177). In a clone of the
running plugin the file printed is the clone's, so the tree's core governs a
session there. The cases are S3, S4 and S7 of work item 1793273065.
"""

import hashlib
import json
import os

from conftest import ROOT, census_case, git_repo, load_hook_module

TARGET = "hooks/lib/core.py"

CORE = ("skills", "core", "SKILL.md")


def core_module():
    return load_hook_module("lib/core.py", "core_for_its_cases")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return path


def plugin(where, name="agentic", version="0.25.0", core="# plugin core\n"):
    """A scratch plugin root at WHERE: its manifest, and its core where CORE
    is not None. A manifest field given as None is left out."""
    fields = {k: v for k, v in (("name", name), ("version", version)) if v}
    write(os.path.join(where, ".claude-plugin", "plugin.json"), json.dumps(fields))
    if core is not None:
        write(os.path.join(where, *CORE), core)
    return str(where)


class Test_manifest:
    def test_accepts_the_object_the_manifest_holds(self, tmp_path):
        core = core_module()
        root = plugin(tmp_path / "plugin", version="1.2.3")
        assert core.manifest(root) == {"name": "agentic", "version": "1.2.3"}

    def test_refuses_a_manifest_that_is_absent_unreadable_or_not_an_object(
        self, tmp_path
    ):
        core = core_module()
        assert core.manifest(str(tmp_path / "none")) == {}
        for n, text in enumerate(("{not json", "[1, 2]", '"agentic"')):
            root = tmp_path / f"p{n}"
            write(os.path.join(root, ".claude-plugin", "plugin.json"), text)
            assert core.manifest(str(root)) == {}, text


class Test_header:
    def test_accepts_the_path_the_version_and_the_digest_as_one_sentence(self):
        core = core_module()
        assert core.header("/Users/x/SKILL.md", "0.25.0", "f" * 64) == (
            f"AgenticSeal core from /Users/x/SKILL.md, plugin 0.25.0, sha256 {'f' * 64}."
        )

    def test_refuses_to_lose_a_path_holding_a_comma_or_the_header_words(self):
        """The pattern is anchored at the end, so a path that holds `, plugin `
        still reads back whole from the line `header` writes."""
        core = core_module()
        path = "/Users/x/a, plugin 9, sha256 b/skills/core/SKILL.md"
        read = core.parse(core.header(path, "1.2.3", "a" * 64))
        assert (read.path, read.version, read.digest) == (path, "1.2.3", "a" * 64)


class Test_parse:
    def test_accepts_the_three_fields_and_the_body(self):
        """A carriage return before the first newline is not part of the
        digest, and the body is everything after that newline."""
        core = core_module()
        line = core.header("/x/SKILL.md", "1.0.0", "0" * 64)
        read = core.parse(line + "\r\n# The core\n\nbody\n")
        assert read == ("/x/SKILL.md", "1.0.0", "0" * 64, "# The core\n\nbody\n")
        assert core.parse(line).body == ""

    def test_refuses_a_first_line_that_is_not_a_header(self):
        core = core_module()
        good = core.header("/x/SKILL.md", "1.0.0", "0" * 64)
        for text in (
            "",
            "# The core\n",
            "prefix " + good,
            good + " and more",
            good[:-1],
            good.replace("0" * 64, "0" * 63),
            good.replace("0" * 64, "A" * 64),
            good.replace("plugin 1.0.0", "plugin 1 0"),
            "\n" + good,
        ):
            assert core.parse(text) is None, text


class Test_origin:
    def test_accepts_a_clone_of_the_running_plugin_and_names_its_core(self, tmp_path):
        """S4: a repository whose manifest names the running plugin and which
        holds a core is a clone of it, from its top level or below."""
        core = core_module()
        root = plugin(tmp_path / "plugin")
        tree = git_repo(tmp_path / "tree")
        plugin(tree, version="0.26.0", core="# the tree's core\n")
        (tree / "docs" / "deep").mkdir(parents=True)
        for cwd in (tree, tree / "docs" / "deep"):
            found = core.origin(str(cwd), root)
            assert os.path.samefile(found, os.path.join(tree, *CORE)), found
        read = core.parse(core.output(str(tree), root))
        assert read.body == "# the tree's core\n"
        # The version is the running plugin's, whatever the clone's says.
        assert read.version == "0.25.0", read

    def test_refuses_every_other_place_and_names_the_plugins_core(self, tmp_path):
        """S4: a repository named for another plugin, one named for this
        plugin with no core file, one whose manifest names nothing, and a
        directory outside git each get the plugin's own core; so do a cwd
        that is not there and one that is not given."""
        core = core_module()
        root = plugin(tmp_path / "plugin")
        own = os.path.join(root, *CORE)
        other = git_repo(tmp_path / "other")
        plugin(other, name="another", core="# another core\n")
        coreless = git_repo(tmp_path / "coreless")
        plugin(coreless, core=None)
        nameless = git_repo(tmp_path / "nameless")
        plugin(nameless, name=None, core="# nameless core\n")
        outside = tmp_path / "outside"
        outside.mkdir()
        for cwd in (other, coreless, nameless, outside, tmp_path / "gone", ""):
            assert core.origin(str(cwd), root) == own, cwd

    def test_refuses_a_tree_where_the_plugins_manifest_names_nothing(self, tmp_path):
        """A plugin root with no `name` in its manifest is a clone of nothing,
        so a tree whose manifest names nothing either is not taken for one."""
        core = core_module()
        root = plugin(tmp_path / "plugin", name=None)
        tree = git_repo(tmp_path / "tree")
        plugin(tree, name=None, core="# tree core\n")
        assert core.origin(str(tree), root) == os.path.join(root, *CORE)


class Test_without_frontmatter:
    def test_accepts_the_text_below_the_closing_line(self):
        """The harness's skill listing already carries the `description:`, so
        the hook prints what stands below the frontmatter's closing `---`,
        from its first line that is not blank."""
        core = core_module()
        text = "---\nname: core\ndescription: |\n  Two.\n---\n\n# The core\n\nOne.\n"
        assert core.without_frontmatter(text) == "# The core\n\nOne.\n"
        assert core.without_frontmatter("---\n---\n# Bare\n") == "# Bare\n"
        crlf = "---\r\nname: core\r\n---\r\n\r\n# The core\r\n"
        assert core.without_frontmatter(crlf) == "# The core\r\n"
        # The first closing line ends it, and a line that only opens with
        # `---` does not: a rule in the body stays in the body.
        ruled = "---\nname: core\n----\n---\n# The core\n\n---\n\nTwo.\n"
        assert core.without_frontmatter(ruled) == "# The core\n\n---\n\nTwo.\n"

    def test_refuses_to_cut_a_text_with_no_frontmatter(self):
        """A text that does not open with `---`, or whose frontmatter never
        closes, is printed whole, leading blank lines and all."""
        core = core_module()
        for text in (
            "# The core\n\n---\n\nOne.\n",
            "\n---\nname: core\n---\n# The core\n",
            "---\nname: core\n# The core\n",
            "",
        ):
            assert core.without_frontmatter(text) == text, text


class Test_output:
    def test_accepts_the_header_then_the_files_body_under_its_digest(self, tmp_path):
        """S3: the output is the header, a newline, then the file's text below
        its frontmatter. The digest is over the whole file's bytes, read here
        on their own."""
        core = core_module()
        text = "---\nname: core\n---\n\n# The core\n\nOne — value.\n"
        root = plugin(tmp_path / "plugin", core=text)
        out = core.output(str(tmp_path / "nowhere"), root)
        path = os.path.join(root, *CORE)
        with open(path, "rb") as f:
            digest = hashlib.sha256(f.read()).hexdigest()
        assert out == (
            core.header(path, "0.25.0", digest) + "\n# The core\n\nOne — value.\n"
        ), out

    def test_refuses_to_print_a_core_that_is_not_a_file(self, tmp_path):
        """A missing core is said in one line, which is not a header."""
        core = core_module()
        root = plugin(tmp_path / "plugin", core=None)
        path = os.path.join(root, *CORE)
        assert core.output("", root) == (
            f"AgenticSeal core: {path} is not a file, so no core was printed."
        )
        assert core.parse(core.output("", root)) is None

    def test_refuses_to_leave_the_version_out_where_the_manifest_names_none(
        self, tmp_path
    ):
        core = core_module()
        root = plugin(tmp_path / "plugin", version=None)
        read = core.parse(core.output("", root))
        assert read.version == "unknown", read


class Test_module:
    def test_the_trees_core_stays_under_the_harness_cap(self):
        """S7: past about 10,000 characters a hook's output reaches the model
        only as a preview, so the whole output this tree's core makes stays
        under `CAP`, and a core grown past it fails here before it ships."""
        core = core_module()
        assert core.CAP == 10_000
        out = core.output(ROOT, ROOT)
        read = core.parse(out)
        assert os.path.samefile(read.path, os.path.join(ROOT, *CORE)), read.path
        assert len(out) < core.CAP, len(out)
        # The tree's frontmatter stays out of what a session receives.
        assert read.body.startswith("# The core\n"), read.body[:80]


test_census = census_case(TARGET)
