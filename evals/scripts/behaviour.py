"""The case writer every behaviour-suite generator shares.

A case is a directory `claude plugin eval` reads: `case.yaml` (config under
`execution:`, which is where the runner reads `max_turns`, `timeout_seconds`
and `model`), `prompt.md` (the prompt and nothing else), `scaffold.sh` (named
by `context.scaffold_script`, a path relative to the case) and one file per
grader under `graders/`. A grader's file name is its name, and its prefix is
its kind for `noninferiority.py`: `reach-`, `shape-`, `truth-`, `rule-`.
"""

import json
import os
import shutil

KINDS = ("reach", "shape", "truth", "rule")
ORCHESTRATOR_TOOLS = ("Agent", "Task", "Bash", "Read", "Write", "Edit", "Glob", "Grep")


def js_escape(text):
    """`text` as a JavaScript regex matching it literally.

    Reads: nothing — it maps the characters of a string it is handed."""
    return "".join("\\" + c if c in "\\^$.*+?()[]{}|/" else c for c in text)


def squote(text):
    """`text` as a YAML single-quoted scalar, which takes no escapes.

    Reads: nothing — it maps the characters of a string it is handed."""
    return "'" + text.replace("'", "''") + "'"


def grader(kind, name, body, **fields):
    """`(file name, text)` for one grader of KIND; FIELDS are its frontmatter.

    Reads: nothing — it formats the fields it is handed."""
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


def report_regex(kind, name, path, pattern, body):
    """A regex grader over the file at PATH, multiline.

    Reads: nothing — it formats the fields it is handed."""
    return grader(
        kind,
        name,
        body,
        type="regex",
        target={"source": "file", "path": path},
        pattern=pattern,
        flags="m",
    )


def reach(agent):
    """The grader that the session spawned `specseal:<agent>` through the
    `Agent` tool, the way production does.

    Reads: nothing — it formats the fields it is handed."""
    return grader(
        "reach",
        agent,
        f"The session spawned specseal:{agent} through the Agent tool.",
        type="tool_used",
        tool="Agent",
        input_match=f'"subagent_type"\\s*:\\s*"specseal:{agent}"',
    )


def write_case(directory, *, name, tags, prompt, scaffold, graders, **execution):
    """Write one case under DIRECTORY, replacing what it held.

    DIRECTORY is removed first when it exists.

    Reads: observed — whether DIRECTORY exists, before it writes; unknown passed"""
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
    for rel, text in files.items():
        with open(os.path.join(directory, rel), "w", encoding="utf-8") as f:
            f.write(text)
    for file_name, text in graders:
        with open(
            os.path.join(directory, "graders", file_name), "w", encoding="utf-8"
        ) as f:
            f.write(text)
