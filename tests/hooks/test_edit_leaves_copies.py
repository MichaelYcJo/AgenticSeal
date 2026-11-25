"""`hooks/edit-leaves-copies.py`: after an `Edit` of a work item's record,
the places in the item's other records that still hold the words the edit
replaced are named to the party that made it.

The hook prints a `PostToolUse` object whose `additionalContext` names each
place, or nothing, and exits 0 on every path (#1612). The cases run the
hook's command as `hooks/hooks.json` spells it, through
`tests/hooks/test_core_start.py#start`: its `python3` half with this
interpreter in place of `python3` and `${CLAUDE_PLUGIN_ROOT}` filled in.
The registration is held by `tests/behaviour/test_chain_hooks_hardening.py`.
"""

import json

from conftest import census_case, load, mark_root
from test_core_start import start

TARGET = "hooks/edit-leaves-copies.py"

hook = load(TARGET, "agentic_edit_leaves_copies")

EVENT = "PostToolUse"
ITEM = "1780000000-a-work-item"

# A sentence a work item's design states, and the same sentence after an
# edit replaced two of its words. The span the edit replaced, with three
# words on each side, is `SPAN`.
BEFORE = (
    "The quote check refuses a line of pr.md whose words no longer stand "
    "in the file it names."
)
AFTER = BEFORE.replace("no longer stand", "do not stand")
SPAN = "pr.md whose words no longer stand in the"


def item(where, files, marked=True):
    """A repository at WHERE whose `seal/` root holds `ITEM`, its records
    FILES, a mapping of `/`-joined paths under the item's directory to their
    text, or to bytes written as they are. The root's `README.md` opens with
    the marker where MARKED, and holds another first line otherwise. The
    item's directory."""
    home = where / "seal"
    if marked:
        mark_root(home)
    else:
        home.mkdir(parents=True)
        (home / "README.md").write_text("# Our own seal package\n", encoding="utf-8")
    directory = home / "threads" / ITEM
    for rel, text in files.items():
        path = directory.joinpath(*rel.split("/"))
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(text, bytes):
            path.write_bytes(text)
        else:
            path.write_text(text, encoding="utf-8")
    return directory


def edited(path, old, new, tool="Edit"):
    """The `PostToolUse` payload of a TOOL call that replaced OLD with NEW
    in the file at PATH."""
    return json.dumps(
        {
            "hook_event_name": EVENT,
            "tool_name": tool,
            "tool_input": {
                "file_path": str(path),
                "old_string": old,
                "new_string": new,
                "replace_all": False,
            },
        }
    )


def run(body, cwd=None):
    """The hook's stdout for BODY, the process started in CWD. `start`
    asserts the exit code 0 and an empty stderr."""
    return start(body, event=EVENT, cwd=cwd)


def context(out):
    """The `additionalContext` of the object OUT holds whole, and nothing
    else."""
    said = json.loads(out)
    assert list(said) == ["hookSpecificOutput"], said
    held = said["hookSpecificOutput"]
    assert sorted(held) == ["additionalContext", "hookEventName"], held
    assert held["hookEventName"] == EVENT, held
    return held["additionalContext"]


def quoted(sentence):
    """A `pr.md` whose third line quotes SENTENCE from `frame/design.md`."""
    return f'# Body\n\n- "{sentence}" (`frame/design.md` *Scope*)\n'


def design(sentence):
    """A `frame/design.md` whose fifth line is SENTENCE."""
    return f"# Design\n\n## Scope\n\n{sentence}\n"


class Test_main:
    """The pairs differ by the records the fixture writes, the path the
    payload names, or the words it replaced."""

    def test_names_a_quote_that_still_holds_the_replaced_words(self, tmp_path):
        """A9. `frame/design.md` no longer holds the sentence its `pr.md`
        quotes on line 3. The context names `pr.md`, its line and the words
        that stand there, and says what the party does with each place."""
        directory = item(
            tmp_path, {"frame/design.md": design(AFTER), "pr.md": quoted(BEFORE)}
        )
        said = context(run(edited(directory / "frame" / "design.md", BEFORE, AFTER)))
        assert f'- `pr.md` line 3: "{SPAN}"' in said, said
        assert "`frame/design.md`" in said and ITEM in said, said
        # What the party does with a place: the rule it cites, and the
        # place that stays.
        assert "skills/agent-contract/SKILL.md` rule 19" in said, said
        assert "A place that states another fact" in said, said

    def test_names_each_place_in_every_record_it_reads_with_its_line(self, tmp_path):
        """A9. A copy in `gaps.md`, one in `frame/questions.md`, one in a
        `pr.<lang>.md` and one left in the edited file itself are each
        named, by the path under the item's directory and the line, in
        path order."""
        text = design(AFTER) + "\nAgain: " + BEFORE + "\n"
        directory = item(
            tmp_path,
            {
                "frame/design.md": text,
                "gaps.md": "# Gaps\n\n" + BEFORE + "\n",
                "frame/questions.md": "# Q\n\n| Q1 | " + BEFORE + " |\n",
                "pr.ko.md": "# 본문\n\n- " + BEFORE + "\n",
            },
        )
        said = context(run(edited(directory / "frame" / "design.md", BEFORE, AFTER)))
        named = [
            "- `frame/design.md` line 7:",
            "- `frame/questions.md` line 3:",
            "- `gaps.md` line 3:",
            "- `pr.ko.md` line 3:",
        ]
        at = [said.find(one) for one in named]
        assert -1 not in at and at == sorted(at), (at, said)

    def test_names_a_quote_whose_words_cross_a_line_break(self, tmp_path):
        """A9. The record holds the words with a line break where the edit
        held a space, and a run of spaces where it held one: whitespace is
        collapsed on both sides, and the line is where the words open."""
        wrapped = BEFORE.replace("words no", "words\nno").replace(" in ", "   in ")
        directory = item(
            tmp_path,
            {"frame/design.md": design(AFTER), "gaps.md": "# Gaps\n\n" + wrapped},
        )
        said = context(run(edited(directory / "frame" / "design.md", BEFORE, AFTER)))
        assert f'- `gaps.md` line 3: "{SPAN}"' in said, said

    def test_names_the_words_around_an_insertion(self, tmp_path):
        """A9. An edit that only inserts words replaces the run they split:
        the three words on each side of the point."""
        old = "alpha bravo charlie delta echo foxtrot golf hotel india"
        new = old.replace("delta echo", "delta and then echo")
        directory = item(
            tmp_path,
            {
                "frame/plan.md": "# Plan\n\n" + new + "\n",
                "gaps.md": "# Gaps\n\n" + old + "\n",
            },
        )
        said = context(run(edited(directory / "frame" / "plan.md", old, new)))
        around = "bravo charlie delta echo foxtrot golf"
        assert f'- `gaps.md` line 3: "{around}"' in said, said

    def test_names_a_span_of_six_words_and_thirty_characters(self, tmp_path):
        """A9, the floor. A span of `MIN_WORDS` words and `MIN_CHARS`
        characters is kept, so a copy of it is named."""
        old = "alpha beta gamma CHANGED ep zz"
        assert len(old.split()) == hook.MIN_WORDS, old
        assert len(old) == hook.MIN_CHARS, old
        new = old.replace("CHANGED", "delta")
        directory = item(
            tmp_path,
            {"frame/plan.md": new + "\n", "gaps.md": old + "\n"},
        )
        said = context(run(edited(directory / "frame" / "plan.md", old, new)))
        assert f'- `gaps.md` line 1: "{old}"' in said, said

    def test_prints_nothing_for_a_span_under_six_words_or_thirty_characters(
        self, tmp_path
    ):
        """A10. A span of five words, and one of six words under thirty
        characters, are not kept, though a copy of each stands in
        `gaps.md`."""
        short = "alpha beta CHANGED gamma epsilon"
        narrow = "a bb cc CHANGED dd ee"
        assert len(narrow.split()) == hook.MIN_WORDS, narrow
        assert len(narrow) < hook.MIN_CHARS, narrow
        for old in (short, narrow):
            new = old.replace("CHANGED", "delta")
            directory = item(
                tmp_path / str(len(old)),
                {"frame/plan.md": new + "\n", "gaps.md": old + "\n"},
            )
            assert run(edited(directory / "frame" / "plan.md", old, new)) == "", old

    def test_prints_nothing_where_the_words_stand_nowhere_else(self, tmp_path):
        """A10. The replaced words stand in no record of the item."""
        directory = item(
            tmp_path, {"frame/design.md": design(AFTER), "pr.md": "# Body\n"}
        )
        out = run(edited(directory / "frame" / "design.md", BEFORE, AFTER))
        assert out == "", out

    def test_prints_nothing_for_an_edit_that_changes_only_whitespace(self, tmp_path):
        """A10. An edit that rewraps the sentence replaces no words, though
        the sentence stands in `pr.md` and in the edited file."""
        wrapped = BEFORE.replace("words no", "words\nno")
        directory = item(
            tmp_path, {"frame/design.md": design(wrapped), "pr.md": quoted(BEFORE)}
        )
        out = run(edited(directory / "frame" / "design.md", BEFORE, wrapped))
        assert out == "", out

    def test_prints_nothing_where_the_words_stand_only_in_trail_or_guarantee(
        self, tmp_path
    ):
        """A10. A round record under `trail/` and `guarantee.md` quote what
        their party read, so a copy there is not named, and neither is one
        in a file that is not a `.md` record."""
        directory = item(
            tmp_path,
            {
                "frame/design.md": design(AFTER),
                "trail/rounds/round-1.md": "# Round 1\n\n" + BEFORE + "\n",
                "guarantee.md": "# Guarantee\n\n" + BEFORE + "\n",
                "notes.txt": BEFORE + "\n",
            },
        )
        out = run(edited(directory / "frame" / "design.md", BEFORE, AFTER))
        assert out == "", out

    def test_prints_nothing_for_an_edit_of_a_file_it_does_not_read(self, tmp_path):
        """A10. A copy stands in `pr.md` each time, and the edited file is
        under `trail/`, is `guarantee.md`, or is not a `.md` file."""
        for rel in ("trail/phases/phase-1.md", "guarantee.md", "frame/design.txt"):
            where = tmp_path / rel.replace("/", "-")
            directory = item(where, {rel: design(AFTER), "pr.md": quoted(BEFORE)})
            path = directory.joinpath(*rel.split("/"))
            assert run(edited(path, BEFORE, AFTER)) == "", rel

    def test_prints_nothing_outside_a_marked_roots_work_item(self, tmp_path):
        """A10. A copy stands in `pr.md` each time, and the root's
        `README.md` does not open with the marker, the edited file stands
        directly under `threads/` or beside it, or the item's directory
        stands under the root outside `threads/`."""
        directory = item(
            tmp_path / "unmarked",
            {"frame/design.md": design(AFTER), "pr.md": quoted(BEFORE)},
            marked=False,
        )
        out = run(edited(directory / "frame" / "design.md", BEFORE, AFTER))
        assert out == "", "unmarked"
        directory = item(tmp_path / "marked", {"pr.md": quoted(BEFORE)})
        for path in (directory.parent / "notes.md", directory.parent.parent / "x.md"):
            path.write_text(design(AFTER), encoding="utf-8")
            assert run(edited(path, BEFORE, AFTER)) == "", path
        aside = directory.parent.parent / "archive" / ITEM
        (aside / "frame").mkdir(parents=True)
        (aside / "frame" / "design.md").write_text(design(AFTER), encoding="utf-8")
        (aside / "pr.md").write_text(quoted(BEFORE), encoding="utf-8")
        out = run(edited(aside / "frame" / "design.md", BEFORE, AFTER))
        assert out == "", "outside threads/"

    def test_prints_nothing_where_a_record_does_not_read_as_utf8(self, tmp_path):
        """A10. A copy stands in `pr.md`, and `gaps.md` holds a byte that is
        not UTF-8: a file that cannot be read prints nothing."""
        directory = item(
            tmp_path,
            {
                "frame/design.md": design(AFTER),
                "pr.md": quoted(BEFORE),
                "gaps.md": b"# Gaps\n\n\xff\n",
            },
        )
        out = run(edited(directory / "frame" / "design.md", BEFORE, AFTER))
        assert out == "", out

    def test_prints_nothing_for_a_payload_of_another_shape(self, tmp_path):
        """A10. Under A9's records, a payload that is not JSON, not an
        object, of another tool, with no `tool_input`, with a field that is
        not a string, with a path relative to the directory the hook runs
        in, or naming a file that is not there prints nothing, writes
        nothing to stderr and exits 0."""
        directory = item(
            tmp_path, {"frame/design.md": design(AFTER), "pr.md": quoted(BEFORE)}
        )
        path = directory / "frame" / "design.md"
        good = json.loads(edited(path, BEFORE, AFTER))
        relative = "/".join(path.relative_to(tmp_path).parts)
        bodies = ["not json", "[]", edited(path, BEFORE, AFTER, tool="Write")]
        for change in (
            {"tool_input": None},
            {"tool_input": {**good["tool_input"], "file_path": 3}},
            {"tool_input": {**good["tool_input"], "old_string": None}},
            {"tool_input": {**good["tool_input"], "new_string": 3}},
            {"tool_input": {**good["tool_input"], "file_path": relative}},
            {
                "tool_input": {
                    **good["tool_input"],
                    "file_path": str(path.parent / "gone.md"),
                }
            },
        ):
            bodies.append(json.dumps({**good, **change}))
        for body in bodies:
            assert run(body, cwd=tmp_path) == "", body
        # The payload the changes start from is A9's, which names `pr.md`.
        assert run(json.dumps(good), cwd=tmp_path) != ""

    def test_keeps_the_text_under_the_limit_and_says_what_it_left(self, tmp_path):
        """A9, G15's limit. Where the places would run past `LIMIT`
        characters, the text names as many as fit, says how many it left,
        and still ends with what the party does with each place."""
        lines = "\n".join(f"{n}. {BEFORE}" for n in range(1000))
        directory = item(
            tmp_path, {"frame/design.md": design(AFTER), "gaps.md": lines + "\n"}
        )
        said = context(run(edited(directory / "frame" / "design.md", BEFORE, AFTER)))
        assert len(said) < hook.LIMIT, len(said)
        assert "- `gaps.md` line 1:" in said, said
        assert "- `gaps.md` line 1000:" not in said, said
        named = said.count("- `gaps.md` line ")
        assert f"and {1000 - named} more places, not listed" in said, said
        assert said.rstrip().endswith("stays as it is."), said[-200:]

    def test_cuts_a_long_span_where_it_names_the_place(self, tmp_path):
        """A9. A span longer than `SHOWN` characters is shown to its first
        `SHOWN` characters and ` ...`, and its place is still named."""
        old = " ".join(f"word{n}" for n in range(80))
        new = "another sentence"
        assert len(old) > hook.SHOWN, len(old)
        directory = item(tmp_path, {"frame/plan.md": new + "\n", "gaps.md": old + "\n"})
        said = context(run(edited(directory / "frame" / "plan.md", old, new)))
        assert f'- `gaps.md` line 1: "{old[: hook.SHOWN]} ..."' in said, said
        assert old not in said, said


test_census = census_case(TARGET)
