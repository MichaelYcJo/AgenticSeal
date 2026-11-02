"""`skills/settle/scripts/passages.py`, one class per function.

The paste check's reader, moved out of
`tests/text/test_no_passage_is_pasted_into_a_second_file.py` by #1216 so that
`skills/code-review/scripts/chain_check.py` reads a design's `to` the way the
test reads the rule documents. The method and why it is verbatim stay in that
test's docstring, and the measurement that chose `WINDOW` in
`tests/text/test_a_moved_rule_leaves_its_definition.py`'s. The two cases of
`Test_words` came from the paste test, where they tested `words` alone.
"""

import itertools
import os

import pytest
from conftest import ROOT, census_case, load_module

TARGET = "skills/settle/scripts/passages.py"

passages = load_module(
    os.path.join(ROOT, "skills", "settle", "scripts", "passages.py"),
    "agentic_passages",
)
WINDOW = passages.WINDOW


def shared(*texts):
    """Whether any two of TEXTS share a run of `WINDOW` normalised words."""
    runs = [passages.windows(passages.words(t)) for t in texts]
    return any(a & b for a, b in itertools.combinations(runs, 2))


class Test_in_corpus:
    @pytest.mark.parametrize(
        "rel",
        [
            "docs/the-review-record.md",
            "skills/implement/SKILL.md",
            "agents/crafter.md",
            "templates/records/sdd-round.md",
            "CLAUDE.md",
            "CONTRIBUTING.md",
            "README.md",
        ],
    )
    def test_accepts_a_rule_document(self, rel):
        assert passages.in_corpus(rel)

    # One path per guard of `in_corpus`, each refused by that guard alone, so
    # widening any one guard fails exactly its path. Membership in
    # `TOP_FILES` and the `TOP_DIRS` prefix are the two sides of one `or`, so
    # each is widened at its boundary: membership to every top-level path,
    # the prefix to its directory names without their slash.
    @pytest.mark.parametrize(
        "rel",
        [
            # Under `skills/` and no edition: the `.md` suffix alone.
            "skills/README.txt",
            # Under `docs/`: the `.ko.md` exclusion alone.
            "docs/the-review-record.ko.md",
            # A tracked top-level `.md` outside `TOP_FILES`: membership alone.
            "SECURITY.md",
            # A directory whose name `docs` begins: the prefix's slash alone.
            "docs-old/notes.md",
        ],
        ids=["the-md-suffix", "the-ko-exclusion", "top-files", "top-dirs-slash"],
    )
    def test_refuses_a_path_one_guard_alone_refuses(self, rel):
        assert not passages.in_corpus(rel)


class Test_words:
    def test_accepts_a_wrapped_section_name_as_one_token(self):
        """A link carries its heading's words; a name broken across a line is
        still the name, and two links to one long heading share nothing."""
        name = (
            "A change writes fragments, never a shared file, and the release "
            "gathers every one of them before it folds"
        )
        assert len(name.split()) > WINDOW
        one = f"See `docs/the-record-layout.md` *{name}* for where it goes.\n"
        wrapped = name.replace(" a shared", chr(10) + "a shared")
        two = f"Read `docs/the-record-layout.md`\n*{wrapped}*\nfirst.\n"
        path = f"`CONTRIBUTING.md`'s *{name}*\n"
        other = f"As docs/the-record-layout.md *{name}* says.\n"
        assert not shared(one, two, path, other)

    def test_refuses_fences_and_headings_and_reads_case_and_backticks_as_no_words(
        self,
    ):
        """A fenced block and a heading line are dropped, and a copy whose first
        word its new sentence capitalised, or which it backticked, is a copy."""
        run = " ".join(f"w{i}" for i in range(WINDOW))
        fenced = f"```\n{run}\n```\n"
        heading = f"## {run}\n"
        for skipped in (fenced, heading):
            assert not shared(skipped, run), skipped
        assert shared(run, run)
        # A copy whose first word was capitalised by its new sentence is a copy.
        assert shared(run.upper(), f"`{run}`")


class Test_windows:
    def test_accepts_each_run_of_window_words_once(self):
        listed = [f"w{i}" for i in range(WINDOW + 1)] + ["w0"]
        assert passages.windows(listed) == {
            " ".join(listed[0:WINDOW]),
            " ".join(listed[1 : WINDOW + 1]),
            " ".join(listed[2 : WINDOW + 2]),
        }

    def test_refuses_a_text_shorter_than_the_window(self):
        assert passages.windows([f"w{i}" for i in range(WINDOW - 1)]) == set()


test_census = census_case(TARGET)
