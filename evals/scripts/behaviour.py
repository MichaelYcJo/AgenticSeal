"""The case writer every behaviour-suite generator shares.

A case is a directory `claude plugin eval` reads: `case.yaml` (config under
`execution:`, which is where the runner reads `max_turns`, `timeout_seconds`
and `model`), `prompt.md` (the prompt and nothing else), `scaffold.sh` (named
by `context.scaffold_script`, a path relative to the case) and one file per
grader under `graders/`. A grader's file name is its name, and its prefix is
its kind for `noninferiority.py`: `reach-`, `shape-`, `truth-`. `grader_from`
reads a grader file back in the shape a side records it.
"""

import json
import os
import re
import shutil

KINDS = ("reach", "shape", "truth")
ORCHESTRATOR_TOOLS = ("Agent", "Task", "Bash", "Read", "Write", "Edit", "Glob", "Grep")
# One scalar of the front matter `grader` writes: single-quoted, a quote
# doubled inside, or a bare word up to the next `,` or `}`.
SCALAR = r"'(?:[^']|'')*'|[^,}]+"


def js_escape(text):
    """`text` as a JavaScript regex matching it literally."""
    return "".join("\\" + c if c in "\\^$.*+?()[]{}|/" else c for c in text)


def squote(text):
    """`text` as a YAML single-quoted scalar, which takes no escapes."""
    return "'" + text.replace("'", "''") + "'"


def grader(kind, name, body, **fields):
    """`(file name, text)` for one grader of KIND; FIELDS are its frontmatter."""
    if kind not in KINDS:
        raise ValueError(f"grader kind {kind!r} is not one of {KINDS}")
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif isinstance(value, int):
            lines.append(f"{key}: {value}")
        elif isinstance(value, dict):
            inner = ", ".join(f"{k}: {squote(str(v))}" for k, v in value.items())
            lines.append(f"{key}: {{{inner}}}")
        else:
            lines.append(f"{key}: {squote(str(value))}")
    lines += ["---", body.strip(), ""]
    return f"{kind}-{name}.md", "\n".join(lines)


def scalar(text):
    """The value of one front-matter scalar of a truth grader: a one-level
    flow map, a single-quoted string, or an integer; anything else is kept
    as its text."""
    text = text.strip()
    if text.startswith("{"):
        return {k: scalar(v) for k, v in re.findall(rf"(\w+): ({SCALAR})", text[1:-1])}
    if text.startswith("'"):
        return text[1:-1].replace("''", "'")
    return int(text) if re.fullmatch(r"-?\d+", text) else text


def grader_from(path, text):
    """The grader file PATH holding TEXT in the shape a side records it:
    `name`, `type`, `weight` (1 where the file names none) and `config`,
    every other front-matter field, with `match` `contains` where the file
    names none.

    A file with no front matter raises ValueError."""
    m = re.match(r"---\n(?P<head>.*?)\n---\n", text, re.S)
    if not m:
        raise ValueError(f"{path} has no front matter")
    fields = {}
    for line in m["head"].split("\n"):
        key, _, value = line.partition(": ")
        fields[key] = scalar(value)
    config = {k: v for k, v in fields.items() if k not in ("type", "weight")}
    config.setdefault("match", "contains")
    return {
        "name": path.rsplit("/", 1)[-1][: -len(".md")],
        "type": fields.get("type"),
        "weight": fields.get("weight", 1),
        "config": config,
    }


def report_regex(kind, name, path, pattern, body, flags="m", **extra):
    """A regex grader over the file at PATH, multiline unless FLAGS says
    otherwise; EXTRA are further frontmatter fields, `match` among them."""
    return grader(
        kind,
        name,
        body,
        type="regex",
        target={"source": "file", "path": path},
        pattern=pattern,
        flags=flags,
        **extra,
    )


def reach(agent):
    """The grader that the session spawned `agentic:<agent>` through the
    `Agent` tool, the way production does."""
    return grader(
        "reach",
        agent,
        f"The session spawned agentic:{agent} through the Agent tool.",
        type="tool_used",
        tool="Agent",
        input_match=f'"subagent_type"\\s*:\\s*"agentic:{agent}"',
    )


# A finding as `templates/records/sdd-round.md` has the proofer write it: the
# `## Findings` heading, then a `### <n>. ` section, then that section's
# finding block, the `seal` block whose first line is its `severity:`, before
# the next heading. A finding the proofer writes has no close block, so the
# grader asks for none.
FINDINGS_SHAPE = (
    r"^## Findings[ \t]*\n(?:(?!^## )[\s\S])*?^### \d+\. [^\n]+\n"
    r"(?:(?!^##)[\s\S])*?^" + "`" * 3 + r"seal\nseverity: \S"
)
# The pictographs and symbols a mark is drawn from, as a JavaScript regex
# with no `u` flag, where an astral pictograph is its surrogate pair.
EMOJI_RANGES = (
    r"\uD83C[\uDC00-\uDFFF]|\uD83D[\uDC00-\uDFFF]|\uD83E[\uDC00-\uDEFF]"
    r"|[☀-➿⬀-⯿️]"
)


def report_shape(agent, report):
    """The reach grader and the three shape graders of a proofer round
    record at REPORT: it exists, it carries a finding in the record's shape,
    and it is written in words."""
    return [
        reach(agent),
        grader(
            "shape",
            "report-exists",
            "The report is at its path.",
            type="file_exists",
            path=report,
        ),
        report_regex(
            "shape",
            "findings",
            report,
            FINDINGS_SHAPE,
            "The report carries `## Findings` with a `### <n>.` section and its "
            "finding block.",
        ),
        report_regex(
            "shape",
            "words-only",
            report,
            EMOJI_RANGES,
            "The report carries no emoji.",
            match="not_contains",
        ),
    ]


def write_case(directory, *, name, tags, prompt, scaffold, graders, **execution):
    """Write one case under DIRECTORY, replacing what it held.

    DIRECTORY is removed first when it exists."""
    if os.path.isdir(directory):
        shutil.rmtree(directory)
    os.makedirs(os.path.join(directory, "graders"))
    tools = execution.pop("allowed_tools", ORCHESTRATOR_TOOLS)
    head = [
        'schema_version: "1.1"',
        f"name: {json.dumps(name, ensure_ascii=False)}",
        f"tags: {json.dumps(list(tags))}",
        f"runs: {execution.pop('runs', 2)}",
        "context:",
        "  scaffold_script: scaffold.sh",
        "execution:",
        f"  max_turns: {execution.pop('max_turns')}",
        f"  timeout_seconds: {execution.pop('timeout_seconds')}",
        f"  model: {json.dumps(execution.pop('model'))}",
        f"  allowed_tools: {json.dumps(list(tools))}",
    ]
    if execution:
        raise TypeError(f"unknown execution fields: {sorted(execution)}")
    files = {
        "case.yaml": "\n".join(head) + "\n",
        "prompt.md": prompt.strip() + "\n",
        "scaffold.sh": "set -eu\n" + scaffold.strip() + "\n",
    }
    # The committed cases are LF (`.gitattributes`), and a case is compared
    # byte for byte with what this writes, so the newline is never the
    # platform's.
    for rel, text in files.items():
        with open(
            os.path.join(directory, rel), "w", encoding="utf-8", newline="\n"
        ) as f:
            f.write(text)
    for file_name, text in graders:
        with open(
            os.path.join(directory, "graders", file_name),
            "w",
            encoding="utf-8",
            newline="\n",
        ) as f:
            f.write(text)
