"""`skills/verify/scripts/session_cost.py`, one class per function.

The numbers nobody can produce from inside a session.

The report exists because nobody can produce these from inside a session. The
fixture below is a hand-built transcript with known answers, so a change to
the parser that quietly stops finding repeats or tool calls fails here.

#942's phase 6 placed here the cases of
`tests/test_session_cost_post.py` and
`tests/test_a_derived_number_reaching_an_int_carries_a_guard.py` beside this
file's own. Their docstrings follow, as they stood.

`--post`: `session_cost.py --post` posts one segment's reading, or refuses.

Issue #330. Of the three acts the ticket measured a miss for, two closed
while it sat and one is still a sentence: posting the segment's reading to
the flow log, written out in full in `skills/verify/orchestration.md` *Measure
the segment, and feed the flow log* and typed by nobody. This is that procedure
as a command, and this module is what holds it.

**Nothing here touches a network.** Every case replaces the module's own
`run_gh`, which is the single seam every `gh` call goes through, and records
the argv it was handed. That is what lets a case assert the two properties
the prose cares about most: that an issue is never opened, and that nothing
is posted in any state but the one open log.

The five states, and the exit each ends on:

  no `--says`                   exit 2, nothing looked up  (A5)
  the label has no history      exit 0, nothing posted     (A6)
  history and nothing open      exit 1, nothing opened     (A7)
  more than one open            exit 1, both named         (A8)
  exactly one open              exit 0, one comment        (A9)

**Red-first, per contract rule 15.** Every case here was run against
`session_cost.py` before the mode existed: `--post` was not a flag, so
argparse exited 2 on all of them, and only A5 was red for its own reason.
The phase record names the run. After the mode landed, each unit it added was
broken one at a time and the module re-run, and the mutations are in that
record too.

The guard on a derived number: Every site in `session_cost.py` that converts a number to an int is
discharged — by a guard, or by an operand that cannot be a derived number.

#192. `count` answers whether each value entering from a transcript is
finite. `load` then adds a turn's `input_tokens` to its
`cache_read_input_tokens`, and `token_thirds` sums those and divides. **Two
values that each passed can make one that would not**, and the report ended
with exit 1 and stdout empty on both the report and `--json`. Round 3 of #175
closed that at one site. What is left is the class, and #192's own reading of
why a second site walk is not it: round 3's defect arrived through a call the
existing arithmetic walk had held in its list from the start, so a walk over
operations answers *which operations exist* and never *what two entered
values make*.

**The class is enumerated by construction and every question about it is
decided by execution.** Nothing here is answered by a list of names, because
a list is what this release exists to replace.

  is this site a conversion to an int
      Two probes, and both halves are the owner's own wording — *converting a
      derived number TO an int*. Python reaches an `int` through exactly six
      operand methods (`__int__`, `__index__`, `__trunc__`, `__round__`,
      `__floor__`, `__ceil__`), so `Operand` below answers those six and
      nothing else and the walk hands one to the site's own callable: that
      settles whether the operand is consumed as an integer. Then the same
      callable is asked for its answer to a benign number, and the site is a
      member only when that answer is an exact `int`. `round`, `int`,
      `math.floor`, an aliased import, a `from`-import and a function written
      in this module ten minutes ago all classify the same way, and no name
      appears anywhere in this file.

  what does the conversion raise
      Probed, not assumed: the callable is handed each value `count` admits
      and would not have refused — an infinity, a `NaN`, and an integer with
      no float of its own — and the exception types it raises are collected.
      `round` raises `OverflowError` on an infinity and `ValueError` on a
      `NaN`; `math.floor` raises the same two; a conversion that raises
      nothing needs no guard and says so. This is why there is no hardcoded
      pair of exception classes anywhere below.

  is this member discharged
      Its operand cannot be a derived number — an integer literal, or integer
      arithmetic over integer literals, where *keeps an int* is itself
      decided by evaluating the operator — or the conversion cannot raise at
      all, or a guard dominates it: a finiteness test on the same operand in
      an enclosing conditional, or a `try` whose handlers cover every
      exception the probe above actually saw. *Finiteness test* is decided by
      probing a resolved callable rather than by naming one, and *covers* by
      `issubclass`, so a tupled or aliased exception classifies correctly.

**The failure direction is toward refusing, and one shape is a measured false
refusal rather than an accident.** A guard written as an early return instead
of an enclosing conditional is refused, because dominance here is the
enclosing construct and an early return is not one; it sits in `GUARD_SHAPES`
with the verdict it actually gets. A wrong refusal is a red case with a
coordinate in it and a message saying what to write; a wrong pass is the
report ending with stdout empty, which is what #175 spent four rounds on.

**Three shapes this property does not reach, stated rather than left to be
found.** The first two are `questions.md` rows for the repository owner, and
`token_thirds`' own docstring carries both so a next editor of that file
meets them:

  a subscript bound
      a slice bound and a list index convert through `__index__`, so a
      subscript is a conversion by this same protocol. Whether one is DERIVED
      cannot be decided without provenance: `inputs[third : 2 * third]` is
      safe because `third` is `len(inputs) // 3`, and `by_family[key][0]`
      indexes with a local name this walk cannot see the value of. Excluded,
      with both directions of the mistake measured in `questions.md` Q1.

  a true division on two derived integers
      `sum(part) / len(part)` raises `OverflowError` on two integers that
      each have a float where their sum does not — the second of round 3's
      two routes — and it converts nothing, so it is not a member here. The
      wider predicate that would catch it (*a site that RAISES on a value
      `count` admits*) also flags `share`'s `part / whole * 100`, which is
      unguarded today and whose operands are durations. `questions.md` Q2.

  a callable that converts an operand and answers with something else
      `math.isfinite` is the measured instance, and the walk finds it: it
      consumes its operand through `__index__`, which is why
      `math.isfinite(HUGE_INT)` raises `OverflowError` — round 2 of #175's
      🔴, closed inside `count` by the `try` that is still there. It is not a
      member because it yields a `bool`, and that exclusion is deliberate:
      the alternative refuses the second call, in `token_thirds`, where
      `mean` is a float by construction and the call cannot raise, and paying
      for that with dead defensive code is the trade round 3 already refused
      once. `test_a_predicate_that_converts_but_answers_a_bool_is_not_a_member`
      is what keeps the exclusion visible instead of incidental.

**What the probe costs, because deciding membership by execution means
calling things.** Every callable probed is one this module's own source
calls, and the operand it is handed answers no protocol but the six — no
path, no string value, no arithmetic, no comparison — so a callable that is
not a numeric consumer raises `TypeError` on the spot and nothing reaches a
filesystem. Output is captured and every exception is swallowed, `SystemExit`
included. A future edit could call something whose mere invocation matters;
the bound on that is the operand, which gives such a call nothing to act on.

**And what an unresolved callee can hide, which is less than it looks.** A
method on a runtime receiver (`pattern.search`, `handle.read`) and a call to
a function defined inside another function cannot be resolved to an object,
so they are not probed. They hide a conversion only when the conversion is
written in code this walk does not read: the walk covers every call in the
module's own tree, nested definitions included, so a converter written HERE
is caught at its own `int(...)` whoever calls it.

The scope is one module because that is the module whose operands come out of
a transcript. Widening to the tree makes every `round(` in every script a
member and stops the diff being about #192.
"""

import ast
import builtins
import contextlib
import datetime as dt
import importlib.util
import io
import json
import math
import os
import re
import subprocess
import sys

import pytest
from conftest import ROOT, census_case

TARGET = "skills/verify/scripts/session_cost.py"

SCRIPT = os.path.join(ROOT, "skills", "verify", "scripts", "session_cost.py")


# An integer literal with no float of its own. `json.loads` builds an
# arbitrary-precision `int` from any integer literal in a transcript, and
# `float(HUGE_INT)` raises `OverflowError` rather than returning an infinity.
HUGE_INT = int("9" * 401)


# A float near the top of the double range. Each one is finite and passes
# `count`; two of them add to an infinity, and two integers of this size each
# have a float where their sum does not.
TOP_FLOAT = 1.5e308


def stamp_at(second):
    """`second` is an offset from a fixed clock; the clock does the carrying."""
    stamp = dt.datetime(2026, 8, 24, 10, 0, 0, tzinfo=dt.UTC) + dt.timedelta(
        seconds=second
    )
    return stamp.isoformat().replace("+00:00", "Z")


def message(second, blocks, message_id=None, uuid=None, tokens=1000):
    """One transcript row.

    A row without `message_id` and `uuid` is its own turn — the shape of a
    transcript from a harness that stamps neither, and the degradation the
    parser must take toward the 1.00 floor rather than an inflated ratio."""
    row = {
        "timestamp": stamp_at(second),
        "message": {"content": blocks, "usage": {"input_tokens": tokens}},
    }
    if message_id:
        row["message"]["id"] = message_id
    if uuid:
        row["uuid"] = uuid
    return json.dumps(row)


def turn(second, block):
    return message(second, [block])


def use(uid, command):
    return {
        "type": "tool_use",
        "id": uid,
        "name": "Bash",
        "input": {"command": command},
    }


def result(second, uid):
    return turn(second, {"type": "tool_result", "tool_use_id": uid})


def call(uid, start, end, command):
    return [
        turn(
            start,
            {
                "type": "tool_use",
                "id": uid,
                "name": "Bash",
                "input": {"command": command},
            },
        ),
        turn(end, {"type": "tool_result", "tool_use_id": uid}),
    ]


@pytest.fixture
def transcript(tmp_path):
    lines = []
    # 10s of tests, then the same scope again with a different pipe (8s), then
    # a 2s git call. Model gaps: 5s and 5s.
    lines += call("a", 0, 10, "pytest tests/unit -q | tail -5")
    lines += call("b", 15, 23, "pytest tests/unit -q | grep FAILED")
    lines += call("c", 28, 30, "git status --short")
    path = tmp_path / "t.jsonl"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def run(args):
    return subprocess.run(
        [sys.executable, SCRIPT, *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


def batch_data(tmp_path, lines, name="m.jsonl"):
    path = tmp_path / name
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    proc = run(["--json", str(path)])
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout)


# --- the token line ---------------------------------------------------------
#
# `message()` above writes `usage` with `input_tokens` alone, so every fixture
# built from it sums to zero output and zero cache. That is deliberate: the
# cases above cannot move when the token line lands. The helpers below write a
# full `usage` block, which is the shape a real assistant row carries.


def spend(
    second,
    output=0,
    cache_write=0,
    cache_read=0,
    message_id=None,
    uuid=None,
    blocks=None,
):
    """One assistant row carrying a full `usage` block.

    `blocks` defaults to a text block, so the row is a turn the token line
    counts and a turn `tools_per_turn` does not — the two counters this module
    holds apart."""
    row = {
        "timestamp": stamp_at(second),
        "message": {
            "content": blocks
            if blocks is not None
            else [{"type": "text", "text": "."}],
            "usage": {
                "input_tokens": 0,
                "output_tokens": output,
                "cache_creation_input_tokens": cache_write,
                "cache_read_input_tokens": cache_read,
            },
        },
    }
    if message_id:
        row["message"]["id"] = message_id
    if uuid:
        row["uuid"] = uuid
    return json.dumps(row)


def plain_result(second, uid):
    """A tool_result row as a harness writes one: no `usage` block, because it
    is not an assistant message. `result()` above carries one, which is a
    fixture artifact — the token line must not count such a row as a turn."""
    return json.dumps(
        {
            "timestamp": stamp_at(second),
            "message": {"content": [{"type": "tool_result", "tool_use_id": uid}]},
        }
    )


def write_run(tmp_path, main_lines, subagents=None):
    """A run on disk: `main.jsonl` with its segments under `main/subagents/`.

    That is the layout `newest` already walks — a run's subagent transcripts
    live in the directory named after the main transcript's own basename."""
    path = tmp_path / "main.jsonl"
    path.write_text("\n".join(main_lines) + "\n", encoding="utf-8")
    for name, lines in (subagents or {}).items():
        target = tmp_path / "main" / "subagents" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def tokens_of(path):
    proc = run(["--json", str(path)])
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout)["tokens"]


def worked(second, uid, command="pytest -q", **usage):
    """A call and its result: the one tool call every fixture here needs, so
    the report does not exit with `no tool calls`."""
    return [
        spend(second, message_id=f"call-{uid}", blocks=[use(uid, command)], **usage),
        plain_result(second + 1, uid),
    ]


def load_script():
    """The script as a module, so a case can call one function directly.

    Every other case here drives the CLI, because that is what a person runs.
    One path cannot be reached that way: `subagent_transcripts` walks for
    FILES, so a name that is not a readable file never becomes a path the CLI
    hands on. Mutation-testing found that — the `except OSError` guard could
    be removed with the whole slice still green."""
    spec = importlib.util.spec_from_file_location("session_cost", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# --- one odd row must not end the report ------------------------------------
#
# Round 1's findings 1 and 2, and round 2's finding 1. `parse_time`'s
# docstring states the file's rule for the whole file — "one odd row must not
# end the report" — and every reader below broke it the same way: a value
# taken out of a transcript was used as a dict key, an arithmetic operand or
# a format target without anything checking what it was. All of them are
# pinned here, because a raise in any one kills the same report.
#
# The class was closed twice, and the second time it was enumerated rather
# than eyeballed. Round 1 fixed six members and left a seventh one line away;
# round 2's fix pass took every field the readers read — the list from
# `grep '\.get(' session_cost.py`, not from memory — crossed it with every
# type JSON can carry and with the field being absent, and ran all 288
# variants. The seventh was the only survivor, and it had two crash sites
# rather than the one the finding named.


def odd(second, usage=None, message_id=None, blocks=None, message=None):
    """One row built field by field, so a case can write a shape the helpers
    above cannot: a `usage` value that is not a number, an id that is not a
    key, a `message` that is not an object at all."""
    if message is None:
        message = {
            "content": blocks
            if blocks is not None
            else [{"type": "text", "text": "."}],
            "usage": {} if usage is None else usage,
        }
        if message_id is not None:
            message["id"] = message_id
    return json.dumps({"timestamp": stamp_at(second), "message": message})


def at(stamp, blocks, message_id=None, usage=None):
    """One row with its timestamp written out rather than taken off the clock.

    `stamp_at` carries a fixed zone-aware clock, so a case built from it can
    never write the two shapes below: two rows sharing one instant, and a
    stamp carrying no zone at all. This harness produces neither — 299 real
    transcripts held 0 calls with `start == end` and 94,514 of 94,514
    timestamps zone-aware — so the cases build them by hand."""
    message = {"content": blocks}
    if usage is not None:
        message["usage"] = usage
    if message_id:
        message["id"] = message_id
    return json.dumps({"timestamp": stamp, "message": message})


def paired(uid, start, end, command="pytest -q"):
    """A call and its result at two stamps given verbatim."""
    return [
        at(start, [use(uid, command)], f"call-{uid}", {"output_tokens": 1}),
        at(end, [{"type": "tool_result", "tool_use_id": uid}]),
    ]


def turn_at(index, usage, uid):
    """One tool-call turn with its `usage` written out.

    `token_thirds` needs three turns carrying a non-zero input count before
    it computes anything, so a case about a non-finite input has to build
    three rather than reuse the one-call fixtures above.

    The stamps come off `stamp_at`, the module's own clock, rather than from
    interpolating `index` into a fixed prefix. The prefix version built
    `10:010:00` at index 10, which `datetime.fromisoformat` refuses — so
    `parse_time` returned None, `load` dropped the row, and the case went on
    asserting exit 0 while measuring one turn fewer than it said."""
    return [
        at(stamp_at(index * 60), [use(uid, "pytest -q")], f"m{uid}", usage),
        at(
            stamp_at(index * 60 + 30),
            [{"type": "tool_result", "tool_use_id": uid}],
        ),
    ]


# --- #145: the orchestrator's row is a spawn cycle, not the whole session ---
#
# Every segment of a chain has a transcript of its own, so its row is the
# whole file. The orchestrator's holds every spawn cycle of the run INSIDE it,
# so until `--spawns` the whole file was the only row it had — which is why
# #51's observation 1 has bands for three segment kinds and none for this one.
#
# A spawn cycle is not a segment. The cases below are `--spawns`', over bands
# inside one transcript; the per-segment cases at the end of this file are
# `--segments`', over the transcripts of the agents a run spawned.


def spawn(uid, start, end, subagent_type, description="a spawn"):
    """One `Agent` call and its result arriving.

    The `prompt` is present and ignored on purpose: `load` writes a call with
    no `command` field as a JSON dump of its whole input, so this is the
    shape that makes `command` a flattened prompt rather than a command line.
    Two cases below rest on that."""
    return [
        turn(
            start,
            {
                "type": "tool_use",
                "id": uid,
                "name": "Agent",
                "input": {
                    "subagent_type": subagent_type,
                    "description": description,
                    "prompt": "run pytest tests/ -q and report",
                },
            },
        ),
        turn(end, {"type": "tool_result", "tool_use_id": uid}),
    ]


@pytest.fixture
def orchestrator(tmp_path):
    """One run with two spawns, laid out so every row has something in it.

    head    two calls, one 5s gap
    cycle 1 the first spawn alone — 600s delegated
    cycle 2 two checks and a 1200s spawn; 7s and 9s gaps, 4s of command time
    tail    one call after the last spawn's result

    Cycle 2 is where the delegated-interval case can discriminate: it holds
    three calls, so it has real model gaps that a leaked 1200s would swamp
    and that dropping the spawn from the walk would shorten."""
    lines = []
    lines += call("a", 0, 10, "git status --short")
    lines += call("b", 15, 18, "cat seal/threads/x/frame/plan.md")
    lines += spawn("A", 25, 625, "agentic:crafter", "Build phase 1")
    lines += call("c", 640, 643, "git log --oneline -5")
    lines += call("d", 650, 651, "cat seal/threads/x/frame/design.md")
    lines += spawn("B", 660, 1860, "agentic:proofer", "Review round 1")
    lines += call("e", 1870, 1880, "./bin/test tests/test_x.py -q")
    path = tmp_path / "orchestrator.jsonl"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def spawns_of(path, args=()):
    return json.loads(run(["--json", *args, str(path)]).stdout)["spawns"]


def batch_spawn(uid, second, subagent_type, message_id="batch"):
    """One block of a message that spawned two agents at once.

    The two blocks carry different row stamps on purpose: a harness writes
    one message as one row per content block, and `load` takes each block's
    start from its own row. That is what lets the spawn sent FIRST be the one
    that reports LAST, which is the only shape where report order and send
    order disagree.

    The prompt is identical in both, and it names `pytest`: two spawns in one
    window carrying the same prompt are what a repeat group reads as a check
    re-run for a result already in hand."""
    return message(
        second,
        [
            {
                "type": "tool_use",
                "id": uid,
                "name": "Agent",
                "input": {
                    "subagent_type": subagent_type,
                    "prompt": "run pytest tests/ -q and report",
                },
            }
        ],
        message_id=message_id,
    )


def delegated_cells(out):
    """The `delegated` column's cells, read by the header's own right edge.

    The column is right-aligned under its header, so a cell ends where the
    word `delegated` does. Reading by position rather than by splitting keeps
    a row label with a space in it from moving the cell, and it is the cell a
    reader sees beside the note rather than any `0.9m` elsewhere on the line."""
    lines = out.splitlines()
    header = next(line for line in lines if line.startswith("  row "))
    end = header.index("delegated") + len("delegated")
    rows = lines[lines.index(header) + 1 :]
    cells = []
    for line in rows:
        if not line.strip():
            break
        if line.endswith("no call in this window"):
            continue
        cell = line[end - 11 : end].strip()
        if cell and cell != "—":
            cells.append(cell)
    return cells


# --- the per-segment reading (#350) ----------------------------------------
#
# Every other mode in this file reads the transcript it was given. This one
# opens the transcripts BESIDE it — one row per spawned segment, read from
# that segment's own file — because the agent's own wall clock is in none of
# the columns any other row has. `--spawns` says so in prose and points at
# `<session-id>/subagents/`; this is the reader that goes there.


@pytest.fixture
def run_with_segments(tmp_path):
    """Two spawns and a transcript for each, opening at its own spawn's
    result stamp — the join's measured shape.

    crafter  spawned at 25, accepted at 625; its file holds two calls, 625-641
    proofer spawned at 660, accepted at 1860; its file holds one call

    The two segments hold different call counts on purpose: a reading taken
    from the PARENT's columns cannot tell them apart, and one taken from each
    segment's own file can."""
    main = []
    main += call("a", 0, 10, "git status --short")
    main += spawn("A", 25, 625, "agentic:crafter", "Build phase 1")
    main += call("b", 640, 643, "git log --oneline -5")
    main += spawn("B", 660, 1860, "agentic:proofer", "Review round 1")
    return write_run(
        tmp_path,
        main,
        {
            "agent-crafter.jsonl": [
                *worked(625, "s1", "./bin/test tests/test_x.py -q", output=700),
                *worked(640, "s2", "ruff check .", cache_write=300),
            ],
            "agent-proofer.jsonl": [
                *worked(1860, "w1", "cat docs/design.md", cache_read=40)
            ],
        },
    )


def segments_of(path, args=()):
    proc = run(["--json", *args, str(path)])
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout)["segments"]


def segment_report(path, args=()):
    proc = run(["--segments", *args, str(path)])
    assert proc.returncode == 0, proc.stderr
    return proc.stdout


# --- the grade: each row against its kind's bar (#640) ----------------------
#
# The bars are `docs/the-review-record.md`'s, per segment kind, and until
# #640 they were nowhere on the page that prints the ratio they judge. A row's
# kind is the `subagent_type` of the spawn it was joined to, so `--segments`
# can grade where the plain reading cannot: a lone transcript carries no kind.


def batched(start, sizes, prefix):
    """A segment's own file whose turns send `sizes[i]` calls each.

    One message per turn, its calls sharing the message id, which is how
    `load` tells a turn that sent three calls from three turns. Each turn's
    results arrive a second after it, and the next turn starts five seconds
    on, so the ratio is `sum(sizes) / len(sizes)` exactly."""
    lines = []
    for index, size in enumerate(sizes):
        second = start + 5 * index
        uids = [f"{prefix}{index}-{n}" for n in range(size)]
        lines.append(
            spend(
                second,
                output=1,
                message_id=f"{prefix}-m{index}",
                blocks=[use(uid, f"cat docs/{uid}.md") for uid in uids],
            )
        )
        lines += [plain_result(second + 1, uid) for uid in uids]
    return lines


def graded_run(tmp_path, segments):
    """A run whose spawns each open one segment file of the given turn sizes.

    `segments` is `[(subagent_type, sizes), ...]`; spawn `i` is made at
    `25 + 1000 * i` and its result lands 600 seconds later, which is where
    that segment's own file opens."""
    main = call("a", 0, 10, "git status --short")
    files = {}
    for index, (agent, sizes) in enumerate(segments):
        made = 25 + 1000 * index
        main += spawn(f"S{index}", made, made + 600, agent, f"segment {index}")
        files[f"agent-{index}.jsonl"] = batched(made + 600, sizes, f"g{index}")
    return write_run(tmp_path, main, files)


def grade_lines(out):
    """The page's per-row grade lines, each flattened to single spaces."""
    return [
        " ".join(line.split())
        for line in out.splitlines()
        if "tools per turn against the" in line
    ]


# 15 calls over 14 turns, 1.07; three single calls, 1.00.
UNDER_PROOFER = [1] * 13 + [2]


SINGLES = [1, 1, 1]


# --- the resume slice: one row is one segment, not one file ----------------


def coordinator_message(second, text="Round 1's record is committed. Fix three."):
    """The row a harness writes when the coordinator sends a running agent a
    new message.

    `skills/verify/SKILL.md` prescribes the hand split *at the user lines
    where the coordinator sent it a new message*, and this is that line in
    the harness's own words. Measured over the 350 segment transcripts on one
    machine: 41 hold an idle gap at or above `analyse`'s 900-second ceiling,
    82 such gaps in all, and the row after a gap is a `type=user` row with
    `isMeta` set and a bare-string content far more often than anything
    else."""
    return json.dumps(
        {
            "timestamp": stamp_at(second),
            "type": "user",
            "isMeta": True,
            "message": {
                "role": "user",
                "content": (
                    "The coordinator sent a message while you were working: " + text
                ),
            },
        }
    )


@pytest.fixture
def resumed_segment(tmp_path):
    """One segment transcript holding two stretches of work separated by an
    idle gap and a coordinator message.

    slice 1  two calls, 625-641
    (idle)   8,359 seconds in which the agent issued nothing
    slice 2  two calls, 9010-9031

    The file's own span is 8,406 seconds. Read whole — which is what the mode
    does before this phase — one row covers the idle gap and reports a span
    over two hours for an agent that worked for 37 seconds."""
    main = call("a", 0, 10, "git status --short") + spawn(
        "A", 25, 625, "agentic:crafter", "Build phase 1"
    )
    return write_run(
        tmp_path,
        main,
        {
            "agent-crafter.jsonl": [
                *worked(625, "s1", "./bin/test tests/test_x.py -q", output=500),
                *worked(640, "s2", "ruff check ."),
                coordinator_message(9000),
                *worked(9010, "s3", "./bin/test tests/test_y.py -q"),
                *worked(9030, "s4", "git commit -m x"),
            ]
        },
    )


# --- #343: an agent that spawned another agent -----------------------------
#
# Contract rule 6 withholds four acts from every agent
# whatever its definition says, and one of them is spawning. Round 1 of #120
# spawned two agents and disclosed neither, with the rule already in the
# agent's payload — so delivery worked and the act still went the other way.
# What notices it is the walk this mode already does.


@pytest.fixture
def segment_that_spawned(tmp_path):
    """A named segment whose own transcript holds an `Agent` call, and the
    nested transcript that call produced.

    The same breach arrives twice: as a call inside the segment, and as a
    transcript the parent cannot name — its opening is 275 seconds from the
    only spawn the parent made, so no stamp can claim it. The mode prints
    both, because the two counts disagreeing is itself a reading."""
    main = call("a", 0, 10, "git status --short") + spawn(
        "A", 25, 625, "agentic:crafter", "Build phase 1"
    )
    return write_run(
        tmp_path,
        main,
        {
            "agent-crafter.jsonl": [
                *worked(625, "s1"),
                *spawn("N", 700, 900, "general-purpose", "search the tree"),
                *worked(910, "s2"),
            ],
            "agent-nested.jsonl": worked(900, "n1"),
        },
    )


# --- #637: a resumed agent's own transcript is sliced ----------------------
#
# The orchestrator holds the path the harness's task output names, and that
# path is the agent's own file. Given it, `--segments` found nothing beside it
# and printed `0 segments found`, so every fix-pass reading since 0.14.0 was
# either the harness's notice or the whole resumed file. The trigger is the
# coordinator's marker in the file itself, not the directory it sits in, so a
# marker-less file keeps the empty branch byte for byte.


def own_file(run_path, name="agent-crafter.jsonl"):
    """The agent's own transcript inside a run `write_run` laid out."""
    return run_path.parent / "main" / "subagents" / name


def plain_of(path):
    proc = run(["--json", str(path)])
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout)


# --- #637 option 3: the plain reading of a resumed file points at the mode --

HINT = (
    "coordinator message in this transcript, so the span below covers every "
    "stretch of work and the waits between them — `--segments` prints one row "
    "per stretch"
)


def _cost():
    """The script, imported so `run_gh` can be replaced.

    Imported rather than shelled out for the reason
    `tests/github/test_roll_flow_measurement_issue.py#_roller` records for its own
    neighbour: the seam is a module attribute, and a subprocess would
    have to be handed a stub on PATH to reach it.
    """
    spec = importlib.util.spec_from_file_location("session_cost_for_post", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _listing(*issues):
    """What `gh issue list --json number,state` hands back."""
    return json.dumps([{"number": n, "state": s} for n, s in issues])


def _gh(monkeypatch, module, listing=None, list_code=0, comment_code=0, stderr=""):
    """Replace `run_gh` and return the list of argvs it was given."""
    seen = []

    def fake(args):
        seen.append(list(args))
        if args[:2] == ["issue", "list"]:
            return list_code, ("[]" if listing is None else listing), stderr
        if args[:2] == ["issue", "comment"]:
            return comment_code, "", stderr
        raise AssertionError(f"no case expects `gh {' '.join(args)}`")

    monkeypatch.setattr(module, "run_gh", fake)
    return seen


def _opened(seen):
    """Whether any call would have created an issue."""
    return [a for a in seen if a[:2] == ["issue", "create"]]


def _posted(seen):
    return [a for a in seen if a[:2] == ["issue", "comment"]]


# --- through `main`, which is where `emit` lives ------------------------------


def _row(second, block):
    return json.dumps(
        {
            "timestamp": f"2026-09-22T00:{second // 60:02d}:{second % 60:02d}.000Z",
            "message": {"content": [block], "usage": {"input_tokens": 1000}},
        }
    )


MODULE = os.path.join(ROOT, "skills", "verify", "scripts", "session_cost.py")


# A number every numeric consumer accepts, filling the argument slots that
# are not carrying the value under probe.
BENIGN = 3.0


# What `count` admits and would not have refused, so what a sum of admitted
# values can be: a non-finite float, and an integer with no float of its own.


DERIVED = (float("inf"), float("-inf"), float("nan"), HUGE_INT)


NON_FINITE = (float("inf"), float("-inf"), float("nan"))


# The whole of Python's route from a number to an `int`. A site consumes its
# operand as an integer when it invokes one of these; nothing else does.
INT_PROTOCOL = (
    "__int__",
    "__index__",
    "__trunc__",
    "__round__",
    "__floor__",
    "__ceil__",
)


# The node kinds the walk classifies. Operators are here so that *no operator
# in this module converts to an int* is derived rather than asserted;
# `Subscript` is deliberately absent and the docstring says why.
SITE_KINDS = (ast.Call, ast.BinOp, ast.UnaryOp, ast.AugAssign, ast.Compare)


class Converted(BaseException):
    """Raised by the recording operand the moment a conversion is asked for.

    It stops the probed callable at the conversion rather than letting it run
    on with a half-converted operand, which is the whole of what it buys.

    **What it does NOT buy, stated because the obvious claim is false.**
    `_recorder` records before it raises, so detection never depends on who
    catches this — a callable that swallows `Exception` around its own `int()`
    still classifies as a converter, which
    `GUARD_SHAPES`' *a converter that already guards itself* is built on.
    Deriving from `BaseException` is therefore a defensive choice no case can
    tell from `Exception`: it survived the mutation battery for #192, and
    that is recorded rather than papered over with a case that would only
    pin the class statement to itself."""


class Operand:
    """An operand that answers the six integer conversions and nothing else.

    Handed to a callable enumerated from the module's source. Anything that
    is not a numeric consumer fails on it immediately — there is no path, no
    string value, no arithmetic and no ordering to act on."""

    def __init__(self):
        self.fired = set()

    def __repr__(self):
        return "<recording operand>"


def _recorder(name):
    def method(self, *_args, **_kwargs):
        self.fired.add(name)
        raise Converted(name)

    method.__name__ = name
    return method


for _name in INT_PROTOCOL:
    setattr(Operand, _name, _recorder(_name))


# --- the module under the walk ----------------------------------------------


def source():
    with open(MODULE, encoding="utf-8") as handle:
        return handle.read()


def namespace_of(path=MODULE):
    """The module's own bindings, so a call resolves to the object it names.

    Resolving the binding rather than matching the written name is what makes
    an alias and a `from`-import classify like the plain call they are."""
    spec = importlib.util.spec_from_file_location("session_cost_under_walk", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return vars(module)


def namespace_of_source(text, directory):
    """The bindings of a constructed module, loaded the way the real one is.

    Written to a file rather than exec'd into a dict because a shape
    classified through a different loader is a shape classified by a
    different code path."""
    path = os.path.join(str(directory), "under_walk.py")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return namespace_of(path)


# --- resolution -------------------------------------------------------------


def resolve(node, namespace):
    """`(object, path)` for what an expression names, or `(None, None)`.

    A bare name comes from the module's own bindings and then from builtins;
    an attribute from its resolved root; a literal is itself, which is what
    makes `" ".join(...)` resolvable. A receiver the module computes at
    runtime resolves to nothing, which is the stated residual."""
    if isinstance(node, ast.Constant):
        return node.value, repr(node.value)
    if isinstance(node, ast.Name):
        if node.id in namespace:
            return namespace[node.id], node.id
        if hasattr(builtins, node.id):
            return getattr(builtins, node.id), node.id
        return None, None
    if isinstance(node, ast.Attribute):
        root, path = resolve(node.value, namespace)
        if root is None:
            return None, None
        try:
            return getattr(root, node.attr), f"{path}.{node.attr}"
        except Exception:
            return None, None
    return None, None


def root_name(node):
    """The bare name an attribute chain hangs off, or None for an expression."""
    while isinstance(node, ast.Attribute):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def names_bound_inside(tree):
    """Every name this module binds somewhere other than at module level.

    Used to show the resolver's misses are runtime receivers rather than
    lookup failures: an unresolved callee is a name the module binds inside a
    function, never one it never binds at all."""
    bound = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            bound.add(node.id)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            bound.add(node.name)
        elif isinstance(node, ast.arg):
            bound.add(node.arg)
        elif isinstance(node, ast.alias):
            bound.add((node.asname or node.name).split(".")[0])
        elif isinstance(node, ast.ExceptHandler) and node.name:
            bound.add(node.name)
    return bound


# --- the probes -------------------------------------------------------------


def quiet(call):
    """Run `call` and answer `(value, exception type)`, printing nothing.

    Every exception is swallowed, `SystemExit` included: a probe reports by
    what it recorded, never by propagating."""
    with (
        contextlib.redirect_stdout(io.StringIO()),
        contextlib.redirect_stderr(io.StringIO()),
    ):
        try:
            return call(), None
        except BaseException as raised:
            return None, type(raised)


def slots_of(positional, keywords, value):
    """Each way one probe value can occupy an argument of this call.

    A derived number can arrive in any slot, so every slot is tried."""
    for index in range(positional):
        args = [BENIGN] * positional
        args[index] = value
        yield args, dict.fromkeys(keywords, BENIGN)
    for name in keywords:
        kwargs = dict.fromkeys(keywords, BENIGN)
        kwargs[name] = value
        yield [BENIGN] * positional, kwargs


def consumes_an_integer(fn, positional, keywords):
    """Whether calling `fn` invokes an integer conversion on one of its operands."""
    if not callable(fn):
        return False
    for args, kwargs in slots_of(positional, keywords, None):
        operand = Operand()
        args = [operand if a is None else a for a in args]
        kwargs = {k: (operand if v is None else v) for k, v in kwargs.items()}
        quiet(lambda: fn(*args, **kwargs))  # noqa: B023
        if operand.fired:
            return True
    return False


def yields_an_int(fn, positional, keywords):
    """Whether `fn` answers a benign number with an exact `int`.

    The second half of *converting a number TO an int*. It is what tells a
    conversion from a predicate that converts in order to answer something
    else — `math.isfinite` consumes its operand as an integer and yields a
    `bool`, and the module docstring holds why that exclusion is deliberate."""
    if not callable(fn):
        return False
    value, _raised = quiet(
        lambda: fn(*([BENIGN] * positional), **dict.fromkeys(keywords, BENIGN))
    )
    return type(value) is int


def raised_by(fn, positional, keywords):
    """The exception types this call raises on a value `count` admits.

    Probed rather than assumed, so no pair of exception classes is written
    down anywhere: `round` answers `OverflowError` for an infinity and
    `ValueError` for a `NaN`, and a conversion that answers nothing at all
    needs no guard."""
    kinds = set()
    for value in DERIVED:
        for args, kwargs in slots_of(positional, keywords, value):
            _value, kind = quiet(lambda: fn(*args, **kwargs))  # noqa: B023
            if kind is not None and kind is not TypeError:
                kinds.add(kind)
    return kinds


def operator_forms(node):
    """The source of each way this node's operator can be written out.

    Built by unparsing a synthetic node carrying the operator the module
    actually wrote, so there is no table of symbols to fall behind `ast`."""
    left = ast.Name(id="a", ctx=ast.Load())
    right = ast.Name(id="b", ctx=ast.Load())
    if isinstance(node, ast.BinOp):
        return [ast.unparse(ast.BinOp(left=left, op=node.op, right=right))]
    if isinstance(node, ast.UnaryOp):
        return [ast.unparse(ast.UnaryOp(op=node.op, operand=left))]
    if isinstance(node, ast.AugAssign):
        target = ast.Name(id="a", ctx=ast.Store())
        return [ast.unparse(ast.AugAssign(target=target, op=node.op, value=right))]
    if isinstance(node, ast.Compare):
        return [
            ast.unparse(ast.Compare(left=left, ops=[op], comparators=[right]))
            for op in node.ops
        ]
    return []


def operator_converts(node, benign=BENIGN):
    """Whether this node's operator reaches an int through one of its operands.

    Probed with numeric operands, because numbers are what a transcript
    yields. `benign` is what the other slot holds, and handing it a sequence
    shows the one route the numeric probe cannot see: `"ab" * n` converts `n`
    through `__index__`. Whether an operand is a sequence is provenance this
    walk does not have, so `2 * third` in `token_thirds` must not be read as
    one — which is why the default stays numeric and
    `test_the_operator_half_is_probed_and_says_what_it_cannot_see` holds the
    positive control."""
    for form in operator_forms(node):
        for env in ({"a": Operand(), "b": benign}, {"a": benign, "b": Operand()}):
            quiet(lambda: exec(form, {}, dict(env)))  # noqa: B023
            if any(isinstance(v, Operand) and v.fired for v in env.values()):
                return True
    return False


def operator_raised(node, benign=BENIGN):
    """The exception types this node's operator raises on derived operands."""
    kinds = set()
    for form in operator_forms(node):
        for value in DERIVED:
            for env in ({"a": value, "b": benign}, {"a": benign, "b": value}):
                _value, kind = quiet(lambda: exec(form, {}, dict(env)))  # noqa: B023
                if kind is not None and kind is not TypeError:
                    kinds.add(kind)
    return kinds


def is_finiteness_test(node, namespace):
    """Whether this call answers the finiteness question about its argument.

    Truthy for a benign float and falsy for every non-finite one. Decided by
    asking the resolved object, so a hand-written predicate and an aliased
    `math.isfinite` are the same thing to the walk."""
    if not isinstance(node, ast.Call):
        return False
    fn, _path = resolve(node.func, namespace)
    if not callable(fn):
        return False
    answer, _raised = quiet(lambda: fn(BENIGN))
    if not answer:
        return False
    return all(quiet(lambda: fn(value))[0] is False for value in NON_FINITE)  # noqa: B023


def evaluated(form):
    """What `form` evaluates to over literals, or None when it will not."""
    value, _raised = quiet(lambda: eval(form, {}, {}))
    return value


def keeps_an_int(node):
    """Whether this operator returns an `int` for integer operands.

    Evaluated rather than looked up: `//` keeps one and `/` does not, and
    saying which is which by hand is the list this file exists without."""
    six, three = ast.Constant(value=6), ast.Constant(value=3)
    if isinstance(node, ast.UnaryOp):
        form = ast.unparse(ast.UnaryOp(op=node.op, operand=six))
    else:
        form = ast.unparse(ast.BinOp(left=six, op=node.op, right=three))
    return type(evaluated(form)) is int


def integer_shaped(node):
    """Whether this expression is an integer nothing derived from a transcript.

    An integer literal, or integer arithmetic over integer literals. A name
    is never integer-shaped: what it holds is provenance, which is the
    subscript question in `questions.md` Q1.

    A `bool` counts, and it is the one place this file parts from `count`.
    `count` excludes `bool` because `True + 1` is a wrong number in a token
    column; the question here is only whether a transcript could have derived
    this operand, and a literal `True` no more derives from one than a
    literal `7` does. Excluding it would refuse `round(True)`, which cannot
    raise."""
    if isinstance(node, ast.Constant):
        return isinstance(node.value, int)
    if isinstance(node, ast.UnaryOp):
        return integer_shaped(node.operand) and keeps_an_int(node)
    if isinstance(node, ast.BinOp):
        return (
            integer_shaped(node.left)
            and integer_shaped(node.right)
            and keeps_an_int(node)
        )
    return False


# --- the walk ---------------------------------------------------------------


def parents_of(tree):
    return {
        child: node for node in ast.walk(tree) for child in ast.iter_child_nodes(node)
    }


def unit_of(tree):
    """Which top-level unit each node sits in, for the coordinate in a message."""
    where = {}
    for top in tree.body:
        if isinstance(top, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            for node in ast.walk(top):
                where[node] = top.name
    return where


def operands_of(node):
    if isinstance(node, ast.Call):
        return list(node.args) + [kw.value for kw in node.keywords]
    if isinstance(node, ast.BinOp):
        return [node.left, node.right]
    if isinstance(node, ast.Compare):
        return [node.left, *node.comparators]
    if isinstance(node, ast.UnaryOp):
        return [node.operand]
    if isinstance(node, ast.AugAssign):
        return [node.target, node.value]
    return []


def catches(handler, exception, namespace):
    if handler.type is None:
        return True
    written = (
        handler.type.elts if isinstance(handler.type, ast.Tuple) else [handler.type]
    )
    for entry in written:
        caught, _path = resolve(entry, namespace)
        if isinstance(caught, type) and issubclass(exception, caught):
            return True
    return False


def try_covers(node, kinds, namespace):
    """Whether this `try` catches every exception the conversion was seen to raise."""
    return all(
        any(catches(handler, exception, namespace) for handler in node.handlers)
        for exception in kinds
    )


def asks_if_finite(test, keys, namespace):
    """Whether `test` asks the finiteness question about one of these operands."""
    for node in ast.walk(test):
        if not is_finiteness_test(node, namespace):
            continue
        if any(ast.dump(arg) in keys for arg in node.args):
            return True
    return False


def negates_finiteness(test, keys, namespace):
    return (
        isinstance(test, ast.UnaryOp)
        and isinstance(test.op, ast.Not)
        and asks_if_finite(test.operand, keys, namespace)
    )


FINITENESS = "a finiteness test on the same operand"


def discharge(site, kinds, parents, namespace):
    """Why this member is safe, or None when nothing makes it safe.

    A dominance question: walking out from the site, the first enclosing
    construct that answers for its operand answers for it. An early return
    is not an enclosing construct, which is the measured false refusal
    `GUARD_SHAPES` carries."""
    operands = operands_of(site)
    if operands and all(integer_shaped(operand) for operand in operands):
        return "the operand cannot be a derived number"
    if not kinds:
        return "the conversion cannot raise on a value the funnel admits"
    keys = {ast.dump(operand) for operand in operands}
    child, node = site, parents.get(site)
    while node is not None:
        if isinstance(node, ast.Try) and child in node.body:
            if try_covers(node, kinds, namespace):
                return "a try that catches what the conversion raises"
        elif isinstance(node, ast.IfExp):
            if child is node.body and asks_if_finite(node.test, keys, namespace):
                return FINITENESS
            if child is node.orelse and negates_finiteness(node.test, keys, namespace):
                return FINITENESS
        elif isinstance(node, ast.If):
            if child in node.body and asks_if_finite(node.test, keys, namespace):
                return FINITENESS
            if child in node.orelse and negates_finiteness(node.test, keys, namespace):
                return FINITENESS
        elif isinstance(node, ast.BoolOp) and isinstance(node.op, ast.And):
            before = node.values[: node.values.index(child)]
            if any(asks_if_finite(value, keys, namespace) for value in before):
                return FINITENESS
        child, node = node, parents.get(node)
    return None


def classify(text, namespace):
    """Every site in `text`, as `(members, unresolved, examined)`.

    `members` are the conversions to an int with what discharges each — None
    where nothing does, which is the failure. `unresolved` are the sites
    whose callee is a value the module computes at runtime. `examined` is
    every node the walk looked at, so the enumeration itself can be compared
    with an independent reading."""
    tree = ast.parse(text)
    parents, units = parents_of(tree), unit_of(tree)
    members, unresolved, examined = [], [], []
    for node in ast.walk(tree):
        if not isinstance(node, SITE_KINDS):
            continue
        examined.append(node)
        where = f"{units.get(node, '<module>')}:{getattr(node, 'lineno', 0)}"
        if isinstance(node, ast.Call):
            fn, path = resolve(node.func, namespace)
            if fn is None:
                unresolved.append((where, node))
                continue
            positional = len(node.args)
            keywords = [kw.arg for kw in node.keywords if kw.arg]
            converts = consumes_an_integer(fn, positional, keywords) and yields_an_int(
                fn, positional, keywords
            )
            kinds = raised_by(fn, positional, keywords) if converts else set()
        else:
            path = ast.unparse(node)[:60]
            converts = operator_converts(node)
            kinds = operator_raised(node) if converts else set()
        if converts:
            members.append((where, path, discharge(node, kinds, parents, namespace)))
    return members, unresolved, examined


@pytest.fixture(scope="module")
def namespace():
    return namespace_of()


@pytest.fixture(scope="module")
def module_text():
    return source()


# --- what the classifier accepts, and what it refuses -----------------------

GUARD_SHAPES = (
    (
        "a finiteness test on the same operand, the shape the module uses",
        "    return [round(mean) if math.isfinite(mean) else 0]",
        True,
    ),
    (
        "a statement-level finiteness test",
        "    if math.isfinite(mean):\n        return [round(mean)]\n    return [0]",
        True,
    ),
    (
        "the same test negated, with the conversion in the other arm",
        "    if not math.isfinite(mean):\n        return [0]\n"
        "    else:\n        return [round(mean)]",
        True,
    ),
    (
        "a finiteness test earlier in the same conjunction",
        "    return [math.isfinite(mean) and round(mean)]",
        True,
    ),
    (
        "a try whose handlers cover both exceptions a conversion raises",
        "    try:\n        return [round(mean)]\n"
        "    except (OverflowError, ValueError):\n        return [0]",
        True,
    ),
    (
        "a bare except, which covers whatever the conversion raises",
        "    try:\n        return [round(mean)]\n    except:\n        return [0]",
        True,
    ),
    (
        "an except Exception, which covers both of them",
        "    try:\n        return [round(mean)]\n"
        "    except Exception:\n        return [0]",
        True,
    ),
    (
        "an integer literal operand, which no transcript derived",
        "    return [round(7)]",
        True,
    ),
    (
        "integer arithmetic over literals, still nothing derived",
        "    return [round(7 // 2)]",
        True,
    ),
    (
        "a boolean literal, which no transcript derived either",
        "    return [round(True)]",
        True,
    ),
    (
        "a converter that already guards itself needs no second guard",
        "    return [safe_int(mean)]",
        True,
    ),
    (
        "a conversion nobody could have put on a name list",
        "    return [to_int(mean) if math.isfinite(mean) else 0]",
        True,
    ),
    (
        "an aliased import doing the converting",
        "    return [m.floor(mean) if math.isfinite(mean) else 0]",
        True,
    ),
    (
        "a hand-written finiteness predicate is a guard",
        "    return [round(mean) if sane(mean) else 0]",
        True,
    ),
    # The refusals. The last one is a measured false refusal, kept here with
    # the verdict it actually gets rather than described in prose.
    (
        "no guard at all — the shape this whole file exists to catch",
        "    return [round(mean)]",
        False,
    ),
    (
        "the same conversion by a local function, with the guard taken away",
        "    return [to_int(mean)]",
        False,
    ),
    (
        "the aliased import unguarded",
        "    return [m.floor(mean)]",
        False,
    ),
    (
        "a from-import doing the converting, unguarded",
        "    return [trunc(mean)]",
        False,
    ),
    (
        "a finiteness test on a different operand",
        "    return [round(mean) if math.isfinite(other) else 0]",
        False,
    ),
    (
        "a guard that answers a different question",
        "    return [round(mean) if mean > 0 else 0]",
        False,
    ),
    (
        "a predicate on the same operand that is not a finiteness test",
        "    return [round(mean) if positive(mean) else 0]",
        False,
    ),
    (
        "a predicate that is falsy for a benign number as well",
        "    return [round(mean) if never(mean) else 0]",
        False,
    ),
    (
        "a conversion reached through a keyword argument, guarded",
        "    return [to_int_kw(value=mean) if math.isfinite(mean) else 0]",
        True,
    ),
    (
        "a try covering only the OverflowError, so a NaN still ends the report",
        "    try:\n        return [round(mean)]\n"
        "    except OverflowError:\n        return [0]",
        False,
    ),
    (
        "an early return rather than an enclosing conditional",
        "    if not math.isfinite(mean):\n        return [0]\n    return [round(mean)]",
        False,
    ),
)


PREAMBLE = (
    "import math\n"
    "import math as m\n"
    "from math import trunc\n"
    "\n\n"
    "def to_int(value):\n"
    "    return int(value)\n"
    "\n\n"
    "def sane(value):\n"
    "    return math.isfinite(value)\n"
    "\n\n"
    "def positive(value):\n"
    "    return value > 0\n"
    "\n\n"
    "def never(value):\n"
    "    return False\n"
    "\n\n"
    "def to_int_kw(value=1.0):\n"
    "    return int(value)\n"
    "\n\n"
    "def safe_int(value):\n"
    "    try:\n"
    "        return int(value)\n"
    "    except (OverflowError, ValueError):\n"
    "        return 0\n"
    "\n\n"
)


class Test_main:
    def test_accepts_a_transcript_and_separates_command_time_from_model_time(
        self, transcript
    ):
        data = json.loads(run(["--json", str(transcript)]).stdout)
        assert data["calls"] == 3
        assert data["command_s"] == 20  # 10 + 8 + 2
        assert data["model_s"] == 10  # two 5s gaps

    def test_a_rerun_that_only_changes_the_pipe_counts_as_a_repeat(self, transcript):
        """The whole point: 8 seconds spent viewing a result already produced."""
        data = json.loads(run(["--json", str(transcript)]).stdout)
        assert data["repeat_same_work_s"] == 8
        assert data["repeat_exact_s"] == 0  # the commands differ after the pipe

    def test_the_family_split_charges_a_compound_command_to_its_test(self, tmp_path):
        lines = call("a", 0, 60, "ruff check . && pytest tests -q")
        path = tmp_path / "c.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        data = json.loads(run(["--json", str(path)]).stdout)
        assert data["by_family"]["test"]["seconds"] == 60

    def test_the_report_names_batching_when_every_turn_sent_one_call(self, transcript):
        out = run([str(transcript)]).stdout
        assert "batching" in out and "1.00 tools per turn" in out

    def test_a_malformed_line_does_not_stop_the_read(self, tmp_path):
        path = tmp_path / "b.jsonl"
        path.write_text(
            "not json\n" + "\n".join(call("a", 0, 5, "pytest -q")) + "\n",
            encoding="utf-8",
        )
        assert run(["--json", str(path)]).returncode == 0

    def test_an_unparseable_timestamp_drops_its_row_not_the_report(self, tmp_path):
        bad = json.dumps(
            {
                "timestamp": "yesterday",
                "message": {
                    "content": [
                        {
                            "type": "tool_use",
                            "id": "z",
                            "name": "Bash",
                            "input": {"command": "ls"},
                        }
                    ]
                },
            }
        )
        worse = json.dumps(
            {
                "timestamp": "yesterday",
                "message": {"content": [{"type": "tool_result", "tool_use_id": "z"}]},
            }
        )
        path = tmp_path / "ts.jsonl"
        path.write_text(
            "\n".join([bad, worse, *call("a", 0, 5, "pytest -q")]) + "\n",
            encoding="utf-8",
        )
        r = run(["--json", str(path)])
        assert r.returncode == 0, r.stderr
        assert json.loads(r.stdout)["calls"] == 1

    def test_two_calls_in_one_message_are_one_turn(self, tmp_path):
        """The meter read exactly 1.00 on five runs of two agent types because it
        could not read anything else: a turn was counted per tool_use BLOCK, so a
        message carrying two calls was two turns and len(calls)/len(turns) was
        pinned at ~1.00. A turn is the MESSAGE. This case reads 1.0 against that
        code and 2.0 against the fix."""
        data = batch_data(
            tmp_path,
            [
                message(0, [use("a", "ls src"), use("b", "ls tests")], message_id="m1"),
                result(10, "a"),
                result(18, "b"),
            ],
        )
        assert data["tools_per_turn"] == 2.0

    def test_the_message_id_outranks_the_row_uuid_when_both_are_present(self, tmp_path):
        """Real rows carry both keys: a per-row uuid and, on a split message, a
        shared message id. Keyed uuid-first, the split message below is one turn
        per row — that mutant reads 1.0 here while every other case stays green,
        because no other fixture carries both keys at once."""
        data = batch_data(
            tmp_path,
            [
                message(0, [use("a", "ls src")], message_id="m1", uuid="u1"),
                result(5, "a"),
                message(6, [use("b", "ls tests")], message_id="m1", uuid="u2"),
                result(9, "b"),
            ],
        )
        assert data["tools_per_turn"] == 2.0

    def test_a_message_split_across_rows_is_one_turn_with_no_model_gap_inside(
        self, tmp_path
    ):
        """A harness writes one assistant message as one row per content block,
        each row carrying the same message id. Two things must hold: the rows are
        one turn, and the wait between the first result and the second call's row
        is the batch executing, not the model thinking."""
        data = batch_data(
            tmp_path,
            [
                message(0, [use("a", "ls src")], message_id="m1"),
                result(10, "a"),
                message(12, [use("b", "ls tests")], message_id="m1"),
                result(18, "b"),
            ],
        )
        assert data["tools_per_turn"] == 2.0
        assert data["model_s"] == 0

    def test_the_uuid_carries_the_turn_when_the_message_has_no_id(self, tmp_path):
        data = batch_data(
            tmp_path,
            [
                message(0, [use("a", "ls src")], uuid="u1"),
                result(5, "a"),
                message(6, [use("b", "ls tests")], uuid="u1"),
                result(9, "b"),
            ],
        )
        assert data["tools_per_turn"] == 2.0

    def test_a_messages_tokens_count_once_however_many_calls_it_carries(self, tmp_path):
        """The two-call message below carried 1000 tokens into the context report
        twice, which skewed every third computed from the list."""
        data = batch_data(
            tmp_path,
            [
                message(
                    0,
                    [use("a", "ls src"), use("b", "ls tests")],
                    message_id="m1",
                    tokens=1000,
                ),
                result(1, "a"),
                result(2, "b"),
                message(10, [use("c", "ls docs")], message_id="m2", tokens=2000),
                result(11, "c"),
                message(20, [use("d", "ls hooks")], message_id="m3", tokens=3000),
                result(21, "d"),
                message(30, [use("e", "ls skills")], message_id="m4", tokens=4000),
                result(31, "e"),
            ],
        )
        assert data["context_growth"] == [1000, 2000, 3500]

    def test_the_gap_after_a_batch_measures_from_its_last_result(self, tmp_path):
        """Two calls go out together; the slow one (x) started first and finished
        last. Model time to the next turn runs from the turn's LAST result (18s),
        not from whichever call sorts last by start (y, ending at 10s) — the
        per-call reading books 15s of thinking where 7s happened."""
        data = batch_data(
            tmp_path,
            [
                message(0, [use("x", "pytest tests/a -q")], message_id="m1"),
                message(5, [use("y", "git status --short")], message_id="m1"),
                result(10, "y"),
                result(18, "x"),
                message(25, [use("c", "git log -1")], message_id="m2"),
                result(30, "c"),
            ],
        )
        assert data["model_s"] == 7

    def test_the_report_stops_claiming_one_at_a_time_above_a_ratio_of_one(
        self, tmp_path
    ):
        """A run at 1.1 mostly sends single calls, but `independent calls are
        going out one at a time` is a claim the number no longer supports — and
        under per-block counting the ratio could never rise to contradict it."""
        lines = [
            message(0, [use("a0", "ls src"), use("a1", "ls tests")], message_id="m0"),
            result(1, "a0"),
            result(2, "a1"),
        ]
        for i in range(1, 6):
            lines += [
                message(i * 10, [use(f"b{i}", f"cat file{i}")], message_id=f"m{i}"),
                result(i * 10 + 1, f"b{i}"),
            ]
        path = tmp_path / "w.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        out = run([str(path)]).stdout
        assert "batching" in out
        assert "one at a time" not in out
        assert "most turns send a single call" in out

    def test_a_plain_reading_printed_at_the_advisory_is_not_flagged(self, tmp_path):
        """Round 2's 🟡 8, round 1's 🟡 1 in the plain reading. 241 calls over
        201 turns is 1.199, which prints as 1.20. The advisory sits below 1.2, so
        a batching line printing 1.20 contradicts the rule that printed it, and
        the `nothing obvious` line went missing beside it.

        Comparing the printed figure moves the verdict only for a ratio in
        [1.195, 1.2), so every reading outside that band reads as it did and
        stays comparable with the readings published since 0.9.4."""
        lines = []
        for i in range(40):
            lines += [
                message(
                    i * 10,
                    [use(f"d{i}a", f"ls a{i}"), use(f"d{i}b", f"ls b{i}")],
                    message_id=f"md{i}",
                ),
                result(i * 10 + 1, f"d{i}a"),
                result(i * 10 + 2, f"d{i}b"),
            ]
        for i in range(161):
            second = 400 + i * 10
            lines += [
                message(second, [use(f"s{i}", f"cat f{i}")], message_id=f"ms{i}"),
                result(second + 1, f"s{i}"),
            ]
        path = tmp_path / "p.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        data = json.loads(run(["--json", str(path)]).stdout)
        assert (data["calls"], data["call_turns"]) == (241, 201), data
        out = run([str(path)]).stdout
        assert "batching" not in out, out
        assert "nothing obvious" in out, out

    def test_a_transcript_with_no_tool_calls_says_so(self, tmp_path):
        path = tmp_path / "e.jsonl"
        path.write_text("{}\n", encoding="utf-8")
        r = run([str(path)])
        assert r.returncode != 0 and "no tool calls" in r.stderr

    def test_the_token_line_sums_the_run_not_just_the_transcript_it_was_given(
        self, tmp_path
    ):
        """#161's run summed `usage` over its transcript AND its subagents with a
        script written for that one occasion. A number covering only the main
        transcript is not comparable with one that covered a whole run, so the sum
        is over both and no flag turns it off."""
        path = write_run(
            tmp_path,
            worked(0, "a", output=10, cache_write=100, cache_read=1000),
            {
                "one.jsonl": [
                    spend(0, output=3, cache_write=30, cache_read=300, message_id="s1")
                ]
            },
        )
        assert tokens_of(path) == {
            "transcripts": 2,
            "turns": 2,
            "output": 13,
            "cache_write": 130,
            "cache_read": 1300,
        }

    def test_each_column_is_its_own_usage_field(self, tmp_path):
        """Three rows, each spending in one field only. A read that puts
        `cache_read_input_tokens` where the cache-write column goes — the two
        names differ by one word in the transcript — passes any fixture whose
        fields move together."""
        path = write_run(
            tmp_path,
            [
                *worked(0, "a", output=7),
                spend(2, cache_write=50, message_id="m2"),
                spend(3, cache_read=900, message_id="m3"),
            ],
        )
        totals = tokens_of(path)
        assert (totals["output"], totals["cache_write"], totals["cache_read"]) == (
            7,
            50,
            900,
        )

    def test_a_split_messages_usage_counts_once(self, tmp_path):
        """A harness writes one assistant message as one row per content block and
        repeats the usage on every row. `load` dedups against that trap for
        `context_growth`; the token line meets the same one, and a per-row sum
        would double a run's headline number."""
        path = write_run(
            tmp_path,
            [
                spend(
                    0,
                    output=10,
                    cache_read=100,
                    message_id="m1",
                    blocks=[use("a", "pytest -q")],
                ),
                spend(
                    1,
                    output=10,
                    cache_read=100,
                    message_id="m1",
                    blocks=[use("b", "ruff check .")],
                ),
                plain_result(5, "a"),
                plain_result(6, "b"),
            ],
        )
        totals = tokens_of(path)
        assert (totals["turns"], totals["output"], totals["cache_read"]) == (1, 10, 100)

    def test_a_segment_measured_alone_reports_one_transcript(self, tmp_path):
        """A subagent's own transcript has no `subagents/` directory beside it.
        That is the ordinary case rather than a failure, and the count says so."""
        path = write_run(tmp_path, worked(0, "a", output=5))
        assert tokens_of(path)["transcripts"] == 1

    def test_a_segment_of_a_segment_is_still_part_of_the_run(self, tmp_path):
        """The subagents directory is walked rather than listed, so a harness that
        nests one segment's transcripts under another still has its spend counted
        in the run's total."""
        path = write_run(
            tmp_path,
            worked(0, "a", output=1),
            {"inner/deep.jsonl": [spend(0, output=40, message_id="s1")]},
        )
        totals = tokens_of(path)
        assert (totals["transcripts"], totals["output"]) == (2, 41)

    def test_the_token_turns_and_tools_per_turn_count_different_things(self, tmp_path):
        """`tools_per_turn`'s denominator counts messages carrying a tool call,
        and the per-segment bars in `docs/the-review-record.md` are
        calibrated against that ratio. The token line's turn count is assistant
        messages carrying `usage` — a turn that only thought is still a turn the
        run paid for. This fixture separates them: two turns sent a call, a third
        only spoke."""
        path = write_run(
            tmp_path,
            [
                *worked(0, "a", output=1),
                *worked(10, "b", command="ruff check .", output=1),
                spend(20, output=1, message_id="m3"),
            ],
        )
        data = json.loads(run(["--json", str(path)]).stdout)
        assert data["tokens"]["turns"] == 3
        assert data["tools_per_turn"] == 1.0

    def test_a_junk_segment_shrinks_the_numbers_rather_than_stopping_the_report(
        self, tmp_path
    ):
        """Three things sit under `subagents/` here: a readable transcript, one
        whose lines are not JSON, and a name that is a directory rather than a
        file. The report degrades to a smaller number the way a malformed line
        does, and the transcript count is what makes the gap visible to the
        person who spawned the segments."""
        path = write_run(
            tmp_path,
            worked(0, "a", output=5),
            {
                "good.jsonl": [spend(0, output=2, message_id="s1")],
                "junk.jsonl": ["not json"],
            },
        )
        (tmp_path / "main" / "subagents" / "gone.jsonl").mkdir()
        proc = run(["--json", str(path)])
        assert proc.returncode == 0, proc.stderr
        totals = json.loads(proc.stdout)["tokens"]
        assert (totals["transcripts"], totals["output"]) == (3, 7)

    def test_the_printed_token_line_names_the_transcripts_it_covered(self, tmp_path):
        """Contract rule 14: the line is text a person reads and acts on, so a case
        pins its wording. The transcript count is the load-bearing half — every
        way this can go wrong prints a SMALLER number rather than failing, and
        only the person who spawned the segments can tell that `1 transcript` is
        wrong for a run that spawned six."""
        path = write_run(
            tmp_path,
            worked(0, "a", output=1000, cache_write=5000, cache_read=9000),
            {
                "one.jsonl": [spend(0, output=234, cache_write=678, message_id="s1")],
                "two.jsonl": [spend(0, cache_read=12, message_id="s2")],
            },
        )
        out = run([str(path)]).stdout
        assert re.search(r"^tokens\s+3 transcripts, 3 turns$", out, re.M), out
        assert re.search(r"^  output\s+1,234$", out, re.M), out
        assert re.search(r"^  cache write\s+5,678$", out, re.M), out
        assert re.search(r"^  cache read\s+9,012$", out, re.M), out

    def test_the_token_line_says_one_transcript_rather_than_1_transcripts(
        self, tmp_path
    ):
        """A count a person reads: `1 transcript`, not `1 transcripts`."""
        path = write_run(tmp_path, worked(0, "a", output=5))
        out = run([str(path)]).stdout
        assert re.search(r"^tokens\s+1 transcript, 1 turn$", out, re.M), out

    def test_a_transcript_with_usage_and_no_tool_call_still_reports_its_tokens(
        self, tmp_path
    ):
        """Finding 1. The token line was computed after `analyse`'s guard, so a
        transcript carrying `usage` and no PAIRED tool call exited with `no tool
        calls in this transcript` and printed nothing — not the time lines it
        cannot produce, and not the tokens it can. That transcript is a segment
        that read and thought, which is exactly what the run-level table's
        per-kind token row is summed over."""
        path = tmp_path / "quiet.jsonl"
        path.write_text(
            odd(0, {"output_tokens": 7, "cache_read_input_tokens": 70}) + "\n",
            encoding="utf-8",
        )
        proc = run([str(path)])
        assert proc.returncode == 0, proc.stderr
        assert "no paired tool call in this transcript" in proc.stdout, proc.stdout
        assert re.search(r"^tokens\s+1 transcript, 1 turn$", proc.stdout, re.M), (
            proc.stdout
        )
        assert re.search(r"^  output\s+7$", proc.stdout, re.M), proc.stdout
        assert re.search(r"^  cache read\s+70$", proc.stdout, re.M), proc.stdout
        assert json.loads(run(["--json", str(path)]).stdout)["tokens"]["output"] == 7

    def test_a_usage_value_that_is_not_a_number_contributes_zero(self, tmp_path):
        """Finding 2, first half. A harness writing `output_tokens` as the string
        `"12"` raised `TypeError: unsupported operand type(s) for +=` out of
        `token_totals`, and a `null` where an int was expected is the same shape.
        A value this file cannot add is a value it does not have — which is the
        direction `token_totals`' docstring promises."""
        path = write_run(
            tmp_path,
            [
                *worked(0, "a", output=5),
                odd(
                    2,
                    {
                        "output_tokens": "12",
                        "cache_write_input_tokens": None,
                        "cache_read_input_tokens": True,
                    },
                    message_id="m2",
                ),
            ],
        )
        totals = tokens_of(path)
        assert (totals["turns"], totals["output"], totals["cache_read"]) == (2, 5, 0)

    def test_a_message_id_that_is_not_a_key_does_not_end_the_report(self, tmp_path):
        """Finding 2, second half, and the same defect in `load`. An id written as
        a list is not hashable, and both readers put it straight into a `set`:
        `load` raised before `token_totals` was ever reached, so one odd row lost
        the whole report rather than its own numbers. The row keys by its own
        position instead, which is the floor `load`'s docstring already names.

        The odd row carries a tool call, because that is what reaches `load`'s
        own set lookup — a row that only spoke short-circuits on `carries_call`
        and would have exercised one reader of the two."""
        path = write_run(
            tmp_path,
            [
                *worked(0, "a", output=5),
                odd(
                    2,
                    {"output_tokens": 3},
                    message_id=["m2"],
                    blocks=[use("b", "ruff check .")],
                ),
                plain_result(3, "b"),
            ],
        )
        data = json.loads(run(["--json", str(path)]).stdout)
        assert data["calls"] == 2
        assert (data["tokens"]["turns"], data["tokens"]["output"]) == (2, 8)

    def test_a_tool_call_whose_id_is_not_a_key_loses_its_pairing_only(self, tmp_path):
        """The same class one level down: `load` indexes `pending` by the
        `tool_use` block's own id, and by the `tool_result`'s `tool_use_id`. A
        list in either raised. The unpairable call cannot be timed, so it is not
        a call — and the rest of the transcript still reports."""
        path = write_run(
            tmp_path,
            [
                *worked(0, "a", output=5),
                odd(
                    10,
                    {"output_tokens": 1},
                    message_id="m3",
                    blocks=[
                        {"type": "tool_use", "id": ["b"], "name": "Bash", "input": {}}
                    ],
                ),
                odd(
                    11,
                    message_id="m4",
                    blocks=[{"type": "tool_result", "tool_use_id": ["b"]}],
                ),
            ],
        )
        data = json.loads(run(["--json", str(path)]).stdout)
        assert data["calls"] == 1
        assert data["tokens"]["output"] == 6

    def test_a_row_that_is_not_the_shape_the_readers_assume_is_dropped(self, tmp_path):
        """`message` as a string and a top-level row that is not an object at
        all. `token_totals` checked both with `isinstance`; `load` checked
        neither and raised `AttributeError` on `.get`. One reader's guard is not
        the other's."""
        path = write_run(
            tmp_path,
            [
                *worked(0, "a", output=5),
                json.dumps({"timestamp": stamp_at(2), "message": "hello"}),
                json.dumps(["not", "a", "row"]),
                json.dumps({"timestamp": stamp_at(3), "message": {"content": "text"}}),
            ],
        )
        data = json.loads(run(["--json", str(path)]).stdout)
        assert data["calls"] == 1
        assert (data["tokens"]["turns"], data["tokens"]["output"]) == (1, 5)

    def test_a_tool_name_that_is_not_a_name_does_not_end_the_report(self, tmp_path):
        """Round 2's finding 1 — the seventh member of the class, three lines
        below the `call_id` the same pass guarded. `load` stored
        `block.get("name", "?")` with no type check, and TWO readers consume it.

        Which reader dies depends on the shape, which is why a guard at the
        reported crash site would have left the other standing. A list or an
        object is unhashable and ends `analyse`, where the name is a `by_family`
        key — before `main` has printed anything, the token block included,
        which is the outcome round 1's finding 1 was raised to end. A `null`
        name hashes fine, passes `analyse`, and raises `unsupported format
        string passed to NoneType.__format__` in `report`'s `by family` block
        instead: the span and token lines are already on screen, so it reads as
        a report that worked and then stopped.

        Both are fixed at the source, so the name is a string before either
        reader sees it. The call is charged to `?` rather than to its family —
        smaller, in the direction `count` and `message_key` already take — and
        `?` is the floor `load` had already written for a block carrying no
        `name` at all, so a name this file cannot use reads as a name that was
        never there."""
        for uid, name in (("b", ["Bash"]), ("c", {"n": 1}), ("d", None)):
            directory = tmp_path / f"name-{uid}"
            directory.mkdir()
            path = write_run(
                directory,
                [
                    *worked(0, "a", output=5),
                    spend(
                        10,
                        output=3,
                        message_id=f"m-{uid}",
                        blocks=[
                            {
                                "type": "tool_use",
                                "id": uid,
                                "name": name,
                                "input": {"command": "ruff check ."},
                            }
                        ],
                    ),
                    plain_result(11, uid),
                ],
            )
            proc = run([str(path)])
            assert proc.returncode == 0, f"{name!r}: {proc.stderr}"
            # `analyse`'s `by_family` key — where a list and an object ended it.
            assert re.search(r"^  \?\s+1 calls", proc.stdout, re.M), (
                f"{name!r}: {proc.stdout}"
            )
            # `report`'s `:<12` format — where a `null` ended it, with these two
            # lines already printed above the `by family` block it died in.
            assert re.search(r"^span\s", proc.stdout, re.M), f"{name!r}: {proc.stdout}"
            assert re.search(r"^tokens\s+1 transcript, 2 turns$", proc.stdout, re.M), (
                f"{name!r}: {proc.stdout}"
            )
            data = json.loads(run(["--json", str(path)]).stdout)
            assert (data["calls"], data["by_family"]["?"]["calls"]) == (2, 1)

    def test_the_report_tells_its_two_turn_counts_apart(self, tmp_path):
        """Finding 5. The printed report carried the word `turns` in two meanings
        over two scopes with nothing between them: the token line's count is every
        assistant message across the whole run, and `tools_per_turn`'s denominator
        is the messages of THIS transcript that sent a call. A reader divided one
        into the other — 1.08 tools per turn printed beside 659 turns and 211
        calls, which divides to 0.32.

        So each count now says what it counts and over what. The numbers are
        unchanged; what changes is that they can no longer be read as one."""
        path = write_run(
            tmp_path,
            [
                *worked(0, "a", output=1),
                *worked(10, "b", command="ruff check .", output=1),
                odd(20, {"output_tokens": 1}, message_id="m3"),
            ],
            {"one.jsonl": [odd(0, {"output_tokens": 1}, message_id="s1")]},
        )
        out = run([str(path)]).stdout
        assert re.search(r"^tokens\s+2 transcripts, 4 turns$", out, re.M), out
        assert "a turn is any assistant message, in every transcript counted" in out, (
            out
        )
        assert "2 calls over 2 turns that sent one, in this transcript alone" in out, (
            out
        )

    def test_a_span_of_zero_prints_what_it_can_rather_than_dividing_by_it(
        self, tmp_path
    ):
        """A transcript whose only paired call begins and ends on one timestamp
        has `span_s == 0.0`, and three lines of `report` divide by it.

        The span line printed and then `ZeroDivisionError` took the rest — the
        token block and the family table included. That is the same shape a
        `null` tool name produced one axis over: a report that worked and then
        stopped, which reads as a report rather than as a crash.

        What replaces the percentage is a dash and one line saying why, not a
        number. A share of a span of zero is not 0% and not 100%; it does not
        exist, and the times themselves are what was measured."""
        path = tmp_path / "zero.jsonl"
        path.write_text(
            "\n".join(paired("a", "2026-08-24T10:00:00Z", "2026-08-24T10:00:00Z"))
            + "\n",
            encoding="utf-8",
        )

        proc = run([str(path)])
        assert proc.returncode == 0, proc.stderr
        assert re.search(r"^span\s+0\.0m\s+\(1 tool calls\)$", proc.stdout, re.M), (
            proc.stdout
        )
        assert (
            "every call shares one timestamp, so there is no span to take a share of"
            in proc.stdout
        ), proc.stdout
        # No percentage invented for a denominator of zero.
        assert re.search(r"^  command\s+0\.0m\s+—$", proc.stdout, re.M), proc.stdout
        assert re.search(
            r"^  model\s+0\.0m\s+—\s+mean gap 0\.0s$", proc.stdout, re.M
        ), proc.stdout
        # The two blocks the crash used to take with it, both below the span line.
        assert re.search(r"^tokens\s+1 transcript, 1 turn$", proc.stdout, re.M), (
            proc.stdout
        )
        assert re.search(r"^  test\s+1 calls", proc.stdout, re.M), proc.stdout

        # `--json` never reached `report`, so it survived a zero span already;
        # this arm is what keeps the guard from being moved into `analyse`.
        machine = run(["--json", str(path)])
        assert machine.returncode == 0, machine.stderr
        assert json.loads(machine.stdout)["span_s"] == 0.0

    def test_a_naive_stamp_does_not_end_the_report(self, tmp_path):
        """`parse_time` is the one place a string becomes a `datetime`, so it is
        where a stamp carrying no zone is given one: UTC, the assumption the same
        line already makes when it rewrites a trailing `Z`.

        Mixing a naive stamp with an aware one raised `TypeError` with stdout
        empty on the report and on `--json` alike, and it raised from two
        different sites depending on how many calls the transcript held. One
        call dies on a SUBTRACTION in `analyse`, where the span is taken. Two
        die earlier, on a COMPARISON in `load`'s sort, before `analyse` is
        called at all — so a guard written at the reported crash site would have
        left the other standing.

        The third shape is why the naive row is normalised rather than dropped
        the way an unparseable one is: a transcript whose stamps are ALL naive
        keeps reporting numbers that are internally consistent, where dropping
        would have left it reporting nothing."""
        shapes = (
            # One call, aware start and naive end — the subtraction in `analyse`.
            (
                "mixed-pair",
                paired("a", "2026-08-24T10:00:00Z", "2026-08-24T10:00:10"),
                10.0,
                10.0,
            ),
            # Two calls, one pair of each — the comparison in `load`'s sort.
            (
                "mixed-calls",
                [
                    *paired("a", "2026-08-24T10:00:00Z", "2026-08-24T10:00:10Z"),
                    *paired(
                        "b",
                        "2026-08-24T10:00:20",
                        "2026-08-24T10:00:25",
                        "ruff check .",
                    ),
                ],
                25.0,
                15.0,
            ),
            # Every stamp naive — the shape that would report nothing if the row
            # were dropped instead of normalised.
            (
                "all-naive",
                paired("a", "2026-08-24T10:00:00", "2026-08-24T10:00:10"),
                10.0,
                10.0,
            ),
        )
        for name, lines, span, command_s in shapes:
            path = tmp_path / f"{name}.jsonl"
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")

            proc = run([str(path)])
            assert proc.returncode == 0, f"{name}: {proc.stderr}"
            assert re.search(r"^span\s", proc.stdout, re.M), f"{name}: {proc.stdout}"
            assert re.search(r"^tokens\s", proc.stdout, re.M), f"{name}: {proc.stdout}"

            # #175 records the naive case as exiting 1 with stdout EMPTY on both,
            # so both arms are asserted rather than the printed one alone.
            machine = run(["--json", str(path)])
            assert machine.returncode == 0, f"{name}: {machine.stderr}"
            data = json.loads(machine.stdout)
            assert (data["span_s"], data["command_s"]) == (span, command_s), (
                f"{name}: {data}"
            )

    def test_a_nan_token_count_does_not_end_the_report(self, tmp_path):
        """`json.loads` accepts the bare tokens `NaN`, `Infinity` and
        `-Infinity`, and all three are `float`, so a type check alone passes
        them through.

        `token_thirds` rounds a mean, and `round()` raises on a non-finite
        float — `ValueError` for a `NaN`, `OverflowError` for an infinity. The
        report ended with exit 1 and stdout EMPTY, on the report and on `--json`
        alike, which is worse than either shape #175 was opened for.

        Every usage field except `output_tokens` reaches that `round`, through
        `load`'s `input_tokens + cache_read_input_tokens` pair. `output_tokens`
        is the one field that does not, and it is the field the residual was
        first measured on — which is how a crash was recorded as printing `nan`
        at exit 0. So the fields are asserted apart rather than together."""
        shapes = (
            ("input-nan", 0, {"input_tokens": float("nan"), "output_tokens": 1}),
            ("input-inf", 0, {"input_tokens": float("inf"), "output_tokens": 1}),
            (
                "cache-read-nan",
                1,
                {
                    "input_tokens": 10,
                    "output_tokens": 1,
                    "cache_read_input_tokens": float("nan"),
                },
            ),
            ("output-nan", 2, {"input_tokens": 10, "output_tokens": float("nan")}),
            # An integer with no float of its own. `json.loads` builds one from
            # any integer literal, and the finiteness question converts before it
            # answers — so asking it raises `OverflowError` instead of answering,
            # inside the very funnel that exists to keep such a value out.
            ("output-huge-int", 0, {"input_tokens": 10, "output_tokens": HUGE_INT}),
            ("input-huge-int", 0, {"input_tokens": HUGE_INT, "output_tokens": 1}),
        )
        for name, odd, usage in shapes:
            lines = []
            for n in range(3):
                plain = {"input_tokens": 10, "output_tokens": 1}
                lines += turn_at(n, usage if n == odd else plain, f"c{n}")
            path = tmp_path / f"{name}.jsonl"
            # `json.dumps` writes bare `NaN` and `Infinity`, which is exactly the
            # shape a harness produces and `json.loads` accepts back.
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")

            proc = run([str(path)])
            assert proc.returncode == 0, f"{name}: {proc.stderr}"
            assert re.search(r"^tokens\s", proc.stdout, re.M), f"{name}: {proc.stdout}"

            machine = run(["--json", str(path)])
            assert machine.returncode == 0, f"{name}: {machine.stderr}"
            data = json.loads(machine.stdout)
            # Charged 0, the direction every funnel in the file already takes —
            # never carried through as `nan`, which prints and compares wrongly.
            assert all(isinstance(v, int) for v in data["context_growth"]), (
                f"{name}: {data['context_growth']}"
            )
            for field in ("output", "cache_read", "cache_write"):
                # An integer of any size is accepted without converting it, and a
                # float has to be finite. Neither arm converts, because both
                # `int(...)` and `math.isfinite(...)` RAISE on a value that got
                # through — the huge-int arms above would then read as a test
                # error rather than as the defect this case pins.
                value = data["tokens"][field]
                assert not isinstance(value, float) or math.isfinite(value), (
                    f"{name}: {data['tokens']}"
                )

    def test_a_sum_of_entered_values_does_not_end_the_report(self, tmp_path):
        """`count` answers for each value that ENTERS. Nothing answered for what
        the arithmetic then MADE of two of them.

        `load` adds `input_tokens` to `cache_read_input_tokens` per turn, and
        `token_thirds` sums a slice of those and divides. Two counts that each
        pass the finiteness question can add to one that does not — and the
        rounding at the end then raised `OverflowError` with stdout empty, on
        the report and on `--json` alike.

        Three arms, because the sum overflows by three different routes:
        two floats whose sum is an infinity; two integers that each have a float
        where the sum does not; and one such field on enough turns that a single
        third of the list sums past the range on its own, which no per-turn
        guard could see.

        This is a separate case from the one above on purpose. That one is about
        the values a transcript carries, and this one is about what the file
        computes from two of them — the distinction three review rounds spent
        themselves on."""
        shapes = (
            # Each field finite, their per-turn sum an infinity.
            (
                "two-floats",
                3,
                {
                    "input_tokens": TOP_FLOAT,
                    "cache_read_input_tokens": TOP_FLOAT,
                    "output_tokens": 1,
                },
                (0,),
            ),
            # Each int HAS a float; their sum does not. `count` passes both.
            (
                "two-ints",
                3,
                {
                    "input_tokens": int(TOP_FLOAT),
                    "cache_read_input_tokens": int(TOP_FLOAT),
                    "output_tokens": 1,
                },
                (0,),
            ),
            # One field, on two of six turns, so one third of the list holds two
            # of them and the SLICE sum overflows with every turn finite.
            (
                "summed-third",
                6,
                {"input_tokens": TOP_FLOAT, "output_tokens": 1},
                (0, 1),
            ),
        )
        for name, count_of_turns, odd_usage, odd_indices in shapes:
            lines = []
            for n in range(count_of_turns):
                plain = {"input_tokens": 10, "output_tokens": 1}
                lines += turn_at(n, odd_usage if n in odd_indices else plain, f"c{n}")
            path = tmp_path / f"{name}.jsonl"
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")

            proc = run([str(path)])
            assert proc.returncode == 0, f"{name}: {proc.stderr}"
            assert re.search(r"^tokens\s", proc.stdout, re.M), f"{name}: {proc.stdout}"

            machine = run(["--json", str(path)])
            assert machine.returncode == 0, f"{name}: {machine.stderr}"
            data = json.loads(machine.stdout)
            # A mean the file could not compute is charged 0, never carried out
            # as an infinity for a reader to mistake for a measurement.
            for value in data["context_growth"]:
                assert isinstance(value, int), f"{name}: {data['context_growth']}"

    def test_a_negative_span_says_what_it_actually_saw(self, tmp_path):
        """A span of zero and a negative span are not the same reading, and one
        sentence claimed the first for both.

        `report` printed *every call shares one timestamp* under any span that is
        not positive. For a transcript whose last result predates the first call
        — a harness writing a result before the call it answers — that sentence
        is false about a file the reader cannot see, which is the failure mode a
        sentence under a dash exists to prevent.

        The share itself is unchanged: neither shape gets a percentage, because
        a share of a non-positive span is not a number anybody can read.

        **#300 narrowed what a negative span means, and one arm below flipped
        with it.** The span ends at the last call to END, so it goes negative
        only when EVERY call ended before the first call began — not merely when
        the last call to begin did. A transcript holding one call that ran for
        two hours is no longer read as negative, which is the shape the third arm
        now pins."""
        lines = [
            at(
                "2026-08-24T10:00:00Z",
                [use("a", "pytest -q")],
                "ma",
                {"output_tokens": 1},
            ),
            at("2026-08-24T09:00:00Z", [{"type": "tool_result", "tool_use_id": "a"}]),
            at(
                "2026-08-24T10:05:00Z",
                [use("b", "ruff check .")],
                "mb",
                {"output_tokens": 1},
            ),
            at("2026-08-24T09:30:00Z", [{"type": "tool_result", "tool_use_id": "b"}]),
        ]
        path = tmp_path / "negative.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

        proc = run([str(path)])
        assert proc.returncode == 0, proc.stderr
        assert re.search(r"^span\s+-\d", proc.stdout, re.M), proc.stdout
        assert "no call ended after the first call began" in proc.stdout, proc.stdout
        # The zero-span sentence must NOT be the one a negative span gets.
        assert "every call shares one timestamp" not in proc.stdout, proc.stdout
        assert re.search(r"^  command\s+\S+\s+—$", proc.stdout, re.M), proc.stdout
        # And no idle figure, which is what a negative denominator makes of the
        # `idle > span * 0.1` threshold: the comparison is against a negative
        # number, so it is true, and the line printed sixty-five minutes of idle
        # beside a span of minus thirty.
        assert "idle" not in proc.stdout, proc.stdout

        # The sentence has to hold for EVERY negative span, not for the one shape
        # it was written against — and after #300 this shape is not one of them.
        # The span ends at the last call to END, so a call running 10:00 to 12:00
        # gives a run of two hours however early the OTHER call's result was
        # written. Under the old rule the span was `calls[-1]["end"]` over a list
        # sorted by start, so this transcript read minus sixty minutes for a run
        # that plainly lasted two, and the sentence below was the true statement
        # about a number that should never have been negative.
        later = [
            at(
                "2026-08-24T10:00:00Z",
                [use("a", "pytest -q")],
                "ma",
                {"output_tokens": 1},
            ),
            at("2026-08-24T12:00:00Z", [{"type": "tool_result", "tool_use_id": "a"}]),
            at(
                "2026-08-24T10:05:00Z",
                [use("b", "ruff check .")],
                "mb",
                {"output_tokens": 1},
            ),
            at("2026-08-24T09:00:00Z", [{"type": "tool_result", "tool_use_id": "b"}]),
        ]
        out_of_order = tmp_path / "out-of-order.jsonl"
        out_of_order.write_text("\n".join(later) + "\n", encoding="utf-8")
        third = run([str(out_of_order)])
        assert third.returncode == 0, third.stderr
        # 120 minutes, and neither non-positive sentence: call `a` really did run
        # from 10:00 to 12:00, and that is the run's wall clock whatever order
        # the results were written in.
        assert re.search(r"^span\s+120\.0m", third.stdout, re.M), third.stdout
        assert "no call ended after the first call began" not in third.stdout, (
            third.stdout
        )
        assert "every call shares one timestamp" not in third.stdout, third.stdout

        # A negative span makes every duration derived from it negative, and the
        # lines that INTERPRET a duration must not fire on one. `repeats` is
        # printed on a truthiness test, which minus sixty minutes satisfies — so
        # the report claimed an hour of work re-run for a result already in hand,
        # on a transcript where nothing was re-run at all. The `nothing obvious`
        # line below is suppressed by the same value, for the same reason.
        repeated = [
            at(
                "2026-08-24T10:00:00Z",
                [use("a", "pytest -q")],
                "ma",
                {"output_tokens": 1},
            ),
            at("2026-08-24T09:00:00Z", [{"type": "tool_result", "tool_use_id": "a"}]),
            at(
                "2026-08-24T10:05:00Z",
                [use("b", "pytest -q")],
                "mb",
                {"output_tokens": 1},
            ),
            at("2026-08-24T09:30:00Z", [{"type": "tool_result", "tool_use_id": "b"}]),
        ]
        repeats = tmp_path / "repeats.jsonl"
        repeats.write_text("\n".join(repeated) + "\n", encoding="utf-8")
        fourth = run([str(repeats)])
        assert fourth.returncode == 0, fourth.stderr
        assert re.search(r"^span\s+-\d", fourth.stdout, re.M), fourth.stdout
        assert "repeats" not in fourth.stdout, fourth.stdout

        # The same negative duration must not SUPPRESS a line either. The
        # `nothing obvious` line is gated on there being no repeat time, and a
        # negative repeat time reads as falsey — so the report went silent on a
        # transcript it had nothing to say about, which is the same defect as
        # the repeats line one gate over. Two calls in ONE message put tools per
        # turn above the threshold that line also needs.
        batched = [
            at(
                "2026-08-24T10:00:00Z",
                [use("x", "pytest -q"), use("y", "pytest -q")],
                "mx",
                {"output_tokens": 1},
            ),
            at("2026-08-24T09:00:00Z", [{"type": "tool_result", "tool_use_id": "x"}]),
            at("2026-08-24T09:30:00Z", [{"type": "tool_result", "tool_use_id": "y"}]),
        ]
        suppressed = tmp_path / "suppressed.jsonl"
        suppressed.write_text("\n".join(batched) + "\n", encoding="utf-8")
        fifth = run([str(suppressed)])
        assert fifth.returncode == 0, fifth.stderr
        assert re.search(r"^span\s+-\d", fifth.stdout, re.M), fifth.stdout
        assert "repeats" not in fifth.stdout, fifth.stdout
        assert "nothing obvious" in fifth.stdout, fifth.stdout

        # And a span of exactly zero keeps the sentence written for it.
        zero = tmp_path / "zero.jsonl"
        zero.write_text(
            "\n".join(paired("a", "2026-08-24T10:00:00Z", "2026-08-24T10:00:00Z"))
            + "\n",
            encoding="utf-8",
        )
        other = run([str(zero)])
        assert other.returncode == 0, other.stderr
        assert "every call shares one timestamp" in other.stdout, other.stdout
        assert "no call ended after the first call began" not in other.stdout, (
            other.stdout
        )

    # --- #193: a third the file could not compute is not a baseline -------------

    def test_a_charged_third_is_not_a_baseline_the_context_line_multiplies(
        self, tmp_path
    ):
        """`token_thirds` charges 0 for a mean it cannot compute, and the context
        line took that 0 for a measurement.

        The threshold is a multiple of the FIRST third, so any positive last third
        clears a threshold of zero. A transcript whose first third overflowed and
        whose last third is ordinary printed `0 -> 10 input tokens; later calls
        cost more than the same call would have earlier` — the input had collapsed
        by 307 orders of magnitude and the line said it grew.

        Which direction the reader was told depended on which third overflowed,
        which is why both are here: with the charged third LAST the line is
        suppressed, and that arm was already correct and must stay so.

        Exit 0 throughout. This is the wrong-number direction rather than the
        ended-report one, which is why nothing above it caught it."""
        for name, odd_index in (("first-third", 0), ("last-third", 5)):
            lines = []
            for n in range(6):
                usage = (
                    {"input_tokens": TOP_FLOAT, "cache_read_input_tokens": TOP_FLOAT}
                    if n == odd_index
                    else {"input_tokens": 10}
                )
                lines += turn_at(n, {**usage, "output_tokens": 1}, f"b{n}")
            path = tmp_path / f"{name}.jsonl"
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")

            proc = run([str(path)])
            assert proc.returncode == 0, f"{name}: {proc.stderr}"
            assert "context" not in proc.stdout, f"{name}: {proc.stdout}"

            machine = run(["--json", str(path)])
            assert machine.returncode == 0, f"{name}: {machine.stderr}"
            growth = json.loads(machine.stdout)["context_growth"]
            assert growth[0 if odd_index == 0 else 2] == 0, f"{name}: {growth}"

    def test_the_context_line_still_prints_where_the_baseline_is_real(self, tmp_path):
        """The conjunct above must not have bought its silence by silencing the
        line. A first third of ten and a last third of a hundred is the growth the
        line exists to report, and it is asserted with the numbers in it."""
        lines = []
        for n in range(6):
            lines += turn_at(n, {"input_tokens": 10 if n < 3 else 100}, f"g{n}")
        path = tmp_path / "real-growth.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

        proc = run([str(path)])
        assert proc.returncode == 0, proc.stderr
        assert "10 → 100 input tokens" in proc.stdout, proc.stdout

    def test_a_negative_input_count_is_dropped_and_a_zero_is_dropped_with_it(
        self, tmp_path
    ):
        """`token_thirds`' input filter was a truthiness test on a signed number,
        so it dropped a zero and KEPT a negative.

        Six turns whose first three carry minus ten give a growth of [-10, 0, 10]
        and print the context line off a baseline no harness can mean. The fix is
        the same inversion round 3's three statements had.

        The zero arm is here to pin the half that did NOT change: `count` answers
        0 both for a field a harness never wrote and for one it wrote as 0, so the
        file cannot tell a turn that spent nothing from a turn nobody measured,
        and both go on being dropped. Six turns carrying zero leave fewer than
        three inputs, so there is no growth at all."""
        negatives = []
        for n in range(6):
            negatives += turn_at(n, {"input_tokens": -10 if n < 3 else 10}, f"n{n}")
        path = tmp_path / "negative.jsonl"
        path.write_text("\n".join(negatives) + "\n", encoding="utf-8")

        proc = run(["--json", str(path)])
        assert proc.returncode == 0, proc.stderr
        assert json.loads(proc.stdout)["context_growth"] == [10, 10, 10], proc.stdout
        printed = run([str(path)])
        assert "context" not in printed.stdout, printed.stdout

        zeros = []
        for n in range(6):
            zeros += turn_at(n, {"input_tokens": 0}, f"z{n}")
        path = tmp_path / "zero-input.jsonl"
        path.write_text("\n".join(zeros) + "\n", encoding="utf-8")

        machine = run(["--json", str(path)])
        assert machine.returncode == 0, machine.stderr
        assert json.loads(machine.stdout)["context_growth"] == [], machine.stdout

    # --- #202: a streamed message is counted at its completed row ---------------

    def test_a_streamed_message_is_counted_at_its_largest_row(self, tmp_path):
        """A streamed assistant message reaches the transcript as several rows
        sharing one `message.id`, and its `output_tokens` grows across them.

        Keeping the first row summed however much had been emitted when that row
        was written. Measured over the 180 transcripts on the machine that found
        it: 9,098 of 13,425 messages are split, and the reported `output` was
        4,976,637 where the completed rows give 8,683,844. One proofer segment
        read as **62 output tokens across 20 turns** against a real 34,441.

        A single-row fixture cannot tell the two behaviours apart, which is why
        every case written before this one passes under either.

        `cache_write` and `cache_read` are asserted alongside because they are the
        control: they are fixed when the request is made and repeat unchanged on
        every row, so the maximum is the same number the first row gave. A change
        that started summing per row rather than per message would move all three
        together, and this case would still be green if it watched `output`
        alone."""
        rows = [
            at("2026-08-24T10:00:00Z", [use("s", "pytest -q")], "stream", partial)
            for partial in (
                {
                    "output_tokens": 3,
                    "cache_creation_input_tokens": 90,
                    "cache_read_input_tokens": 7,
                },
                {
                    "output_tokens": 400,
                    "cache_creation_input_tokens": 90,
                    "cache_read_input_tokens": 7,
                },
                {
                    "output_tokens": 1234,
                    "cache_creation_input_tokens": 90,
                    "cache_read_input_tokens": 7,
                },
            )
        ]
        rows.append(
            at("2026-08-24T10:00:05Z", [{"type": "tool_result", "tool_use_id": "s"}])
        )
        path = tmp_path / "streamed.jsonl"
        path.write_text("\n".join(rows) + "\n", encoding="utf-8")

        data = json.loads(run(["--json", str(path)]).stdout)
        tokens = data["tokens"]
        assert tokens["turns"] == 1, tokens
        assert tokens["output"] == 1234, tokens
        assert (tokens["cache_write"], tokens["cache_read"]) == (90, 7), tokens

    def test_a_message_whose_rows_arrive_out_of_order_keeps_the_completed_count(
        self, tmp_path
    ):
        """The reason the fix takes the maximum rather than the last row.

        The two agree on every one of the 13,425 messages measured, with 0 rows
        out of order, so last-row-wins would have been green everywhere it was
        checked. It would also have rested on an ordering the transcript format
        does not promise — and this is the transcript that separates them."""
        rows = [
            at("2026-08-24T10:00:00Z", [use("o", "pytest -q")], "reordered", usage)
            for usage in ({"output_tokens": 900}, {"output_tokens": 12})
        ]
        rows.append(
            at("2026-08-24T10:00:05Z", [{"type": "tool_result", "tool_use_id": "o"}])
        )
        path = tmp_path / "reordered.jsonl"
        path.write_text("\n".join(rows) + "\n", encoding="utf-8")

        tokens = json.loads(run(["--json", str(path)]).stdout)["tokens"]
        assert (tokens["turns"], tokens["output"]) == (1, 900), tokens

    def test_a_split_message_is_still_one_turn_and_not_one_per_row(self, tmp_path):
        """The half of the dedup that was right and had to stay right.

        A harness writes one message as one row per content block and repeats the
        usage on each. Taking the maximum per field must not become a sum per row:
        three rows of one message are one turn, and `cache_read` — which repeats
        unchanged — must read 500 rather than 1,500."""
        rows = [
            at(
                "2026-08-24T10:00:00Z",
                [use(f"b{n}", "pytest -q")],
                "one",
                {
                    "output_tokens": 10,
                    "cache_read_input_tokens": 500,
                },
            )
            for n in range(3)
        ]
        rows += [
            at(
                "2026-08-24T10:00:05Z",
                [{"type": "tool_result", "tool_use_id": f"b{n}"}],
            )
            for n in range(3)
        ]
        path = tmp_path / "split.jsonl"
        path.write_text("\n".join(rows) + "\n", encoding="utf-8")

        tokens = json.loads(run(["--json", str(path)]).stdout)["tokens"]
        assert (tokens["turns"], tokens["output"], tokens["cache_read"]) == (
            1,
            10,
            500,
        ), tokens

    def test_the_reading_charges_reading_to_its_own_row(self, tmp_path):
        """Through a transcript, so the wiring from `load`'s `ran` to the table
        is pinned and not only the rule. The write beside the read stays
        `other`."""
        lines = []
        lines += call("a", 0, 4, "cd /x\nsed -n 1p f")
        lines += call("b", 9, 12, "cat > f <<'EOF'\nx\nEOF")
        path = tmp_path / "read.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

        data = json.loads(run(["--json", str(path)]).stdout)
        assert data["by_family"]["read"] == {"calls": 1, "seconds": 4}, data[
            "by_family"
        ]
        assert data["by_family"]["other"] == {"calls": 1, "seconds": 3}, data[
            "by_family"
        ]

    def test_the_family_reads_the_command_as_the_harness_recorded_it(self, tmp_path):
        """Both places `analyse` asks for a family read the command with its
        newlines kept. The table's row is the first; the repeats figures are the
        second, because they keep only `test`, `lint/type` and `build`, and a test
        run after a heredoc is one of them only when the text is read unflattened.

        What is PRINTED keeps reading the flattened text: the `slowest` entry and
        the `other` note name a command on one line, as before."""
        lines = []
        lines += call("a", 0, 10, "cd /x\ngit status")
        lines += call("b", 15, 23, "cat > f <<'EOF'\nx\nEOF\npytest -q")
        lines += call("c", 28, 33, "cat > f <<'EOF'\nx\nEOF\npytest -q")
        path = tmp_path / "raw.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

        data = json.loads(run(["--json", str(path)]).stdout)
        assert data["by_family"]["git"] == {"calls": 1, "seconds": 10}, data[
            "by_family"
        ]
        assert data["by_family"]["test"] == {"calls": 2, "seconds": 13}, data[
            "by_family"
        ]
        assert "other" not in data["by_family"], data["by_family"]
        assert data["repeat_exact_s"] == 5, data
        assert data["slowest"][0]["command"] == "cd /x git status", data["slowest"]

    def test_the_report_names_the_command_the_table_could_not(self, tmp_path):
        """`other` leading the table means the rows above it describe a minority
        of the run, and nothing on the page said so — which is how #200 was
        published for four releases.

        Both arms, because a line that always prints is furniture: it appears when
        `other` leads and is absent when a named family does."""
        # Built so that two wrong answers are visible rather than merely
        # possible. `./bin/lint-docs` is the FIRST unnamed command, so an entry
        # taken in arrival order names it; `./bin/report` is the largest SINGLE
        # command, so an entry that does not group two pipes of one command names
        # that instead. Only grouping by `strip_pipe` and then taking the largest
        # answers `./bin/deploy --wait`.
        lines = []
        lines += call("a", 0, 5, "./bin/lint-docs")
        lines += call("b", 10, 70, "./bin/deploy --wait | tail -3")
        lines += call("c", 80, 140, "./bin/deploy --wait | head -1")
        lines += call("d", 150, 250, "./bin/report --long")
        # Larger than every unnamed command and charged to a family that HAS a
        # meaning, so an entry collected over the whole table rather than over
        # `other` alone names this and the case says so. `other` still leads by
        # total seconds, which is what the line is conditioned on.
        lines += call("e", 260, 460, "./bin/test --slow")
        lines += call("f", 470, 475, "pytest -q")
        unnamed_leads = tmp_path / "unnamed.jsonl"
        unnamed_leads.write_text("\n".join(lines) + "\n", encoding="utf-8")

        out = run([str(unnamed_leads)]).stdout
        assert "`other` is the largest family and names nothing" in out, out
        named_line = next(
            line for line in out.splitlines() if "Slowest command charged there" in line
        )
        # Grouped by `strip_pipe`, so two runs of one command behind different
        # pipes are one entry and the pipe is not part of what a family would
        # have to learn. The `slowest` block below prints the pipe and is not
        # what this asserts on.
        assert named_line.endswith(": ./bin/deploy --wait"), named_line
        assert re.search(r"^  other\s+4 calls", out, re.M), out
        assert re.search(r"^  test\s+2 calls", out, re.M), out

        named = []
        named += call("d", 0, 120, "./bin/test -q")
        named += call("e", 130, 135, "./bin/deploy")
        test_leads = tmp_path / "named.jsonl"
        test_leads.write_text("\n".join(named) + "\n", encoding="utf-8")

        other = run([str(test_leads)]).stdout
        assert "names nothing" not in other, other
        assert re.search(r"^  test\s+1 calls", other, re.M), other

    def test_two_spawns_are_two_cycles_each_naming_what_it_spawned(self, orchestrator):
        """The acceptance row: two `Agent` calls, two cycles, each named."""
        spawns = spawns_of(orchestrator)
        assert spawns["found"] == 2, spawns
        cycles = [row for row in spawns["rows"] if row["kind"] == "cycle"]
        assert [row["cycle"] for row in cycles] == [1, 2], cycles
        assert [row["subagent_type"] for row in cycles] == [
            "agentic:crafter",
            "agentic:proofer",
        ], cycles
        assert [row["description"] for row in cycles] == [
            "Build phase 1",
            "Review round 1",
        ], cycles

    def test_the_framing_and_the_closing_work_are_each_their_own_row(
        self, orchestrator
    ):
        """`frame/design.md`: the work outside any cycle is reported rather than dropped.

        The head is the two framing calls before the first spawn went out and the
        tail is the one call after the last spawn's result — the closing work,
        which is the half a slice quietly drops when it stops at the last one."""
        rows = spawns_of(orchestrator)["rows"]
        kinds = [row["kind"] for row in rows]
        assert kinds == ["head", "cycle", "cycle", "tail"], kinds
        head, tail = rows[0], rows[-1]
        assert head["numbers"]["calls"] == 2, head
        assert head["numbers"]["command_s"] == 13, head  # 10 + 3
        assert tail["numbers"]["calls"] == 1, tail
        assert tail["numbers"]["command_s"] == 10, tail

    def test_every_call_lands_in_exactly_one_row(self, orchestrator):
        """The property the whole table rests on, asserted as a sum.

        A slice that drops the run's closing work, or one that charges a call
        that outlived the cut its row ends at to both rows either side of it,
        both pass every other case here and fail this one."""
        data = json.loads(run(["--json", str(orchestrator)]).stdout)
        rows = data["spawns"]["rows"]
        counted = sum(row["numbers"]["calls"] for row in rows if row["numbers"])
        assert counted == data["calls"] == 7, (counted, data["calls"])

    def test_a_row_with_no_call_keeps_its_place_in_the_partition(self, tmp_path):
        """A run whose first act is a spawn has an empty head, and that is a
        reading rather than a gap. Dropping the row would make the rows stop
        partitioning the run, which is the property above."""
        lines = spawn("A", 0, 60, "agentic:crafter") + call("a", 70, 75, "git status")
        path = tmp_path / "no-head.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        rows = spawns_of(path)["rows"]
        assert [row["kind"] for row in rows] == ["head", "cycle", "tail"], rows
        assert rows[0]["numbers"] is None, rows[0]
        out = run(["--spawns", str(path)]).stdout
        assert "no call in this window" in out, out

    def test_a_batch_of_two_spawns_is_bounded_by_when_each_report_arrived(
        self, tmp_path
    ):
        """Two agents spawned in one turn, and the first one sent reports last.

        A cycle is bounded by its REPORT, so cycle 1 is the window ending at the
        first report — whichever spawn that was. Ordering the spawns by when they
        went out instead swaps both names, which is what the name assertion
        catches; nothing else in this module can tell the two orderings apart,
        because everywhere else a spawn reports in the order it was sent.

        Both calls sit in cycle 1, which is where the orchestrator actually made
        them, and cycle 2's window holds nothing at all."""
        lines = [
            batch_spawn("A", 0, "agentic:proofer"),
            batch_spawn("B", 10, "agentic:tracer"),
            result(300, "B"),
            result(900, "A"),
        ]
        path = tmp_path / "batch.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        rows = spawns_of(path)["rows"]
        cycles = [row for row in rows if row["kind"] == "cycle"]
        assert [row["subagent_type"] for row in cycles] == [
            "agentic:tracer",
            "agentic:proofer",
        ], cycles
        assert cycles[0]["numbers"]["calls"] == 2, cycles[0]
        assert cycles[1]["numbers"] is None, cycles[1]
        # Two delegated calls in ONE window, with one prompt between them. Left in
        # the repeat groups they read as 290 seconds of work re-run for a result
        # already produced, on a run where nothing was re-run.
        assert cycles[0]["numbers"]["repeat_same_work_s"] == 0, cycles[0]["numbers"]

    def test_the_subagents_own_interval_is_not_charged_to_the_orchestrator(
        self, orchestrator
    ):
        """The acceptance row, on cycle 2's fabricated 1200s spawn.

        Three implementations are separated here. Charging the delegated interval
        to the orchestrator gives a model time of 1266s or a command time of
        1204s. Dropping the spawn call out of the list handed to the analysis
        gives a model time of 7s, because the gap either side of it collapses
        into one. What is right is the third: the call stays in the walk that
        bounds the gaps and its duration leaves the command time."""
        cycles = [
            row for row in spawns_of(orchestrator)["rows"] if row["kind"] == "cycle"
        ]
        second = cycles[1]["numbers"]
        assert second["delegated_s"] == 1200, second
        assert second["command_s"] == 4, second  # 3 + 1, the two checks
        assert second["model_s"] == 16, second  # 7s and 9s, neither swallowed
        assert second["calls"] == 3, second  # the spawn is still a call it made

    def test_a_delegated_call_is_kept_out_of_the_slowest_and_the_repeats(
        self, orchestrator
    ):
        """A prompt is not a check.

        A spawn's `command` is the JSON dump of its input, so the prompt arrives
        at the classifier as a command line — the fixture's prompt names `pytest`
        on purpose. Left in, two spawns carrying the same prompt read as a check
        re-run for a result already in hand, and a twenty-minute wait sits at the
        top of `slowest` telling the reader what they already knew."""
        cycles = [
            row for row in spawns_of(orchestrator)["rows"] if row["kind"] == "cycle"
        ]
        second = cycles[1]["numbers"]
        assert second["repeat_same_work_s"] == 0, second
        assert all(
            "subagent_type" not in row["command"] for row in second["slowest"]
        ), second["slowest"]
        assert max(row["seconds"] for row in second["slowest"]) == 3, second["slowest"]

    def test_a_cycle_is_divided_by_its_own_turns_and_not_the_runs(self, orchestrator):
        """`tools_per_turn` is the one number in the row with a denominator, and
        handing `analyse` the whole run's turn list is the way to get it wrong
        without getting anything else wrong.

        Cycle 2 sent three calls over three turns, so its ratio is 1.00. Divided
        by the run's seven turns it reads 0.43 — under every threshold the
        printed advisory has — and every other number in the row stays right,
        which is what would make it survive a reading."""
        cycles = [
            row for row in spawns_of(orchestrator)["rows"] if row["kind"] == "cycle"
        ]
        second = cycles[1]["numbers"]
        assert second["call_turns"] == 3, second
        assert second["tools_per_turn"] == 1.0, second
        head = spawns_of(orchestrator)["rows"][0]["numbers"]
        assert head["call_turns"] == 2, head

    def test_a_report_stamped_before_its_call_does_not_move_a_call_out_of_its_row(
        self,
        tmp_path,
    ):
        """The running maximum on the cuts, with the guarantee removed.

        A harness writing a result before the call it answers gives that spawn a
        negative duration, which is the one shape that can make a later cut
        earlier than the one before it. Cuts that go backwards are not a sorted
        list, so the search that assigns calls to windows answers from a binary
        search over an assumption that no longer holds — and the call at 55s,
        which belongs to the framing before any spawn, is charged to a cycle
        instead. The count still partitions, so only the assignment shows it.

        `share` and `report` already answer the non-positive span for the printed
        report. This is the same harness one reader over, and until this case the
        defence against it had never been tried."""
        lines = call("a", 55, 60, "git status --short")
        lines += [
            turn(
                100,
                {
                    "type": "tool_use",
                    "id": "A",
                    "name": "Agent",
                    "input": {"subagent_type": "agentic:crafter", "prompt": "x"},
                },
            ),
            result(50, "A"),
        ]
        lines += spawn("B", 200, 300, "agentic:proofer")
        path = tmp_path / "backwards.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        data = json.loads(run(["--json", str(path)]).stdout)
        rows = data["spawns"]["rows"]
        head = rows[0]["numbers"]
        assert head is not None and head["calls"] == 1, rows
        counted = sum(row["numbers"]["calls"] for row in rows if row["numbers"])
        assert counted == data["calls"] == 3, (counted, data["calls"])

    def test_an_unparseable_turn_stamp_does_not_end_the_slicing(self, tmp_path):
        """The file's own rule — one odd row must not end the report — reaching
        the one reader that orders a turn against a time.

        `parse_time` already drops the unpairable CALL on such a row, and the
        turn is appended with the stamp as written. A turn with no time has no
        window to fall in, and asking which window it falls in compares `None`
        with a `datetime`: `TypeError`, out of the slice, with stdout empty —
        which is `count`'s failure one reader over and the shape `report`'s own
        docstrings say this file refuses. Dropped from the denominator instead,
        the direction every funnel here takes."""
        bad = json.dumps(
            {
                "timestamp": "yesterday",
                "message": {
                    "content": [
                        {
                            "type": "tool_use",
                            "id": "z",
                            "name": "Bash",
                            "input": {"command": "ls"},
                        }
                    ],
                    "usage": {"input_tokens": 500},
                },
            }
        )
        lines = [bad, *spawn("A", 10, 70, "agentic:crafter"), *call("a", 80, 85, "ls")]
        path = tmp_path / "odd-turn.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        proc = run(["--json", str(path)])
        assert proc.returncode == 0, proc.stderr
        rows = json.loads(proc.stdout)["spawns"]["rows"]
        assert [row["kind"] for row in rows] == ["head", "cycle", "tail"], rows

    def test_two_prompts_that_differ_after_a_pipe_are_not_a_check_re_run(
        self, tmp_path
    ):
        """The repeat groups, with the shape a real orchestrator's prompts have.

        A spawn's `command` is the JSON dump of its whole input, and the repeat
        groups key on that string with everything after the first `|` cut off —
        plumbing, on a command line. A spawn prompt carries markdown tables, so
        two prompts that share a sentence and then differ inside a table collapse
        into one group, and the two spawns read as 290 seconds of work re-run for
        a result already in hand. Nothing was re-run: they are two different
        agents doing two different things."""
        lines = [
            message(
                0,
                [
                    {
                        "type": "tool_use",
                        "id": "A",
                        "name": "Agent",
                        "input": {
                            "subagent_type": "agentic:proofer",
                            "prompt": "run pytest, then review round 1 | file | verdict | 1",
                        },
                    }
                ],
                message_id="pair",
            ),
            message(
                10,
                [
                    {
                        "type": "tool_use",
                        "id": "B",
                        "name": "Agent",
                        "input": {
                            "subagent_type": "agentic:proofer",
                            "prompt": "run pytest, then review round 1 | file | verdict | 2",
                        },
                    }
                ],
                message_id="pair",
            ),
            result(300, "B"),
            result(900, "A"),
        ]
        path = tmp_path / "pipes.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        first = spawns_of(path)["rows"][1]["numbers"]
        assert first["calls"] == 2, first
        assert first["repeat_same_work_s"] == 0, first
        assert first["repeat_exact_s"] == 0, first

    def test_a_cycle_carries_the_same_numbers_the_whole_run_does(self, orchestrator):
        """The acceptance row: the cycle row's keys ARE the whole run's keys.

        What it stops is a second meter hand-rolled for cycles. The labels are
        named rather than subtracted loosely, so adding one is a decision
        somebody makes here rather than a key that appears in a published
        reading.

        `segments` is the second such decision, taken when #350 landed: it is a
        reading of the transcripts BESIDE this one, so like `tokens` and `spawns`
        it is not one of `analyse`'s keys and does not belong in a cycle row's
        numbers. The case caught it on the commit that added it, which is the
        whole reason the exclusion is a literal list."""
        data = json.loads(run(["--json", str(orchestrator)]).stdout)
        whole = set(data) - {"tokens", "spawns", "segments"}
        for row in data["spawns"]["rows"]:
            assert set(row) == {
                "kind",
                "cycle",
                "subagent_type",
                "description",
                "numbers",
            }
            if row["numbers"]:
                assert set(row["numbers"]) == whole, (row["kind"], set(row["numbers"]))
        for key in (
            "span_s",
            "command_s",
            "model_s",
            "calls",
            "tools_per_turn",
            "gap_mean_s",
        ):
            assert key in whole, key

    def test_the_plain_reading_is_the_number_it_was_before_the_mode_existed(
        self, orchestrator
    ):
        """Every reading this repository has published was taken without the
        mode, and a value that quietly moves makes those incomparable with
        nothing on the page saying so — which is what #200 and #202 were.

        So the whole-run row still charges the delegated 1800s to command time,
        and its `delegated_s` is 0.0 because nothing was removed from it. The
        `Agent` row of the family table is where the delegated time stays
        visible in that reading."""
        data = json.loads(run(["--json", str(orchestrator)]).stdout)
        assert data["command_s"] == 1827, data["command_s"]  # 600 + 1200 included
        assert data["delegated_s"] == 0.0, data["delegated_s"]
        assert data["by_family"]["Agent"] == {"calls": 2, "seconds": 1800}, data[
            "by_family"
        ]

    def test_a_run_with_no_spawn_names_the_count_rather_than_printing_a_table(
        self, transcript
    ):
        """#200's failure shape, repaid the way #200 was.

        An empty cycle table reads as *this run spawned nothing* — and a run that
        DID spawn reads exactly the same way the moment a harness stops writing a
        spawn as an `Agent` call. So the count and the transcript path are printed
        and the table is not."""
        spawns = spawns_of(transcript)
        assert spawns == {"found": 0, "rows": []}, spawns
        out = run(["--spawns", str(transcript)]).stdout
        assert "0 spawns found" in out, out
        assert str(transcript) in out, out
        assert "t/turn" not in out and "cycle 1" not in out, out

    def test_the_printed_table_names_each_cycle_and_what_it_spawned(self, orchestrator):
        """The rendered text, because that is what a person posts to the log.

        The partition line is printed even when it agrees: the rows resting on it
        is the reason a reader gets to see it hold rather than taking the file's
        word for it."""
        out = run(["--spawns", str(orchestrator)]).stdout
        assert "2 spawns found" in out, out
        assert "cycle 1  agentic:crafter" in out, out
        assert "cycle 2  agentic:proofer" in out, out
        assert re.search(r"^  head\s", out, re.M), out
        assert re.search(r"^  tail\s", out, re.M), out
        assert "7 calls over the rows above, of 7 calls in the transcript" in out, out
        assert "Build phase 1" in out and "Review round 1" in out, out
        # 20.0m delegated in cycle 2, and a dash where nothing was delegated.
        assert "20.0m" in out, out
        assert "—" in out, out

    def test_a_delegated_column_of_seconds_says_which_of_two_things_it_is(
        self, orchestrator, tmp_path
    ):
        """Measured on this harness: an `Agent` call pairs in 1.5-3.7 seconds
        because its result is written when the spawn is ACCEPTED, and each
        subagent's transcript opens at that same stamp — 61 of 67 spawns across
        three runs, within one second. The agent then runs for a median of about
        1,000 seconds, in NO column of any row —
        `test_the_delegated_wait_is_in_no_column_of_any_row` is where that is
        pinned.

        So a `delegated` column of near-zeroes is not the reading it looks like,
        and a reader taking it for *nothing was delegated* is #200's failure
        shape one column over. Both arms, because a line that always prints is
        furniture: absent where a spawn's own interval really does cover its run,
        present where none of them can."""
        quick = spawn("A", 0, 3, "agentic:crafter") + call("a", 20, 25, "git status")
        path = tmp_path / "quick.jsonl"
        path.write_text("\n".join(quick) + "\n", encoding="utf-8")
        out = run(["--spawns", str(path)]).stdout
        assert "`delegated` never reaches a minute here — 3s at most" in out, out
        # Whitespace-collapsed, so the wording is what this pins rather than
        # which column the line happens to wrap at.
        assert "result is written when the spawn is ACCEPTED" in " ".join(
            out.split()
        ), out

        covered = run(["--spawns", str(orchestrator)]).stdout
        assert "never reaches a minute" not in covered, covered

    def test_the_delegated_note_follows_the_minute_the_column_prints(self, tmp_path):
        """The note is a sentence about the `delegated` column, so it decides on
        the value the column prints: `minutes`, to one place of minutes.

        Compared raw against 60, a spawn paired in 59.6 s printed `1.0m` in the
        column and, under it, *never reaches a minute here — 60s at most* (#701;
        #640's round 3, 🟡 10). That is the cause #640 fixed twice for the
        tools-per-turn ratio, on a duration.

        Both edges of the band, and the cell asserted beside the note at each, so
        the case ties the decision to what the column prints rather than to the
        number 60: if the column's unit ever changes, the 57.0 s half is what
        goes red. 57.0 s is the band's floor — `57 / 60` sits just under 0.95 in
        binary, so the column prints `0.9m` there and `1.0m` a millisecond
        above."""
        over = spawn("A", 0, 59.6, "agentic:crafter") + call("a", 80, 85, "git status")
        path = tmp_path / "over.jsonl"
        path.write_text("\n".join(over) + "\n", encoding="utf-8")
        out = run(["--spawns", str(path)]).stdout
        assert delegated_cells(out) == ["1.0m"], out
        assert "never reaches a minute" not in out, out
        assert "60s at most" not in out, out
        data = json.loads(run(["--json", str(path)]).stdout)
        delegated = [
            r["numbers"]["delegated_s"] for r in data["spawns"]["rows"] if r["numbers"]
        ]
        assert 59.6 in delegated, delegated

        floor = spawn("A", 0, 57.0, "agentic:crafter") + call("a", 80, 85, "git status")
        path = tmp_path / "floor.jsonl"
        path.write_text("\n".join(floor) + "\n", encoding="utf-8")
        out = run(["--spawns", str(path)]).stdout
        assert delegated_cells(out) == ["0.9m"], out
        assert "`delegated` never reaches a minute here — 57s at most" in out, out

    def test_a_long_agent_name_is_cut_so_its_cells_stay_under_their_headers(
        self, tmp_path
    ):
        """#712: a label longer than the column pushed every cell of its row to
        the right of its header. Read by the header's right edge, the row's
        `delegated` cell was the `model` cell, `0.0m`, where the spawn's own
        interval printed `1.0m`.

        `cycle_label` cuts to `LABEL_WIDTH` from the right with no mark, the way
        `segment_label` cuts a named agent, so the row is exactly as long as its
        header and each cell ends where its header does. A label cut to the full
        column has no space after it, so the line under *what each cycle
        spawned* puts one before the description. `--json` keeps the whole
        name, and that is where a reader of a cut row finds it."""
        name = "vercel:performance-optimizer"
        lines = spawn("A", 0, 59.6, name, "Build phase 1")
        lines += call("a", 80, 85, "git status")
        path = tmp_path / "long.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        out = run(["--spawns", str(path)]).stdout
        assert delegated_cells(out) == ["1.0m"], out
        printed = out.splitlines()
        header = next(line for line in printed if line.startswith("  row "))
        row = next(line for line in printed if line.startswith("  cycle 1 "))
        assert row.startswith("  cycle 1  vercel:performance-op "), out
        assert len(row) == len(header), out
        assert "  cycle 1  vercel:performance-op Build phase 1" in printed, out
        cycle = [r for r in spawns_of(path)["rows"] if r["kind"] == "cycle"]
        assert [r["subagent_type"] for r in cycle] == [name], cycle

    def test_the_delegated_wait_is_in_no_column_of_any_row(self, tmp_path):
        """Where the agent's wall clock actually goes, on the ACCEPTED harness.

        A window's `span_s` starts at its own first call and the model walk never
        counts the gap before that call, so the wait after a spawn's result is in
        no column of the row that follows it — under the 900s ceiling as much as
        above it. Nine pages said it was in the next row's `model` while it
        stayed under fifteen minutes; this is the case that would have caught
        that, and it is the number a reader of the band table needs."""
        lines = call("z", 0, 1, "git status --short")
        lines += spawn("A", 5, 7, "agentic:crafter")
        # 300s of silence: the agent running, well under the 900s ceiling.
        lines += call("b", 307, 310, "git log --oneline -5")
        lines += call("c", 315, 317, "cat seal/threads/x/frame/design.md")
        path = tmp_path / "accepted.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        rows = spawns_of(path)["rows"]
        tail = rows[-1]["numbers"]
        assert tail["span_s"] == 10, tail  # 307 to 317, not 7 to 317
        assert tail["model_s"] == 5, tail  # 315-310 alone; the 300s is not here
        assert tail["command_s"] == 5, tail
        assert tail["delegated_s"] == 0.0, tail
        data = json.loads(run(["--json", str(path)]).stdout)
        outside = data["span_s"] - sum(
            row["numbers"]["span_s"] for row in rows if row["numbers"]
        )
        # 304 and not 300, which is why the printed line says MOSTLY the wait:
        # 300s of it is the wait after the spawn's result, and 4s is the head's
        # own last call to the cut. On the three measured runs that second part
        # is 0.6-0.8m of a 42-168m total, and here it is deliberately visible.
        assert outside == 304, outside
        out = " ".join(run(["--spawns", str(path)]).stdout.split())
        assert "in NONE of the columns above" in out, out
        assert "5.1m of the run's 5.3m is BETWEEN the rows" in out, out

    def test_a_call_that_outlives_a_cut_prints_no_between_the_rows_figure(
        self, tmp_path
    ):
        """The rows partition the CALLS, and the difference can go the other way.

        `in_windows` assigns a call by its start, which is what makes the calls
        partition and is not enough to make the spans partition: a call that
        outlives the cut its row ends at stays in the row it began in while the
        next row's calls have already started, so two rows' spans cover the same
        seconds and their sum can pass the run's own span. The line above then
        subtracts to a negative and printed `-16.5m of the run's 16.6m is
        BETWEEN the rows -- mostly the wait`: a negative interval, named as the
        delegated wait, in the one report this work item exists to make honest.

        A background `Bash` command is the ordinary way to reach it, which is
        what this transcript is."""
        lines = call("bg", 0, 1000, "npm run dev")
        lines += spawn("A", 5, 7, "agentic:crafter")
        lines += call("b", 10, 12, "git status --short")
        lines += call("c", 990, 995, "git log --oneline -5")
        path = tmp_path / "outlives.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        rows = spawns_of(path)["rows"]
        spans = sum(row["numbers"]["span_s"] for row in rows if row["numbers"])
        data = json.loads(run(["--json", str(path)]).stdout)
        # The premise: the spans overlap, so they sum past the run's own span.
        assert spans > data["span_s"], (spans, data["span_s"])
        out = " ".join(run(["--spawns", str(path)]).stdout.split())
        # What the reader gets is the two SUMS, not their difference and not "the
        # rows overlap by 16.4m". `minutes` is one decimal, so a difference under
        # three seconds rounds to `by 0.0m` and reads as nothing having happened
        # beside a refusal; two figures the reader subtracts never round one away.
        #
        # And the difference is not the overlap. After #300 every row's interval
        # is a subinterval of the run's, so what the subtraction gives is the
        # gaps between the rows MINUS their overlap. Here the head row covers the
        # whole run, so there are no gaps and the 987s happens to equal the
        # overlap — which is why naming it the overlap would be a claim that
        # holds on this fixture and fails in general.
        assert "the rows' spans sum to 33.1m against the run's own 16.7m" in out, out
        assert "no between-the-rows figure" in out, out
        # The whole point: no negative is stated, and nothing is called the wait.
        assert "is BETWEEN the rows" not in out, out
        assert "-16.4m" not in out, out
        # The cut a row ends at, never a spawn's result: the head row's cut is
        # the first spawn's START.
        assert "outlived the cut its row ends at" in out, out
        assert "outlived a spawn's result" not in out, out

    def test_the_printed_report_calls_a_cycle_row_a_band(self, orchestrator):
        """The row covers the wait, the verifying and the framing at once, and
        posting it as an attribution to one of those overstates it. The caveat is
        on the page rather than only in `plan.md`, because the page is what gets
        pasted into the log."""
        out = run(["--spawns", str(orchestrator)]).stdout
        assert "band over several acts and never an attribution" in out, out
        assert "spawn N-1's result arriving until spawn N's arrives" in out, out
        assert "the `Agent` call's own tool_use-to-tool_result span" in out, out

    def test_a_spawn_that_names_no_subagent_type_still_gets_a_row(self, tmp_path):
        """A label this file cannot print is a label that was never there. The
        row is what the reading needs; the name on it is what makes it easy to
        read, and a blank label would leave a reader unable to tell one row from
        the next."""
        lines = [
            turn(0, {"type": "tool_use", "id": "A", "name": "Agent", "input": {}}),
            result(60, "A"),
        ]
        path = tmp_path / "unnamed.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        rows = spawns_of(path)["rows"]
        assert rows[1]["subagent_type"] == "", rows[1]
        assert "cycle 1  ?" in run(["--spawns", str(path)]).stdout

    # --- #300: a window's span ends at the last call to END ---------------------

    def test_a_span_covers_every_call_it_counts(self, tmp_path):
        """A window's span ends at the last call to END, not the last to BEGIN.

        `analyse` took the span as `calls[-1]["end"] - calls[0]["start"]` over a
        list `load` sorts by START, so a call that outlived every later call
        ended after the window it was counted in. A background command running
        0-1000s beside calls at 10-12s and 990-995s gave a span of 995s — five
        seconds shorter than the single call the window holds — and `command_s`
        counted that call in full, so the printed share was taken against a
        whole that did not contain its own part.

        The invariant this pins is the one that makes a span a span: no call it
        counted ends after it."""
        lines = call("bg", 0, 1000, "npm run dev")
        lines += call("b", 10, 12, "git status --short")
        lines += call("c", 990, 995, "git log --oneline -5")
        path = tmp_path / "outlives-the-span.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        data = json.loads(run(["--json", str(path)]).stdout)
        assert data["span_s"] == 1000, data["span_s"]
        # `slowest` is sorted by duration, so its head is the longest single
        # call. A span shorter than that is a window that does not contain one
        # of its own calls, which is what 995 against 1000 was.
        longest = data["slowest"][0]["seconds"]
        assert longest == 1000, data["slowest"][0]
        assert data["span_s"] >= longest, (data["span_s"], longest)
        out = run([str(path)]).stdout
        assert "span          16.7m" in out, out

    def test_a_head_call_outlives_the_cut_without_outliving_a_spawns_result(
        self, tmp_path
    ):
        """The head row's cut is the first spawn's START, not a spawn's result.

        `spawn_cuts` opens its cut list at the first spawn's start, so a head
        call can outlive its own row's cut and still end before that spawn's
        result arrives. The refusal must not name a cause this transcript does
        not carry, and it must not print a magnitude that rounds to nothing.

        The two sums are what removes the magnitude. `minutes` is one decimal, so
        a difference under three seconds printed `by 0.0m` as the grounds for
        withholding a figure: #145's round 3 measured that on a one-second
        overlap. The difference here is three seconds and printed `by 0.1m`; what
        this fixture pins is item 1, the cut rather than the result. Note that
        both sums round to 0.2m on it, so the reader's own subtraction gives 0.0m
        — the two figures stop the line ASSERTING a magnitude of zero, and they
        do not recover one."""
        lines = call("bg", 0, 8, "npm run dev")
        lines += spawn("A", 5, 9, "agentic:crafter")
        lines += call("b", 6, 9, "pytest -q")
        lines += call("c", 9, 10, "git status --short")
        path = tmp_path / "head-cut.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        out = " ".join(run(["--spawns", str(path)]).stdout.split())
        assert "no between-the-rows figure" in out, out
        assert "outlived the cut its row ends at" in out, out
        # No call in this transcript ends after the spawn's result at 9s.
        assert "outlived a spawn's result" not in out, out
        # The two sums, so nothing rounds to `by 0.0m`.
        assert "sum to 0.2m against the run's own 0.2m" in out, out
        assert "by 0.0m" not in out, out

    def test_an_exact_cover_reads_as_the_partition_agreeing(self, tmp_path):
        """`outside == 0` takes the between-the-rows line, not the refusal.

        The guard is `>= 0` and not `> 0`, and until now nothing pinned that
        choice: the rows summing to exactly the run's span is the partition
        agreeing, and the tally above it is printed when it agrees for the same
        reason. Under `> 0` this transcript would print a refusal — *no
        between-the-rows figure* — for a run whose rows cover it exactly, which
        is the one shape where the reader can see the arithmetic work.

        Head 0-8s, spawn 5-7s, call 10-12s: run span 12s against row spans of 8s,
        2s and 2s. The figure is 0.0m and it is a real reading."""
        lines = call("bg", 0, 8, "npm run dev")
        lines += spawn("A", 5, 7, "agentic:crafter")
        lines += call("c", 10, 12, "git status --short")
        path = tmp_path / "exact-cover.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        rows = spawns_of(path)["rows"]
        spans = sum(row["numbers"]["span_s"] for row in rows if row["numbers"])
        data = json.loads(run(["--json", str(path)]).stdout)
        assert data["span_s"] == 12, data["span_s"]
        assert spans == 12, spans
        out = " ".join(run(["--spawns", str(path)]).stdout.split())
        assert "0.0m of the run's 0.2m is BETWEEN the rows — mostly the wait" in out, (
            out
        )
        assert "no between-the-rows figure" not in out, out

    def test_each_spawned_segment_is_named_by_the_spawn_it_opened_at(
        self, run_with_segments
    ):
        """The acceptance row. Two segments, each named by the spawn whose result
        its transcript opens at, and each carrying numbers read from its own
        file rather than from the parent's columns."""
        segments = segments_of(run_with_segments)
        assert (segments["transcripts"], segments["spawns"]) == (2, 2), segments
        assert (segments["unnamed"], segments["unclaimed"]) == (0, 0), segments
        assert segments["tolerance_s"] == 1.0, segments
        assert [row["agent"] for row in segments["rows"]] == [
            "agentic:crafter",
            "agentic:proofer",
        ], segments["rows"]
        assert all(row["named"] for row in segments["rows"]), segments["rows"]
        # Read from each segment's own file: the crafter's holds two calls over
        # 625-641, the proofer's one. Neither number is in the parent transcript.
        crafter, proofer = segments["rows"]
        assert (crafter["numbers"]["calls"], crafter["numbers"]["span_s"]) == (2, 16), (
            crafter
        )
        assert (proofer["numbers"]["calls"], proofer["numbers"]["span_s"]) == (1, 1), (
            proofer
        )

    def test_a_segments_tokens_are_its_own_file_and_not_the_runs(
        self, run_with_segments
    ):
        """A column that looks summable and is not is #200's failure shape in a
        new place. Each row's tokens cover that segment's own transcript, so the
        run total — which sums the whole tree — is the larger number."""
        data = json.loads(run(["--json", str(run_with_segments)]).stdout)
        rows = data["segments"]["rows"]
        assert all("tokens" in row for row in rows), rows
        assert sum(row["tokens"]["transcripts"] for row in rows) == 2, rows
        assert data["tokens"]["transcripts"] == 3, data["tokens"]

    def test_a_segment_opening_outside_the_tolerance_is_named_by_nobody(self, tmp_path):
        """Both directions, because a join that cannot fail names everything.

        The same fixture is built twice and only the segment's opening stamp
        moves: on the spawn's result it is named, three seconds off it is not."""

        def built(opening, name):
            main = call("a", 0, 10, "git status --short") + spawn(
                "A", 25, 625, "agentic:crafter", "Build phase 1"
            )
            root = tmp_path / name
            root.mkdir()
            return write_run(root, main, {"agent-one.jsonl": worked(opening, "s1")})

        on_time = segments_of(built(625, "on-time"))
        assert on_time["unnamed"] == 0, on_time
        assert on_time["rows"][0]["agent"] == "agentic:crafter", on_time["rows"]

        late = segments_of(built(628, "late"))
        assert late["unnamed"] == 1, late
        assert late["rows"][0]["named"] is False, late["rows"]
        assert late["rows"][0]["agent"] == "", late["rows"]
        # The spawn is still there and still counted — it simply claimed nothing.
        assert (late["spawns"], late["unclaimed"]) == (1, 1), late

    def test_a_segment_the_parent_cannot_name_is_counted_rather_than_dropped(
        self, tmp_path
    ):
        """A subagent of a subagent has no `Agent` call in the parent at all, so
        no stamp can name it. `frame/design.md`: it gets a row and the count says how
        many there were — a smaller answer rather than none, which is the
        direction `tool_name` and `count` already take."""
        main = call("a", 0, 10, "git status --short") + spawn(
            "A", 25, 625, "agentic:crafter", "Build phase 1"
        )
        path = write_run(
            tmp_path,
            main,
            {
                "agent-crafter.jsonl": worked(625, "s1"),
                "inner/agent-deep.jsonl": worked(700, "d1"),
            },
        )
        segments = segments_of(path)
        assert (segments["transcripts"], segments["spawns"]) == (2, 1), segments
        assert segments["unnamed"] == 1, segments
        named = [row for row in segments["rows"] if row["named"]]
        anonymous = [row for row in segments["rows"] if not row["named"]]
        assert [row["agent"] for row in named] == ["agentic:crafter"], named
        assert len(anonymous) == 1, anonymous
        # Dropped rather than counted, the row would be invisible AND its numbers
        # would be missing from every reading of the run.
        assert anonymous[0]["numbers"]["calls"] == 1, anonymous

    def test_one_spawn_is_claimed_by_one_segment(self, tmp_path):
        """Two transcripts opening at the same instant and one spawn between
        them. Without the claim, both rows carry the same agent's name and a
        reader adding the column counts one segment twice."""
        main = call("a", 0, 10, "git status --short") + spawn(
            "A", 25, 625, "agentic:crafter", "Build phase 1"
        )
        path = write_run(
            tmp_path,
            main,
            {
                "agent-one.jsonl": worked(625, "s1"),
                "agent-two.jsonl": worked(625, "s2"),
            },
        )
        segments = segments_of(path)
        assert segments["transcripts"] == 2, segments
        assert [row["named"] for row in segments["rows"]].count(True) == 1, segments[
            "rows"
        ]
        assert segments["unnamed"] == 1, segments
        assert segments["unclaimed"] == 0, segments

    def test_a_run_with_no_segments_reads_rather_than_raising(self, transcript):
        """A segment measured on its own has no `subagents/` directory beside it.
        That is the ordinary case for this mode, not a failure — for a segment the
        coordinator never restarted, the reading is empty and the exit code is 0.
        A restarted one is read slice by slice (#637), and this fixture has no
        coordinator message."""
        proc = run(["--json", str(transcript)])
        assert proc.returncode == 0, proc.stderr
        assert json.loads(proc.stdout)["segments"] == {
            "tolerance_s": 1.0,
            "transcripts": 0,
            "spawns": 0,
            "unnamed": 0,
            "unclaimed": 0,
            "rows": [],
        }

    def test_the_printed_segment_table_names_each_agent_and_its_own_span(
        self,
        run_with_segments,
    ):
        """The rendered text, because that is what a person posts to the flow log.

        The two spans are the whole point of the mode: 16s and 1s, read from each
        segment's own file. Neither number is in any column of any `--spawns` row
        — there the same two agents read as 600s and 1200s of `delegated`, which
        is the interval until the spawn was ACCEPTED."""
        out = segment_report(run_with_segments)
        assert "agentic:crafter" in out, out
        assert "agentic:proofer" in out, out
        for header in ("span", "calls", "t/turn", "gap", "tokens"):
            assert header in out, (header, out)
        # 16s and 1s, printed by `minutes` at one decimal, and each segment's own
        # token spend: 700 output + 300 cache write for the crafter, 40 cache read
        # for the proofer. A column pinned only at zero is a column that could be
        # printing anything.
        assert re.search(
            r"^  agentic:crafter\s+0\.3m\s+2\s+[\d.]+\s+\d+s\s+1,000\s+300$", out, re.M
        ), out
        assert re.search(
            r"^  agentic:proofer\s+0\.0m\s+1\s+[\d.]+\s+\d+s\s+40\s+40$", out, re.M
        ), out

    def test_the_segment_report_names_the_tolerance_it_joined_within(
        self, run_with_segments
    ):
        """A join is a reading about a harness, not a fact this file asserts. The
        tolerance is on the page so a reader can tell a segment that matched
        nothing from a window that was too tight."""
        assert "1.0s" in segment_report(run_with_segments), segment_report(
            run_with_segments
        )

    def test_the_segment_report_states_its_counts_even_when_they_agree(
        self, run_with_segments
    ):
        """`report_spawns` prints its partition tally even when it agrees, and
        for the same reason: a join that silently matched nothing reads exactly
        like a run that spawned nothing. Two transcripts, two spawns, nothing
        unmatched on either side — and all four numbers print."""
        out = " ".join(segment_report(run_with_segments).split())
        assert "2 segment transcripts" in out, out
        assert "2 spawns" in out, out
        assert "0 segments named by nobody" in out, out
        assert "0 spawns that claimed none" in out, out

    def test_a_segment_named_by_nobody_carries_its_transcript_instead(self, tmp_path):
        """A name it cannot print is a name that was never there — and a path is
        what the reader can actually open. The count says how many there were."""
        main = call("a", 0, 10, "git status --short") + spawn(
            "A", 25, 625, "agentic:crafter", "Build phase 1"
        )
        path = write_run(
            tmp_path,
            main,
            {
                "agent-crafter.jsonl": worked(625, "s1"),
                "inner/agent-deep.jsonl": worked(700, "d1"),
            },
        )
        out = segment_report(path)
        assert "1 segment named by nobody" in " ".join(out.split()), out
        assert "agent-deep.jsonl" in out, out
        assert "no `Agent` call" in out, out

    def test_a_run_with_no_segment_names_the_count_rather_than_printing_a_table(
        self,
        transcript,
    ):
        """#200's failure shape, repaid the way `report_spawns` repays it: an
        empty table reads as a run that spawned nothing, and a run that DID spawn
        reads the same way the moment a harness moves the directory."""
        out = segment_report(transcript)
        assert "0 segments found" in out, out
        assert str(transcript) in out, out
        assert "t/turn" not in out, out
        assert "subagents/" in out, out

    def test_the_token_column_says_it_is_not_the_runs_own(self, run_with_segments):
        """A column that looks summable and is not is #200's failure shape in a
        new place, so the page says which of the two it is rather than leaving a
        reader to add it to the run's own total."""
        out = " ".join(segment_report(run_with_segments).split())
        assert "own file" in out, out
        assert "counting the same tokens twice" in out, out

    def test_the_reading_names_the_release_it_is_comparable_from(
        self, run_with_segments
    ):
        """#200 and #202 both moved what a token and a family row MEAN, and both
        were fixed in 0.9.4. A reading that does not say so is a number a reader
        will compare with one taken before the repair."""
        out = " ".join(segment_report(run_with_segments).split())
        assert "0.9.4" in out, out

    def test_the_reading_says_its_family_rows_moved_at_377(self, run_with_segments):
        """#377 moved what a family row MEANS a second time: a `git` call after a
        `cd` used to read as `other`. The token column did not move, so the page
        names the family rows alone and where their release is written down.

        The issue and not the version, because the line is written before the
        release that carries it, and `tests/behaviour/test_release_hygiene.py` refuses a
        loaded file naming a version that has not shipped."""
        out = " ".join(segment_report(run_with_segments).split())
        assert (
            "Family rows, in the run's own reading and in `--spawns`, are comparable "
            "only with readings taken on a release that carries #377" in out
        ), out
        # #728: the release's own file, not the index, lists the issue.
        assert "#377, which its file under `changelog/` names" in out, out
        assert (
            "on a line of its own or after a heredoc was charged to `other`, and so "
            "was a test run after a heredoc. The repeats lines filter by family and "
            "moved with them." in out
        ), out

    def test_the_reading_says_its_family_rows_moved_at_642(self, run_with_segments):
        """#642 moved what a family row MEANS a third time: a call that only
        read was `other`, and it is `read`. Only the `other` row and the note
        under it move, so the line says the repeats lines did not, which is what
        tells it apart from the #377 line above it."""
        out = " ".join(segment_report(run_with_segments).split())
        assert (
            "Family rows are comparable only with readings taken on a release that "
            "carries #642 as well: before it, a call that only read a file or listed "
            "a directory was charged to `other`, and there was no `read` row. The "
            "repeats lines did not move." in out
        ), out

    def test_the_mode_exits_zero_whether_it_finds_a_segment_or_not(
        self, run_with_segments, transcript
    ):
        """A measurement command that fails on a finding is a gate wearing a
        report's shape. Nothing reads this exit code today, and the orchestrator's
        own posting step would break on exactly the discovery it was posting."""
        for path in (run_with_segments, transcript):
            proc = run(["--segments", str(path)])
            assert proc.returncode == 0, (path, proc.returncode, proc.stderr)

    def test_no_existing_printed_line_moves_when_the_mode_is_not_asked_for(
        self,
        run_with_segments,
    ):
        """`analyse`'s docstring sets the condition and #200 and #202 are what
        breaking it cost. The plain reading and `--spawns` are byte-identical to
        what they printed before this mode existed."""
        plain = run([str(run_with_segments)]).stdout
        assert "segment transcripts beside this one" not in plain, plain
        assert "named by nobody" not in plain, plain
        spawns = run(["--spawns", str(run_with_segments)]).stdout
        assert "named by nobody" not in spawns, spawns
        assert "2 spawns found" in spawns, spawns

    def test_a_proofer_row_under_its_bar_is_named_with_the_bar(self, tmp_path):
        """S4. The ratio, the kind's bar and the protocol's name for the kind, on
        one line a reader can post. The prefixed name and the bare one are one
        kind, so a framer spawned as `framer` is graded the way
        `agentic:framer` would be."""
        out = segment_report(
            graded_run(
                tmp_path, [("agentic:proofer", UNDER_PROOFER), ("framer", SINGLES)]
            )
        )
        assert grade_lines(out) == [
            "agentic:proofer 1.07 tools per turn against the reviewing bar of 1.8",
            "framer 1.00 tools per turn against the framing bar of 1.4",
        ], out
        flat_out = " ".join(out.split())
        assert "every graded row meets its kind's bar" not in flat_out, flat_out
        assert "2 graded, 0 exempt, 0 ungraded" in flat_out, flat_out

    def test_a_framer_row_under_its_bar_is_named(self, tmp_path):
        """S5. 4 calls over 3 turns is 1.33, under the framing bar of 1.4 and
        over the plain reading's 1.2 -- so this row is one only the grade names."""
        out = segment_report(graded_run(tmp_path, [("agentic:framer", [2, 1, 1])]))
        assert grade_lines(out) == [
            "agentic:framer 1.33 tools per turn against the framing bar of 1.4"
        ], out

    def test_a_crafter_row_is_never_graded_and_the_page_says_why(self, tmp_path):
        """S6. An edit-test loop is serial, and the protocol judges it on
        `repeats = 0` and never on tools per turn. A crafter at the floor beside a
        proofer under its bar: the proofer is named and the crafters are not.

        Two crafters, one of them bare, because with one crafter and one proofer the
        mutation pass found that counting the PROOFER as exempt instead gives the
        same three numbers."""
        out = segment_report(
            graded_run(
                tmp_path,
                [
                    ("agentic:crafter", SINGLES),
                    ("crafter", SINGLES),
                    ("agentic:proofer", UNDER_PROOFER),
                ],
            )
        )
        lines = grade_lines(out)
        assert not any("crafter" in line for line in lines), lines
        assert len(lines) == 1, lines
        flat_out = " ".join(out.split())
        assert "1 graded, 2 exempt, 0 ungraded" in flat_out, flat_out
        assert (
            "A crafter row is exempt: an edit-test loop is serial, and the protocol "
            "judges it on `repeats = 0` rather than on this ratio." in flat_out
        ), flat_out

    def test_a_row_at_its_bar_is_silent_and_the_counts_print(self, tmp_path):
        """S7. Exactly at the bar is meeting it: 9 calls over 5 turns is 1.8 and
        7 over 5 is 1.4, both exact in binary arithmetic. A grade that read the
        bar as a floor to clear rather than to reach names both."""
        out = segment_report(
            graded_run(
                tmp_path,
                [
                    ("agentic:proofer", [2, 2, 2, 2, 1]),
                    ("agentic:framer", [2, 1, 2, 1, 1]),
                ],
            )
        )
        assert grade_lines(out) == [], out
        flat_out = " ".join(out.split())
        assert "every graded row meets its kind's bar" in flat_out, flat_out
        assert "2 graded, 0 exempt, 0 ungraded" in flat_out, flat_out

    def test_a_row_printed_at_its_bar_meets_it(self, tmp_path):
        """Round 1's 🟡 1. 79 calls over 44 turns is 1.7955 and 67 over 48 is
        1.3958: the table prints both as 1.80 and 1.40, so a line naming either
        under 1.8 or 1.4 contradicts the row printed above it. The grade compares
        the figure a reader sees."""
        out = segment_report(
            graded_run(
                tmp_path,
                [
                    ("agentic:proofer", [2] * 35 + [1] * 9),
                    ("agentic:framer", [2] * 19 + [1] * 29),
                ],
            )
        )
        assert re.search(r"agentic:proofer\s+\S+\s+79\s+1\.80\s", out), out
        assert re.search(r"agentic:framer\s+\S+\s+67\s+1\.40\s", out), out
        assert grade_lines(out) == [], out
        assert "every graded row meets its kind's bar" in " ".join(out.split()), out

    def test_a_row_with_no_kind_is_counted_as_ungraded(self, tmp_path):
        """S8. A kind the table does not know, and a row the parent could not
        name. Neither is named under a bar, the proofer beside them still is, and
        the ungraded count holds both -- the counted silence rather than the
        silent one."""
        path = graded_run(
            tmp_path, [("agentic:tracer", SINGLES), ("agentic:proofer", UNDER_PROOFER)]
        )
        deep = tmp_path / "main" / "subagents" / "inner" / "agent-deep.jsonl"
        deep.parent.mkdir(parents=True)
        deep.write_text("\n".join(batched(5000, SINGLES, "d")) + "\n", encoding="utf-8")
        out = segment_report(path)
        assert grade_lines(out) == [
            "agentic:proofer 1.07 tools per turn against the reviewing bar of 1.8"
        ], out
        flat_out = " ".join(out.split())
        assert "1 graded, 0 exempt, 2 ungraded" in flat_out, flat_out
        assert "a kind not listed, a row no spawn named" in flat_out, flat_out
        rows = segments_of(path)["rows"]
        assert [(row["kind"], row["bar"]) for row in rows] == [
            ("tracer", None),
            ("proofer", 1.8),
            ("", None),
        ], rows

    def test_a_row_with_no_paired_call_is_ungraded(self, tmp_path):
        """S8, the fourth shape. A proofer segment that read and thought and
        called nothing has a kind and a bar and no ratio, so there is nothing to
        hold against the bar; it is counted as ungraded, never as meeting it."""
        main = call("a", 0, 10, "git status --short") + spawn(
            "W", 25, 625, "agentic:proofer", "Review round 1"
        )
        path = write_run(
            tmp_path, main, {"agent-w.jsonl": [spend(625, output=5, message_id="t")]}
        )
        out = segment_report(path)
        assert "no paired call" in out, out
        assert grade_lines(out) == [], out
        flat_out = " ".join(out.split())
        assert "0 graded, 0 exempt, 1 ungraded" in flat_out, flat_out
        assert "no row here has a bar to be graded against" in flat_out, flat_out
        # Round 1's ⬜ 5. This row HAS a bar; the counts sentence listed a
        # segment that made no call among the rows with none.
        assert (
            "A row with no bar — a kind not listed, a row no spawn named — is "
            "ungraded, and so is a graded kind's segment that made no call." in flat_out
        ), flat_out
        assert [(r["kind"], r["bar"]) for r in segments_of(path)["rows"]] == [
            ("proofer", 1.8)
        ]

    def test_an_own_files_rows_are_ungraded(self, resumed_segment):
        """S8, the third shape. An agent's own file was joined to no spawn, so no
        row of it has a kind, and the page grades none while saying so."""
        out = segment_report(own_file(resumed_segment))
        assert grade_lines(out) == [], out
        flat_out = " ".join(out.split())
        assert "no row here has a bar to be graded against" in flat_out, flat_out
        assert "0 graded, 0 exempt, 2 ungraded" in flat_out, flat_out
        assert "every graded row meets" not in flat_out, flat_out

    def test_the_grade_carries_the_protocols_caveats(self, run_with_segments):
        """S9. One case per sentence, each seen red with that sentence deleted.
        A bar printed without them reads as a threshold the round failed."""
        flat_out = " ".join(segment_report(run_with_segments).split())
        assert (
            "The bar is a lens for rounds of ordinary size and never a refusal "
            "threshold, so this page refuses nothing and exits 0." in flat_out
        ), flat_out
        assert "A small round has few independent batches to rise on." in flat_out, (
            flat_out
        )
        assert (
            "A proofer's verifying round is exempt by the protocol, and this page "
            "cannot tell one from a finding round, so a reader applies that "
            "exemption by hand." in flat_out
        ), flat_out

    def test_the_grade_sits_between_the_table_and_the_section_six_block(
        self,
        segment_that_spawned,
    ):
        """Spec I5: under the table and before the contract rule 6 block, so the grade reads
        against the rows just above it."""
        out = segment_report(segment_that_spawned)
        table = out.index("t/turn")
        grade = out.index("Tools per turn against each kind's bar")
        breach = out.index("Contract rule 6 — an agent spawned another agent")
        assert table < grade < breach, out

    def test_the_plain_reading_and_spawns_carry_no_grade(self, tmp_path):
        """S10. The grade is the segments page's alone. The plain reading of the
        same run keeps its own advisory and gains nothing, and `--spawns` gains
        nothing."""
        path = graded_run(tmp_path, [("agentic:proofer", UNDER_PROOFER)])
        for args in ([str(path)], ["--spawns", str(path)]):
            out = run(args).stdout
            assert "against each kind's bar" not in out, (args, out)
            assert "tools per turn against the" not in out, (args, out)

    def test_every_json_row_carries_its_kind_and_bar(self, tmp_path):
        """S11. Two keys added and nothing else moved: `kind` is the basename,
        `bar` the number or null. The page's named rows are exactly the rows
        with a bar and a ratio under it."""
        path = graded_run(
            tmp_path,
            [
                ("agentic:crafter", SINGLES),
                ("proofer", UNDER_PROOFER),
                ("agentic:framer", [2, 2]),
            ],
        )
        rows = segments_of(path)["rows"]
        assert [(row["kind"], row["bar"]) for row in rows] == [
            ("crafter", None),
            ("proofer", 1.8),
            ("framer", 1.4),
        ], rows
        for row in rows:
            assert {
                "agent",
                "description",
                "named",
                "transcript",
                "slice",
                "slices",
                "idle_gap_s",
                "spawns",
                "numbers",
                "tokens",
            } < set(row), row
        under = [
            row["agent"]
            for row in rows
            if row["bar"] is not None
            and round(row["numbers"]["tools_per_turn"], 2) < row["bar"]
        ]
        assert [line.split()[0] for line in grade_lines(segment_report(path))] == under

    def test_a_resumed_segment_is_one_row_per_slice_not_one_per_file(
        self, resumed_segment
    ):
        """The acceptance row, and the assertion the whole-file reading fails.

        Two slices, each with its own span, and their sum well under the file's
        own — because the idle gap between them belongs to neither. A mode that
        inherits the whole-file reading has not solved the problem it was built
        for."""
        segments = segments_of(resumed_segment)
        assert len(segments["rows"]) == 2, segments["rows"]
        spans = [row["numbers"]["span_s"] for row in segments["rows"]]
        assert spans == [16, 21], spans
        # The file's own span, which is what one row would have reported.
        assert sum(spans) < 8406, spans
        assert [row["slice"] for row in segments["rows"]] == [1, 2], segments["rows"]
        assert all(row["slices"] == 2 for row in segments["rows"]), segments["rows"]

    def test_a_later_slice_inherits_the_name_from_the_files_first(
        self, resumed_segment
    ):
        """Only the file's opening stamp can be joined to a spawn's result — a
        resume has no `Agent` call of its own anywhere. So the name is the file's
        and every slice carries it, rather than the second slice reading as a
        segment nobody spawned."""
        rows = segments_of(resumed_segment)["rows"]
        assert [row["agent"] for row in rows] == ["agentic:crafter"] * 2, rows
        assert all(row["named"] for row in rows), rows
        assert segments_of(resumed_segment)["unnamed"] == 0, rows

    def test_an_unnamed_file_that_was_resumed_is_counted_once(self, tmp_path):
        """The count is a reading about the harness — how many files this run
        holds that no `Agent` call in the parent can name. A resumed file is
        several rows carrying one name, so counting rows makes the number climb
        with every resume, which is exactly what giving each slice the file's
        name exists to prevent.

        Red before the fix: `unnamed` reads 2 for one unnamable file, and the
        reconciliation below prints a disagreement that is not there."""
        main = call("a", 0, 10, "git status --short") + spawn(
            "A", 25, 625, "agentic:crafter", "Build phase 1"
        )
        path = write_run(
            tmp_path,
            main,
            {
                "agent-crafter.jsonl": [
                    *worked(625, "s1"),
                    *spawn("N", 700, 701, "general-purpose", "search the tree"),
                ],
                # The child of that spawn: no `Agent` call in the parent can name
                # it, and the coordinator resumed it.
                "inner/agent-deep.jsonl": [
                    *worked(701, "d1"),
                    coordinator_message(9000),
                    *worked(9010, "d2"),
                ],
            },
        )
        segments = segments_of(path)
        assert segments["transcripts"] == 2, segments
        assert len(segments["rows"]) == 3, segments["rows"]
        assert segments["unnamed"] == 1, segments
        out = " ".join(segment_report(path).split())
        assert "1 segment named by nobody" in out, out
        # One call inside a segment against one file the parent cannot name: the
        # two agree, and the sentence that fires on a disagreement must not.
        assert "1 `Agent` call inside a segment, against 1 segment" in out, out
        assert "the two agree" in out, out
        assert "do not agree" not in out, out

    def test_a_files_tokens_are_carried_by_its_first_slice_only(self, resumed_segment):
        """`token_totals` dedups a streamed message by its id and keeps the
        largest count each field reached (#202). Re-deriving that per slice would
        duplicate the rule, and a message whose rows straddled a slice boundary
        would be counted in both — #202's failure shape rebuilt in a new place.
        So the figure stays the file's, and every later slice prints a dash
        rather than a number a reader would add up."""
        rows = segments_of(resumed_segment)["rows"]
        assert rows[0]["tokens"]["output"] == 500, rows[0]
        assert rows[1]["tokens"] is None, rows[1]

    def test_a_segment_with_no_marker_names_the_gap_it_could_not_split(self, tmp_path):
        """The floor `plan.md` names. Where the marker is absent and an idle gap
        above the 900-second ceiling is present, one row prints and the report
        says what that does to the span — rather than a span quietly covering a
        wait nobody can see in the columns."""
        main = call("a", 0, 10, "git status --short") + spawn(
            "A", 25, 625, "agentic:crafter", "Build phase 1"
        )
        path = write_run(
            tmp_path,
            main,
            {
                "agent-crafter.jsonl": [
                    *worked(625, "s1", "./bin/test tests/test_x.py -q"),
                    *worked(2000, "s2", "ruff check ."),
                ]
            },
        )
        rows = segments_of(path)["rows"]
        assert len(rows) == 1, rows
        assert rows[0]["slices"] == 1, rows[0]
        # 626 to 2000 — the gap `analyse`'s model walk already drops and no
        # column has ever named.
        assert rows[0]["idle_gap_s"] == 1374, rows[0]
        out = " ".join(segment_report(path).split())
        assert "no coordinator message" in out, out
        assert "22.9m" in out, out

    def test_a_segment_that_was_not_resumed_reports_one_slice_and_no_gap(
        self,
        run_with_segments,
    ):
        """The negative half. A segment that ran straight through is one slice
        with nothing to name, and a report that says otherwise is reading a
        marker into a file that has none."""
        rows = segments_of(run_with_segments)["rows"]
        assert all(row["slices"] == 1 and row["slice"] == 1 for row in rows), rows
        assert all(row["idle_gap_s"] == 0 for row in rows), rows
        out = " ".join(segment_report(run_with_segments).split())
        assert "no coordinator message" not in out, out
        assert "resumed" not in out, out

    def test_two_coordinator_messages_in_a_row_do_not_invent_a_slice(self, tmp_path):
        """A cut is a marker, not a stretch of work. The coordinator can send one
        message and then another before the agent acts, and the empty window
        between them is not a slice — printing it gives the file a stretch the
        agent never worked and reports the second of two as `3/3`.

        Red before the fix: three rows, the middle one `no paired call`."""
        main = call("a", 0, 10, "git status --short") + spawn(
            "A", 25, 625, "agentic:crafter", "Build phase 1"
        )
        path = write_run(
            tmp_path,
            main,
            {
                "agent-crafter.jsonl": [
                    *worked(625, "s1"),
                    coordinator_message(9000),
                    coordinator_message(9005),
                    *worked(9010, "s2"),
                ]
            },
        )
        rows = segments_of(path)["rows"]
        assert len(rows) == 2, rows
        assert [(row["slice"], row["slices"]) for row in rows] == [(1, 2), (2, 2)], rows
        assert all(row["numbers"] for row in rows), rows
        # The file's token figure still rides one row, and it is the first kept.
        assert rows[1]["tokens"] is None, rows[1]
        out = segment_report(path)
        assert "no paired call" not in out, out
        assert "agentic:crafter  2/2" in out, out

    def test_a_file_whose_first_window_is_empty_still_carries_its_tokens(
        self, tmp_path
    ):
        """The token figure rides the first KEPT slice, not window 0 — which may
        have been dropped for holding no call. An agent resumed before it issued
        anything has exactly that shape: the marker arrives, and every call it
        made is on the far side of it.

        Found by mutating `position == 0` back to `index == 0`, which the two
        cases above leave green because their window 0 holds calls. Red under
        that mutation: no slice carries the figure at all and the file's tokens
        vanish from the table."""
        main = call("a", 0, 10, "git status --short") + spawn(
            "A", 25, 625, "agentic:crafter", "Build phase 1"
        )
        path = write_run(
            tmp_path,
            main,
            {
                "agent-crafter.jsonl": [
                    coordinator_message(625),
                    *worked(626, "s1", "./bin/test tests/test_x.py -q", output=500),
                    *worked(640, "s2", "ruff check ."),
                ]
            },
        )
        rows = segments_of(path)["rows"]
        assert len(rows) == 1, rows
        assert rows[0]["named"] and (rows[0]["slice"], rows[0]["slices"]) == (1, 1), (
            rows
        )
        assert rows[0]["tokens"]["output"] == 500, rows[0]

    def test_a_resumed_file_that_called_nothing_at_all_still_gets_its_row(
        self, tmp_path
    ):
        """The other arm of the same branch, and the reason it is not a bare
        filter. Dropping every call-less window would drop a transcript that
        paired no call anywhere — which `measure_segments`' docstring keeps a row
        for, because a segment that read and thought and called nothing is a real
        reading and it spent tokens the run paid for.

        Red before the fix for a different number: the file prints two rows, one
        per window, where it owes exactly one."""
        main = call("a", 0, 10, "git status --short") + spawn(
            "A", 25, 625, "agentic:crafter", "Build phase 1"
        )
        path = write_run(
            tmp_path,
            main,
            {
                "agent-crafter.jsonl": [
                    spend(625, message_id="thought", output=100),
                    coordinator_message(9000),
                    spend(9010, message_id="thought-2", output=200),
                ]
            },
        )
        rows = segments_of(path)["rows"]
        assert len(rows) == 1, rows
        assert (rows[0]["slice"], rows[0]["slices"]) == (1, 1), rows
        assert rows[0]["numbers"] is None, rows
        assert rows[0]["tokens"] is not None, rows
        assert "no paired call" in segment_report(path), segment_report(path)

    def test_the_printed_table_says_which_slice_of_its_file_a_row_is(
        self, resumed_segment
    ):
        """Two rows carrying one agent's name is unreadable without it — a reader
        cannot tell a resumed segment from two agents of the same kind."""
        out = segment_report(resumed_segment)
        assert "agentic:crafter  1/2" in out, out
        assert "agentic:crafter  2/2" in out, out
        assert "coordinator" in out, out

    def test_the_two_count_sentences_agree_with_their_own_number(
        self, tmp_path, resumed_segment
    ):
        """`1 segment was resumed` and `2 segments was resumed` — the second is
        what a first draft printed, and it is the failure
        `test_the_token_line_says_one_transcript_rather_than_1_transcripts`
        already polices one line over. Read off a real run before it was caught:
        `6 segments was resumed` and `2 rows above covers an idle gap`.

        Both sentences are built so no verb has to agree with a count, which is
        the repair rather than two branches that can drift apart. This pins each
        at one and at more than one."""
        one = " ".join(segment_report(resumed_segment).split())
        assert "come from 1 segment the coordinator restarted" in one, one

        # Two resumed files in one run, so the same sentence has to carry a
        # plural subject.
        main = (
            call("a", 0, 10, "git status --short")
            + spawn("A", 25, 625, "agentic:crafter", "Build phase 1")
            + spawn("B", 700, 1200, "agentic:proofer", "Review round 1")
        )
        both = write_run(
            tmp_path,
            main,
            {
                "agent-crafter.jsonl": [
                    *worked(625, "s1"),
                    coordinator_message(9000),
                    *worked(9010, "s2"),
                ],
                "agent-proofer.jsonl": [
                    *worked(1200, "w1"),
                    coordinator_message(9500),
                    *worked(9510, "w2"),
                ],
            },
        )
        many = " ".join(segment_report(both).split())
        assert "come from 2 segments the coordinator restarted" in many, many

    def test_the_idle_gap_sentence_agrees_with_its_own_number(self, tmp_path):
        """The other half of the same class: `2 rows above covers`. The sentence
        puts the count in an object rather than a subject, so one row and two
        read the same way."""
        main = (
            call("a", 0, 10, "git status --short")
            + spawn("A", 25, 625, "agentic:crafter", "Build phase 1")
            + spawn("B", 700, 1200, "agentic:proofer", "Review round 1")
        )
        path = write_run(
            tmp_path,
            main,
            {
                "agent-crafter.jsonl": [*worked(625, "s1"), *worked(2000, "s2")],
                "agent-proofer.jsonl": [*worked(1200, "w1"), *worked(4000, "w2")],
            },
        )
        out = " ".join(segment_report(path).split())
        assert "sits inside 2 rows above" in out, out

    def test_a_segment_row_carries_its_own_spawn_count(self, segment_that_spawned):
        """Per segment and not per run, because the line has to name which agent
        did it — and after phase 3, per SLICE, so a resumed agent's breach is
        attributed to the stretch it happened in."""
        rows = segments_of(segment_that_spawned)["rows"]
        by_name = {row["agent"] or row["transcript"]: row for row in rows}
        assert by_name["agentic:crafter"]["spawns"] == 1, rows
        nested = [row for row in rows if not row["named"]]
        assert len(nested) == 1 and nested[0]["spawns"] == 0, rows

    def test_a_spawn_inside_a_segment_prints_a_line_naming_agent_count_and_section(
        self,
        segment_that_spawned,
    ):
        """#343's whole answer. It notices and stops nothing — a report is read by
        a person who can skip it — and that is the claim the evidence's location
        permits, because a transcript never leaves the machine that produced it."""
        out = " ".join(segment_report(segment_that_spawned).split())
        assert "Contract rule 6" in out, out
        assert "agentic:crafter" in out, out
        assert "1 `Agent` call" in out, out
        assert "spawn no agent" in out, out

    def test_a_clean_run_prints_no_such_line(self, run_with_segments):
        """The negative half, planted in the same commit. A breach line nobody
        has seen fail is a counterfeit seal: these two segments made no `Agent`
        call, and the section is not mentioned at all."""
        out = segment_report(run_with_segments)
        assert "rule 6" not in out, out
        assert "spawn no agent" not in out, out
        rows = segments_of(run_with_segments)["rows"]
        assert all(row["spawns"] == 0 for row in rows), rows

    def test_the_breach_line_says_which_agents_the_section_binds(
        self, segment_that_spawned
    ):
        """The line fires on any `Agent` call in any segment's transcript, and
        the walk cannot tell an agent this plugin spawns from one whose own
        procedure instructs the fan-out. Measured over the 43 runs on this
        machine: 13 carry the line and 12 of those name an agent this plugin
        spawns — the thirteenth names `claude-preset:code-reviewer`, which no
        definition here governs.

        The absence half is `test_a_clean_run_prints_no_such_line`, which asserts
        `rule 6` appears nowhere in a clean run and so covers this sentence too.

        Red before the fix: the report cites the section and never says who it
        reaches."""
        out = " ".join(segment_report(segment_that_spawned).split())
        assert "Contract rule 6 binds the agents this plugin spawns" in out, out
        assert "for that agent's own definition to say" in out, out

    def test_the_two_counts_of_one_breach_are_reconciled_and_printed(
        self,
        segment_that_spawned,
    ):
        """A spawn inside a segment shows up twice — as a call in that segment's
        file and as a transcript the parent cannot name. Both numbers print, so a
        reader can see them agree rather than taking this file's word for it,
        which is `report_spawns`' partition tally one mode over."""
        out = " ".join(segment_report(segment_that_spawned).split())
        assert "1 `Agent` call inside a segment" in out, out
        assert "1 segment the parent could not name" in out, out
        # The discriminating half: this fixture's two counts DO agree, so the
        # sentence that fires on a disagreement must not.
        assert "the two agree" in out, out
        assert "do not agree" not in out, out

    def test_a_disagreement_between_the_two_counts_is_printed_not_resolved(
        self, tmp_path
    ):
        """An agent can spawn and have its child's transcript go missing, or a
        segment can be unnamable for the other reason — its opening outside the
        tolerance. The mode has no way to tell which, so it says the two
        disagree instead of picking one."""
        main = call("a", 0, 10, "git status --short") + spawn(
            "A", 25, 625, "agentic:crafter", "Build phase 1"
        )
        path = write_run(
            tmp_path,
            main,
            {
                "agent-crafter.jsonl": [
                    *worked(625, "s1"),
                    *spawn("N", 700, 900, "general-purpose", "search the tree"),
                ]
            },
        )
        out = " ".join(segment_report(path).split())
        assert "1 `Agent` call inside a segment" in out, out
        assert "0 segments the parent could not name" in out, out
        assert "do not agree" in out, out

    def test_the_mode_still_exits_zero_when_it_finds_a_breach(
        self, segment_that_spawned
    ):
        """It notices; it is not a gate. Nothing reads this exit code today, and
        the orchestrator's own posting step would break on exactly the discovery
        it was posting."""
        assert run(["--segments", str(segment_that_spawned)]).returncode == 0

    def test_a_transcript_with_no_stamp_to_join_on_still_gets_a_row(self, tmp_path):
        """Found by the mutation pass: dropping the unjoinable file kept every
        case green.

        A transcript that cannot be opened, holds no parseable line, or carries
        no `timestamp` has nothing to join on. It is still part of the run, and
        dropping it would take its numbers out of the reading while the
        transcripts-walked count went on including it — two numbers disagreeing
        with nothing on the page saying so, which is the failure every other
        count in this mode prints to avoid."""
        main = call("a", 0, 10, "git status --short") + spawn(
            "A", 25, 625, "agentic:crafter", "Build phase 1"
        )
        stampless = json.dumps(
            {"message": {"role": "user", "content": [{"type": "text", "text": "."}]}}
        )
        path = write_run(
            tmp_path,
            main,
            {
                "agent-crafter.jsonl": worked(625, "s1"),
                "agent-stampless.jsonl": [stampless, "{ not json", ""],
            },
        )
        segments = segments_of(path)
        assert segments["transcripts"] == 2, segments
        # The row count and the transcripts-walked count agree, which is the
        # whole property dropping it would break.
        assert len(segments["rows"]) == 2, segments["rows"]
        assert segments["unnamed"] == 1, segments
        anonymous = [row for row in segments["rows"] if not row["named"]]
        assert anonymous[0]["numbers"] is None, anonymous
        assert "agent-stampless.jsonl" in segment_report(path), segment_report(path)

    def test_a_spawn_in_a_later_slice_is_named_by_that_slice(self, tmp_path):
        """Found by the mutation pass: zeroing the SLICED branch's spawn count
        kept every case green, because the breach fixture was never resumed.

        A resumed agent that spawns in its second stretch must be named as that
        stretch — `agentic:crafter  2/2` — or the line points at work the agent
        was doing an hour earlier."""
        main = call("a", 0, 10, "git status --short") + spawn(
            "A", 25, 625, "agentic:crafter", "Build phase 1"
        )
        path = write_run(
            tmp_path,
            main,
            {
                "agent-crafter.jsonl": [
                    *worked(625, "s1"),
                    coordinator_message(9000),
                    *worked(9010, "s2"),
                    *spawn("N", 9100, 9200, "general-purpose", "search the tree"),
                ]
            },
        )
        rows = segments_of(path)["rows"]
        assert [row["spawns"] for row in rows] == [0, 1], rows
        out = " ".join(segment_report(path).split())
        assert "agentic:crafter 2/2 made 1 `Agent` call" in out, out

    def test_an_agents_own_resumed_transcript_is_one_row_per_slice(
        self, resumed_segment
    ):
        """The acceptance row. Given the agent's own file rather than the run's,
        the mode prints the same two stretches of work it prints when it walks
        the run, and their spans sum to well under the file's own.

        Red at `ab116d1e`: no row at all, and the page reads `0 segments found`."""
        path = own_file(resumed_segment)
        rows = segments_of(path)["rows"]
        assert [(row["slice"], row["slices"]) for row in rows] == [(1, 2), (2, 2)], rows
        assert sum(row["numbers"]["calls"] for row in rows) == plain_of(path)["calls"]
        spans = [row["numbers"]["span_s"] for row in rows]
        assert sum(spans) < plain_of(path)["span_s"] / 100, spans
        out = segment_report(path)
        assert "agent-crafter.jsonl  1/2" in out, out
        assert "agent-crafter.jsonl  2/2" in out, out
        assert "0 segments found" not in out, out

    def test_an_own_file_with_three_stretches_is_three_rows(self, tmp_path):
        """Two coordinator messages, each followed by work: three slices, and
        every call of the file lands in one of them."""
        path = write_run(
            tmp_path,
            call("a", 0, 10, "git status --short"),
            {
                "agent-crafter.jsonl": [
                    *worked(625, "s1"),
                    coordinator_message(9000),
                    *worked(9010, "s2"),
                    coordinator_message(20000),
                    *worked(20010, "s3"),
                    *worked(20030, "s4"),
                ]
            },
        )
        own = own_file(path)
        rows = segments_of(own)["rows"]
        assert [(row["slice"], row["slices"]) for row in rows] == [
            (1, 3),
            (2, 3),
            (3, 3),
        ], rows
        assert [row["numbers"]["calls"] for row in rows] == [1, 1, 2], rows
        assert sum(row["numbers"]["calls"] for row in rows) == plain_of(own)["calls"]

    def test_an_own_file_whose_messages_are_adjacent_invents_no_slice(self, tmp_path):
        """`test_two_coordinator_messages_in_a_row_do_not_invent_a_slice` on the
        own-file route: two messages and no work between them are two slices, and
        the header counts the messages apart from the slices."""
        path = write_run(
            tmp_path,
            call("a", 0, 10, "git status --short"),
            {
                "agent-crafter.jsonl": [
                    *worked(625, "s1"),
                    coordinator_message(9000),
                    coordinator_message(9005),
                    *worked(9010, "s2"),
                ]
            },
        )
        own = own_file(path)
        rows = segments_of(own)["rows"]
        assert [(row["slice"], row["slices"]) for row in rows] == [(1, 2), (2, 2)], rows
        out = " ".join(segment_report(own).split())
        assert "cut at 2 coordinator messages into 2 slices" in out, out
        assert "no paired call" not in out, out

    def test_either_route_prints_the_same_slices(self, resumed_segment):
        """The ticket's *the second must print the slices the third prints*, on a
        fixture. Walked from the run's transcript or given the agent's own file,
        each slice's span, calls, tools per turn, mean gap and tokens are the
        same; only the label differs, because only the run's transcript holds
        the spawn that names it."""

        def numbers(rows):
            # `kind` and `bar` are labels too (#640): derived from `agent`, so
            # the own file's rows carry `""` and None where the walk's carry the
            # spawn's kind, for the same reason `agent` differs.
            labels = ("agent", "description", "named", "transcript", "kind", "bar")
            return [{k: v for k, v in row.items() if k not in labels} for row in rows]

        walked = segments_of(resumed_segment)["rows"]
        own = segments_of(own_file(resumed_segment))["rows"]
        assert len(own) == 2, own
        assert numbers(own) == numbers(walked), (own, walked)

    def test_an_own_file_with_no_marker_keeps_the_empty_branch(self, tmp_path):
        """The ticket's *must not break*. An agent's file the coordinator never
        restarted has nothing to cut, and the directory it sits in is not the
        trigger: its reading is exactly what it was, wherever it lives.

        Green at the base; red under the mutant that slices every file under
        `subagents/` whatever its markers."""
        path = write_run(
            tmp_path,
            call("a", 0, 10, "git status --short"),
            {"agent-crafter.jsonl": [*worked(625, "s1"), *worked(640, "s2")]},
        )
        own = own_file(path)
        assert segments_of(own) == {
            "tolerance_s": 1.0,
            "transcripts": 0,
            "spawns": 0,
            "unnamed": 0,
            "unclaimed": 0,
            "rows": [],
        }
        elsewhere = tmp_path / "copied.jsonl"
        elsewhere.write_text(own.read_text(encoding="utf-8"), encoding="utf-8")
        out = segment_report(own)
        assert out.startswith(f"0 segments found beside {own}\n"), out
        assert out.replace(str(own), "<t>") == segment_report(elsewhere).replace(
            str(elsewhere), "<t>"
        )

    def test_an_own_file_page_says_what_its_rows_are(self, resumed_segment):
        """Nothing was joined, so the page does not print the join counts or a
        legend claiming a spawn named each row. It names the file, how many
        coordinator messages cut it and into how many slices.

        Red at the base, which printed the empty branch."""
        path = own_file(resumed_segment)
        out = " ".join(segment_report(path).split())
        assert (
            f"{path}: an agent's own transcript, cut at 1 coordinator message "
            "into 2 slices" in out
        ), out
        assert "No spawn was joined" in out, out
        assert "the same slices carry its name" in out, out
        for absent in (
            "named by nobody",
            "segment transcripts beside this one",
            "the parent could not name",
            "whose result this segment opened at",
        ):
            assert absent not in out, (absent, out)
        # What the walked page prints about a resumed file prints here too.
        assert "come from 1 segment the coordinator restarted" in out, out

    def test_a_spawn_inside_an_own_slice_is_named_without_a_reconciliation(
        self, tmp_path
    ):
        """The contract rule 6 list is exactly what an `Agent` call in an agent's own stretch
        of work exists to name. Its reconciliation against the files the parent
        could not name is not printed, because no parent is in view and a line
        saying the two counts disagree would send a reader after a child
        transcript nobody lost."""
        path = write_run(
            tmp_path,
            call("a", 0, 10, "git status --short"),
            {
                "agent-crafter.jsonl": [
                    *worked(625, "s1"),
                    coordinator_message(9000),
                    *worked(9010, "s2"),
                    *spawn("N", 9100, 9200, "general-purpose", "search the tree"),
                ]
            },
        )
        out = " ".join(segment_report(own_file(path)).split())
        assert "agent-crafter.jsonl 2/2 made 1 `Agent` call" in out, out
        assert "Contract rule 6 binds the agents this plugin spawns" in out, out
        assert "inside a segment, against" not in out, out
        assert "agree" not in out, out
        assert "One spawn arrives twice" not in out, out

    def test_an_own_files_json_carries_the_rows_the_page_prints(self, resumed_segment):
        """`measure_segments` is the one place rows come from, so `--json` gains
        them too. `unnamed` counts walked transcripts and the given file is not
        one, so it stays 0; `own_file` is the one key added, and only here."""
        segments = segments_of(own_file(resumed_segment))
        assert segments["own_file"] is True, segments
        assert (segments["transcripts"], segments["unnamed"]) == (0, 0), segments
        assert [row["transcript"] for row in segments["rows"]] == [
            "agent-crafter.jsonl"
        ] * 2, segments["rows"]
        assert not any(row["named"] for row in segments["rows"]), segments["rows"]
        assert "own_file" not in segments_of(resumed_segment), "walked run"

    def test_a_file_with_transcripts_beside_it_is_walked_whatever_its_markers(
        self, tmp_path
    ):
        """The walked route outranks the own-file one. A file carrying a
        coordinator message AND transcripts beside it is a run's, and its rows
        are the files it walks, joined to their spawns — not its own slices.

        Found by the mutation pass: dropping the nothing-beside condition kept
        every other case green, because no fixture's run transcript carried a
        marker."""
        main = [
            *call("a", 0, 10, "git status --short"),
            coordinator_message(15),
            *spawn("A", 25, 625, "agentic:crafter", "Build phase 1"),
        ]
        path = write_run(tmp_path, main, {"agent-crafter.jsonl": worked(625, "s1")})
        segments = segments_of(path)
        assert "own_file" not in segments, segments
        assert [row["agent"] for row in segments["rows"]] == ["agentic:crafter"], (
            segments
        )
        assert "an agent's own transcript" not in segment_report(path)

    def test_the_plain_reading_of_a_resumed_file_adds_one_line_and_moves_nothing(
        self,
        resumed_segment,
    ):
        """`analyse`'s docstring forbids changing what the plain reading prints,
        and #601's whole-transcript readings are what that reading of a resumed
        file produced. So it keeps every line and gains one, before the span that
        gets quoted, saying why that span is not one stretch of work.

        The rest is compared with the same file whose marker is reworded: the
        two differ in nothing the numbers read, so every line but the hint must
        match. Red at the base: no such line."""
        own = own_file(resumed_segment)
        out = run([str(own)]).stdout
        assert out.startswith("1 " + HINT.split(", so")[0]), out
        hint, rest = out.split("\n\n", 1)
        assert HINT in " ".join(hint.split()), out
        assert rest.startswith("span "), rest
        reworded = own.parent / "reworded.jsonl"
        reworded.write_text(
            own.read_text(encoding="utf-8").replace(
                "The coordinator sent a message", "Somebody wrote"
            ),
            encoding="utf-8",
        )
        assert run([str(reworded)]).stdout == rest

    def test_the_hint_counts_the_files_coordinator_messages(self, tmp_path):
        """The count is the file's messages and not its slices: two adjacent
        messages cut one file into two stretches, and the line says two."""
        path = write_run(
            tmp_path,
            call("a", 0, 10, "git status --short"),
            {
                "agent-crafter.jsonl": [
                    *worked(625, "s1"),
                    coordinator_message(9000),
                    coordinator_message(9005),
                    *worked(9010, "s2"),
                ]
            },
        )
        out = run([str(own_file(path))]).stdout
        assert out.startswith("2 coordinator messages in this transcript,"), out

    def test_no_hint_where_there_is_nothing_to_split(
        self, tmp_path, run_with_segments, transcript
    ):
        """The condition is the own-file mode's: a coordinator message, and no
        transcripts beside. A run's own transcript and a file nobody restarted
        print exactly what they did — and so does a run's transcript carrying a
        marker, because `--segments` walks that one rather than cutting it."""
        marked = tmp_path / "marked"
        marked.mkdir()
        walked = write_run(
            marked,
            [*call("a", 0, 10, "git status --short"), coordinator_message(15)],
            {"agent-crafter.jsonl": worked(625, "s1")},
        )
        for path in (
            run_with_segments,
            transcript,
            own_file(run_with_segments),
            walked,
        ):
            out = " ".join(run([str(path)]).stdout.split())
            assert "coordinator message in this transcript" not in out, (path, out)

    def test_no_hint_where_every_call_sits_in_one_stretch(self, tmp_path):
        """A coordinator message after the agent's last call cuts nothing: the
        window after it holds no call, so the file is one stretch, its span covers
        no wait, and `--segments` prints one slice with the same span. A line
        saying the span covers the waits between stretches is false there.

        Round 1's 🟡 1. Red at 7b4162fd: the hint printed, then `span 0.3m`."""
        path = write_run(
            tmp_path,
            call("a", 0, 10, "git status --short"),
            {
                "agent-crafter.jsonl": [
                    *worked(625, "s1"),
                    *worked(640, "s2"),
                    coordinator_message(9000),
                ]
            },
        )
        out = " ".join(run([str(own_file(path))]).stdout.split())
        assert "coordinator message in this transcript" not in out, out
        assert out.startswith("span "), out

    def test_no_hint_where_the_only_message_precedes_the_first_call(self, tmp_path):
        """The other shape that cuts nothing: a coordinator message before the
        agent's first call leaves every call in the window after it, so the file
        is one stretch and `--segments` prints one slice with the same span. The
        one-stretch case above builds only the message after the last call, and
        a condition of *a call after the first message* is right there and wrong
        here."""
        path = write_run(
            tmp_path,
            call("a", 0, 10, "git status --short"),
            {
                "agent-crafter.jsonl": [
                    coordinator_message(600),
                    *worked(625, "s1"),
                    *worked(640, "s2"),
                ]
            },
        )
        out = " ".join(run([str(own_file(path))]).stdout.split())
        assert "coordinator message in this transcript" not in out, out
        assert out.startswith("span "), out

    def test_a_resumed_file_copied_out_of_subagents_is_still_cut(
        self, resumed_segment, tmp_path
    ):
        """In 1: the trigger is the marker, never the directory. A resumed
        agent's file copied anywhere else is cut the same way, and its plain
        reading carries the same line. Every other own-file case sits under
        `subagents/`, so a directory condition added to either trigger kept them
        all green (round 1's ⬜ 2)."""
        copied = tmp_path / "copied-agent.jsonl"
        copied.write_text(
            own_file(resumed_segment).read_text(encoding="utf-8"), encoding="utf-8"
        )
        rows = segments_of(copied)["rows"]
        assert [(row["slice"], row["slices"]) for row in rows] == [(1, 2), (2, 2)], rows
        assert segments_of(copied)["own_file"] is True
        out = run([str(copied)]).stdout
        assert out.startswith("1 coordinator message in this transcript,"), out

    # --- A5: the reading is the orchestrator's, and the command refuses without it

    def test_post_without_says_refuses_and_says_where_the_reading_comes_from(
        self, monkeypatch, capsys, tmp_path
    ):
        """A5. `parser.error` exits 2, and the message names both ways in: a file
        and `-`. The refusal has to carry that, because the whole point is that
        the command will not write the sentence itself."""
        module = _cost()
        seen = _gh(monkeypatch, module)
        monkeypatch.setattr(
            module.sys, "argv", ["session_cost.py", "x.jsonl", "--post"]
        )
        with pytest.raises(SystemExit) as exit_info:
            module.main()
        assert exit_info.value.code == 2
        said = capsys.readouterr().err
        assert "--says" in said
        assert "stdin" in said and "invented" in said
        assert seen == [], "nothing may be looked up before the refusal"

    def test_refuses_post_with_json(self, monkeypatch, capsys):
        """The two ask for different things — one posts, one prints for a program
        — and silently preferring either is a reading somebody does not get."""
        module = _cost()
        monkeypatch.setattr(
            module.sys,
            "argv",
            ["session_cost.py", "x.jsonl", "--post", "--says", "-", "--json"],
        )
        with pytest.raises(SystemExit) as exit_info:
            module.main()
        assert exit_info.value.code == 2
        assert "separately" in capsys.readouterr().err

    def test_refuses_the_printed_segment_report_under_json(self, run_with_segments):
        """`--json` is read by a program, and `--segments` beside it asks for the
        rows inside that reading. The printed page there is text the program
        cannot parse."""
        proc = run(["--segments", "--json", str(run_with_segments)])
        assert proc.returncode == 0, proc.stderr
        rows = json.loads(proc.stdout)["segments"]["rows"]
        assert [row["agent"] for row in rows] == [
            "agentic:crafter",
            "agentic:proofer",
        ], rows


class Test_emit:
    """The `--post` cases run through `main`, where `emit` decides between
    printing a reading and posting it. Their `transcript` is the class's
    own, the one paired call they were written over, from
    `tests/test_session_cost_post.py`."""

    @pytest.fixture
    def transcript(self, tmp_path):
        """The smallest transcript with a paired call in it, built the way
        `tests/skills/test_session_cost.py` builds its own."""
        path = tmp_path / "t.jsonl"
        path.write_text(
            "\n".join(
                [
                    _row(
                        0,
                        {
                            "type": "tool_use",
                            "id": "a",
                            "name": "Bash",
                            "input": {"command": "pytest tests -q"},
                        },
                    ),
                    _row(10, {"type": "tool_result", "tool_use_id": "a"}),
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        return path

    def test_accepts_a_reading_and_posts_the_report_it_would_have_printed(
        self, monkeypatch, capsys, tmp_path, transcript
    ):
        """`emit` is the seam between printing a reading and posting it, and the
        body has to carry the same text either way. A mode that posted an empty
        body would look identical in every argv assertion above."""
        module = _cost()
        says = tmp_path / "says.md"
        says.write_text("one call, ten seconds of it\n", encoding="utf-8")
        seen = _gh(monkeypatch, module, listing=_listing((42, "OPEN")))
        bodies = {}
        stub = module.run_gh

        def capture(args):
            if args[:2] == ["issue", "comment"]:
                with open(
                    args[args.index("--body-file") + 1], encoding="utf-8"
                ) as handle:
                    bodies["text"] = handle.read()
            return stub(args)

        monkeypatch.setattr(module, "run_gh", capture)
        monkeypatch.setattr(
            module.sys,
            "argv",
            ["session_cost.py", str(transcript), "--post", "--says", str(says)],
        )
        assert module.main() == 0
        assert _posted(seen)[0][2] == "42"
        assert "one call, ten seconds of it" in bodies["text"]
        # The report's own words, so the body is the reading rather than an empty
        # fence with the sentence above it.
        assert "command" in bodies["text"]
        printed = capsys.readouterr().out
        assert "posted the segment's reading to #42" in printed

    def test_the_posted_body_does_not_carry_the_transcripts_path(
        self, monkeypatch, tmp_path, transcript
    ):
        """Round 1's 🔴. `--post` writes into an issue tracker and a transcript
        path lives under the user's home directory, carrying the account name
        twice and the session id once. The report prints it; the body must not.

        The branch that leaks is the documented one: `report_segments`' empty
        branch fires whenever the named transcript has no subagents beside it,
        which is every segment measured on its own that the coordinator never
        restarted — the case
        `skills/verify/orchestration.md` *Measure the segment, and feed the flow
        log* is written for.
        """
        module = _cost()
        says = tmp_path / "says.md"
        says.write_text("one call, ten seconds of it\n", encoding="utf-8")
        _gh(monkeypatch, module, listing=_listing((42, "OPEN")))
        bodies = {}
        stub = module.run_gh

        def capture(args):
            if args[:2] == ["issue", "comment"]:
                with open(
                    args[args.index("--body-file") + 1], encoding="utf-8"
                ) as handle:
                    bodies["text"] = handle.read()
            return stub(args)

        monkeypatch.setattr(module, "run_gh", capture)
        monkeypatch.setattr(
            module.sys,
            "argv",
            [
                "session_cost.py",
                str(transcript),
                "--segments",
                "--post",
                "--says",
                str(says),
            ],
        )
        assert module.main() == 0
        assert str(transcript) not in bodies["text"]
        assert os.path.dirname(str(transcript)) not in bodies["text"]
        # The basename stays, because a reading that names no file is a reading
        # nobody can place.
        assert os.path.basename(str(transcript)) in bodies["text"]

    def test_an_own_files_posted_body_does_not_carry_its_path(
        self, monkeypatch, tmp_path
    ):
        """#637. A resumed agent's own file now prints its slices instead of the
        empty branch, under a header that names the file. That header reaches the
        body through `emit` like every other line, so the body carries the
        basename and neither the path nor the directories above it."""
        marker = json.dumps(
            {
                "timestamp": "2026-09-22T00:30:00.000Z",
                "type": "user",
                "isMeta": True,
                "message": {
                    "role": "user",
                    "content": "The coordinator sent a message while you were "
                    "working: fix round 1",
                },
            }
        )
        lines = []
        for uid, second in (("a", 0), ("b", 1900)):
            lines.append(
                _row(
                    second,
                    {
                        "type": "tool_use",
                        "id": uid,
                        "name": "Bash",
                        "input": {"command": "pytest tests -q"},
                    },
                )
            )
            lines.append(_row(second + 5, {"type": "tool_result", "tool_use_id": uid}))
        lines.insert(2, marker)
        own = tmp_path / "main" / "subagents" / "agent-x.jsonl"
        own.parent.mkdir(parents=True)
        own.write_text("\n".join(lines) + "\n", encoding="utf-8")
        module = _cost()
        says = tmp_path / "says.md"
        says.write_text("two stretches of work\n", encoding="utf-8")
        _gh(monkeypatch, module, listing=_listing((42, "OPEN")))
        bodies = {}
        stub = module.run_gh

        def capture(args):
            if args[:2] == ["issue", "comment"]:
                with open(
                    args[args.index("--body-file") + 1], encoding="utf-8"
                ) as handle:
                    bodies["text"] = handle.read()
            return stub(args)

        monkeypatch.setattr(module, "run_gh", capture)
        monkeypatch.setattr(
            module.sys,
            "argv",
            ["session_cost.py", str(own), "--segments", "--post", "--says", str(says)],
        )
        assert module.main() == 0
        # The own-file page, not the empty branch that carried the path before.
        assert "an agent's own transcript" in bodies["text"], bodies["text"]
        assert str(own) not in bodies["text"]
        assert str(own.parent) not in bodies["text"]
        assert "agent-x.jsonl" in bodies["text"]

    def test_the_spawns_report_leaks_no_path_either(
        self, monkeypatch, tmp_path, transcript
    ):
        """The same empty branch, one report over. `report_spawns` prints
        `0 spawns found in {path}` and reaches the body through the same seam, so
        fixing one call site and not the other is the shape the finding is about:
        the rule was already in the file and applied in one place of three."""
        module = _cost()
        says = tmp_path / "says.md"
        says.write_text("no spawns in this one\n", encoding="utf-8")
        _gh(monkeypatch, module, listing=_listing((42, "OPEN")))
        bodies = {}
        stub = module.run_gh

        def capture(args):
            if args[:2] == ["issue", "comment"]:
                with open(
                    args[args.index("--body-file") + 1], encoding="utf-8"
                ) as handle:
                    bodies["text"] = handle.read()
            return stub(args)

        monkeypatch.setattr(module, "run_gh", capture)
        monkeypatch.setattr(
            module.sys,
            "argv",
            [
                "session_cost.py",
                str(transcript),
                "--spawns",
                "--post",
                "--says",
                str(says),
            ],
        )
        assert module.main() == 0
        assert os.path.dirname(str(transcript)) not in bodies["text"]

    def test_refuses_an_empty_reading_rather_than_posting_it(
        self, monkeypatch, capsys, tmp_path, transcript
    ):
        """Round 1's second finding. The invariant is that the numbers are the
        script's and the sentence is not, and `frame/design.md` *Scope* states it as *it
        refuses to post without a reading* — not without the flag. Enforced
        against the missing flag alone, a `--says` naming an empty file posts a
        fence with nothing above it, which is the shape a session reaches by
        accident with `--says -` and nothing piped in."""
        module = _cost()
        says = tmp_path / "empty.md"
        says.write_text("   \n", encoding="utf-8")
        seen = _gh(monkeypatch, module, listing=_listing((42, "OPEN")))
        monkeypatch.setattr(
            module.sys,
            "argv",
            ["session_cost.py", str(transcript), "--post", "--says", str(says)],
        )
        assert module.main() == 1
        assert _posted(seen) == [] and _opened(seen) == []
        assert "no reading" in capsys.readouterr().out

    def test_an_empty_reading_is_refused_before_the_log_is_looked_up(
        self, monkeypatch, tmp_path, transcript
    ):
        """The refusal is about what the session supplied, so it does not depend
        on the tracker answering. Checked at the seam rather than by reading the
        message: nothing reaches `gh` at all."""
        module = _cost()
        says = tmp_path / "empty.md"
        says.write_text("\n\n", encoding="utf-8")
        seen = _gh(monkeypatch, module, listing=_listing((42, "OPEN")))
        monkeypatch.setattr(
            module.sys,
            "argv",
            ["session_cost.py", str(transcript), "--post", "--says", str(says)],
        )
        assert module.main() == 1
        assert seen == [], seen

    def test_main_without_post_still_prints_the_report(
        self, monkeypatch, capsys, transcript
    ):
        """The refactor that made `--post` possible must leave the printing path
        exactly where it was: every reading this script takes now runs through
        `emit`."""
        module = _cost()
        monkeypatch.setattr(module.sys, "argv", ["session_cost.py", str(transcript)])
        assert module.main() == 0
        assert "command" in capsys.readouterr().out

    def test_refuses_to_post_the_absolute_spelling_of_a_path_given_relative(
        self, monkeypatch, tmp_path
    ):
        """A path given relative has an absolute spelling too, and a line
        printing that spelling carries every directory above the file. `emit`
        replaces both spellings of the one path, the longer first."""
        module = _cost()
        monkeypatch.chdir(tmp_path)
        given = os.path.join("runs", "t.jsonl")
        says = tmp_path / "says.md"
        says.write_text("a reading\n", encoding="utf-8")
        posted = {}

        def post(body, said, label):
            posted["body"] = body
            return 0

        monkeypatch.setattr(module, "post", post)
        args = module.argparse.Namespace(
            post=True, says=str(says), label=module.ROLLING_LABEL
        )

        def render():
            print(f"# {os.path.abspath(given)}")

        assert module.emit(args, render, given) == 0
        assert os.getcwd() not in posted["body"], posted
        assert "t.jsonl" in posted["body"], posted


class Test_post:
    # --- A6: a repository that never made the log is the expected case ------------

    def test_no_history_posts_nothing_and_does_not_fail(self, monkeypatch, capsys):
        """A6. Measured 2026-09-22 (`questions.md` Q1): the lookup exits 0 with
        empty output where the label exists nowhere. Most installed repositories
        are in that state, so a command that went red here would be red for
        following the document beside it."""
        module = _cost()
        seen = _gh(monkeypatch, module, listing="[]")
        code = module.post("the reading", "what it says", "flow-measurement")
        assert code == 0
        said = capsys.readouterr().out
        assert "does not run that log" in said
        assert _posted(seen) == [] and _opened(seen) == []

    def test_an_unreadable_lookup_is_a_no_op_and_never_a_post(
        self, monkeypatch, capsys
    ):
        """A non-zero exit is a lookup that FAILED, which is a different fact
        from an absent label — and `plan.md`'s failure direction says a wrong
        guess must cost a refusal and never a wrong post."""
        module = _cost()
        seen = _gh(
            monkeypatch, module, list_code=1, stderr="could not resolve to a Repository"
        )
        code = module.post("the reading", "what it says", "flow-measurement")
        assert code == 0
        said = capsys.readouterr().out
        assert "could not run" in said and "could not resolve" in said
        assert _posted(seen) == [] and _opened(seen) == []

    def test_gh_missing_from_path_is_the_same_no_op(self, monkeypatch, capsys):
        """`run_gh` answers `None` for a `gh` that is not installed, which the
        caller must not read as the exit code 0 that `None` is not."""
        module = _cost()
        seen = _gh(monkeypatch, module, list_code=None, stderr="no gh")
        assert module.post("r", "s", "flow-measurement") == 0
        assert "not on PATH" in capsys.readouterr().out
        assert _posted(seen) == [] and _opened(seen) == []

    # --- A7: a closed log is named, never reopened --------------------------------

    def test_a_closed_log_is_named_and_nothing_is_opened(self, monkeypatch, capsys):
        """A7. Opening one is not a session's act: two sessions finishing
        segments at once both read zero and both create, and the next release
        fails on two or more."""
        module = _cost()
        seen = _gh(
            monkeypatch, module, listing=_listing((41, "CLOSED"), (40, "CLOSED"))
        )
        code = module.post("the reading", "what it says", "flow-measurement")
        assert code == 1
        said = capsys.readouterr().out
        assert "nothing is open" in said
        assert "not a session's act" in said
        assert _opened(seen) == [], "a closed log must never be reopened"
        assert _posted(seen) == []

    # --- A8: a broken invariant is named, not guessed past ------------------------

    def test_refuses_to_post_where_more_than_one_log_is_open(self, monkeypatch, capsys):
        """A8. Both numbers in the message, because picking the current log is
        what a person does next."""
        module = _cost()
        seen = _gh(
            monkeypatch,
            module,
            listing=_listing((42, "OPEN"), (41, "OPEN"), (40, "CLOSED")),
        )
        code = module.post("the reading", "what it says", "flow-measurement")
        assert code == 1
        said = capsys.readouterr().out
        assert "#41" in said and "#42" in said
        assert "exactly one may" in said
        assert _posted(seen) == [] and _opened(seen) == []

    # --- A9: exactly one open posts once ------------------------------------------

    def test_accepts_one_open_log_and_posts_once_to_it(self, monkeypatch, capsys):
        """A9. The argv is asserted, not just the exit: what makes this mode
        worth having is that the command is composed the same way every time."""
        module = _cost()
        seen = _gh(monkeypatch, module, listing=_listing((42, "OPEN"), (41, "CLOSED")))
        bodies = {}
        real = module.run_gh

        def capture(args):
            if args[:2] == ["issue", "comment"]:
                with open(
                    args[args.index("--body-file") + 1], encoding="utf-8"
                ) as handle:
                    bodies["text"] = handle.read()
            return real(args)

        monkeypatch.setattr(module, "run_gh", capture)
        code = module.post(
            "span 19m, 99 calls", "the rounds ran long", "flow-measurement"
        )
        assert code == 0
        posted = _posted(seen)
        assert len(posted) == 1, posted
        assert posted[0][:3] == ["issue", "comment", "42"]
        assert "--body-file" in posted[0]
        assert _opened(seen) == []
        assert "posted the segment's reading to #42" in capsys.readouterr().out
        assert "the rounds ran long" in bodies["text"]
        assert "span 19m, 99 calls" in bodies["text"]

    def test_the_body_file_is_removed_after_the_post(self, monkeypatch):
        """A temp file per segment boundary, left behind, is the leaving
        contract rule 7 is about — and this one is the command's, not a
        probe's, so nothing else would ever clean it."""
        module = _cost()
        paths = []
        seen = _gh(monkeypatch, module, listing=_listing((42, "OPEN")))
        real = module.run_gh

        def capture(args):
            if args[:2] == ["issue", "comment"]:
                paths.append(args[args.index("--body-file") + 1])
            return real(args)

        monkeypatch.setattr(module, "run_gh", capture)
        module.post("r", "s", "flow-measurement")
        assert paths and not os.path.exists(paths[0])
        assert seen

    def test_a_comment_that_fails_to_post_is_named_and_fails(self, monkeypatch, capsys):
        """The one state where the log was found and the write did not land.
        Silently exiting 0 there is the counterfeit: the reading is gone and the
        log looks fed."""
        module = _cost()
        _gh(
            monkeypatch,
            module,
            listing=_listing((42, "OPEN")),
            comment_code=1,
            stderr="HTTP 403",
        )
        assert module.post("r", "s", "flow-measurement") == 1
        assert "was not posted" in capsys.readouterr().out

    def test_the_durable_log_is_reachable_under_its_own_label(
        self, monkeypatch, capsys
    ):
        """`skills/verify/SKILL.md` names two logs and says a cross-version
        reading posted to the rolling one is scheduled for deletion. One flag is
        what keeps the durable one reachable with the same code."""
        module = _cost()
        seen = _gh(monkeypatch, module, listing=_listing((7, "OPEN")))
        assert module.post("r", "s", "flow-baseline") == 0
        assert seen[0][seen[0].index("--label") + 1] == "flow-baseline"
        assert _posted(seen)[0][2] == "7"

    def test_unreadable_json_is_a_no_op_rather_than_a_crash(self, monkeypatch, capsys):
        """`gh` answering something that is not the JSON it was asked for is a
        lookup that did not work, and it takes the same exit as one that failed
        outright."""
        module = _cost()
        seen = _gh(monkeypatch, module, listing="not json at all")
        assert module.post("r", "s", "flow-measurement") == 0
        assert "could not run" in capsys.readouterr().out
        assert _posted(seen) == [] and _opened(seen) == []

    def test_no_state_ever_opens_an_issue(self, monkeypatch):
        """The property, over every state rather than in the one case about it.
        A command that opened a log would break the invariant from the other
        side, which is the failure the skill names."""
        module = _cost()
        for listing in (
            "[]",
            _listing((1, "CLOSED")),
            _listing((1, "OPEN")),
            _listing((1, "OPEN"), (2, "OPEN")),
        ):
            seen = _gh(monkeypatch, module, listing=listing)
            module.post("r", "s", "flow-measurement")
            assert _opened(seen) == [], listing


class Test_newest:
    @staticmethod
    def project_of(module, directory):
        """Where `~/.claude/projects` keeps DIRECTORY's transcripts, by the slug
        rule `newest` states: every character that is not a letter, a digit or
        a hyphen of the absolute path becomes a hyphen."""
        slug = re.sub(r"[^A-Za-z0-9-]", "-", os.path.abspath(directory))
        return os.path.join(module.PROJECTS, slug)

    def test_accepts_the_latest_transcript_under_a_directorys_project(
        self, monkeypatch, tmp_path
    ):
        """`--latest` reads the transcript written last under the directory's
        project, a segment's nested one included. The projects root is moved
        under the case, so no home directory is read."""
        module = load_script()
        monkeypatch.setattr(module, "PROJECTS", str(tmp_path / "projects"))
        work = tmp_path / "work"
        work.mkdir()
        project = self.project_of(module, work)
        older = os.path.join(project, "a.jsonl")
        newer = os.path.join(project, "a", "subagents", "agent-b.jsonl")
        for offset, path in enumerate((older, newer)):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as handle:
                handle.write("{}\n")
            os.utime(path, (1_000_000 + offset, 1_000_000 + offset))
        assert module.newest(str(work)) == newer

    def test_refuses_a_directory_with_no_project_or_no_transcript(
        self, monkeypatch, tmp_path
    ):
        module = load_script()
        monkeypatch.setattr(module, "PROJECTS", str(tmp_path / "projects"))
        work = tmp_path / "work"
        work.mkdir()
        assert module.newest(str(work)) is None
        os.makedirs(self.project_of(module, work))
        assert module.newest(str(work)) is None


class Test_report_segments:
    def test_accepts_a_run_whose_segments_are_all_named_with_no_word_on_the_unnamed(
        self, run_with_segments
    ):
        out = " ".join(segment_report(run_with_segments).split())
        assert "0 segments named by nobody" in out, out
        assert "A segment named by nobody carries" not in out, out

    def test_refuses_to_print_an_unnamed_segment_without_saying_why_it_has_no_name(
        self, segment_that_spawned
    ):
        """A row labelled by its path and not by an agent reads as a defect of
        the page unless the page says the two ways a segment goes unnamed."""
        out = " ".join(segment_report(segment_that_spawned).split())
        assert "1 segment named by nobody" in out, out
        assert (
            "A segment named by nobody carries its transcript's path instead" in out
        ), out


class Test_report_breaches:
    def test_accepts_a_run_with_no_spawn_and_no_unnamed_segment_as_nothing_to_say(
        self, capsys
    ):
        load_script().report_breaches({"rows": [{"spawns": 0}], "unnamed": 0})
        assert capsys.readouterr().out == ""

    def test_refuses_to_stay_silent_where_a_segment_is_unnamed_and_nothing_spawned(
        self, capsys
    ):
        """One spawn arrives twice, so a transcript the parent could not name
        in a run where no segment made an `Agent` call is two counts that
        disagree, and the page says so."""
        load_script().report_breaches({"rows": [{"spawns": 0}], "unnamed": 1})
        out = " ".join(capsys.readouterr().out.split())
        assert (
            "0 `Agent` calls inside a segment, against 1 segment the parent could "
            "not name, and the two do not agree." in out
        ), out


class Test_report:
    @staticmethod
    def two_turns_of_two(tmp_path, second_check):
        """The plain reading of two turns that each send two calls, a ratio of
        2.00, with `pytest -q` first and SECOND_CHECK in the second turn."""
        lines = [
            message(
                0,
                [use("a", "pytest -q"), use("b", "git status --short")],
                message_id="m1",
            ),
            plain_result(10, "a"),
            plain_result(10, "b"),
            message(
                15,
                [use("c", second_check), use("d", "git log --oneline -5")],
                message_id="m2",
            ),
            plain_result(20, "c"),
            plain_result(20, "d"),
        ]
        path = tmp_path / "t.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        proc = run([str(path)])
        assert proc.returncode == 0, proc.stderr
        return proc.stdout

    def test_accepts_a_batched_run_with_no_repeat_as_nothing_obvious(self, tmp_path):
        out = self.two_turns_of_two(tmp_path, "ruff check .")
        assert "nothing obvious" in out, out
        assert "repeats" not in out, out

    def test_refuses_nothing_obvious_beside_a_repeat(self, tmp_path):
        """The ratio clears the batching advisory, and a check re-run for a
        result already in hand is still time that could go elsewhere, so the
        page names it and does not also say nothing is obvious."""
        out = self.two_turns_of_two(tmp_path, "pytest -q")
        assert "repeats" in out, out
        assert "nothing obvious" not in out, out


class Test_resume_cuts:
    def test_accepts_the_coordinators_message_as_a_cut(self, tmp_path):
        module = load_script()
        path = tmp_path / "agent.jsonl"
        path.write_text(coordinator_message(9000) + "\n", encoding="utf-8")
        assert module.resume_cuts(str(path)) == [module.parse_time(stamp_at(9000))]

    def test_refuses_the_coordinators_words_on_a_row_the_harness_did_not_mark(
        self, tmp_path
    ):
        """The harness marks the row it writes with `isMeta`. The same words on
        an unmarked user row are somebody quoting the sentence, and cutting
        there would split one stretch of work in two."""
        row = json.loads(coordinator_message(9000))
        del row["isMeta"]
        path = tmp_path / "agent.jsonl"
        path.write_text(json.dumps(row) + "\n", encoding="utf-8")
        assert load_script().resume_cuts(str(path)) == []


class Test_subagent_transcripts:
    def test_accepts_every_transcript_under_subagents_nested_ones_included(
        self, tmp_path
    ):
        path = write_run(tmp_path, ["{}"], {"agent-a.jsonl": ["{}"]})
        nested = tmp_path / "main" / "subagents" / "deeper" / "agent-b.jsonl"
        nested.parent.mkdir()
        nested.write_text("{}\n", encoding="utf-8")
        assert load_script().subagent_transcripts(str(path)) == sorted(
            [str(tmp_path / "main" / "subagents" / "agent-a.jsonl"), str(nested)]
        )

    def test_refuses_a_transcript_beside_subagents_rather_than_in_it(self, tmp_path):
        path = write_run(tmp_path, ["{}"], {"agent-a.jsonl": ["{}"]})
        (tmp_path / "main" / "stray.jsonl").write_text("{}\n", encoding="utf-8")
        assert load_script().subagent_transcripts(str(path)) == [
            str(tmp_path / "main" / "subagents" / "agent-a.jsonl")
        ]


class Test_token_thirds:
    def test_accepts_three_inputs_as_one_mean_each(self):
        turns = [("t1", 10), ("t2", 20), ("t3", 30)]
        assert load_script().token_thirds(turns) == [10, 20, 30]

    def test_refuses_two_inputs_as_too_few_for_thirds(self):
        assert load_script().token_thirds([("t1", 10), ("t2", 20)]) == []


class Test_analyse:
    def test_accepts_a_model_gap_under_fifteen_minutes(self, tmp_path):
        lines = call("a", 0, 10, "git status --short")
        lines += call("b", 909, 910, "git log --oneline -5")
        assert batch_data(tmp_path, lines)["model_s"] == 899

    def test_refuses_a_model_gap_of_fifteen_minutes_or_more(self, tmp_path):
        """A gap that long is a wait, not the model thinking: `resume_cuts`
        and `report_segments` both rest on the walk dropping it."""
        lines = call("a", 0, 10, "git status --short")
        lines += call("b", 910, 911, "git log --oneline -5")
        assert batch_data(tmp_path, lines)["model_s"] == 0

    def test_refuses_an_unnamed_command_run_twice_as_a_repeat(self, tmp_path):
        """The repeats figures keep the families whose second run produces a
        result already in hand. A command no family names may change the world
        each time it runs."""
        lines = call("a", 0, 10, "terraform apply")
        lines += call("b", 15, 25, "terraform apply")
        data = batch_data(tmp_path, lines)
        assert data["by_family"]["other"]["calls"] == 2, data["by_family"]
        assert (data["repeat_exact_s"], data["repeat_same_work_s"]) == (0, 0)


class Test_load:
    def test_accepts_a_stamped_call_as_one_call_and_one_turn(self, tmp_path):
        path = tmp_path / "t.jsonl"
        path.write_text("\n".join(call("a", 0, 10, "pytest -q")) + "\n", "utf-8")
        calls, turns = load_script().load(str(path))
        assert [c["command"] for c in calls] == ["pytest -q"]
        assert len(turns) == 1

    def test_refuses_a_row_with_no_timestamp_as_a_turn(self, tmp_path):
        row = json.loads(turn(0, use("a", "pytest -q")))
        del row["timestamp"]
        path = tmp_path / "t.jsonl"
        lines = [json.dumps(row), *call("b", 20, 30, "git status --short")]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        calls, turns = load_script().load(str(path))
        assert [c["command"] for c in calls] == ["git status --short"]
        assert len(turns) == 1, turns


class Test_count:
    def test_accepts_a_finite_number_as_itself(self):
        module = load_script()
        assert [module.count(value) for value in (0, 12, 2.5)] == [0, 12, 2.5]

    def test_refuses_a_non_finite_float_as_zero(self):
        module = load_script()
        for value in (math.nan, math.inf, -math.inf):
            assert module.count(value) == 0, value


class Test_family:
    # --- #200: the family names the runner a repository actually uses -----------

    def test_accepts_a_runner_named_by_path_as_a_test_run(self, tmp_path):
        """A project that ships `bin/test` has said what its test command is, in
        the filesystem, and the five names the family knew did not include it.

        Measured over the 180 transcripts on the machine that found it: of the
        `./bin/test` calls, 266 were charged to `other` — the row nobody reads
        because it is the row everything falls into — and the rest landed in four
        different families depending on what else shared the command line.

        The negative arm is the same size as the positive one on purpose. A
        pattern widened until the row is never empty is a row that means nothing,
        so a directory called `testdata`, a `git log` mentioning the word, and a
        lint run that shares a line with none of them must all stay out."""
        module = load_script()
        for command in (
            "./bin/test",
            "bin/test -q",
            "scripts/test",
            "scripts/test.sh --fast",
            "./test.sh",
            "make test",
            "npm test",
            "npm run test",
            "pnpm run test -- --watch=false",
            "./gradlew test",
            "just test",
            "tox -e py312",
            "nox -s tests",
            "rspec spec/models",
            "phpunit --testsuite unit",
            "dotnet test",
            "bun test",
            "deno test -A",
            "uv run --with pytest pytest tests/ -q",
        ):
            assert module.family(command) == "test", command

        for command in (
            "bin/testdata --list",
            "git log --oneline -- test",
            "uvx ruff check .",
            "./bin/evidence-check",
            "python3 .github/scripts/rider_check.py",
            "cat tests/skills/test_session_cost.py",
        ):
            assert module.family(command) != "test", command

    def test_a_runner_named_inside_a_heredoc_is_not_a_run_of_it(self, tmp_path):
        """The other half of #200's *wrong in both directions*, in the same
        reading: the one call the family did charge to `test` was a `cat > …`
        heredoc whose body contains the word `pytest`.

        These commands are flat, the shape `load`'s `command` has, so none has a
        closing line and each is cut from the heredoc operator to the end. That
        answers it for every family at once and needs no list of the words a
        document might contain. A command with its newlines kept has its body
        removed to the closing line instead, and the case after this one's #377
        cases pins that.

        The last two are the bound. A `<<` followed by a lowercase unquoted word
        is more often a quoted comparison than a heredoc, so it is left alone:
        charging a real run to `other` is the error this whole change exists to
        remove, and a lowercase heredoc delimiter classified the way it is today
        is the smaller of the two."""
        module = load_script()
        for command in (
            "cat > x.py <<'EOF' import pytest EOF",
            "cat > x.py <<EOF import pytest EOF",
            'cat > q.sql <<-"SQL" select 1 from pytest SQL',
            "python3 - <<'PY' subprocess.run(['pytest']) PY",
        ):
            assert module.family(command) == "other", command

        assert module.family("echo 'a << b' && pytest -q") == "test"
        assert module.family("cat > x <<eof pytest eof") == "test"

    # --- #377: `git` is a command word, not a position ---
    #
    # The `git` family was the one pattern anchored at the start of the line, so a
    # `git` or `gh` call after `cd … &&` -- the shape nearly every worktree session
    # writes -- was charged to `other`. Measured over 353 transcripts on one
    # machine, 2026-09-28: 2,734 calls and 21,147 seconds in that shape alone.

    def test_a_git_call_after_cd_is_charged_to_git(self):
        """The finding's own instance, and the shapes #619's segment readings
        printed. The two after them are the control: a line that runs no `git`
        must not become one because a `cd` precedes it.

        The loop that only reads was `other` here until #642 gave reading a
        family of its own, and it is `read` now. The `python3 -` heredoc stays
        `other`: the owner answered that a script handed to an interpreter gets
        no family, because a row counting it would move whenever agents switch
        between the `Edit` tool and a shell edit."""
        module = load_script()
        for command in (
            "cd /x && git status",
            "cd /x && gh issue view 1",
            "cd /w; gh issue view 616 --json title",
            "W=/w; cd $W; git grep -n x",
            "cd /w && git -C /w grep x",
            "git -C /w commit -q -F - <<'EOF'\ndocs: x\nEOF",
        ):
            assert module.family(command) == "git", command

        assert (
            module.family("W=/w; cd $W; for f in a b; do grep -c x $f; done") == "read"
        )
        assert module.family("cd ~/p && python3 - <<'EOF'\nimport json\nEOF") == "other"

    def test_git_is_read_at_every_command_word(self):
        """A command word is the first word after any separator, a subshell's
        `(`, a reserved word or a leading assignment -- not only after `&&`. A
        rule that knew the separators and not the reserved words would still
        charge a loop over issues to `other`."""
        module = load_script()
        for command in (
            "for n in 1 2; do gh issue view $n; done",
            "if git diff --quiet; then echo y; fi",
            "FOO=1 git status",
            "(cd /x && git status)",
            "(gh pr view 1)",
            "cat x | git apply",
            "/usr/bin/git status",
            "ls || gh pr list",
            "sleep 1 & git fetch",
            "while ! git pull; do sleep 1; done",
            "{ gh pr view 1; }",
            "time git log -1",
        ):
            assert module.family(command) == "git", command

    def test_refuses_git_named_anywhere_but_a_command_word(self):
        """The other direction, and the one the anchor was buying. Un-anchoring
        the pattern to a bare word boundary would charge every one of these to
        `git`: a search for the word, a path through a `.git/` directory, a
        message naming it, a quoted separator, a command substitution and a
        wrapper. The last two are the rule's stated bounds, not oversights."""
        module = load_script()
        for command in (
            'grep -rn "git" .',
            "ls /a/git/b",
            'x --message "git"',
            "cat .git/config",
            "echo git",
            "rg gh docs/",
            "echo 'a; git b'",
            "cd $(git rev-parse --show-toplevel) && ls",
            'echo "$(git log -1)"',
            "x=$(git log -1) ; ls",
            "diff <(git show HEAD:a) a",
            "timeout 40 gh issue list",
            "echo ';' git x",
            'echo "&&" git x',
            "echo \\; git x",
        ):
            assert module.family(command) != "git", command

    def test_a_line_running_two_families_is_charged_by_their_order(self):
        """`FAMILIES` is first-match in priority order and `read` is last, so a
        compound that runs a test is charged to the test. Reading `git` by
        command word must not jump it ahead of the families it follows.

        `read` is judged after all four (#642), so a line that reads and runs a
        `git` is `git`, and a search naming a runner keeps the family it has had
        since 0.9.4: `grep -rn pytest` is `test`. That is the mirror #377
        recorded as out of scope, and #642 lists keeping it as what must not
        break. A rule judging `read` first turns the two searches red. The lines
        that also run `git` or `ruff` would keep their family even then, because
        a line running either is not `read` at all."""
        module = load_script()
        assert module.family("cd x && git add . && pytest -q") == "test"
        assert module.family("git stash && ruff check .") == "lint/type"
        assert module.family("ls && git status") == "git"
        assert module.family("grep -rn pytest docs/") == "test"
        assert module.family("cat tests/x/test.sh") == "test"
        assert module.family("cat f && ruff check .") == "lint/type"

    def test_a_command_the_tokeniser_refuses_is_judged_as_before(self):
        """An unmatched quote makes the tokeniser raise, and the error must never
        escape into a reading, which would end the report on one odd call.

        The words read before the refusal still count, so `git log 'x` and
        `cd /x && git log 'x` answer from their `git`. A line refused before its
        first word is finished is judged by the anchored pattern `family` used
        before #377 -- `git'x` -- so the new rule never answers worse than the
        old one did. Each arm has its own mutant: letting the error escape,
        judging the whole line by the pattern, and answering `other` on refusal."""
        module = load_script()
        assert module.family("echo 'unbalanced git") == "other"
        assert module.family("git log 'x") == "git"
        assert module.family("cd /x && git log 'x") == "git"
        assert module.family("git'x") == "git"
        assert module.family("cd /x && echo 'unbalanced") == "other"

    def test_a_command_after_a_heredoc_is_read_and_its_body_is_not(self):
        """A heredoc body runs from the line after its operator to the first line
        equal to its delimiter, and what follows that line is a command the shell
        ran. Cutting from the operator to the end charged the `gh issue create`
        after a `cat > body.md <<'EOF'` to `other`, and a `bin/test` after a
        `python3 - <<'EOF'` script too.

        The body is still data, so a `git` written inside one is not a run of it.
        The rest of the operator's own line runs, so it is kept. `<<-` lets the
        closing line carry leading tabs. A heredoc with no closing line is cut to
        the end as before, which is what every flattened command is."""
        module = load_script()
        for command, expected in (
            ("cat > b.md <<'EOF'\nbody\nEOF\ngh issue create --body-file b.md", "git"),
            ("python3 - <<'EOF'\nx=1\nEOF\nbin/test -q", "test"),
            ("cat > f <<-'EOF'\n\tbody\n\tEOF\ngit add f", "git"),
            ("cat > f <<'EOF' && git add f\nbody\nEOF", "git"),
            ("cat <<'A' <<'B'\na\nA\nb\nB\ngit status", "git"),
            ("cat > f <<'EOF'\ngit is here\nEOF", "other"),
            ("cat > f <<'EOF'\n\tEOF\ngit add f\nEOF", "other"),
            ("cat > f <<'EOF'\nbody\ngit status", "other"),
        ):
            assert module.family(command) == expected, command

    def test_a_continued_line_in_an_unquoted_heredoc_body_closes_nothing(self):
        """Bash removes `\\⏎` from an unquoted heredoc's body before it compares
        a line with the delimiter, so a body line ending in one backslash joins
        the next line, and that line closes nothing. #635's round 3 found the
        body closing there instead, which charged the `git push` written inside
        the body to `git`.

        A quoted delimiter keeps the backslash, so its body closes where it did.
        An even run of backslashes is an escaped backslash and joins nothing."""
        module = load_script()
        for command, expected in (
            ("cat <<EOF\nbody \\\nEOF\ngit push", "other"),
            ("cat <<EOF\nbody \\\nEOF\ngit push\nEOF", "other"),
            ("cat <<'EOF'\nbody \\\nEOF\ngit push", "git"),
            ("cat <<EOF\nbody \\\\\nEOF\ngit push", "git"),
            ("cat <<EOF\nbody \\\nmore\nEOF\ngit push", "git"),
        ):
            assert module.family(command) == expected, command

    def test_a_command_on_a_line_of_its_own_is_a_command_word(self):
        """A newline separates two commands the way `;` does, and a comment ends
        at one. `load` used to flatten every newline before `family` saw the
        text, so `cd /x⏎git status` read as `cd` with three arguments.

        The trailing comment is the tokeniser's own trap: its comment handling
        consumes the newline that ends a comment, which would join the next
        line's command onto the one before it."""
        module = load_script()
        for command in (
            "cd /x\ngit status",
            "# stage the record\ngit add a",
            "cd /x\n\n  gh pr view 1",
            "cd /x  # into the tree\ngit status",
        ):
            assert module.family(command) == "git", command

    def test_a_separator_inside_a_substitution_does_not_reach_the_line(self):
        """A command substitution is not a command position, and neither is any
        word inside one: a separator inside `$( … )`, `<( … )` or `>( … )`
        separates the substitution's commands, not the line's. What follows the
        `)` that closes the outermost one is the line's again.

        Round 1 of #377's review found the first three reading `git` while the
        rule four sentences state said they could not.

        Round 2 found the count moved by a parenthesis bash reads as a letter --
        a quoted `)` closing the substitution early, a quoted `(` keeping it open
        to the end of the command -- and by a token that closes one and opens a
        subshell at once (`);(`, `)&&(`, `)|(`), which counting cannot order."""
        module = load_script()
        for command in (
            "x=$(cd /y && git log -1)",
            "diff <(cd a; git show) b",
            "echo x | tee >(cd a; git hash-object --stdin)",
            "echo $(echo $(cd a; git s))",
            "x=$(printf ')'; cd a; git log)",
            'x=$(echo ")"; cd a; git log)',
            "x=$(echo $(pwd); cd a; git log)",
            "x=$( (ls); cd a; git log)",
            "echo a;<(git s)",
        ):
            assert module.family(command) != "git", command
        for command in (
            "echo $(git a); git b",
            "echo $(( 1 + 2 )); git s",
            "x=$(cd /y && ls) && git status",
            "x=$(echo '(') ; git s",
            "n=$(grep -c '(' f)\ngit commit -m x",
            "x=$(pwd);(cd a && git s)",
            "echo $(date)&&(cd a; git x)",
            "echo $(pwd)|(git c)",
            "diff <(ls a)<(ls b); git s",
        ):
            assert module.family(command) == "git", command

    def test_a_comment_runs_nothing_whatever_it_holds(self):
        """A `#` that begins a word starts a comment to the end of its line, so a
        separator inside one separates nothing. A `#` inside a word or inside
        quotes starts no comment, and a comment's apostrophe is not a quote.

        Round 1 of #377's review found the first two reading `git`, where the
        anchored rule before #377 read `other`.

        Round 2 found a comment that opens a continuation line read as words,
        because bash removes `\\⏎` before it reads a word and the walk did not.
        The lines after it pin each character a comment may follow -- a newline,
        a tab, `;`, `&`, `|`, `(` and `)` -- beside the space above, since
        reducing that set to a space and a newline left every case green."""
        module = load_script()
        for command in (
            "# cd x && git push\nls",
            "ls  # then; git push",
            "echo \\' # an escaped quote opens nothing; git push",
            "ls \\\n# x; git push",
            "ls\n# c; git push",
            "ls\t# c; git push",
            "ls;# c; git push",
            "ls&# c; git push",
            "ls|# c; git push",
            "(# c; git push\nls)",
            "(ls)# c; git push",
        ):
            assert module.family(command) != "git", command
        for command in (
            "# don't forget\ngit add a",
            "echo '#'; git s",
            "echo a#b; git s",
            "echo ${#x}; git s",
            'echo "a # b"; git s',
            "cd /x && \\\ngit status",
        ):
            assert module.family(command) == "git", command

    # --- #642: reading is charged to `read` ---
    #
    # A call that only read a file or listed a directory was `other`, so `other`
    # led nearly every reading and the note under it named a `sed -n`. A call is
    # `read` when every command it runs is a read word or a neutral one, at least
    # one reads, nothing writes and nothing is hidden from the walk.

    def test_a_call_that_only_reads_is_charged_to_read(self):
        """The ticket's own instance first, then every shape of a line whose
        commands only read: a pipe between two readers, a redirection into
        `/dev/null` or onto a descriptor, a loop, a test, a subshell, a leading
        assignment, a line of its own, a path to the binary, and a quoted
        operator, which is part of a word and separates nothing."""
        module = load_script()
        for command in (
            "cd /x && sed -n 1,5p f",
            "grep -n x f | head -5",
            "ls -la /x 2>/dev/null || echo none",
            "cat f 2>&1 | tail -3",
            "grep x f 2>&-",
            "grep -q x f >/dev/null && echo y",
            "sed -n 1p -- f",
            "sort -- f",
            "rg --pre-glob '*.gz' x f",
            "ls & ls",
            "(ls) <f",
            "(cd /x && ls) 2>&1 | head",
            "(ls) | head -5",
            "for f in a b; do wc -l $f; done",
            "[ -f x ] && cat x",
            "if grep -q x f; then echo y; fi",
            "(cd /x && ls)",
            "{ ls; }",
            "FOO=1 rg x",
            "W=/w; cd $W; for f in a b; do grep -c x $f; done",
            "while read l; do grep -c $l f; done < list",
            "cd /x\nsed -n 1p f",
            "/usr/bin/grep x f",
            "grep -E 'a|b;c' f",
            'rg "x > y" docs/',
            "find . -name '*.py' | sort | nl",
            "diff a b; awk '{print $1}' f",
            "tail -n 20 log  # the last lines",
            "(cd /x && ls) 2>/dev/null",
            "{ ls; } 2>/dev/null",
            "(ls)>/dev/null",
            "ls &>/dev/null",
            "cat ${f:-x}",
            "[[ -f x ]] && cat x",
        ):
            assert module.family(command) == "read", command

    def test_a_write_is_never_read(self):
        """#200's *wrong in both directions*, from the side a new family opens:
        a write charged to reading is worse than a read left in `other`.

        Every redirection into a file, `sed`'s in-place edit in each spelling
        its option parser takes (a single-dash cluster is read wholesale, and a
        long option may be abbreviated), `sort`'s output file, `find`'s actions
        and `awk`'s in-place include. A heredoc writing a file is a write and a
        heredoc at once."""
        module = load_script()
        for command in (
            "sed -i s/a/b/ f",
            "sed -i.bak s/a/b/ f",
            "sed -ni 1p f",
            "sed -Ei s/a/b/ f",
            "sed -es/a/i/ f",
            "sed --in-place s/a/b/ f",
            "sed --in-place=.bak s/a/b/ f",
            "sed --in s/a/b/ f",
            "cat f > g",
            "cat f >g",
            "grep x f >> g",
            "ls >| g",
            "ls &> g",
            "ls 2> err",
            "ls > 2",
            "cat f >&g",
            "cat f <> g",
            "grep x f 2>&1 >g",
            "ls; echo hi > f",
            "sort -o g f",
            "sort -uo g f",
            "sort --output=g f",
            "sort --out g f",
            "grep x f | sort -o g",
            "find . -delete",
            "find . -exec rm {} +",
            "find . -execdir rm {} +",
            "find . -okdir rm {} +",
            "find . -fprint g",
            "find . -fls g",
            "awk -i inplace '{print}' f",
            "awk --include=inplace '{print}' f",
            "sed -I '' s/a/b/ f",
            "sed -I.bak s/a/b/ f",
            "rg --pre ./x.sh pat",
            "rg --pre=sh pat",
            "sort --compress-program=sh f",
            "rg --hostname-bin ./x pat",
            "rg --hostname-bin=./x pat",
            "cat > f <<'EOF'\nx\nEOF",
        ):
            assert module.family(command) != "read", command

    def test_a_line_that_does_more_than_read_is_not_read(self):
        """One read word is not enough, and neither is a read word first. A pipe
        into `tail` sits behind nearly every kind of command, and `ls && rm -rf
        x` begins by reading. A wrapper is not looked through, as it is not for
        `git`: `timeout` is the command word."""
        module = load_script()
        for command in (
            "./bin/deploy --wait | tail -3",
            "cat f | python3 -c 'x'",
            "ls; rm x",
            "ls && rm -rf x",
            "grep x f; python3 build.py",
            "sleep 5; tail log",
            "timeout 9 grep x f",
            "xargs grep x < list",
            "cat f | tee g",
        ):
            assert module.family(command) == "other", command

    def test_what_the_walk_cannot_see_is_not_read(self):
        """A heredoc, a here-string, a command or process substitution, a line
        the tokeniser refuses, a `case` arm, whose commands the walk does not
        put in command position, and a leading redirection, which does not put
        one there either. `runs_git` reads past a substitution; here the same
        blindness would let `x=$(rm y); ls` read as reading, so each of these
        keeps the line out. The heredocs are the owner's answer: a script handed
        to an interpreter gets no family."""
        module = load_script()
        for command in (
            "python3 - <<'EOF'\nx\nEOF",
            "cat <<'EOF'\ntext\nEOF",
            "cat <<eof\ntext\neof",
            'grep x <<< "$y"',
            "x=$(rm y); ls",
            "cat $(ls)",
            'cat "$(ls)"',
            "cat `ls`",
            "diff <(ls a) <(ls b)",
            "echo $((1 + 2)); ls",
            "cat 'x",
            "case $x in a) rm f;; esac; ls",
            "<f cat",
            "ls; >/dev/null rm -rf x",
            "ls && >/dev/null rm -rf x",
            "ls;>/dev/null rm -rf x",
            "ls&&>/dev/null rm x",
            "</dev/null rm x; ls",
            "(>/dev/null rm x); ls",
            "ls; >&2 rm x",
            "cat f\n</dev/null python3 build.py",
            "if [[ -f a ]] rm a; ls",
            "if [[ -f a ]] { rm a }; ls",
            "{ ls; } always { rm a; }",
            "{ ls } always { rm b }",
            "cat ${ rm x; }",
            "ls &</dev/null rm x",
            "ls &\n>/dev/null rm x",
            "ls &|>/dev/null rm x",
            "if (( ! true )) rm a; ls",
            "if (( ! true )) 2>/dev/null rm a; ls",
            "for f (ls) rm $f; ls",
        ):
            assert module.family(command) == "other", command

        # A stray `)` leaves the word after it in no command, and a line the
        # shell refuses must not end the reading. `") 2"` is the one that
        # reaches the no-command guard, because a descriptor number after a `)`
        # is not zsh's short-form body.
        assert module.family(") x") == "other"
        assert module.family(") 2") == "other"

    def test_a_line_of_neutral_words_alone_is_not_read(self):
        """A neutral word neither reads a file nor writes one, so it keeps a
        reading line `read` and makes nothing `read` on its own."""
        module = load_script()
        for command in ("cd /x", "echo hi", "W=1", "true", "cd /x && pwd"):
            assert module.family(command) == "other", command


# --- #945: the largest context any one turn read ----------------------------
#
# A resumed agent pays its whole earlier context again on every turn, so its
# largest turn is what tells a resume worth taking from one that is not. The
# column reads every assistant message once, with all three input fields,
# beside `load`'s `turns` rather than through it.


def context_turn(second, uid, message_id=None, **usage):
    """One call-carrying assistant row with its `usage` written field by
    field, and the call's result a second later.

    The fields are passed under the harness's own names, so a case can set
    exactly the one a reader might leave out."""
    return [
        at(stamp_at(second), [use(uid, "pytest -q")], message_id or f"c-{uid}", usage),
        plain_result(second + 1, uid),
    ]


class Test_largest_context:
    def test_accepts_a_segments_largest_turn_as_a_json_key_and_a_column(
        self, run_with_segments
    ):
        """S1. The crafter's file holds turns of 0 and 300 (a cache write), the
        proofer's one of 40 (a cache read). Each row carries its largest under
        one key, and the page names the column and says what it reads."""
        rows = segments_of(run_with_segments)["rows"]
        assert [row["largest_context"] for row in rows] == [300, 40], rows
        out = segment_report(run_with_segments)
        assert re.search(r"^  agent\s.*\stokens\s+context$", out, re.M), out
        flat = " ".join(out.split())
        assert (
            "context the largest input any one turn read: the tokens sent fresh, "
            "written to the cache and read from it" in flat
        ), flat

    def test_accepts_a_message_split_over_rows_once(self, tmp_path):
        """S2. A harness writes one message as one row per content block and
        repeats the usage on each, so a message counts once by its key: 1,150
        for the split message, not twice that."""
        usage = {
            "input_tokens": 100,
            "cache_creation_input_tokens": 50,
            "cache_read_input_tokens": 1000,
        }
        lines = [
            at(stamp_at(0), [use("a", "pytest -q")], "split", usage),
            at(stamp_at(0), [use("b", "git status")], "split", usage),
            plain_result(1, "a"),
            plain_result(1, "b"),
            *context_turn(5, "c", cache_read_input_tokens=900),
        ]
        path = tmp_path / "t.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        assert load_script().largest_context(str(path)) == [1150]

    def test_accepts_every_input_field_of_a_turn(self, tmp_path):
        """S2. A turn's context is the tokens sent fresh, written to the cache
        and read from it. `load`'s `turns` leave the cache write out, which is
        why the column does not read them: 327 here, never 307."""
        lines = context_turn(
            0,
            "a",
            input_tokens=7,
            cache_creation_input_tokens=20,
            cache_read_input_tokens=300,
        )
        path = tmp_path / "t.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        assert load_script().largest_context(str(path)) == [327]

    def test_accepts_a_turn_that_called_no_tool(self, tmp_path):
        """S2. A message that answers in text and calls nothing is still one
        model call that read its whole context, so it counts where `load`'s
        `turns` would drop it."""
        lines = [
            *context_turn(0, "a", cache_read_input_tokens=500),
            at(
                stamp_at(5),
                [{"type": "text", "text": "."}],
                "said",
                {"cache_read_input_tokens": 800},
            ),
        ]
        path = tmp_path / "t.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        assert load_script().largest_context(str(path)) == [800]

    def test_accepts_each_slice_of_a_resumed_file_as_its_own(self, tmp_path):
        """S3. A resumed file's slices each print the largest turn inside
        them, walked from the run or given as the agent's own file: 900 and
        400, never the file's 900 on both."""
        path = write_run(
            tmp_path,
            call("a", 0, 10, "git status --short")
            + spawn("A", 25, 625, "agentic:crafter", "Build phase 1"),
            {
                "agent-crafter.jsonl": [
                    *context_turn(625, "s1", cache_read_input_tokens=900),
                    *context_turn(640, "s2", cache_read_input_tokens=100),
                    coordinator_message(9000),
                    *context_turn(9010, "s3", cache_read_input_tokens=400),
                ]
            },
        )
        walked = [row["largest_context"] for row in segments_of(path)["rows"]]
        own = [row["largest_context"] for row in segments_of(own_file(path))["rows"]]
        assert walked == own == [900, 400], (walked, own)

    def test_refuses_a_zero_for_a_slice_that_holds_no_assistant_message(self, tmp_path):
        """S3. A slice whose call was written with no `usage` block has no
        turn to read, so it carries None and prints a dash: a zero would read
        as a turn that sent nothing."""
        path = tmp_path / "agent-crafter.jsonl"
        lines = [
            *context_turn(625, "s1", cache_read_input_tokens=900),
            coordinator_message(9000),
            at(stamp_at(9010), [use("s2", "pytest -q")], "bare"),
            plain_result(9011, "s2"),
        ]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        rows = segments_of(path)["rows"]
        assert [row["largest_context"] for row in rows] == [900, None], rows
        out = segment_report(path)
        assert re.search(r"^  agent-crafter\.jsonl  1/2\s.*\s900$", out, re.M), out
        assert re.search(r"^  agent-crafter\.jsonl  2/2\s.*\s—\s+—$", out, re.M), out


class Test_module:
    def test_a_transcript_that_cannot_be_opened_is_skipped_rather_than_raised(
        self, tmp_path
    ):
        """A segment deleted between the walk and the open, or one whose
        permissions the walk could not see. Both totals shrink — one fewer
        transcript, and that segment's spend missing — and nothing raises."""
        good = tmp_path / "good.jsonl"
        good.write_text(spend(0, output=9, message_id="s1") + "\n", encoding="utf-8")
        totals = load_script().token_totals([str(tmp_path / "gone.jsonl"), str(good)])
        assert (totals["transcripts"], totals["turns"], totals["output"]) == (1, 1, 9)

    def test_load_returns_input_counts_only(self, tmp_path):
        """`load`'s per-turn tuple used to carry a third element, this message's
        `output_tokens`, and nothing in the file read it.

        It is removed rather than repaired: `output_tokens` is the one field that
        grows across a split message's rows, so what sat there was the first
        partial count — the same defect as #202, waiting for its first reader.
        The input-side fields are fixed when the request is made and repeat
        unchanged, which is why they can be taken from the first row.

        Pinned on the shape rather than on the length alone, so a tuple that
        regrows a third element under a different meaning still fails."""
        module = load_script()
        rows = [
            at(
                "2026-08-24T10:00:00Z",
                [use("l", "pytest -q")],
                "m",
                {
                    "input_tokens": 11,
                    "cache_read_input_tokens": 4,
                    "output_tokens": 999,
                },
            ),
            at("2026-08-24T10:00:05Z", [{"type": "tool_result", "tool_use_id": "l"}]),
        ]
        path = tmp_path / "load.jsonl"
        path.write_text("\n".join(rows) + "\n", encoding="utf-8")

        _calls, turns = module.load(str(path))
        assert len(turns) == 1, turns
        assert len(turns[0]) == 2, turns
        assert turns[0][1] == 15, turns

    def test_the_walk_yields_each_commands_arguments_and_nothing_inside_a_substitution(
        self,
    ):
        """`shell_words` is the one walk both rules read: `command_words` takes
        its command words, and `only_reads` its arguments and operators too. A
        word inside `$( … )` is neither, and what is left of an operator token
        once a substitution's parentheses are taken out is yielded only when
        something is left."""
        module = load_script()
        assert list(module.shell_words("cd /x && ls -l $(rm f) y 2>&1")) == [
            ("command", "cd"),
            ("argument", "/x"),
            ("operator", "&&"),
            ("command", "ls"),
            ("argument", "-l"),
            ("argument", "$"),
            ("argument", "y"),
            ("argument", "2"),
            ("operator", ">&"),
            ("argument", "1"),
        ]

    def test_says_reads_from_stdin(self, monkeypatch):
        """`--says -` is the form a session already has the sentence in hand for."""
        module = _cost()
        monkeypatch.setattr(module.sys, "stdin", io.StringIO("the segment ran long\n"))
        assert module.read_says("-").strip() == "the segment ran long"

    def test_says_reads_from_a_file(self, tmp_path):
        module = _cost()
        path = tmp_path / "says.md"
        path.write_text("nine rounds, and the cap never bound\n", encoding="utf-8")
        assert "nine rounds" in module.read_says(str(path))

    # --- the lookup and the body --------------------------------------------------

    def test_the_lookup_reads_the_label_and_the_whole_history(self, monkeypatch):
        """One call, not two. `--state all` answers both of the skill's
        questions, because every open issue is in it — and the limit is raised
        off the default so a label with more than thirty closed logs does not
        read as one that never existed."""
        module = _cost()
        seen = _gh(monkeypatch, module, listing=_listing((42, "OPEN")))
        module.open_log("flow-baseline")
        assert len(seen) == 1, seen
        argv = seen[0]
        assert argv[:2] == ["issue", "list"]
        assert argv[argv.index("--label") + 1] == "flow-baseline"
        assert argv[argv.index("--state") + 1] == "all"
        assert int(argv[argv.index("--limit") + 1]) > 30

    def test_the_default_label_is_the_rolling_log(self):
        module = _cost()
        assert module.ROLLING_LABEL == "flow-measurement"

    def test_the_body_carries_the_judgment_before_the_numbers(self):
        """What a reader of the log came for is what the numbers say. The reading
        is fenced below it so the report's columns survive markdown."""
        module = _cost()
        body = module.comment_body(
            "agent   span   calls\ncrafter   19m    99", "it ran long"
        )
        assert body.index("it ran long") < body.index("agent")
        assert "```" in body

    @pytest.mark.parametrize(
        "listing, expected",
        [
            ("[]", "no history"),
            (_listing((1, "CLOSED")), "closed"),
            (_listing((1, "OPEN")), "one open"),
            (_listing((1, "OPEN"), (2, "OPEN")), "many open"),
        ],
    )
    def test_the_four_states_are_read_off_one_listing(
        self, monkeypatch, listing, expected
    ):
        module = _cost()
        _gh(monkeypatch, module, listing=listing)
        state, _payload = module.open_log("flow-measurement")
        assert state == expected

    # --- the property, over the shipped module ----------------------------------

    def test_every_int_conversion_in_the_module_is_discharged(
        self, module_text, namespace
    ):
        """The class, over the module as it stands.

        A member with nothing discharging it is a derived number one non-finite
        sum away from ending the report with stdout empty, which is what #175's
        four rounds were about."""
        members, _unresolved, _examined = classify(module_text, namespace)
        undischarged = [(where, path) for where, path, why in members if why is None]
        assert not undischarged, (
            "a site converts a number to an int and nothing discharges it. Put a "
            "finiteness test on the same operand in the ENCLOSING conditional, or "
            "wrap it in a `try` catching what the conversion raises:\n"
            + "\n".join(f"  session_cost.py#{w}  {p}" for w, p in undischarged)
        )

    def test_the_class_holds_the_site_the_defect_came_through(
        self, module_text, namespace
    ):
        """A property that found no members would pass on anything.

        The member named here is the one round 3 of #175 fixed, so this case dies
        if the walk stops reaching it — which is how this check would go vacuous
        without anybody noticing."""
        members, _unresolved, _examined = classify(module_text, namespace)
        assert any(where.startswith("token_thirds:") for where, _p, _w in members), (
            f"the walk no longer reaches the conversion in token_thirds: {members}"
        )

    def test_the_walk_examines_every_call_and_operator_site(
        self, module_text, namespace
    ):
        """The enumeration is by construction, checked against a second reading.

        What `classify` looked at is compared with a set taken independently off
        the module's tree, so a site cannot be dropped on the way through the
        classifier without this case saying so. The claim is set equality; no
        count appears, because a count is what #192 exists to stop standing in
        for a property."""

        def coordinates(nodes):
            return {
                (type(n).__name__, getattr(n, "lineno", 0), getattr(n, "col_offset", 0))
                for n in nodes
            }

        _members, _unresolved, examined = classify(module_text, namespace)
        independent = [
            node
            for node in ast.walk(ast.parse(module_text))
            if isinstance(node, SITE_KINDS)
        ]
        # Two parses give two node objects for one site, so the readings are
        # compared by position and kind rather than by identity.
        assert coordinates(examined) == coordinates(independent)
        assert independent, (
            "the module has no call or operator site; the walk is vacuous"
        )

    def test_no_operator_in_this_module_converts_a_number_to_an_int(self, module_text):
        """The other dimension, closed by construction rather than by assertion.

        `//` and `%` produce integers and neither converts one — `inf // 3` is a
        `nan` and nothing raises — so the operators are enumerated and probed and
        the answer is derived. This case is what turns red if a future operator
        changes it."""
        converting = [
            ast.unparse(node)[:60]
            for node in ast.walk(ast.parse(module_text))
            if isinstance(node, (ast.BinOp, ast.UnaryOp, ast.AugAssign, ast.Compare))
            and operator_converts(node)
        ]
        assert not converting, converting

    def test_the_unresolved_callees_are_runtime_receivers(self, module_text, namespace):
        """The residual, named as a shape a next editor can act on.

        Round 3 of #175 asked for exactly this — a limit written as something
        actionable rather than as an excuse. Every callee this walk cannot
        resolve is a name the module binds inside a function, or an expression
        with no name at all; never a name the module binds nowhere, which would
        be the resolver failing rather than a receiver being a runtime value."""
        _members, unresolved, _examined = classify(module_text, namespace)
        bound = names_bound_inside(ast.parse(module_text))
        stray = [
            (where, ast.unparse(node.func)[:60])
            for where, node in unresolved
            if root_name(node.func) is not None and root_name(node.func) not in bound
        ]
        assert not stray, (
            "a callee resolved to nothing and the module binds its name nowhere, "
            f"so the resolver missed it rather than the receiver being runtime: {stray}"
        )

    def test_the_operator_half_is_probed_and_says_what_it_cannot_see(self):
        """The operator dimension, with a positive control so its `no` is a
        measurement rather than an unreachable branch.

        Over numeric operands no binary operator reaches an int through an
        operand — `//` and `%` build integers out of integers and convert
        nothing — which is what the walk reports for the module. Sequence
        repetition does convert, and it is the route a numeric probe cannot see.

        `//` on a huge integer and a float DOES raise, and it is still not a
        member: what a site raises only matters once it converts, and this is
        the line between #192's class and the wider one in `questions.md` Q2."""
        mult = ast.parse("a * b").body[0].value
        floordiv = ast.parse("a // b").body[0].value
        assert operator_forms(mult) == ["a * b"]
        assert operator_forms(floordiv) == ["a // b"]
        assert not operator_converts(mult)
        assert not operator_converts(floordiv)
        assert operator_converts(mult, benign="ab"), (
            "sequence repetition no longer converts, so the negative answer above "
            "is an unreachable branch rather than a measurement"
        )
        assert operator_raised(mult, benign="ab") == {OverflowError}
        assert operator_raised(floordiv) == {OverflowError}

    def test_a_type_error_is_not_a_hazard_the_guard_has_to_cover(self):
        """A `TypeError` is the probe's own filler talking, not a hazard.

        Measured: `round(3.0, inf)` raises `TypeError` because `ndigits` has to
        be an index, so a derived value in that slot says nothing about the
        conversion — and demanding a guard for it would refuse a site over the
        probe's choice of filler. That filler cuts the other way too and this is
        where the limit is stated: with a benign float in an index slot, every
        call raises `TypeError` first, so a two-argument conversion's hazards
        come from the slot the probe can still reach."""
        assert quiet(lambda: round(3.0, float("inf")))[1] is TypeError
        assert TypeError not in raised_by(round, 2, [])
        assert raised_by(round, 1, []) == {OverflowError, ValueError}

    def test_a_call_on_a_literal_receiver_resolves(self, module_text, namespace):
        """`" ".join(text.split())` in `load` is a method on a literal.

        The resolver answers for it, because a literal is itself. Left
        unresolved it would join the residual, and the residual is the set this
        file promises holds only receivers computed at runtime."""
        _members, unresolved, _examined = classify(module_text, namespace)
        literal_receivers = [
            where
            for where, node in unresolved
            if isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Constant)
        ]
        assert not literal_receivers, literal_receivers
        assert any(
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Constant)
            for node in ast.walk(ast.parse(module_text))
        ), "the module no longer calls a method on a literal, so this case is vacuous"

    def test_the_residual_check_names_a_callee_the_module_binds_nowhere(self, tmp_path):
        """The residual check can fail, which is what makes it a check.

        A call through a name the module binds nowhere is the resolver missing
        something rather than a receiver being a runtime value, and that is the
        one shape `test_the_unresolved_callees_are_runtime_receivers` refuses."""
        text = "def under_test(value):\n    return nowhere.convert(value)\n"
        _members, unresolved, _examined = classify(
            text, namespace_of_source(text, tmp_path)
        )
        bound = names_bound_inside(ast.parse(text))
        stray = [
            where
            for where, node in unresolved
            if root_name(node.func) is not None and root_name(node.func) not in bound
        ]
        assert stray, "a callee the module binds nowhere was not named"

    def test_a_callable_that_yields_an_int_without_converting_is_not_a_member(
        self, tmp_path
    ):
        """Both probes have to agree, and this is the half the first one answers.

        A function that answers with an integer without ever consuming its
        operand as one cannot raise on a derived value, so requiring a guard of
        it would be a refusal with nothing behind it."""
        text = (
            "def bucket(value):\n"
            "    return 1 if value > 0 else 0\n"
            "\n\n"
            "def under_test(mean):\n"
            "    return [bucket(mean)]\n"
        )
        bindings = namespace_of_source(text, tmp_path)
        assert yields_an_int(bindings["bucket"], 1, [])
        assert not consumes_an_integer(bindings["bucket"], 1, [])
        members, _unresolved, _examined = classify(text, bindings)
        assert not [
            where for where, _p, _why in members if where.startswith("under_test:")
        ]

    def test_a_predicate_that_converts_but_answers_a_bool_is_not_a_member(
        self, namespace
    ):
        """The third stated residual, kept visible instead of incidental.

        `math.isfinite` consumes its operand through the integer protocol — which
        is why `math.isfinite` on an integer with no float of its own raises, the
        🔴 of round 2 of #175 — and it answers with a `bool`, so it is not a
        conversion TO an int and not a member here. Both halves are asserted,
        because the exclusion rests on the second one and a later edit that
        dropped `yields_an_int` would otherwise pass silently."""
        isfinite = namespace["math"].isfinite
        assert consumes_an_integer(isfinite, 1, [])
        assert not yields_an_int(isfinite, 1, [])
        assert raised_by(isfinite, 1, []) == {OverflowError}, (
            "the hazard this exclusion accepts is no longer the one it was measured against"
        )

    @pytest.mark.parametrize(
        ("name", "body", "discharged"),
        [pytest.param(*row, id=row[0]) for row in GUARD_SHAPES],
    )
    def test_the_guard_shapes_are_decided_by_what_they_catch(
        self, name, body, discharged, tmp_path
    ):
        """Nineteen constructed shapes, each classified rather than asserted about.

        Three of them are the point of the design: a converter written in the
        module under test, an aliased import and a `from`-import all classify
        like `round`, and a hand-written predicate counts as a guard — none of
        them appears in this file as a name. The refusals are the other half: a
        `try` covering only `OverflowError` leaves a `NaN` ending the report, and
        a test on a different operand answers about a different value."""
        text = f"{PREAMBLE}def under_test(mean, other=1.0):\n{body}\n"
        members, _unresolved, _examined = classify(
            text, namespace_of_source(text, tmp_path)
        )
        inside = [
            (where, why)
            for where, _p, why in members
            if where.startswith("under_test:")
        ]
        assert inside, f"{name}: the walk found no conversion in the unit at all"
        assert all(why is not None for _w, why in inside) == discharged, (
            f"{name}: {inside}"
        )

    def test_an_unguarded_conversion_added_to_the_module_is_named(
        self, module_text, namespace
    ):
        """The mutation, in the suite: the real module with one unguarded site.

        A check that has never failed proves nothing, and this is the shape the
        class exists for — a new conversion added by a later edit, in a unit
        nobody thought to look at."""
        text = module_text.replace(
            "def strip_pipe(command):",
            "def total_seconds(spans):\n    return int(sum(spans))\n\n\n"
            "def strip_pipe(command):",
            1,
        )
        assert "def total_seconds" in text, "the mutation did not land"
        members, _unresolved, _examined = classify(text, namespace)
        undischarged = [where for where, _p, why in members if why is None]
        assert any(where.startswith("total_seconds:") for where in undischarged), (
            f"the added site was not named: {members}"
        )

    def test_the_module_states_the_rule_and_the_two_shapes_it_misses(self, module_text):
        """A rule nobody meets is a rule the next edit breaks.

        `token_thirds` is where the conversion is, so its docstring is where a
        next editor reads what the class is, where the check lives, and the two
        shapes the property does not reach. Pinned here because a stated limit
        that can be deleted silently is not stated."""
        unit = next(
            node
            for node in ast.parse(module_text).body
            if isinstance(node, ast.FunctionDef) and node.name == "token_thirds"
        )
        text = " ".join((ast.get_docstring(unit) or "").split())
        assert "tests/skills/test_session_cost.py" in text, (
            "the docstring does not name the check that enforces the rule"
        )
        for shape in ("subscript", "division"):
            assert shape in text, f"the docstring does not name the {shape} residual"
        assert "#192" in text, (
            "the docstring does not name the issue the class came from"
        )


test_census = census_case(TARGET)
