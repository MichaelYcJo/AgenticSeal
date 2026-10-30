"""`tests/censuses.py`'s cases, and the sweep of every file no module file
declares (#942).

Each census judges one file. A module file runs every census over its own
target through `test_census = census_case(TARGET)`, and `Test_module` here
runs them over every other tracked file. Each census's cases write a file
into a temporary root and judge it there, so none of them runs git; the
sweep lists the tracked files once.

The cases came from the modules that held each census whole:
`test_every_file_the_plugin_reads_or_writes_names_its_encoding.py` (#741,
#762), the S19 cases of `test_every_reader_ends_a_line_where_gfm_does.py`,
`test_a_format_has_one_reader.py` (#867), the floor half of
`test_a_script_says_which_interpreter_it_needs.py`,
`test_no_living_file_writes_the_section_sign.py` (#1005) and
`test_no_real_identifiers.py`. The work item's `trail/phases/phase-3.md`
names every old case and where it went.

Seen red before they were committed (contract rule 15): every case failed
against the tree without `tests/censuses.py`, and `seal mutate` broke each
census's refusal in turn and watched a case of its class fail. `old_names`
(#1051) was seen red over the tree at the commit before the rename's sweep.
`vacated_paths` (#1060) failed its cases before the census existed, and was
seen red over the tree after `templates/` moved and before its citations were
swept: 231 lines in 75 files.
"""

import ast
import importlib.util
import inspect
import os

import censuses
import pytest
from conftest import ROOT, census_case, git_listing, on_disk

TARGET = "tests/censuses.py"

_LAYOUT = importlib.util.spec_from_file_location(
    "agentic_layout_for_censuses",
    os.path.join(ROOT, "skills", "verify", "scripts", "test_layout.py"),
)
layout = importlib.util.module_from_spec(_LAYOUT)
_LAYOUT.loader.exec_module(layout)

SIGN = "\N{SECTION SIGN}"
# Built from halves, so this file holds neither whole: RFC 2606 reserves the
# domain, and the user path belongs to nobody.
REFUSED_DOMAIN = "fixture.example" + ".net"
REFUSED_USER_PATH = "/" + "Users/someone/"
PRODUCT_HOST = "claude" + ".ai"
RUFF = '[per-file-target-version]\n"hooks/*.py" = "py39"\n'


def plant(root, rel, text):
    """TEXT written at REL under ROOT, the directories made; ROOT as text."""
    path = root.joinpath(*rel.split("/"))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return str(root)


class Test_judge:
    def test_accepts_a_file_every_census_passes(self, tmp_path):
        root = plant(
            tmp_path, "hooks/x.py", 'def f(p):\n    return open(p, encoding="utf-8")\n'
        )
        assert censuses.judge("hooks/x.py", root) == []

    def test_refuses_a_file_two_censuses_flag_naming_each(self, tmp_path):
        root = plant(tmp_path, "hooks/x.py", "open(p)\nx = t.splitlines()\n")
        found = censuses.judge("hooks/x.py", root)
        assert [line.split(": ")[0:2] for line in found] == [
            ["hooks/x.py:1", "encoding"],
            ["hooks/x.py:2", "splitlines"],
        ], found

    @pytest.mark.parametrize(
        "text",
        [
            "# exempt from encoding: a fixture read in the locale on purpose\n"
            "    # the next line splits git's output\n"
            "# exempt from splitlines: git output\n"
            "x = open(p).read().splitlines()\n",
            "# write `# exempt from splitlines: <why>` above it\nx = 1\n",
        ],
        ids=["exemptions-above-the-line", "a-comment-quoting-the-form"],
    )
    def test_accepts_a_line_under_its_exemptions(self, tmp_path, text):
        assert censuses.judge("hooks/x.py", plant(tmp_path, "hooks/x.py", text)) == []

    def test_refuses_an_exemption_above_a_line_no_census_flags(self, tmp_path):
        text = "x = 1\n# exempt from splitlines: git output\ny = 2\n"
        assert censuses.judge("hooks/x.py", plant(tmp_path, "hooks/x.py", text)) == [
            "hooks/x.py:2: splitlines: the exemption excuses nothing, because "
            "splitlines does not flag the line below it; remove the comment"
        ]

    @pytest.mark.parametrize(
        "text, named",
        [
            (
                "x = t.splitlines()  # exempt from splitlines: git output\n"
                "# exempt from splitlines: git output",
                [
                    ["hooks/x.py:1", "splitlines"],
                    ["hooks/x.py:2", "splitlines"],
                    ["hooks/x.py:1", "splitlines"],
                ],
            ),
            (
                "x = 1  # exempt from splitlines: git output\n",
                [["hooks/x.py:1", "splitlines"]],
            ),
            (
                "# exempt from encoding: git output\nx = t.splitlines()\n",
                [["hooks/x.py:1", "encoding"], ["hooks/x.py:2", "splitlines"]],
            ),
            (
                "# exempt from splitlines:\nx = t.splitlines()\n",
                [["hooks/x.py:2", "splitlines"]],
            ),
        ],
        ids=[
            "at-the-end-or-ending-a-line",
            "ending-an-unflagged-line",
            "from-another-census",
            "without-a-reason",
        ],
    )
    def test_refuses_an_exemption_out_of_place(self, tmp_path, text, named):
        found = censuses.judge("hooks/x.py", plant(tmp_path, "hooks/x.py", text))
        assert [line.split(": ")[0:2] for line in found] == named, found


class Test_encoding:
    def test_accepts_a_named_encoding_and_a_file_of_another_kind(self, tmp_path):
        plant(tmp_path, "docs/x.md", "open(p)\n")
        root = plant(tmp_path, "hooks/x.py", 'open(p, encoding="utf-8")\n')
        assert censuses.encoding("docs/x.md", root) == []
        assert censuses.encoding("hooks/x.py", root) == []

    def test_refuses_an_unnamed_call_under_a_root_nobody_listed(self, tmp_path):
        root = plant(tmp_path, "evals/new.py", "p.write_text(s)\n")
        assert censuses.encoding("evals/new.py", root) == [
            "evals/new.py:1: encoding: .write_text() in <module> reads or "
            "writes in the locale's encoding, which is cp1252 on the Windows "
            'leg; name `encoding="utf-8"`, or put '
            "`# exempt from encoding: <why>` on its own line above it"
        ]


# `(source, kind)`: the source holds one unnamed call on its last line.
UNNAMED = {
    "builtin open": ("open(p)", "open()"),
    "builtin open, text mode": ('open(p, "w")', "open()"),
    "io.open": ("import io\nio.open(p)", "io.open()"),
    "codecs.open": ("import codecs\ncodecs.open(p)", "codecs.open()"),
    "os.fdopen": ('import os\nos.fdopen(fd, "w")', "os.fdopen()"),
    "Path.open": ("p.open()", "<expr>.open()"),
    "Path.open, text mode": ('p.open("w")', "<expr>.open()"),
    "read_text": ("p.read_text()", ".read_text()"),
    "write_text": ("p.write_text(s)", ".write_text()"),
    "subprocess.run text": (
        "import subprocess\nsubprocess.run(c, text=True)",
        "subprocess.run(text=)",
    ),
    "subprocess.Popen universal_newlines": (
        "import subprocess\nsubprocess.Popen(c, universal_newlines=1)",
        "subprocess.Popen(universal_newlines=)",
    ),
    "subprocess.check_output errors": (
        'import subprocess\nsubprocess.check_output(c, errors="replace")',
        "subprocess.check_output(errors=)",
    ),
    "subprocess.call text": (
        "import subprocess\nsubprocess.call(c, text=t)",
        "subprocess.call(text=)",
    ),
    "subprocess.check_call text": (
        "import subprocess\nsubprocess.check_call(c, text=True)",
        "subprocess.check_call(text=)",
    ),
    "subprocess.getoutput": (
        "import subprocess\nsubprocess.getoutput(c)",
        "subprocess.getoutput()",
    ),
    "subprocess.getstatusoutput": (
        "import subprocess\nsubprocess.getstatusoutput(c)",
        "subprocess.getstatusoutput()",
    ),
    "os.popen": ("import os\nos.popen(c)", "os.popen()"),
    "NamedTemporaryFile text": (
        'import tempfile\ntempfile.NamedTemporaryFile("w")',
        "tempfile.NamedTemporaryFile()",
    ),
    "TemporaryFile text": (
        'import tempfile\ntempfile.TemporaryFile(mode="w+")',
        "tempfile.TemporaryFile()",
    ),
    "SpooledTemporaryFile text": (
        'import tempfile\ntempfile.SpooledTemporaryFile(0, "w+")',
        "tempfile.SpooledTemporaryFile()",
    ),
    "TextIOWrapper": ("import io\nio.TextIOWrapper(b)", "io.TextIOWrapper()"),
    "fileinput": ("import fileinput\nfileinput.input(fs)", "fileinput.input()"),
    # Round 1 of #741: a method called on its class takes the path first.
    "Path.read_text, unbound": (
        "from pathlib import Path\nPath.read_text(p)",
        ".read_text()",
    ),
    "pathlib.Path.write_text, unbound": (
        "import pathlib\npathlib.Path.write_text(p, s)",
        ".write_text()",
    ),
    "Path.open, unbound": (
        'from pathlib import Path\nPath.open(p, "r", -1)',
        "<expr>.open()",
    ),
    # Round 1 of #741: the standard library's other text openers, found by
    # every public callable whose signature carries `encoding=None`.
    "gzip.open text": ('import gzip\ngzip.open("x.gz", "rt")', "gzip.open()"),
    "bz2.open text, a b in the path": (
        'import bz2\nbz2.open("x.bz2", "rt")',
        "bz2.open()",
    ),
    "lzma.open text, imported by name": (
        'from lzma import open\nopen(p, "rt")',
        "lzma.open()",
    ),
    "compression.zstd.open text": (
        'from compression import zstd\nzstd.open(p, "rt")',
        "compression.zstd.open()",
    ),
    "logging.FileHandler": (
        "import logging\nlogging.FileHandler(p)",
        "logging.FileHandler()",
    ),
    "RotatingFileHandler": (
        "import logging.handlers\nlogging.handlers.RotatingFileHandler(p)",
        "logging.handlers.RotatingFileHandler()",
    ),
    "TimedRotatingFileHandler, imported by name": (
        "from logging.handlers import TimedRotatingFileHandler\nTimedRotatingFileHandler(p)",
        "logging.handlers.TimedRotatingFileHandler()",
    ),
    "WatchedFileHandler": (
        "import logging.handlers\nlogging.handlers.WatchedFileHandler(p)",
        "logging.handlers.WatchedFileHandler()",
    ),
    "logging.basicConfig with a file": (
        "import logging\nlogging.basicConfig(filename=p)",
        "logging.basicConfig(filename=)",
    ),
    "logging.config.fileConfig": (
        "import logging.config\nlogging.config.fileConfig(p)",
        "logging.config.fileConfig()",
    ),
    "fileinput.FileInput": (
        "import fileinput\nfileinput.FileInput(fs)",
        "fileinput.FileInput()",
    ),
    "fileinput.hook_compressed": (
        'import fileinput\nfileinput.hook_compressed(p, "r")',
        "fileinput.hook_compressed()",
    ),
    "argparse.FileType": (
        'import argparse\nargparse.FileType("w")',
        "argparse.FileType()",
    ),
    "doctest.testfile": ("import doctest\ndoctest.testfile(p)", "doctest.testfile()"),
    "doctest.DocFileSuite": (
        "import doctest\ndoctest.DocFileSuite(p)",
        "doctest.DocFileSuite()",
    ),
    "socket makefile": ("s.makefile()", ".makefile()"),
    "trace write_results_file": (
        "r.write_results_file(p, l, n, h)",
        ".write_results_file()",
    ),
    "zipfile.Path open is still judged": (
        "import zipfile\nzipfile.Path(z).open()",
        "zipfile.Path.open()",
    ),
    # #762: called on its class, `zipfile.Path.open` takes the path first, so
    # `"r"` is the mode and no encoding is named.
    "zipfile.Path open unbound, mode only": (
        'import zipfile\nzipfile.Path.open(q, "r")',
        "zipfile.Path.open()",
    ),
    "zipfile.Path open unbound, imported by name": (
        'from zipfile import Path\nPath.open(q, "r")',
        "zipfile.Path.open()",
    ),
    "zipfile.Path open unbound, aliased module": (
        'import zipfile as z\nz.Path.open(q, "r")',
        "zipfile.Path.open()",
    ),
    # #762: `Traversable.read_text(self, encoding=None)` passes `None` on to
    # the locale, so called on the class, `t` is the traversable.
    "Traversable.read_text unbound": (
        "from importlib.resources.abc import Traversable\nTraversable.read_text(t)",
        ".read_text()",
    ),
    "Traversable.read_text unbound, the importlib.abc spelling": (
        "import importlib.abc\nimportlib.abc.Traversable.read_text(t)",
        ".read_text()",
    ),
    # #762 round 2: both classes inherit `Traversable.read_text`.
    "ResourceHandle.read_text unbound, inherited from Traversable": (
        "from importlib.resources.simple import ResourceHandle\n"
        "ResourceHandle.read_text(h)",
        ".read_text()",
    ),
    "ResourceHandle.read_text unbound, the importlib.simple spelling": (
        "import importlib.simple\nimportlib.simple.ResourceHandle.read_text(h)",
        ".read_text()",
    ),
    "ResourceContainer.read_text unbound, inherited from Traversable": (
        "from importlib.resources.simple import ResourceContainer\n"
        "ResourceContainer.read_text(c)",
        ".read_text()",
    ),
    "ResourceContainer.read_text unbound, the importlib.simple spelling": (
        "import importlib.simple\nimportlib.simple.ResourceContainer.read_text(c)",
        ".read_text()",
    ),
    # `Template.open(file, rw)` opens `file` with `open(file, rw)` or a pipe
    # with `os.popen`, both in the locale, and takes no encoding.
    "pipes.Template.open unbound": (
        'import pipes\npipes.Template.open(t, f, "r")',
        "pipes.Template.open()",
    ),
}

# The same calls with the encoding named (by keyword, or positionally where
# the signature allows), or in a binary mode.
NAMED = {
    "builtin open, keyword": 'open(p, encoding="utf-8")',
    "builtin open, 4th positional": 'open(p, "r", -1, "utf-8")',
    "builtin open, binary": 'open(p, "rb")',
    "io.open, keyword": 'import io\nio.open(p, encoding="utf-8")',
    "codecs.open, 3rd positional": 'import codecs\ncodecs.open(p, "r", "utf-8")',
    "os.fdopen, binary": 'import os\nos.fdopen(fd, "wb")',
    "os.fdopen, keyword": 'import os\nos.fdopen(fd, "w", encoding="utf-8")',
    "Path.open, keyword": 'p.open(encoding="utf-8")',
    "Path.open, 3rd positional": 'p.open("r", -1, "utf-8")',
    "Path.open, binary": 'p.open("rb")',
    "read_text, keyword": 'p.read_text(encoding="utf-8")',
    "read_text, positional": 'p.read_text("utf-8")',
    "write_text, keyword": 'p.write_text(s, encoding="utf-8")',
    "write_text, positional": 'p.write_text(s, "utf-8")',
    "subprocess.run, encoding": (
        'import subprocess\nsubprocess.run(c, text=True, encoding="utf-8")'
    ),
    "subprocess.run, bytes": "import subprocess\nsubprocess.run(c, capture_output=True)",
    "subprocess.run, text=False": "import subprocess\nsubprocess.run(c, text=False)",
    "NamedTemporaryFile, default binary": "import tempfile\ntempfile.NamedTemporaryFile()",
    "NamedTemporaryFile, keyword": (
        'import tempfile\ntempfile.NamedTemporaryFile("w", encoding="utf-8")'
    ),
    "TextIOWrapper, positional": 'import io\nio.TextIOWrapper(b, "utf-8")',
    "fileinput, keyword": 'import fileinput\nfileinput.input(fs, encoding="utf-8")',
    "fileinput, binary": 'import fileinput\nfileinput.input(fs, mode="rb")',
    "os.open is not a file opener": "import os\nos.open(p, os.O_RDONLY)",
    "webbrowser.open is not a file opener": "import webbrowser\nwebbrowser.open(u)",
    "Path.read_text, unbound, positional": 'from pathlib import Path\nPath.read_text(p, "utf-8")',
    "Path.write_text, unbound, positional": (
        'from pathlib import Path\nPath.write_text(p, s, "utf-8")'
    ),
    "gzip.open, binary by default": "import gzip\ngzip.open(p)",
    "gzip.open text, keyword": 'import gzip\ngzip.open(p, "rt", encoding="utf-8")',
    "lzma.open text, keyword": 'import lzma\nlzma.open(p, "rt", encoding="utf-8")',
    "logging.FileHandler, positional": 'import logging\nlogging.FileHandler(p, "a", "utf-8")',
    "RotatingFileHandler, 5th positional": (
        'import logging.handlers\nlogging.handlers.RotatingFileHandler(p, "a", 0, 0, "utf-8")'
    ),
    "logging.basicConfig, no file": "import logging\nlogging.basicConfig(level=1)",
    "logging.basicConfig, file and encoding": (
        'import logging\nlogging.basicConfig(filename=p, encoding="utf-8")'
    ),
    "argparse.FileType, binary": 'import argparse\nargparse.FileType("rb")',
    "fileinput.FileInput, binary": 'import fileinput\nfileinput.FileInput(fs, mode="rb")',
    "socket makefile, binary": 's.makefile("rb")',
    "ElementInclude.default_loader, xml": (
        'from xml.etree import ElementInclude\nElementInclude.default_loader(h, "xml")'
    ),
    "getoutput, keyword": 'import subprocess\nsubprocess.getoutput(c, encoding="utf-8")',
    "tarfile.open is binary": "import tarfile\ntarfile.open(p)",
    "TarFile.open is binary": "import tarfile\ntarfile.TarFile.open(p)",
    "ZipFile(...).open is binary": "import zipfile\nzipfile.ZipFile(z).open(n)",
    "shelve.open is not a text file": "import shelve\nshelve.open(p)",
    "dbm.open is not a text file": "import dbm\ndbm.open(p)",
    "wave.open is binary": "import wave\nwave.open(p)",
    # Round 2 of #741.
    "ElementInclude.default_loader, text reads UTF-8 itself": (
        'from xml.etree import ElementInclude\nElementInclude.default_loader(h, "text")'
    ),
    "dbm.dumb.open is not a text file": "import dbm.dumb\ndbm.dumb.open(p)",
    "zipfile.Path open, 2nd positional": (
        'import zipfile\nzipfile.Path(z).open("r", "utf-8")'
    ),
    "zipfile.Path open unbound, 3rd positional": (
        'import zipfile\nzipfile.Path.open(q, "r", "utf-8")'
    ),
    # #762: every standard-library module whose module-level `open` takes no
    # locale encoding, enumerated over every importable module on 3.12 to 3.14.
    "dbm.gnu.open is not a text file": "import dbm.gnu\ndbm.gnu.open(p)",
    "dbm.ndbm.open is not a text file": "import dbm.ndbm\ndbm.ndbm.open(p)",
    "dbm.sqlite3.open is not a text file": "import dbm.sqlite3\ndbm.sqlite3.open(p)",
    "aifc.open is binary": "import aifc\naifc.open(p)",
    "sunau.open is binary": "import sunau\nsunau.open(p)",
    "tokenize.open reads the encoding the file declares": (
        "import tokenize\ntokenize.open(p)"
    ),
    "posix.open is os.open": "import posix\nposix.open(p, 0)",
    "nt.open is os.open": "import nt\nnt.open(p, 0)",
    "ossaudiodev.open is an audio device": 'import ossaudiodev\nossaudiodev.open("w")',
    # #762 round 2: `open(mode='r', *args)` hands `args[0]` to `TextIOWrapper`
    # as the encoding, so called on the class it sits right after the mode.
    "Traversable.open unbound, encoding after the mode": (
        "from importlib.resources.abc import Traversable\n"
        'Traversable.open(t, "r", "utf-8")'
    ),
    "Traversable.open unbound, the importlib.abc spelling": (
        'import importlib.abc\nimportlib.abc.Traversable.open(t, "r", "utf-8")'
    ),
    "ResourceHandle.open unbound, encoding after the mode": (
        "from importlib.resources.simple import ResourceHandle\n"
        'ResourceHandle.open(h, "r", "utf-8")'
    ),
    "ResourceHandle.open unbound, the importlib.simple spelling": (
        'import importlib.simple\nimportlib.simple.ResourceHandle.open(h, "r", "utf-8")'
    ),
    "ResourceContainer.open unbound, encoding after the mode": (
        "from importlib.resources.simple import ResourceContainer\n"
        'ResourceContainer.open(c, "r", "utf-8")'
    ),
    "ResourceContainer.open unbound, the importlib.simple spelling": (
        "import importlib.simple\n"
        'importlib.simple.ResourceContainer.open(c, "r", "utf-8")'
    ),
}

# #762: a receiver no import binds is a value the walk cannot prove (K2),
# whatever it is spelled, so its `.open()` is judged as `Path.open`.
# `(source, kind, qualname)`: the source holds the call on its last line.
UNIMPORTED_RECEIVERS = {
    "a local named after a module": (
        "wave = make(p)\nwave.open()",
        "<expr>.open()",
        "<module>",
    ),
    "a parameter named after a module": (
        "def f(tarfile):\n    return tarfile.open()",
        "<expr>.open()",
        "f",
    ),
    "a loop variable named after a module": (
        'for shelve in d:\n    shelve.open("w")',
        "<expr>.open()",
        "<module>",
    ),
    "a parameter named os": (
        "def f(os):\n    return os.open(p, 0)",
        "<expr>.open(), mode not a literal",
        "f",
    ),
    "a module the walk excuses, not imported": (
        "dbm.gnu.open(p)",
        "<expr>.open(), mode not a literal",
        "<module>",
    ),
    "a bare module name the walk excuses, not imported": (
        "tokenize.open(p)",
        "<expr>.open(), mode not a literal",
        "<module>",
    ),
}

# K2: what the walk cannot prove counts as unnamed.
UNPROVEN = {
    "a mode that is not a literal": ("open(p, m)", "open(), mode not a literal"),
    "encoding=None written out": ("open(p, encoding=None)", "open()"),
    "None in the encoding's position": ('open(p, "r", -1, None)', "open()"),
    "a ** splat": ("open(p, **kw)", "open(), splat"),
    "a * splat": ("open(*a)", "open(), splat"),
    "a ** splat on read_text": ("p.read_text(**kw)", ".read_text(), splat"),
    "a ** splat on subprocess": (
        "import subprocess\nsubprocess.run(c, **kw)",
        "subprocess.run(), splat",
    ),
    "a tempfile mode that is not a literal": (
        "import tempfile\ntempfile.TemporaryFile(m)",
        "tempfile.TemporaryFile(), mode not a literal",
    ),
    "a gzip mode that is not a literal": (
        "import gzip\ngzip.open(p, m)",
        "gzip.open(), mode not a literal",
    ),
}


class Test_unnamed_sites:
    @pytest.mark.parametrize("shape", sorted(NAMED))
    def test_accepts_each_named_shape(self, shape):
        assert censuses.unnamed_sites(NAMED[shape]) == []

    @pytest.mark.parametrize("shape", sorted({**UNNAMED, **UNPROVEN}))
    def test_refuses_each_unnamed_shape_and_what_the_walk_cannot_prove(self, shape):
        source, kind = {**UNNAMED, **UNPROVEN}[shape]
        line = source.count("\n") + 1
        assert censuses.unnamed_sites(source) == [(line, kind, "<module>")]

    @pytest.mark.parametrize("shape", sorted(UNIMPORTED_RECEIVERS))
    def test_refuses_a_receiver_no_import_binds_under_every_spelling(self, shape):
        source, kind, qualname = UNIMPORTED_RECEIVERS[shape]
        line = source.count("\n") + 1
        assert censuses.unnamed_sites(source) == [(line, kind, qualname)]

    def test_refuses_a_call_through_an_aliased_module(self):
        source = "import subprocess as sp\nsp.run(c, text=True)\n"
        assert censuses.unnamed_sites(source) == [
            (2, "subprocess.run(text=)", "<module>")
        ]

    def test_refuses_a_function_imported_by_name(self):
        source = "from subprocess import run as r, check_output\n" + (
            "r(c, text=True)\ncheck_output(c, text=True)\n"
        )
        assert censuses.unnamed_sites(source) == [
            (2, "subprocess.run(text=)", "<module>"),
            (3, "subprocess.check_output(text=)", "<module>"),
        ]

    def test_accepts_a_local_function_named_run(self):
        source = "def run(c, text):\n    return c\n\nrun(c, text=True)\nx.run(c, text=True)\n"
        assert censuses.unnamed_sites(source) == []

    def test_refuses_a_call_an_import_inside_a_function_binds(self):
        source = "def f():\n    from os import popen\n    return popen(c)\n"
        assert censuses.unnamed_sites(source) == [(3, "os.popen()", "f")]

    def test_refuses_each_site_under_its_enclosing_qualname(self):
        source = (
            "class C:\n"
            "    def m(self):\n"
            "        def inner():\n"
            "            return p.read_text()\n"
            "        return inner\n"
            "p.write_text(s)\n"
        )
        assert censuses.unnamed_sites(source) == [
            (4, ".read_text()", "C.m.inner"),
            (6, ".write_text()", "<module>"),
        ]


GUARD = 'if __name__ == "__main__":\n'


class Test_entry_point:
    def test_accepts_the_call_first_a_module_and_a_file_outside_hooks(self, tmp_path):
        plant(tmp_path, "hooks/fixed.py", GUARD + "    console.to_utf8()\n    main()\n")
        plant(tmp_path, "hooks/module.py", "x = 1\n")
        root = plant(tmp_path, "tests/x.py", GUARD + "    main()\n")
        for rel in ("hooks/fixed.py", "hooks/module.py", "tests/x.py"):
            assert censuses.entry_point(rel, root) == [], rel

    def test_refuses_a_block_without_the_call_and_one_with_it_after_main(
        self, tmp_path
    ):
        plant(tmp_path, "hooks/sub/deep.py", "import os\n\n" + GUARD + "    main()\n")
        root = plant(
            tmp_path, "hooks/after.py", GUARD + "    main()\n    console.to_utf8()\n"
        )
        assert censuses.entry_point("hooks/sub/deep.py", root) == [
            "hooks/sub/deep.py:3: entry_point: the `__main__` block does not open "
            "with `console.to_utf8()`, so a hook that raises while printing dies "
            "with stdout empty; make the call the block's first statement, or "
            "put `# exempt from entry_point: <why>` on its own line above it"
        ]
        assert [
            p.split(": ")[0] for p in censuses.entry_point("hooks/after.py", root)
        ] == ["hooks/after.py:1"]


class Test_splitlines:
    def test_accepts_a_call_outside_the_shipped_directories(self, tmp_path):
        root = plant(tmp_path, "tests/x.py", "def f(t):\n    return t.splitlines()\n")
        assert censuses.splitlines("tests/x.py", root) == []

    @pytest.mark.parametrize(
        "source, line",
        [
            (
                "def reader(text):\n    return (\n        text\n"
                "        .splitlines()\n    )\n",
                "skills/new.py:4: splitlines: `.splitlines(` ends a line where GFM "
                "does not; a reader of markdown or record text reads "
                "`hooks/lib/blocks.py#gfm_lines`, and a call over any other text puts "
                "`# exempt from splitlines: <what it splits>` on its own line "
                "above it",
            ),
            (
                "def reader(a, b):\n"
                "    # exempt from splitlines: git output\n"
                "    return a.splitlines() + b.splitlines()\n",
                "skills/new.py:3: splitlines: two calls on one line, and an "
                "exemption names one; put each call on a line of its own",
            ),
        ],
        ids=["at-the-line-that-names-it", "a-second-call-under-one-exemption"],
    )
    def test_refuses_a_planted_call(self, tmp_path, source, line):
        root = plant(tmp_path, "skills/new.py", source)
        assert censuses.splitlines("skills/new.py", root) == [line]


class Test_heading_rule:
    def test_accepts_the_spelling_in_a_docstring_and_a_whole_line_comment(
        self, tmp_path
    ):
        source = (
            'def f(line):\n    """Not `line.startswith("#")`."""\n'
            '    # nor startswith("#")\n    return line\n'
        )
        root = plant(tmp_path, "hooks/x.py", source)
        assert censuses.heading_rule("hooks/x.py", root) == []

    def test_refuses_a_counted_run_and_a_startswith(self, tmp_path):
        source = 'import re\nH = re.compile(r"#{1,6} ")\nok = line.startswith("#")\n'
        root = plant(tmp_path, "skills/x.py", source)
        assert [
            p.split(": ")[0] for p in censuses.heading_rule("skills/x.py", root)
        ] == [
            "skills/x.py:2",
            "skills/x.py:3",
        ]
        assert censuses.heading_rule("skills/x.py", root)[0].endswith(
            "heading_rule: a second spelling of the heading rule; a reader of a "
            "document's sections asks `skills/verify/scripts/unverified_check.py"
            "#heading_level`"
        )


PLANTED = "import datetime\nzip(a, b, strict=True)\ndatetime.UTC\n"


class Test_newer_than:
    def test_accepts_both_constructs_at_the_version_that_has_them(self):
        assert censuses.newer_than(PLANTED, (3, 11)) == []

    def test_refuses_both_constructs_and_a_newer_syntax_at_the_floor(self):
        assert {what for _, what in censuses.newer_than(PLANTED, (3, 9))} == set(
            censuses.NEWER
        )
        assert censuses.newer_than("match x:\n    case 1:\n        pass\n", (3, 9))


class Test_matches:
    def test_accepts_a_star_across_a_slash_and_a_bare_name(self):
        assert censuses.matches("hooks/*.py", "hooks/git/pre-commit.py")
        assert censuses.matches("seal_stamp.py", "skills/verify/scripts/seal_stamp.py")

    def test_refuses_another_directory(self):
        assert not censuses.matches("hooks/*.py", "skills/verify/scripts/broad_gate.py")


class Test_floor_syntax:
    def test_accepts_a_file_no_floor_pattern_names(self, tmp_path):
        plant(tmp_path, "ruff.toml", RUFF)
        root = plant(tmp_path, "skills/x.py", PLANTED)
        assert censuses.floor_syntax("skills/x.py", root) == []

    def test_refuses_a_construct_newer_than_the_files_floor(self, tmp_path):
        plant(tmp_path, "ruff.toml", RUFF)
        root = plant(tmp_path, "hooks/x.py", PLANTED)
        assert censuses.floor_syntax("hooks/x.py", root) == [
            "hooks/x.py:2: floor_syntax: `zip(..., strict=...)` needs a python3 "
            "newer than 3.9, the version ruff.toml lints this file at, and it "
            "runs before any floor is checked",
            "hooks/x.py:3: floor_syntax: `datetime.UTC` needs a python3 newer "
            "than 3.9, the version ruff.toml lints this file at, and it runs "
            "before any floor is checked",
        ]


class Test_section_sign:
    def test_accepts_a_record_a_clean_file_and_one_that_is_not_text(self, tmp_path):
        plant(tmp_path, "seal/threads/1-x/frame/design.md", f"see {SIGN}3\n")
        plant(tmp_path, "evals/behaviour/c.md", f"see {SIGN}3\n")
        (tmp_path / "x.png").write_bytes(b"\xff\xd8\xff")
        root = plant(tmp_path, "hooks/b.py", "# clean\n")
        for rel in (
            "seal/threads/1-x/frame/design.md",
            "evals/behaviour/c.md",
            "x.png",
            "hooks/b.py",
        ):
            assert censuses.section_sign(rel, root) == [], rel

    def test_refuses_the_sign_at_its_line(self, tmp_path):
        root = plant(tmp_path, "seal/follow-up.md", f"clean\nsee {SIGN}3\n")
        assert censuses.section_sign("seal/follow-up.md", root) == [
            "seal/follow-up.md:2: section_sign: a living file writes the section "
            "sign. Cite a contract rule as `contract rule <N>`, and another "
            "file's section by its path and its heading text in italics"
        ]


class Test_real_identifiers:
    def test_accepts_the_fixture_values_and_the_product_hosts_directory(self, tmp_path):
        plant(tmp_path, "kept.md", "example.com and /Users/x/\n")
        root = plant(
            tmp_path,
            "ok.md",
            f"from a {PRODUCT_HOST} account, at {PRODUCT_HOST}/directory/manage\n",
        )
        (tmp_path / "x.png").write_bytes(b"\x89PNG " + REFUSED_DOMAIN.encode())
        assert censuses.real_identifiers("kept.md", root) == []
        assert censuses.real_identifiers("ok.md", root) == []
        assert censuses.real_identifiers("x.png", root) == []

    def test_refuses_a_domain_a_user_path_and_the_product_host_elsewhere(
        self, tmp_path
    ):
        text = (
            f"a domain {REFUSED_DOMAIN} and a path {REFUSED_USER_PATH}\n"
            f"a conversation at {PRODUCT_HOST}/share/0000\n"
            f"write to someone@{PRODUCT_HOST}\n"
            f"a host under it, docs.{PRODUCT_HOST}\n"
        )
        root = plant(tmp_path, "leak.md", text)
        found = censuses.real_identifiers("leak.md", root)
        assert [p.split(": ")[0] for p in found] == [
            f"leak.md:{n}" for n in (1, 2, 3, 4)
        ]
        assert found[0] == (
            f"leak.md:1: real_identifiers: {REFUSED_DOMAIN} is a real-looking "
            "domain, and fixtures and examples use example.com; "
            f"{REFUSED_USER_PATH} is a real user path, and fixtures use /Users/x/"
        )

    def test_refuses_a_user_path_spelled_as_a_projects_directorys_slug(self, tmp_path):
        """#1177 round 6 finding 4. A projects directory spells the path its
        session started in with dashes, so a scratchpad path reaches a record
        as `-Users-<name>-<repo>`, and the slashed pattern read none of it.
        The fixture user `x` passes in that spelling too, and a placeholder
        or a character class is no user name."""
        slug = "-" + "Users-somebody-"
        root = plant(
            tmp_path,
            "leak.md",
            f"a draft at /private/tmp/claude-501/{slug}Documents-GitHub-repo/s\n"
            "a fixture at ~/.claude/projects/-Users-x-repo/1.jsonl\n"
            "a pattern `-Users-[A-Za-z]` and a placeholder -Users-<name>-repo\n",
        )
        assert censuses.real_identifiers("leak.md", root) == [
            f"leak.md:1: real_identifiers: {slug} is a real user path, and "
            "fixtures use /Users/x/"
        ]


OLD = "Spec" + "Seal"
# One line for each family of old names OLD_NAME refuses, built from halves
# so this file does not write them, with the spelling each is reported by.
OLD_SPELLINGS = [
    (f"the {OLD} workflow", OLD),
    (f"`{OLD.lower()}:implement`", OLD.lower()),
    (f"{OLD.upper()}_RECORD_DIR", OLD.upper()),
    ("Specs, " + "sealed", "Specs, " + "sealed"),
    ("the " + "smi" + "th builds it", "smi" + "th"),
    ("the " + "War" + "den reviews it", "War" + "den"),
    ("`agents/" + "scr" + "ibe.md`", "scr" + "ibe"),
    ("`seal/" + "specs/1-x/routing.md`", "seal/" + "specs"),
    ("the frame's `" + "spec" + ".md`", "spec" + ".md"),
    ("`" + "over" + "view.md` holds it", "over" + "view.md"),
    ("`broad" + "-gate.md` at HEAD", "broad" + "-gate"),
    ("`<item>/pha" + "ses/phase-1.md`", "pha" + "ses/"),
    ("`rounds" + "/round-1.md`", "rounds" + "/"),
    ("run `mutation" + "-check`", "mutation" + "-check"),
]


class Test_old_names:
    def test_accepts_the_new_names_kept_spellings_records_and_the_migration(
        self, tmp_path
    ):
        living = (
            "AgenticSeal, `agentic:crafter`, the proofer and the tracer\n"
            "`seal/threads/1-x/frame/design.md`, `gaps.md`, `trail/gate.md`\n"
            "`<thread>/trail/phases/phase-1.md` and `trail/rounds/round-1.md`\n"
            "`docs/the-broad" + "-gate.md` and `graders/shape-writes-spec.md`\n"
            f"a commit made before the rename carries `{OLD}-Routing:`\n"
            f"<!-- {OLD.lower()}:start --> and <!-- {OLD.lower()}:end -->\n"
            f"# {OLD.lower()}-git-hook\n"
            f"git clone https://github.com/MichaelYcJo/{OLD}.git\n"
            f"claude plugin marketplace remove {OLD.lower()}, then "
            f"`{OLD.lower()}@{OLD.lower()}` is gone\n"
            f'"renames": {{"{OLD.lower()}": "agentic"}}\n'
            f"git mv .{OLD.lower()}/README.md seal/README.md\n"
        )
        old = "\n".join(line for line, _ in OLD_SPELLINGS) + "\n"
        plant(tmp_path, "docs/living.md", living)
        for rel in (
            "seal/threads/1-x/frame/design.md",
            "evals/behaviour/proofer/replay-1-r1/prompt.md",
            "evals/behaviour/proofer/seeded-1/prompt.md",
            "evals/scripts/recurred_truths.json",
            "hooks/root-migrate.py",
            "tests/hooks/test_root_migrate.py",
        ):
            plant(tmp_path, rel, old)
        (tmp_path / "x.png").write_bytes(b"\xff\xd8\xff" + OLD.encode())
        root = plant(
            tmp_path,
            "hooks/kept.py",
            "# exempt from old_names: the old name a reader still meets\n"
            f'OLD = "{OLD.lower()}"\n',
        )
        for rel in (
            "docs/living.md",
            "seal/threads/1-x/frame/design.md",
            "evals/behaviour/proofer/replay-1-r1/prompt.md",
            "evals/behaviour/proofer/seeded-1/prompt.md",
            "evals/scripts/recurred_truths.json",
            "hooks/root-migrate.py",
            "tests/hooks/test_root_migrate.py",
            "x.png",
            "hooks/kept.py",
        ):
            assert censuses.old_names(rel, root) == [], rel

    def test_refuses_each_old_name_at_its_line(self, tmp_path):
        text = "clean\n" + "\n".join(line for line, _ in OLD_SPELLINGS) + "\n"
        rel = "evals/behaviour/proofer/rule-x/prompt.md"
        found = censuses.old_names(rel, plant(tmp_path, rel, text))
        assert found == [
            f"{rel}:{number}: old_names: `{spelling}` is a name the rename to "
            "AgenticSeal replaced; write the new one from #1051's mapping, or "
            "put `# exempt from old_names: <why>` on its own line above a line "
            "that keeps it on purpose"
            for number, (_, spelling) in enumerate(OLD_SPELLINGS, 2)
        ], found

    def test_accepts_an_old_path_only_where_a_commit_holds_it(self, tmp_path):
        """A released work item's record is a coordinate into git history,
        which the move does not rewrite: `<commit>:<path>` is the one form
        that passes, because `git show` opens it as written. The same path
        with no commit, or after one that is not hex, is refused."""
        old = "seal/" + "specs/1790000000-a-released-item"
        phase, design = "pha" + "ses/phase-3.md", "sp" + "ec.md"
        text = (
            f"measured in `5f11923f:{old}/{phase}` and in\n"
            f"`67694cba:{old}/{design}` *Scope*, the work item `0ed5dd3b:{old}/`\n"
            f"`{old}/{phase}`\n"
            f"`HEAD:{old}/{design}`\n"
        )
        root = plant(tmp_path, "docs/x.md", text)
        assert [p.split(": ")[0] for p in censuses.old_names("docs/x.md", root)] == [
            "docs/x.md:3",
            "docs/x.md:4",
        ]

    def test_refuses_an_old_name_beside_a_kept_spelling(self, tmp_path):
        text = f"`{OLD}-Routing:` is what the {OLD} trailer was\n"
        root = plant(tmp_path, "docs/x.md", text)
        assert [p.split(": ")[0:2] for p in censuses.old_names("docs/x.md", root)] == [
            ["docs/x.md:1", "old_names"]
        ]


VACATED_MESSAGE = (
    "{rel}:{number}: vacated_paths: `{old}` is a path no file holds since the "
    "file moved to `{new}`; write the path the file stands at, or put "
    "`# exempt from vacated_paths: <why>` on its own line above a line that "
    "keeps it on purpose"
)


def plant_moved(root):
    """One file moved into each kind of subdirectory the census reads, and
    `hooks/kept.py`, which stands in `hooks/lib/` and at the top too."""
    for rel in (
        "hooks/lib/moved.py",
        "hooks/lib/kept.py",
        "hooks/kept.py",
        "templates/records/sdd-x.md",
        "templates/setup/y.md",
        "tests/skills/test_moved.py",
        "tests/e2e/test_deep.py",
    ):
        plant(root, rel, "x\n")
    return str(root)


class Test_vacated_paths:
    def test_accepts_a_tree_where_nothing_moved(self, tmp_path):
        root = plant(tmp_path, "docs/x.md", "`hooks/moved.py`, `templates/y.md`\n")
        assert censuses.vacated_paths("docs/x.md", root) == []

    def test_refuses_the_spelling_one_level_up_of_each_moved_file(self, tmp_path):
        text = (
            "clean\n"
            "`hooks/moved.py` loads it\n"
            "read `$CLAUDE_PLUGIN_ROOT/templates/sdd-x.md`\n"
            "copied from ${PLUGIN}/templates/y.md.\n"
            "`tests/test_moved.py::test_case`\n"
            "`HEAD:hooks/moved.py`\n"
        )
        plant_moved(tmp_path)
        root = plant(tmp_path, "docs/x.md", text)
        assert censuses.vacated_paths("docs/x.md", root) == [
            VACATED_MESSAGE.format(rel="docs/x.md", number=number, old=old, new=new)
            for number, old, new in (
                (2, "hooks/moved.py", "hooks/lib/moved.py"),
                (3, "templates/sdd-x.md", "templates/records/sdd-x.md"),
                (4, "templates/y.md", "templates/setup/y.md"),
                (5, "tests/test_moved.py", "tests/skills/test_moved.py"),
                (6, "hooks/moved.py", "hooks/lib/moved.py"),
            )
        ]

    def test_accepts_the_new_path_a_longer_path_a_file_still_there_and_a_commit(
        self, tmp_path
    ):
        text = (
            "`hooks/lib/moved.py`, `templates/records/sdd-x.md`\n"
            "`other/hooks/moved.py`, `myhooks/moved.py`, `hooks/moved.pyc`\n"
            "`hooks/kept.py` and `tests/test_deep.py`, which `tests/e2e/` holds\n"
            "measured in `5f11923f:hooks/moved.py`\n"
            "# exempt from vacated_paths: the layout a release before the move had\n"
            "`templates/y.md`\n"
        )
        plant_moved(tmp_path)
        root = plant(tmp_path, "docs/x.md", text)
        assert censuses.vacated_paths("docs/x.md", root) == []

    def test_accepts_the_records_and_a_recorded_case(self, tmp_path):
        root = plant_moved(tmp_path)
        records = (
            "seal/threads/1-x/frame/design.md",
            "evals/behaviour/proofer/replay-1-r1/prompt.md",
            ".test_durations",
        )
        for rel in records:
            plant(tmp_path, rel, "`hooks/moved.py`\n")
        for rel in records:
            assert censuses.vacated_paths(rel, root) == [], rel


class Test_module:
    def test_every_file_no_module_file_declares_meets_every_census(self):
        """The censuses over every tracked file whose module file does not run
        them itself: the documents, and every module not yet in the layout."""
        tracked, _missing = on_disk(ROOT, git_listing(ROOT, "ls-files", check=True))
        assert tracked, (
            "git ls-files listed no tracked file, so the sweep judged nothing"
        )
        declared = set()
        for directory, _dirs, names in os.walk(os.path.join(ROOT, "tests")):
            for name in names:
                if name.startswith("test_") and name.endswith(".py"):
                    with open(os.path.join(directory, name), encoding="utf-8") as f:
                        source = f.read()
                    # Only a file that runs the censuses takes its target out
                    # of the sweep: one that declares and runs none leaves it
                    # here, judged.
                    if layout.runs_the_censuses(ast.parse(source)):
                        declared.add(layout.declared_target(source))
        found = [
            p for rel in tracked if rel not in declared for p in censuses.judge(rel)
        ]
        assert not found, "\n".join(found)

    def test_no_method_is_matched_by_its_dotted_name(self):
        """#762: a method called on its class takes the path first, and only
        the `.open` branch of `judge_call` moves the positions for it. A
        method's row in a table `judge_call` matches by dotted name is reached
        there first, unshifted, so its path is read as the mode and its mode
        as the encoding."""
        tables = tables_matched_by_dotted_name()
        assert "OPENERS" in tables, tables
        moved = {"OPENERS": {"zipfile.Path.open": (0, 1), "io.open": (1, 3)}}
        assert methods_of_unbound_receivers(moved) == ["OPENERS['zipfile.Path.open']"]
        unshifted = sorted(
            set(censuses.OPEN_METHODS) - {"<expr>"} - censuses.UNBOUND_RECEIVERS
        )
        assert not unshifted, (
            f"OPEN_METHODS rows {unshifted} name a class outside "
            "UNBOUND_RECEIVERS, so the method called on its class is judged "
            "without the shift"
        )
        methods = methods_of_unbound_receivers(tables)
        assert not methods, (
            f"{methods} are methods of a class in UNBOUND_RECEIVERS, matched by "
            "their dotted name before the `.open` branch can shift them"
        )


def tables_matched_by_dotted_name():
    """`{name: table}` for every table `judge_call` tests `target in`, read
    from `judge_call`'s own source, so a table added there later is read
    here too."""

    tree = ast.parse(inspect.getsource(censuses.judge_call))
    names = {
        node.comparators[0].id
        for node in ast.walk(tree)
        if isinstance(node, ast.Compare)
        and isinstance(node.left, ast.Name)
        and node.left.id == "target"
        and isinstance(node.ops[0], ast.In)
        and isinstance(node.comparators[0], ast.Name)
    }
    return {name: vars(censuses)[name] for name in sorted(names)}


def methods_of_unbound_receivers(tables):
    """Each key of `tables` that is a method of a class in
    `UNBOUND_RECEIVERS`, as `TABLE['key']`."""
    return sorted(
        f"{name}[{key!r}]"
        for name, table in tables.items()
        for key in table
        if key.rsplit(".", 1)[0] in censuses.UNBOUND_RECEIVERS
    )


test_census = census_case(TARGET)
