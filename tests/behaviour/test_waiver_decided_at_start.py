"""Where the work is going is decided in the first minute, and written down.

The rule spans several documents — the orchestrator's half of the skill
states it, the policy says what the gate does with it, the framer's
definition says what the framer writes, and the template is what gets
written. What these cases read is the facts a reader acts on across them:
the answers `hooks/lib/routing.py` parses, the template's placeholders, the
box table the person is asked, and the citations between the files. The
rule's sentences are the proofer's to read.

The rule: how a work item is routed is asked in one batch before the first
edit, and the answer goes into `seal/threads/<work-item-id>/routing.md`
rather than being re-derived at every commit.

The second axis is not decoration. Opening a pull request is an outward-facing
act, and asked at the end it IS a mid-round prompt — the thing this release
removes. And the answer had to be recorded rather than inferred, because
"routed to the chain, not reviewed yet" and "nobody decided anything" were
byte-identical to the gate: one row of the old table said work routed to the
chain "needs no marker at all", which was true only after the first review
mark landed and false for every commit before it.
"""

import os
import re

from conftest import ROOT, read

AXES = (
    "through the review chain",
    "straight to the PR",
    "open the pull request",
    "stop before the pull request",
    # The third axis. Its answers are `crafter` and `the session`; only the
    # second is pinned, because `crafter` appears in these documents for a dozen
    # unrelated reasons -- it is the name of the agent one of them IS -- and
    # would pass on any of them.
    "the session",
)


# The routing section — the axes, the checkbox, the file, the four
# combinations, the wake/quiet table — is `implement`'s orchestrator half
# since #292: the session that asks reads `orchestration.md`, and no crafter
# spawn preloads it. The per-command waiver stays in `SKILL.md`, because
# the implementer is who types the command.
ORCH = ("skills", "implement", "orchestration.md")

# The shape of the asking, in the ONE spelling the orchestrator's section
# states (#911): question 1 alone, and
# the boxes in a second call only where its answer was `per axis`, because
# under the other two answers they mean nothing and were on screen anyway.
# Fourteen words, from when the block's template shared it: at fifteen a
# sentence two documents share is a pasted passage to
# `tests/text/test_no_passage_is_pasted_into_a_second_file.py`.
SHAPE = "Ask question 1 alone; the boxes in a second call only under `per axis`."


def flat(text):
    """Rewrapped prose and table cells compare the same way collapsed.

    A literal with a newline in it was asserting the column width once.
    """
    return " ".join(text.split())


def in_force(rel, section):
    """The policy in force at SECTION of REL, flattened: the section as the
    policy root holds it, with each pending `## Rule changes` item for that
    section applied, a `change` replacing its `from` and an `add` appended
    (`skills/implement/SKILL.md` *Document layout — two roots, three
    lifetimes*). #1148 moved the routing rows' grounds from the orchestration
    skill to the policy root through its rule changes, so these cases read
    the grounds where they stand before the settle and after it alike."""
    from conftest import load_hook_module, load_module

    rules = load_module(
        os.path.join(ROOT, "skills", "settle", "scripts", "rule_changes.py"),
        "agentic_rule_changes_for_waiver",
    )
    config = load_hook_module("lib/config.py", "agentic_config_for_waiver")
    text = read(*rel.split("/"))
    span, why = rules.section_lines(text, section)
    assert span, f"{rel}: {why}"
    lines = rules.reader().gfm_lines(text)
    body = flat("\n".join(lines[span[0] - 1 : span[1]]))
    policy = config.policy_root(os.path.join(ROOT, "seal"))
    for op, _item in rules.pending(ROOT, policy):
        if op.file != rel or op.section != section:
            continue
        if op.kind == "change" and flat(op.old) in body:
            body = body.replace(flat(op.old), flat(op.new))
        elif op.kind == "add":
            body += " " + flat(op.new)
    return body


# The two policy sections the routing rows cite for their grounds (#1148).
DECLARATION = (
    "docs/the-review-and-parity-arms.md",
    "The declaration, and where the check went",
)
SPAWN_COSTS = ("docs/the-agent-set.md", "What a spawn costs")


def cites(rel, section):
    """A citation of SECTION of REL in the shape the skills write one."""
    return f"`{rel}` *{section}*"


def checkbox_tables(text):
    """Every table of boxes in `text`, as a list of its body rows.

    Found by the header naming a box rather than by position, because the
    question's shape is what changes and a reader looking for `| Checkbox |`
    exactly once is a reader that finds nothing the day it becomes two
    questions. What stays true across every shape is that a table of boxes
    has a column named for one.
    """
    lines = text.splitlines()
    tables = []
    for i, line in enumerate(lines):
        if not line.startswith("|"):
            continue
        header = [c.strip() for c in line.strip("|").split("|")]
        if not any(c in ("Checkbox", "Box") for c in header):
            continue
        rows = []
        for body in lines[i + 2 :]:
            if not body.startswith("|"):
                break
            rows.append(body)
        tables.append(rows)
    return tables


def test_the_implementation_row_offers_the_answers_the_parser_reads():
    """Round 1, M1: the count said three, the table showed two, nothing red.

    The `AXES` tuple cannot carry this one. `the session` occurs nine times
    in `skills/implement/SKILL.md` and only two of them are about the axis,
    so the row is read by its label and its answers are read in it."""
    rows = [
        ln for ln in read(*ORCH).splitlines() if ln.startswith("| Implementation |")
    ]
    assert len(rows) == 1, (
        f"the axes table has {len(rows)} `Implementation` rows; the count "
        "beside it promises exactly one"
    )
    # The two answers `hooks/lib/routing.py#IMPLEMENTATION_ANSWERS` accepts,
    # which the orchestrator copies into `routing.md`'s `Implementation` row.
    assert "`crafter` or `the session`" in rows[0], (
        "the row lost the vocabulary, so a session reads a third axis with no answers"
    )


def test_the_optional_row_cites_where_its_criterions_grounds_stand():
    """#120: the row asked `crafter` · `the session` and never said how to
    answer, so it was answered by habit — and #263 is where that habit was
    measured against the same class of change done in the parent session.

    The criterion stands where the orchestrator, who fills the row, reads how
    the work is routed: `skills/implement/orchestration.md` *What the answer
    writes*. Since #1148 the skill states the criterion in one sentence and
    the grounds stand in the policy root, `docs/the-agent-set.md` *What a
    spawn costs*, which the skill cites. The criterion's sentence and its
    grounds are the proofer's to read."""
    tpl = " ".join(read(*ORCH).split())
    # The citation `docs/the-agent-set.md` *What a spawn costs*, which a
    # reader who questions the criterion resolves to its grounds.
    assert cites(*SPAWN_COSTS) in tpl, (
        "the criterion no longer cites where its grounds stand"
    )


def test_the_template_PARSES_into_the_three_answers_it_ships():
    """Round 1, M4: `| Implementor | Crafter the agent |` shipped green.

    Every check on this file compared strings the test itself supplied, so
    the one reader that decides whether a declaration means anything --
    `parse()` -- had never been pointed at the template a session copies. A
    corrupt third row costs nothing at the gate, which is exactly why nothing
    else would ever report it."""
    import sys

    sys.path.insert(0, os.path.join(ROOT, "hooks", "lib"))
    import routing

    template = read("templates", "records", "sdd-routing.md")
    parsed = routing.parse(template)
    assert parsed is not None, "the template no longer parses as a declaration"
    assert parsed["review"] == routing.CHAIN
    assert parsed["destination"] == routing.OPEN_PR

    # Shipped as a PLACEHOLDER, unlike the other two, and that is the whole
    # point: a wrong answer in the first two is caught at the next commit
    # because the gate stops recognising the file, and a wrong answer here is
    # never contradicted by anything. So copy-and-never-revisit has to land on
    # "not answered" rather than on a confident `crafter` nobody performed.
    assert parsed["implementation"] is None, (
        "the template pre-answers the one axis nothing checks, which makes "
        "the commonest mistake produce a WRONG record instead of no record"
    )
    # Round 2: `is None` is satisfied by an empty cell and by `TBD`, and both
    # were green. `parse()` cannot tell them apart -- all three are outside
    # the vocabulary -- but a PERSON can, and the person is who the
    # placeholder is for. An empty cell reads as "nothing to fill in"; `TBD`
    # reads as an answer somebody will get to. Only the shipped text says
    # what the two choices are.
    assert "| Implementation | <crafter, or: the session> |" in template, (
        "the placeholder TEXT is the half a person reads, and a blank cell "
        "or `TBD` parses identically while reading as answered"
    )

    # The label, which the placeholder cannot exercise. Substituting each
    # documented answer must yield that answer -- `| Implementor | … |` or a
    # backticked value reads as unanswered forever, silently, in every work
    # item that copies this file.
    rows = [ln for ln in template.splitlines() if ln.startswith("| Implementation |")]
    assert len(rows) == 1, "the template has no single `Implementation` row"
    for answer in routing.IMPLEMENTATION_ANSWERS:
        filled = template.replace(rows[0], f"| Implementation | {answer} |")
        assert routing.parse(filled)["implementation"] == answer, (
            f"the template's row does not accept `{answer}`, so a session "
            "filling it in as instructed still records nothing"
        )


def test_the_template_PARSES_into_the_FOURTH_axis_it_ships():
    """The fourth axis's vocabulary is read out of the template, never retyped.

    `hooks/lib/routing.py`'s `parse()` docstring promises that
    `templates/records/sdd-routing.md` is the only spelling a session should copy and
    that a test parses the file so the two cannot drift. This is that test for
    the `Planning` row: every constant the parser accepts is substituted into
    the template's own row and parsed back, so a row labelled `Planner` or a
    vocabulary that moved in one file only is red here rather than silent in
    every work item that copies the file.

    Shipped as a placeholder for the reason the third axis is: nothing
    contradicts a wrong answer in either, so copy-and-never-revisit has to land
    on "not answered".
    """
    import sys

    sys.path.insert(0, os.path.join(ROOT, "hooks", "lib"))
    import routing

    template = read("templates", "records", "sdd-routing.md")
    parsed = routing.parse(template)
    assert parsed is not None, "the template no longer parses as a declaration"
    assert parsed["planning"] is None, (
        "the template pre-answers the fourth axis, which makes the commonest "
        "mistake produce a WRONG record instead of no record"
    )
    # The template's placeholder row, which `offered` below parses for the
    # two answers a person reads at the row.
    assert "| Planning | <framer, or: the session> |" in template, (
        "the placeholder TEXT is the half a person reads, and a blank cell or "
        "`TBD` parses identically while reading as answered"
    )

    rows = [ln for ln in template.splitlines() if ln.startswith("| Planning |")]
    assert len(rows) == 1, "the template has no single `Planning` row"
    for answer in routing.PLANNING_ANSWERS:
        filled = template.replace(rows[0], f"| Planning | {answer} |")
        assert routing.parse(filled)["planning"] == answer, (
            f"the template's row does not accept `{answer}`, so a session "
            "filling it in as instructed still records nothing"
        )
    # The vocabulary is READ OUT of the template and compared, rather than
    # each constant being looked for inside it. Substituting the constants
    # into the row above is self-consistent by construction -- rename
    # `BY_FRAMER` and the substitution renames with it -- so on its own it
    # cannot see the two files drift apart. This direction can: the answers
    # the comment offers a person have to BE the answers the parser accepts.

    stated = offered(template, routing.PLANNING)
    assert stated, (
        "the placeholder no longer states the fourth axis's two answers, so "
        "a person reads no vocabulary at the row"
    )
    assert stated == routing.PLANNING_ANSWERS, (
        f"the template offers {stated} and the parser accepts "
        f"{routing.PLANNING_ANSWERS}; a session filling the row in as "
        "instructed would record nothing"
    )


def offered(template, label):
    """The two answers the template's LABEL row offers a person, read out of
    its placeholder `<first, or: second>`; None where the row has no such
    placeholder."""
    m = re.search(
        rf"^\| {re.escape(label)} \| <([^,>]+), or: ([^>]+)> \|$", template, re.M
    )
    return m.groups() if m else None


def test_the_template_PARSES_into_the_TWO_NEWEST_rows_it_ships():
    """The fifth and sixth rows, on the terms the third and fourth have.

    `Automation` is a property of the run and `Answer pressed` is which of
    question 1's options was pressed. Both are read out of the template and
    parsed back, so a row labelled `Automated` or a vocabulary that moved in
    one file only is red here rather than silent in every work item that
    copies the file.

    Shipped as placeholders, and for this pair the reason is sharper than for
    the two above. An absent `Automation` row means nobody was ever asked; a
    pre-answered one means a question nobody put reads as a promise somebody
    made. That is #151's shape, which is the thing the row exists to end.
    """
    import sys

    sys.path.insert(0, os.path.join(ROOT, "hooks", "lib"))
    import routing

    template = read("templates", "records", "sdd-routing.md")
    parsed = routing.parse(template)
    assert parsed is not None, "the template no longer parses as a declaration"
    for key in ("automation", "pressed"):
        assert parsed[key] is None, (
            f"the template pre-answers `{key}`, which makes the commonest "
            "mistake produce a WRONG record instead of no record"
        )
    for label, answers in (
        (routing.AUTOMATION, routing.AUTOMATION_ANSWERS),
        (routing.ANSWER_PRESSED, routing.ANSWER_PRESSED_ANSWERS),
    ):
        rows = [ln for ln in template.splitlines() if ln.startswith(f"| {label} |")]
        assert len(rows) == 1, f"the template has no single `{label}` row"
        assert rows[0].split("|")[2].strip().startswith("<"), (
            f"the `{label}` row stopped shipping a placeholder a person reads"
        )
        key = "automation" if label == routing.AUTOMATION else "pressed"
        for answer in answers:
            filled = template.replace(rows[0], f"| {label} | {answer} |")
            assert routing.parse(filled)[key] == answer, (
                f"the template's `{label}` row does not accept `{answer}`, so "
                "a session filling it in as instructed still records nothing"
            )
        # The vocabulary READ OUT of the placeholder, the direction that can
        # see the two files drift. Substituting the constants is
        # self-consistent by construction; what the person reads has to BE
        # what the parser takes.
        stated = offered(template, label)
        assert stated, f"the placeholder no longer states `{label}`'s two answers"
        assert stated == answers, (
            f"the template offers {stated} for `{label}` and the "
            f"parser accepts {answers}"
        )


def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def labelled_table(text, first_column, second_column):
    """The body rows of the table whose header is exactly those two columns.

    Question 1 is `| Order | Label | Description |` and question 2 is
    `| Order | Box | Checked | Not checked |`, so the pair names one of them
    without either being found by position in the file.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not line.startswith("|"):
            continue
        header = cells(line)
        if header[:2] != [first_column, second_column]:
            continue
        rows = []
        for body in lines[i + 2 :]:
            if not body.startswith("|"):
                break
            rows.append(cells(body))
        return rows
    raise AssertionError(f"no table headed `| {first_column} | {second_column} |`")


def test_question_1_is_asked_alone_and_the_boxes_only_under_per_axis():
    """S1, and #911. One batch before the first edit, and the boxes only
    where they mean something.

    The two questions used to go in one call, so a person pressing
    `automation` or `no work item` was shown four boxes that meant nothing
    under either answer. Question 1 now goes alone, and the boxes follow in
    a second call only under `per axis`, at once and before the first edit.
    So both tables have to be there AND the sentence that says when each is
    asked.
    """
    skill = read(*ORCH)
    assert len(labelled_table(skill, "Order", "Label")) == 3, (
        "question 1 does not offer exactly three options"
    )
    assert len(labelled_table(skill, "Order", "Box")) == 4, (
        "question 2 does not offer exactly four boxes"
    )
    # ONE spelling, which `tests/text/test_review_axes.py` also reads in
    # this section: two spellings of one decision is the drift both catch.
    assert SHAPE in flat(skill)


def test_the_boxes_are_in_the_stated_order():
    """S5. The first box is a property of the run; the three below name
    parties, in the order they run.

    Asserted as an ORDER rather than as a membership, because the defect it
    guards against is positional: a reader meeting four boxes of apparently
    the same kind reads the first as a fourth party to switch on. Swap the
    first two rows and the boxes are all still present. Whether the section
    says the order is load-bearing is the proofer's to read.
    """
    rows = labelled_table(read(*ORCH), "Order", "Box")
    boxes = [r[1] for r in rows]
    # The box labels in the order the orchestrator puts them to the person
    # in question 2's `AskUserQuestion` call; label and position are the fact.
    assert "run end to end" in boxes[0], (
        f"the property-of-the-run box is at position {boxes.index(next(b for b in boxes if 'run end to end' in b)) + 1}, "
        "not first. The order is the specification: a party box read first "
        "makes the run's own property look like a fifth party"
    )
    for i, party in enumerate(("crafter", "proofer", "pull request"), start=1):
        assert party in boxes[i], (
            f"box {i + 1} is `{boxes[i]}`; the three party boxes follow the "
            "run's property in the order they run"
        )


def test_every_box_states_what_UNCHECKED_means():
    """S6. The half a label cannot say, and the half the measured instance
    got wrong — the owner read `straight to the PR` as *call no agents at
    all*, where it turns off `proofer` alone.

    Each phrase is asserted in the box it belongs to rather than anywhere in
    the file, because a document can carry all four words in prose two
    sections down while the box a person reads at the moment of answering
    carries none of them.
    """
    rows = labelled_table(read(*ORCH), "Order", "Box")
    unchecked = {r[1]: r[3] for r in rows}
    wanted = {
        "run end to end": "may be asked",
        "crafter": "this session writes the code",
        "proofer": "nothing reviews",
        "pull request": "stop before",
    }
    for box, phrase in wanted.items():
        found = [v for k, v in unchecked.items() if box in k]
        assert found, f"no box named for `{box}`"
        assert phrase in found[0], (
            f"the `{box}` box's unchecked half does not say `{phrase}`; a "
            "person answering reads the label and this cell and nothing else"
        )


def test_the_exit_names_what_does_not_run_rather_than_where_it_ends():
    """S4. The rule the measured instance produced: a label must name what it
    turns off, not where it ends.

    So the exit's label carries no destination, and its description names the
    five things that do not happen. `straight to the PR` is the counter-example
    and it stays in the tree — as the `Review` row's value, which is machine
    vocabulary 16 committed declarations carry. What moved is the LABEL.
    """
    rows = labelled_table(read(*ORCH), "Order", "Label")
    exits = [r for r in rows if "no work item" in r[1]]
    assert exits, "question 1 has no exit option labelled `no work item`"
    label, description = exits[0][1], exits[0][2]
    for destination in ("the PR", "pull request"):
        assert destination not in label, (
            f"the exit's label names a destination (`{label}`), which is the "
            "defect the measured instance is an instance of"
        )
    for noun in (
        "no frame",
        "no review",
        "no seal",
        "no `routing.md`",
        "`seal no-work-item`",
    ):
        assert noun in description, (
            f"the exit's description does not name `{noun}`, so a person "
            "pressing it cannot see what they are turning off"
        )
    assert rows[-1][1] == label, (
        "the exit is not last. It is one click and the least-verified path, "
        "so it sits where a reader's eye lands last"
    )


def test_the_ceiling_is_stated_beside_the_shape():
    """S7. The next person meets the constraint instead of discovering it:
    the section states the cap on a question's options. Where the room for
    the fourth box came from, and what a fifth does to the shape, are the
    proofer's to read.
    """
    skill = flat(read(*ORCH))
    # The value four, the most options the harness's `AskUserQuestion`
    # takes per question, which bounds the boxes the orchestrator puts.
    assert "at most four options per question" in skill, "the cap is unstated"


def test_the_preset_and_the_boxes_write_the_answer_pressed_values():
    """S2 and S3 at the document. Both write the same party rows; the row
    that says which answer was pressed is the only difference, and the
    section gives the value each writes into it and the `Automation` row's
    two answers. Why the row exists is the policy's, which
    `test_the_policy_tables_the_review_answers_and_the_skill_cites_it` reads
    the skill citing, and the proofer's to read.
    """
    skill = flat(read(*ORCH))
    # The `Answer pressed` row and the two values the orchestrator writes in
    # it, which `hooks/lib/routing.py#ANSWER_PRESSED_ANSWERS` accepts.
    for derivation in (
        "`Answer pressed` = `automation`",
        "`Answer pressed` =\n`per axis`",
    ):
        assert flat(derivation) in skill, (
            f"the section does not say the preset writes {flat(derivation)}, "
            "so a session has the row and no rule for filling it"
        )
    rows = [ln for ln in read(*ORCH).splitlines() if ln.startswith("| Automation |")]
    assert len(rows) == 1, (
        f"the section has {len(rows)} `Automation` rows; the declaration has one"
    )
    # The two answers `hooks/lib/routing.py#AUTOMATION_ANSWERS` accepts,
    # which the orchestrator copies into `routing.md`'s `Automation` row.
    assert "`yes` or `no`" in rows[0], "the row lost its vocabulary"


FRAMER = ("agents", "framer.md")


def test_no_agent_definition_tells_an_agent_to_ask_a_person():
    """The class behind 🟡 4, pinned by the one name that was measured.

    An agent definition instructing an agent to call a tool it cannot reach is
    exactly what went undetected here: the build moved the routing batch to
    `agents/framer.md`, every case stayed green, and nothing in the tree could
    see that the instruction was unperformable.

    **This is one name, not a vocabulary.** A sweep over `agents/*.md` for
    every tool an agent cannot reach needs a list of what each agent has, kept
    in step with the harness — that is mechanism this case does not add, and
    it is handed over as a ticket instead. What this case holds
    is the measured instance and the glob: a fourth agent definition added
    tomorrow is checked on the day it lands.
    """
    import glob

    definitions = sorted(glob.glob(os.path.join(ROOT, "agents", "*.md")))
    assert len(definitions) >= 3, f"agents/*.md matched {len(definitions)} files"
    for path in definitions:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        name = os.path.relpath(path, ROOT)
        for line in text.splitlines():
            if "AskUserQuestion" not in line:
                continue
            # Naming the tool to say it is ABSENT is the whole repair, so the
            # sentence that does it has to be allowed. What is refused is an
            # instruction to use it.
            # ONE spelling across every definition, deliberately. A marker
            # list that grows a phrase per file is a list that stops being a
            # check, so a definition saying the tool is absent says it this
            # way — and the case is what keeps the four sentences in step.
            assert "no `AskUserQuestion`" in line, (
                f"{name} names `AskUserQuestion` outside the sentence that "
                "says an agent does not have it. No agent this plugin spawns "
                "can reach that tool, so an instruction to use it is an "
                "instruction nothing can carry out"
            )


def test_the_framer_writes_rule_changes_from_the_index():
    """S15 of #953. The framer states each rule change in `## Rule changes`
    as the settle skill's section says, picks its file from the index, and
    reads the policy in force as the implement skill states it. The
    definition cites the grammar, the index and the model; whether it
    restates either is the proofer's to read."""
    framer = flat(read(*FRAMER))
    # The citation `skills/settle/SKILL.md` *Rule changes*, which the framer
    # resolves to the grammar `rule_changes.py#parse` reads; the citation is
    # the fact.
    assert "as `skills/settle/SKILL.md` *Rule changes* states it" in framer
    # The path `<policy root>/README.md`, which the framer opens to pick each
    # `file:`.
    assert "picked from the index, `<policy root>/README.md`" in framer
    # The citation of the policy-in-force model, which the framer resolves.
    assert (
        "the policy in force as "
        + ("`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*")
        in framer
    )


def test_a_mark_is_not_the_answer_to_a_blocked_step():
    """#1148, `frame/design.md` *Scope* item 6. The framer decides whether a
    work item adds a mark, so the owner's rule stands in its definition: a
    design adding a mechanism names what it takes out in `## Removes`, and a
    blocked step is answered at its cause. The rule ends in its check line."""
    raw = read(*FRAMER)
    framer = flat(raw)
    lead = "**A mark is not the answer to a blocked step.**"
    assert lead in framer, "the framer's definition lost the rule"
    for phrase in (
        "names in `## Removes` what it takes out",
        "never by a new mark",
        "`skills/core/SKILL.md` *The rule a mechanism is kept against*",
    ):
        assert phrase in framer, f"the rule lost `{phrase}`"
    paragraph = raw[raw.index(lead) :].split("\n\n", 1)[0]
    assert paragraph.splitlines()[-1] == (
        "check: tests/behaviour/test_waiver_decided_at_start.py"
    ), "the rule does not end in its check line"


def test_both_halves_of_the_frame_reading_cite_the_alternatives_table():
    """#1148, `frame/design.md` *Scope* item 12. The orchestrator reads the
    frame against the issue before the first build spawn and the framer
    answers in one exchange. Both halves send a rejected proposal to the
    plan's *Alternatives considered*. The answers, the bound and the check
    line are the proofer's to read."""
    raw = read(*FRAMER)
    lead = "**An orchestrator's reading of the frame is answered in one exchange.**"
    assert lead in flat(raw), "the framer's definition lost the rule"
    paragraph = raw[raw.index(lead) :].split("\n\n", 1)[0]
    orchestration = flat(read(*ORCH))
    heading = "### The frame is read against the issue at the spawn"
    assert heading in orchestration, "the orchestrator's section is gone"
    section = orchestration[orchestration.index(heading) :].split(" ## ", 1)[0]
    for half, text in (("framer", flat(paragraph)), ("orchestration", section)):
        # The heading *Alternatives considered*, which the framer resolves in
        # `frame/plan.md` to write a rejected proposal as a row.
        assert "*Alternatives considered*" in text, (
            f"the {half} half no longer sends a rejection to the plan's "
            "Alternatives table"
        )


def test_the_framer_leaves_a_mark_in_the_tree():
    """S12. Measured at the frame: 0 of 84 work items carry any mark in
    `frame/design.md`, and the definition asked for none.

    `crafter` leaves a mark and `proofer` writes round records, so the framer was
    the only party in the chain whose work left no evidence that it happened —
    only a claim in a row somebody typed. The existing framer mark is in the
    repository's git dir, and a git dir does not travel, so the check at the
    pull request cannot read it.

    Both ends are asserted: the definition that tells a framer to write it and
    the template a session copies. Either alone ships a mark nobody writes or
    a line nobody was told to fill in. Why the git dir's mark does not do is
    the proofer's to read.
    """
    # The mark's shape, which `chain_check.py#MARK_RE` matches at the foot
    # of `frame/design.md`, in the template and in the framer's definition.
    line = "Framed <date> by <who>, before the build."
    template = read("templates", "records", "sdd-design.md")
    assert line in template, (
        "`templates/records/sdd-design.md` ships no mark, so every spec copied from it "
        "is a frame with no evidence it was framed"
    )
    assert template.rstrip().endswith(line), (
        "the mark is not at the foot of the file; the check reads the same "
        "shape `routing.md` and `plan.md` already end with"
    )
    framer = flat(read(*FRAMER))
    assert line in framer, (
        "the framer is not told to write the mark, so the template's line "
        "survives into the committed spec as a placeholder"
    )


def test_the_planning_row_is_a_record_and_not_a_checkbox():
    """#88, cited rather than re-argued: the question grows only where a
    decision is genuinely a person's, and `agents/framer.md`'s `## Job` says
    the SDD ladder decides this one.

    Both halves are asserted, because either alone passes over the state that
    matters. The row has to be IN the orchestrator's routing section — an axis
    nobody documents is a template row a session meets with no account of it —
    and it must not appear among the boxes.

    **Renamed and rewritten from
    `test_the_fourth_axis_is_a_record_and_not_a_fourth_checkbox`, which named
    `Planning` by POSITION and counted the boxes.** Both spellings stopped
    being about `Planning` the moment a row was added: the declaration's
    fourth row is not `Planning` any more, and the question's box count is
    four because one of the new rows genuinely IS a person's decision — which
    is what #88's rule permits rather than what it forbids. The rule was
    always about this row and never about a number, so the assertions are
    over the row's NAME. A count here would have gone red at the next phase
    for a change the rule allows, and a reader would have read that red as
    the rule being broken.
    """
    skill = read(*ORCH)
    rows = [ln for ln in skill.splitlines() if ln.startswith("| Planning |")]
    assert len(rows) == 1, (
        f"the routing section has {len(rows)} `Planning` rows; the declaration "
        "has exactly one"
    )
    # The two answers `hooks/lib/routing.py#PLANNING_ANSWERS` accepts, which
    # the orchestrator copies into `routing.md`'s `Planning` row.
    assert "`framer` or `the session`" in rows[0], (
        "the row lost the vocabulary, so a session reads an axis with no answers"
    )

    # The box tables the orchestrator puts to the person carry no `Planning`
    # box, so the person is never asked an axis the SDD ladder decides.
    for boxes in checkbox_tables(skill):
        assert not any("framer" in b or "Planning" in b for b in boxes), (
            "the `Planning` axis reached a checkbox table, which is the one "
            "place #88 says it must not be"
        )


def test_no_committed_declaration_still_carries_a_template_placeholder():
    """Round 2: nothing reads the third axis, so nothing reports a work item
    that copied the template and never filled the row in.

    The `Branch` row is the contrast that shows this is a real gap rather
    than a tidy one: leaving ITS placeholder produces a branch name nothing
    matches, `for_branch` finds no declaration, and the gate asks again at
    the next commit. The third axis has no such reader, so the placeholder
    would sit in the record forever, reading to a person as an answer."""
    import glob

    for path in sorted(
        glob.glob(os.path.join(ROOT, "seal", "threads", "*", "routing.md"))
    ):
        with open(path, encoding="utf-8") as f:
            for line in f:
                if not line.startswith("|"):
                    continue
                label, _, value = line.strip().strip("|").partition("|")
                assert not value.strip().startswith("<"), (
                    f"{os.path.relpath(path, ROOT)} still carries the "
                    f"template placeholder for `{label.strip()}`"
                )


def test_the_policy_tables_the_review_answers_and_the_skill_cites_it():
    """Four combinations, because two of them are the ones that surprise
    people: a chain declaration that never opens a pull request is checked by
    nothing. Since #1148 the policy section the skill cites holds them: its
    table gives what each `Review` answer owes at the pull request, keyed by
    the answer. The paragraph on the two that open none is the proofer's to
    read."""
    skill = flat(read(*ORCH))
    policy = in_force(*DECLARATION)
    # The two `Review` answers `hooks/lib/routing.py#REVIEW_ANSWERS` accepts,
    # as the policy table's row keys a reader looks an answer up by.
    for answer in ("| through the review chain |", "| straight to the PR |"):
        assert answer in policy, f"the policy's table lost the row `{answer}`"
    # The citation `docs/the-review-and-parity-arms.md` *The declaration, and
    # where the check went*, which the orchestrator resolves to the table.
    assert cites(*DECLARATION) in skill, "the skill does not cite the combinations"


def test_the_skill_names_where_the_answer_is_written():
    skill = flat(read(*ORCH))
    assert "seal/threads/<work-item-id>/routing.md" in skill
    assert "templates/records/sdd-routing.md" in skill
    assert "Committed" in skill or "committed" in skill


def test_the_skill_names_the_record_and_no_per_command_waiver():
    """#1027: nothing reads `[no-review]` any more, so the skill that taught
    it as the way past the gate names the record that replaced it."""
    skill = flat(read("skills", "implement", "SKILL.md"))
    assert "`seal no-work-item`" in skill
    assert "[no-review]" not in skill and "waives **one command**" not in skill


def test_the_skill_cites_the_policy_on_a_standing_waiver():
    """The cheap way to stop the interruptions is to switch the gate off for a
    session, and it is the one way that costs the gate its reason to exist.
    The reasoning is the policy's since #1148, and the skill cites it; the
    rule's sentences are the proofer's to read."""
    skill = flat(read(*ORCH))
    # The citation `docs/the-review-and-parity-arms.md` *There is no standing
    # waiver*, which the orchestrator resolves to the reasoning.
    assert cites(
        "docs/the-review-and-parity-arms.md", "There is no standing waiver"
    ) in (skill)


def test_the_skill_names_where_a_late_finding_goes():
    """Once the batch is answered the session runs to the pull request, and
    what surfaces after it is written down rather than raised. The skill
    names the three places it goes; the rule's sentences are the proofer's
    to read."""
    skill = read("skills", "implement", "SKILL.md")
    # The two paths and the closing memo's `## Not done` section, which the
    # session resolves to write a late finding down.
    for destination in ("questions.md", "seal/follow-up.md", "Not done"):
        assert destination in skill, (
            f"the skill lost `{destination}` as somewhere a late finding goes"
        )


def test_the_orchestration_offers_the_vocabulary_the_parser_accepts():
    """Words the orchestrator writes into `routing.md` that the reader
    rejects produce a declaration that reads as none, which is what a branch
    that never declared looks like. The table of what the answer writes is
    where the orchestrator reads the words; the template ships two of them
    answered and the rest as placeholders."""
    orch = read(*ORCH)
    routing = read("hooks", "lib", "routing.py")
    for answer in AXES:
        assert f"`{answer}`" in orch, f"the orchestration lost `{answer}`"
        assert f'"{answer}"' in routing, f"the parser does not accept `{answer}`"
