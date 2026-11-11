"""`lib/sibling.py`: the one loader a script reaches another module by.

Each case runs a copy of the module whose root is a tree under `tmp_path`,
so the files it loads are written there and named by a stem no other case
and no tracked module uses; the stems a case registers are taken out of
`sys.modules` after it.
"""

import os
import shutil
import sys

import pytest
from conftest import LIB, census_case, load_module

TARGET = "lib/sibling.py"


@pytest.fixture
def tree(tmp_path):
    """`(loader, root, stems)`: a copy of the module under ROOT's `lib/`,
    run under a name of its own, and the list a case adds each stem it
    registers to."""
    root = tmp_path / "plugin"
    (root / "lib").mkdir(parents=True)
    shutil.copy(os.path.join(LIB, "sibling.py"), root / "lib" / "sibling.py")
    loader = load_module(root / "lib" / "sibling.py", f"sibling_{tmp_path.name}")
    stems = []
    yield loader, root, stems
    for stem in stems:
        sys.modules.pop(stem, None)


def plant(root, rel, text):
    """Write TEXT at the `/`-joined REL under ROOT."""
    path = root.joinpath(*rel.split("/"))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


# A module that counts how many times its body ran, in a file beside it.
COUNTED = (
    "import os\n"
    "with open(os.path.join(os.path.dirname(__file__), 'runs'), 'a') as f:\n"
    "    f.write('run\\n')\n"
)


class Test_load:
    def test_accepts_a_module_and_runs_it_once(self, tree):
        """Two loads of one file are one module under its stem, and its body
        ran once: what a settle that loaded `lib/blocks.py` 32 times now
        does (`frame/design.md` G6, S1)."""
        loader, root, stems = tree
        stems.append("counted_once_by_sibling")
        plant(root, "skills/x/scripts/counted_once_by_sibling.py", COUNTED)
        first = loader.load("skills/x/scripts/counted_once_by_sibling.py")
        again = loader.load("skills/x/scripts/counted_once_by_sibling.py")
        assert first is again
        assert sys.modules["counted_once_by_sibling"] is first
        runs = root / "skills" / "x" / "scripts" / "runs"
        assert runs.read_text(encoding="utf-8") == "run\n"

    def test_accepts_the_module_lib_imported_by_its_plain_name(self, tree):
        """A `lib/` module imports its neighbour by a plain name, which
        registers the neighbour under its stem; `load` hands back that
        module rather than running the file a second time (G14). The
        directory is spelt the way a script puts it on `sys.path`, through
        `..`, so the module's `__file__` is another spelling of the path
        `load` builds."""
        loader, root, stems = tree
        stems.append("neighbour_of_sibling")
        plant(root, "lib/neighbour_of_sibling.py", COUNTED)
        (root / "skills").mkdir()
        spelt = os.path.join(str(root), "skills", "..", "lib")
        sys.path.insert(0, spelt)
        try:
            import neighbour_of_sibling
        finally:
            sys.path.remove(spelt)
        assert loader.load("lib/neighbour_of_sibling.py") is neighbour_of_sibling
        assert (root / "lib" / "runs").read_text(encoding="utf-8") == "run\n"

    def test_refuses_an_absent_file_in_one_sentence_at_exit_2(self, tree, capsys):
        """S5. An absent module is the one sentence naming its absolute
        path, whichever script asked, and exit 2 as an integer: a string
        argument to `SystemExit` exits 1 (#590)."""
        loader, root, _stems = tree
        with pytest.raises(SystemExit) as stopped:
            loader.load("skills/x/scripts/absent_beside_sibling.py")
        assert stopped.value.code == 2
        path = os.path.join(
            str(root), "skills", "x", "scripts", "absent_beside_sibling.py"
        )
        assert capsys.readouterr().err == (
            f"cannot read {path}, which this command loads. It ships in the "
            "plugin beside this script; a copy of one script taken on its own "
            "is not a plugin. Nothing was read.\n"
        )
        assert "absent_beside_sibling" not in sys.modules

    def test_refuses_a_stem_another_file_holds(self, tree):
        """A file whose stem another file already runs under is refused with
        both paths, and the module there stays: a stem names one file in a
        process (G16)."""
        loader, root, stems = tree
        stems.append("held_by_another_file")
        other = plant(root, "lib/held_by_another_file.py", "")
        plant(root, "skills/x/scripts/held_by_another_file.py", "")
        held = load_module(other, "held_by_another_file")
        sys.modules["held_by_another_file"] = held
        with pytest.raises(ImportError) as refused:
            loader.load("skills/x/scripts/held_by_another_file.py")
        message = str(refused.value)
        assert str(other) in message
        assert (
            os.path.join("skills", "x", "scripts", "held_by_another_file.py") in message
        )
        assert sys.modules["held_by_another_file"] is held

    @pytest.mark.parametrize(
        "body, raised",
        [
            ("raise ValueError('mid-run')\n", ValueError),
            ("raise SystemExit(3)\n", SystemExit),
        ],
        ids=["an-exception", "an-exit"],
    )
    def test_refuses_to_keep_a_module_that_raises(self, tree, body, raised):
        """A module that raises while it runs reaches the caller with its own
        exception, an exit keeping its code, and is not left registered, so
        the caller's contract decides what it means (*Scope* item 4)."""
        loader, root, stems = tree
        stems.append("raises_under_sibling")
        plant(root, "skills/x/scripts/raises_under_sibling.py", body)
        with pytest.raises(raised) as caught:
            loader.load("skills/x/scripts/raises_under_sibling.py")
        if raised is SystemExit:
            assert caught.value.code == 3
        assert "raises_under_sibling" not in sys.modules


test_census = census_case(TARGET)
