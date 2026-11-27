"""`lib/core.py`: what the core hook prints into a session.

A session in a repository that holds a `seal/` root receives the core,
`skills/core/SKILL.md`, from the plugin's `SessionStart` hook, under one
first line naming the file printed and the running plugin's version, and
above one closing line naming where work starts (#1177, #1430). A session
in a repository with no root receives nothing. In a clone of the running
plugin the file printed is the clone's, so the tree's core governs a
session there.
"""

import json
import os

from conftest import ROOT, census_case, git_repo, load_lib_module, mark_root

TARGET = "lib/core.py"

CORE = ("skills", "core", "SKILL.md")


def core_module():
    return load_lib_module("core.py", "core_for_its_cases")


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


def sized_core(where, core, length):
    """A scratch plugin root at WHERE whose own core, a text with no
    frontmatter, makes a whole output of LENGTH characters; the path of that
    core."""
    path = os.path.join(str(where), *CORE)
    room = length - len(core.whole("", path, "0.25.0"))
    plugin(where, core="x" * room)
    return path


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
    def test_accepts_the_path_and_the_version_as_one_sentence(self):
        core = core_module()
        assert core.header("/Users/x/SKILL.md", "0.25.0") == (
            "AgenticSeal core from /Users/x/SKILL.md, plugin 0.25.0."
        )

    def test_refuses_to_quote_or_cut_a_path_holding_the_headers_words(self):
        """A session reads the path as written, so a path holding a comma or
        `, plugin ` is carried whole, with nothing quoted or escaped."""
        core = core_module()
        path = "/Users/x/a, plugin 9./skills/core/SKILL.md"
        assert core.header(path, "1.2.3") == (
            f"AgenticSeal core from {path}, plugin 1.2.3."
        )


class Test_origin:
    def test_accepts_a_clone_of_the_running_plugin_and_names_its_core(self, tmp_path):
        """A repository whose manifest names the running plugin and which
        holds a core is a clone of it, from its top level or below, and the
        version printed is the running plugin's, whatever the clone's says."""
        core = core_module()
        root = plugin(tmp_path / "plugin")
        tree = git_repo(tmp_path / "tree")
        plugin(tree, version="0.26.0", core="# the tree's core\n")
        mark_root(tree / "seal")
        (tree / "docs" / "deep").mkdir(parents=True)
        for cwd in (tree, tree / "docs" / "deep"):
            found = core.origin(str(cwd), root)
            assert os.path.samefile(found, os.path.join(tree, *CORE)), found
        out = core.output(str(tree), root)
        first, _, body = out.partition("\n")
        assert first == core.header(core.origin(str(tree), root), "0.25.0"), first
        assert body.startswith("# the tree's core\n"), body

    def test_refuses_every_other_place_and_names_the_plugins_core(self, tmp_path):
        """A repository named for another plugin, one named for this plugin
        with no core file, one whose manifest names nothing, and a directory
        outside git each get the plugin's own core; so do a cwd that is not
        there and one that is not given."""
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


class Test_closing:
    """The two cases differ by the plugin root given: none, for the plugin's
    own core, and one, for a core at another path."""

    def test_accepts_a_root_and_names_it_once_after_the_relative_paths(self):
        """A core at another path is closed by the two files named relative
        to the plugin's root, then one sentence naming that root, absolute."""
        core = core_module()
        root = "/Users/x/plugins/agentic/0.25.0"
        closing = core.closing(root)
        assert closing == (
            core.START
            + " Both paths are relative to the running plugin's root, "
            + f"`{root}`."
        ), closing
        assert closing.count(root) == 1, closing
        assert "`skills/implement/orchestration.md`" in closing, closing
        assert "*Orchestrator: the order inside a ticket*" in closing, closing
        assert "`skills/code-review/SKILL.md`" in closing, closing

    def test_refuses_to_name_a_root_where_none_is_given(self):
        """The plugin's own core is closed by the same two relative paths
        and a sentence that names no root, since the first line already
        names the core's file under it."""
        core = core_module()
        closing = core.closing()
        assert closing == (
            core.START + " Both paths are relative to the plugin's root."
        ), closing
        assert "running plugin" not in closing, closing
        assert "`/" not in closing, closing


class Test_whole:
    """The two cases differ by the plugin root given, which decides only the
    closing line's last sentence."""

    def test_accepts_the_header_the_text_and_the_closing_line(self):
        """The whole output is the header naming PATH and VERSION, a newline,
        the text, a newline and `closing()`, and no file is read: PATH names
        none."""
        core = core_module()
        path = "/Users/x/gone/skills/core/SKILL.md"
        assert core.whole("# The core\n\nOne.\n", path, "1.2.3") == (
            core.header(path, "1.2.3") + "\n# The core\n\nOne.\n\n" + core.closing()
        )

    def test_refuses_the_plugins_own_sentence_where_a_root_is_given(self):
        core = core_module()
        path = "/Users/x/tree/skills/core/SKILL.md"
        root = "/Users/x/plugins/agentic/0.25.0"
        out = core.whole("# The core\n", path, "1.2.3", root)
        assert out == core.header(path, "1.2.3") + "\n# The core\n\n" + core.closing(
            root
        ), out


class Test_rendered:
    def test_accepts_the_header_the_body_and_the_closing_line(self, tmp_path):
        """The output is the header, a newline, the file's text below its
        frontmatter, a newline, then the closing line, which names the
        orchestrator's section and the review skill relative to the plugin's
        root. The plugin's own core names that root once, in the first
        line."""
        core = core_module()
        text = "---\nname: core\n---\n\n# The core\n\nOne — value.\n"
        root = plugin(tmp_path / "plugin", core=text)
        path = os.path.join(root, *CORE)
        out = core.rendered(path, root)
        assert out == (
            core.header(path, "0.25.0")
            + "\n# The core\n\nOne — value.\n\n"
            + core.closing()
        )
        assert out.count(root) == 1, out
        assert root in out.split("\n", 1)[0], out

    def test_accepts_a_core_at_another_path_with_the_running_plugins_root_once(
        self, tmp_path
    ):
        """A clone's core is printed under the running plugin's version, and
        its closing line names the running plugin's root, the one place that
        root stands in the output."""
        core = core_module()
        root = plugin(tmp_path / "plugin")
        tree = plugin(tmp_path / "tree", version="0.26.0", core="# tree core\n")
        path = os.path.join(tree, *CORE)
        out = core.rendered(path, root)
        assert out == (
            core.header(path, "0.25.0") + "\n# tree core\n\n" + core.closing(root)
        ), out
        assert out.count(root) == 1, out

    def test_refuses_to_print_a_core_whose_whole_output_reaches_the_cap(self, tmp_path):
        """An output the harness would cut to a preview is not printed: one
        line names the core's file and says to open it, and the closing line
        names the running plugin's root. It does not open as a printed core
        does, so a session reads it as no core."""
        core = core_module()
        path = sized_core(tmp_path / "plugin", core, core.CAP)
        root = str(tmp_path / "plugin")
        out = core.rendered(path, root)
        assert out == (
            f"AgenticSeal core: printing {path} here would pass the harness's "
            "cap of 10,000 characters on a hook's output, so no core was "
            "printed. Open that file whole before anything else.\n" + core.closing(root)
        ), out
        assert not out.startswith("AgenticSeal core from"), out
        assert len(out) < core.CAP, len(out)

    def test_accepts_a_core_one_character_under_the_cap_whole(self, tmp_path):
        core = core_module()
        path = sized_core(tmp_path / "plugin", core, core.CAP - 1)
        out = core.rendered(path, str(tmp_path / "plugin"))
        assert len(out) == core.CAP - 1, len(out)
        assert out.startswith(core.header(path, "0.25.0") + "\nxxx"), out[:200]
        assert out.endswith("x\n" + core.closing()), out[-400:]

    def test_refuses_to_print_a_core_that_is_not_a_file(self, tmp_path):
        """A missing core is said in one line, which is not a header and
        carries no closing line."""
        core = core_module()
        root = plugin(tmp_path / "plugin", core=None)
        path = os.path.join(root, *CORE)
        assert core.rendered(path, root) == (
            f"AgenticSeal core: {path} is not a file, so no core was printed."
        )

    def test_refuses_to_leave_the_version_out_where_the_manifest_names_none(
        self, tmp_path
    ):
        core = core_module()
        root = plugin(tmp_path / "plugin", version=None)
        first = core.rendered(os.path.join(root, *CORE), root).split("\n", 1)[0]
        assert first.endswith(", plugin unknown."), first


class Test_output:
    def test_accepts_a_repository_holding_a_marked_root(self, tmp_path):
        """A session whose repository holds a `seal/` root receives
        `rendered` for the core `origin` names."""
        core = core_module()
        root = plugin(tmp_path / "plugin")
        repo = git_repo(tmp_path / "repo")
        mark_root(repo / "seal")
        assert core.output(str(repo), root) == core.rendered(
            os.path.join(root, *CORE), root
        )

    def test_refuses_a_repository_with_no_marked_root(self, tmp_path):
        """#1430. A repository with no `seal/` root, one whose `seal/` lacks
        the marker, a directory outside git and a cwd not given each receive
        nothing: the root is what says the repository runs the AgenticSeal
        process."""
        core = core_module()
        root = plugin(tmp_path / "plugin")
        bare = git_repo(tmp_path / "bare")
        unmarked = git_repo(tmp_path / "unmarked")
        write(str(unmarked / "seal" / "README.md"), "# a package of our own\n")
        outside = tmp_path / "outside"
        outside.mkdir()
        for cwd in (bare, unmarked, outside, ""):
            assert core.output(str(cwd), root) == "", cwd


class Test_module:
    def test_the_trees_core_stays_under_the_harness_cap(self):
        """Past about 10,000 characters a hook's output reaches the model
        only as a preview, so the whole output this tree's core makes as an
        installed plugin's own, the closing line included, stays under `CAP`
        at a plugin root of `ROOT_ROOM` characters, and a core grown past it
        fails here before it ships. The root is a string that names no
        directory, so where this checkout stands decides nothing."""
        core = core_module()
        assert core.CAP == 10_000
        with open(os.path.join(ROOT, *CORE), encoding="utf-8") as f:
            text = core.without_frontmatter(f.read())
        # The tree's frontmatter stays out of what a session receives.
        assert text.startswith("# The core\n"), text[:200]
        root = "/" + "r" * (core.ROOT_ROOM - 1)
        version = core.manifest(ROOT)["version"]
        out = core.whole(text, os.path.join(root, *CORE), version)
        assert len(out) < core.CAP, (
            f"the hook's whole output is {len(out):,} characters at a plugin "
            f"root of {core.ROOT_ROOM} characters (lib/core.py#ROOT_ROOM), "
            f"against a cap of {core.CAP:,} (lib/core.py#CAP)"
        )


test_census = census_case(TARGET)
