#!/usr/bin/env python3
"""payload_meter — what a session's and each agent's startup payload is made
of, and what it costs in tokens.

Every spawn of an agent this plugin defines pays for the same prefix again:
the definition under `agents/`, every `SKILL.md` its `skills:` list injects,
and the two `CLAUDE.md` files the harness adds (the repository's and the
user's, in the config directory in use, `${CLAUDE_CONFIG_DIR:-$HOME/.claude}`,
#1367) with every file their `@` lines import, up to four hops
(`imports_of`, #1177). The prefix is cached for five minutes, and no two
spawns of one agent in a review chain fall inside five minutes of each other
(#292, `frame/design.md` *Measured before the first edit*) — so in a chain it is
written on every spawn. This reads the tree and says what that prefix is.

A session pays for a prefix of its own, which `session_composition` lists in
a table before the agents': the same `CLAUDE.md` pair with its imports, and
the core the plugin's `SessionStart` hook prints, counted as
`lib/core.py#rendered` for the measured tree's core (#1177, #1430). The
hook's output reaches the session and no subagent (#1177's probe of a plugin
`SessionStart` hook), so no agent's table carries it.

  bytes, chars    counted from the files.
  tokens          NEVER counted. Every token figure, the session's and each
                  agent's, is the row's bytes over `ASSUMED_RATIO`, labelled
                  `BASIS`. A bare number is refused by the module's own
                  tests, because the six calibration spawns put three agents
                  at 2.7, 3.2 and 3.4 bytes per token — one ratio does not
                  fit all of them.

Usage:
  payload_meter.py                          one table for the session and
                                            one per agent
  payload_meter.py --json                   the same as data
  payload_meter.py --root DIR --agent NAME  a different tree, a subset

A skill name resolves to `skills/<name>/SKILL.md` in the user's config
directory when the user has one, shadowing the plugin's, so the row reports
the tree's file and notes the shadow.

Exit codes: 0 measured · 1 no `agents/*.md` under the root · 2 nothing ran:
`lib/blocks.py` or `lib/lines.py`, which say where a fence, a comment or a
code span stands, is not in the plugin around it where a `CLAUDE.md` the
meter reads exists, `lib/core.py`, which says what the core hook prints, is
not in the plugin around it, or the arguments were unusable (argparse's
usage error). An interpreter below the floor never reaches this file through
`seal payload`: `lib/launch.py` refuses `seal` with 2 first.
"""

import argparse
import datetime as dt
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(HERE, "..", "..", "..", "lib")

# `lib/sibling.py` loads every other module this command reads, and an
# absent one is its sentence and exit 2: here 1 means an input that could
# not be measured, and a copy of this script taken without its siblings is
# a broken plugin copy, where nothing ran (#610). Where it is absent itself,
# the refusal is the same sentence about it, spelt here because the file
# that holds the sentence is the one missing.
sys.path.insert(0, LIB)
try:
    import sibling
except ImportError:
    sys.stderr.write(
        "cannot read "
        + os.path.normpath(os.path.join(LIB, "sibling.py"))
        + ", which this command loads. It ships in the plugin beside this "
        "script; a copy of one script taken on its own is not a plugin. "
        "Nothing was read.\n"
    )
    raise SystemExit(2) from None

# The bytes-per-token ratio every token figure is estimated at. Between the
# three measured agents (2.71, 3.16, 3.44 over tree bytes; 2.87, 3.41, 3.44
# over the bytes the spawns read), and labelled `assumed` on every figure it
# produces.
ASSUMED_RATIO = 3.2

# The basis every token figure carries, the session's and each agent's.
BASIS = f"estimated ({ASSUMED_RATIO} B/token, an assumed ratio)"

# A `CLAUDE.md` import, `imports_of`'s reading of it: `@` at the start of a
# line or after whitespace, then a path a quote or a backtick does not open,
# which runs to the next whitespace except a space with a backslash before
# it. That path group is Claude Code's own (#1185). `imports_of` runs it over
# each live piece of a line, with the line's offsets, so the lookbehind still
# sees the character before the piece. Then the hops the harness follows
# (code.claude.com/docs/en/memory.md, read for #1177 and #1185); and what
# joins an imported row's name to its importer's.
IMPORT = re.compile(r"(?:^|(?<=\s))@(?![\"'`])((?:[^\s\\]|\\ )+)")
HOPS = 4
ARROW = " → "

# The session table's row for what the plugin's `SessionStart` hook prints.
HOOK_ROW = "SessionStart hook: skills/core/SKILL.md"


def _fence_rule():
    """`lib/blocks.py`, for the line split `imports_of` reads each
    `CLAUDE.md` and imported file through."""
    return sibling.load("lib/blocks.py")


def _line_reader():
    """`lib/lines.py`, for the scan of fences, HTML comments and code spans
    `imports_of` asks for each `CLAUDE.md` and imported file that exists
    (#1185)."""
    return sibling.load("lib/lines.py")


def _core():
    """`lib/core.py` of the plugin around this script, the one definition of
    what the core hook prints."""
    return sibling.load("lib/core.py")


# --- the tree -----------------------------------------------------------------


def plugin_root():
    """`skills/verify/scripts/` → the plugin root, wherever the copy lives."""
    return os.path.abspath(os.path.join(HERE, "..", "..", ".."))


def _shown(path):
    """The path relative to the working directory where that spelling
    exists, else as given. A relative spelling is a courtesy: on Windows
    `relpath` raises `ValueError` for a path on another drive than the
    working directory (#329's Windows leg — the pytest temp dir on `C:`, the
    checkout on `D:`), and a meter that dies there has measured nothing."""
    try:
        return os.path.relpath(path)
    except ValueError:
        return path


def frontmatter(text):
    """The `name:` and `skills:` an agent definition's frontmatter declares.

    `skills:` is read in every spelling YAML gives the same list: a block
    sequence, indented or not, and the flow form on one line — `[a, b]` or
    `a, b`. The one-line form used to read as no skills at all, silently, so
    the meter measured such a definition as its whole payload and the check
    that shares this parser had nothing to check (#292 round 1).

    A line ends at LF, CR or CRLF, YAML 1.2's line breaks. `read` decodes
    the bytes as they are, so the text is taken through universal newlines
    here and split at LF alone, as `deferral_check.py#runners_in` splits,
    and an entry holding U+2028, which `str.splitlines` also ends a line
    at, reads whole (#1198)."""
    name, skills = None, []
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if not text.startswith("---"):
        return name, skills
    end = text.find("\n---", 3)
    block = text[3:end] if end != -1 else text[3:]
    in_skills = False
    for line in block.split("\n"):
        if re.match(r"^name:\s*\S", line):
            name = line.split(":", 1)[1].strip()
            in_skills = False
        elif re.match(r"^skills:\s*\S", line):
            inline = line.split(":", 1)[1].strip()
            if inline.startswith("[") and inline.endswith("]"):
                inline = inline[1:-1]
            skills.extend(
                s.strip().strip("'\"") for s in inline.split(",") if s.strip()
            )
            in_skills = False
        elif re.match(r"^skills:\s*$", line):
            in_skills = True
        elif in_skills and re.match(r"^\s*-\s*\S", line):
            skills.append(line.split("-", 1)[1].strip().strip("'\""))
        elif re.match(r"^\S", line):
            in_skills = False
    return name, skills


def read(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw, raw.decode("utf-8", errors="replace")


def file_row(root, rel, display, share):
    path = os.path.join(root, rel)
    row = {"path": display, "share": share}
    if not os.path.isfile(path):
        row.update({"bytes": 0, "chars": 0, "missing": True})
        return row
    raw, text = read(path)
    row.update({"bytes": len(raw), "chars": len(text)})
    return row


def imports_of(path, home, depth=HOPS, seen=None):
    """`[(chain, real_path)]`: every file the file at `path` imports, depth
    first, as code.claude.com/docs/en/memory.md resolves them (#1177,
    `frame/design.md` *Scope* item 5).

    An import is read in the file's live text alone (#1185), the docs'
    "Import parsing skips Markdown code spans and fenced code blocks". Live
    text is text outside a fenced code block, an HTML comment and a code
    span, as `lib/lines.py#live_pieces` places them with spans read
    across the lines of a paragraph; a fence or a comment nobody closed
    hides the rest of the file. There an import is `@` at the start of a
    line or after whitespace, then a path (`IMPORT`). The path runs to the
    next whitespace or the end of its live piece, and a backslash before a
    space keeps it going, the docs' "put a backslash before each space". The
    target is the path with each `\\ ` read as a space, and `chain` keeps
    the backslash. A path that opens with a quote or a backtick is not one.
    A leading `~` is `home`, the home the meter was given, never the
    process's. Any other relative path resolves against the directory of
    the file that holds the line, at every hop. `chain` is the path of each
    hop as written, so the last entry is this import's own.

    At most `depth` hops, four by the docs. A real path in `seen` is skipped,
    and each one found is added to it, so one file imported twice, or a cycle,
    is read once. A target that is not a file is returned, for its row to say
    `missing`, and is not followed.

    **What this does not model.** Claude Code 2.1.318's reader goes past
    its docs, and the meter follows the docs (#1185, `frame/questions.md`
    Q1). The harness also reads no import in an indented code block, in an
    HTML block other than a comment or in a YAML frontmatter block, and the
    meter reads one in each. The harness cuts a path at its first `#`, and
    the meter keeps the `#` and what follows it. The harness refuses a path
    by its first character and skips an imported file whose extension is
    not text, and the meter follows either.

    Two differences come from the shared scan, `lib/lines.py#_scan`,
    which keeps no model of markdown's blocks. Its fence rule reads each
    line with no list item or block quote around it. So it opens no fence
    behind `>` or a list marker, and the meter reads an import inside such
    a fence. And it reads that fence's closing line as an opener where the
    line stands within three spaces of the margin. From there the meter's
    fences stand out of step with the file's, until a later fence line
    happens to bring them back or the file ends. Live text can be hidden,
    and what a later fence quotes can be read. The scan also opens a
    comment at every `<!--` in live text and closes it at the next `-->`,
    however far below. CommonMark reads a `<!--` as text where it neither
    opens a line nor has its `-->` in the same paragraph: inside a
    paragraph without that `-->`, or after a comment that closed on its
    line. There the meter hides the imports up to the next `-->`, or to the
    end of the file where none follows, and the harness reads them.

    And the meter reads no import whose `@` follows a code span, a comment,
    emphasis or a link with no whitespace between them, where the harness
    can begin a text token with the `@`."""
    seen = set() if seen is None else seen
    if depth <= 0 or not os.path.isfile(path):
        return []
    rule = _fence_rule()
    lines = rule.gfm_lines(read(path)[1])
    found = (
        match.group(1)
        for line, pieces in zip(
            lines,
            _line_reader().live_pieces(lines, spans_cross_lines=True),
            strict=True,
        )
        for start, end in pieces
        for match in IMPORT.finditer(line, start, end)
    )
    out = []
    for written in found:
        target = written.replace("\\ ", " ")
        if target == "~" or target.startswith("~/"):
            target = os.path.join(home, target[2:])
        real = os.path.realpath(os.path.join(os.path.dirname(path), target))
        if real in seen:
            continue
        seen.add(real)
        out.append(((written,), real))
        for chain, deeper in imports_of(real, home, depth - 1, seen):
            out.append(((written, *chain), deeper))
    return out


def user_dir(home, config):
    """`(directory, label)`: the user's config directory, where Claude Code
    keeps the user's `CLAUDE.md` and user skills (#1367), and the label its
    rows carry. `config` is `CLAUDE_CONFIG_DIR` as the caller read it; where
    it is `None` or empty, the directory is `home`'s `.claude`, labelled
    `~/.claude`, as the shell's `${CLAUDE_CONFIG_DIR:-$HOME/.claude}` reads
    it. Otherwise it is `config`, labelled `$CLAUDE_CONFIG_DIR`, so no
    account name reaches a table or the JSON. A `@~/` import is not under
    it: `imports_of` resolves `~` against `home`."""
    if config:
        return config, "$CLAUDE_CONFIG_DIR"
    return os.path.join(home, ".claude"), "~/.claude"


def composition(root, home, name, definition, user=None):
    """The rows of one agent's payload, in the order the harness lays them
    out: the definition, each skill, then the harness's `CLAUDE.md` pair with
    its imports (`pair_rows`). A skill's shadow is read in `user`, the pair
    `user_dir` returns. No row is the core hook's: its output reaches no
    subagent.

    `user` left out is `user_dir(home, None)`, because the release report
    the plugin's repository runs in CI, `.github/scripts/release_report.py`,
    calls this with four arguments."""
    user = user or user_dir(home, None)
    directory, label = user
    _name, skills = frontmatter(read(os.path.join(root, definition))[1])
    rows = [file_row(root, definition, definition, "agent")]
    for skill in skills:
        rel = os.path.join("skills", skill, "SKILL.md")
        row = file_row(root, rel, rel.replace(os.sep, "/"), "agent")
        shadow = os.path.join(directory, "skills", skill, "SKILL.md")
        if os.path.isfile(shadow):
            row["shadow"] = {
                "path": f"{label}/skills/{skill}/SKILL.md",
                "bytes": len(read(shadow)[0]),
            }
        rows.append(row)
    return rows + pair_rows(root, home, user)


def pair_rows(root, home, user):
    """The harness's `CLAUDE.md` pair, the repository's and the one in
    `user`, the pair `user_dir` returns, each file followed by the files its
    `@` lines import (`imports_of`, against `home`). An imported row is the
    importer's name, an arrow and each hop as written, with `via` naming the
    file that holds its line; one real path is one row across the pair, and
    a file of the pair is never a row of the other's."""
    directory, label = user
    rows = []
    pair = (
        (os.path.join(root, "CLAUDE.md"), "CLAUDE.md"),
        (os.path.join(directory, "CLAUDE.md"), f"{label}/CLAUDE.md"),
    )
    seen = {os.path.realpath(path) for path, _display in pair}
    for path, display in pair:
        rows.append(
            file_row(
                os.path.dirname(path),
                os.path.basename(path),
                display,
                "harness",
            )
        )
        for chain, real in imports_of(path, home, seen=seen):
            row = file_row(
                os.path.dirname(real),
                os.path.basename(real),
                ARROW.join((display, *chain)),
                "harness",
            )
            row["via"] = ARROW.join((display, *chain[:-1]))
            rows.append(row)
    return rows


def _estimated(rows):
    """`{"files": rows, "total": total}`, each row given its tokens, its
    bytes over `ASSUMED_RATIO`, and `BASIS`. The total sums the rows' bytes,
    characters and tokens, so the token column a reader adds up is the
    total under it."""
    for row in rows:
        row["tokens"] = round(row["bytes"] / ASSUMED_RATIO)
        row["basis"] = BASIS
    total = {key: sum(row[key] for row in rows) for key in ("bytes", "chars", "tokens")}
    total["basis"] = BASIS
    return {"files": rows, "total": total}


def session_composition(root, home, user):
    """The rows of a session's prefix in the tree at ROOT: the `CLAUDE.md`
    pair with its imports (`pair_rows`, with `user` the pair `user_dir`
    returns), then `HOOK_ROW`, share `hook`, whose bytes and characters are
    `lib/core.py#rendered` for the core `lib/core.py#origin` names in ROOT,
    header and closing line included: what a session in ROOT receives where
    ROOT holds a `seal/` root. Where ROOT
    holds no core to print, as a release before the hook does, the row is 0
    bytes marked `missing`: the hook's one-line refusal is printed only by a
    tree that has the hook. Every token figure is `_estimated`'s."""
    core = _core()
    rows = pair_rows(root, home, user)
    hook = {"path": HOOK_ROW, "share": "hook"}
    path = core.origin(root, root)
    if os.path.isfile(path):
        printed = core.rendered(path, root)
        hook.update({"bytes": len(printed.encode("utf-8")), "chars": len(printed)})
    else:
        hook.update({"bytes": 0, "chars": 0, "missing": True})
    rows.append(hook)
    return _estimated(rows)


def agents_in(root, only=()):
    directory = os.path.join(root, "agents")
    found = {}
    if not os.path.isdir(directory):
        return found
    for entry in sorted(os.listdir(directory)):
        if not entry.endswith(".md"):
            continue
        rel = os.path.join("agents", entry)
        name, _skills = frontmatter(read(os.path.join(root, rel))[1])
        name = name or entry[: -len(".md")]
        if only and name not in only:
            continue
        found[name] = rel.replace(os.sep, "/")
    return found


# --- the measurement ----------------------------------------------------------


def measure(root, home, agents=(), config=None):
    """The whole reading as data. `config` is `CLAUDE_CONFIG_DIR` as the
    caller read it, and `user_dir` places the user's files from it and
    `home`; a call that passes none reads only the `home` it was given."""
    user = user_dir(home, config)
    out = {
        "measured_at": dt.date.today().isoformat(),
        "root": _shown(root),
        "session": session_composition(root, home, user),
        "agents": {},
    }
    for name, definition in agents_in(root, agents).items():
        out["agents"][name] = _estimated(
            composition(root, home, name, definition, user)
        )
    return out


# --- the report ---------------------------------------------------------------


def _n(value):
    return f"{value:,}" if isinstance(value, int) else str(value)


def render(data):
    lines = [f"# seal payload — {data['root']} ({data['measured_at']})", ""]
    session = data.get("session")
    if session:
        lines += _session_lines(session)
    for name, agent in data["agents"].items():
        lines += [f"## {name}", ""]
        lines += ["| File | Bytes | Chars | Tokens | Basis |", "|---|---|---|---|---|"]
        pair = []
        for row in agent["files"]:
            if row["share"] == "harness":
                pair.append(row)
                continue
            lines.append(_file_line(row))
        if pair:
            names = " + ".join(f"`{p['path']}`" for p in pair)
            lines.append(
                f"| CLAUDE.md pair ({names}) | {_n(sum(p['bytes'] for p in pair))} | "
                f"{_n(sum(p['chars'] for p in pair))} | "
                f"{_n(sum(p['tokens'] for p in pair))} | {pair[0]['basis']} — inside "
                f"every agent's prefix |"
            )
            for row in pair:
                if row.get("missing"):
                    lines.append(
                        f"| &nbsp;&nbsp;`{row['path']}` | 0 | 0 | 0 | missing |"
                    )
                elif "via" in row:
                    lines.append(
                        f"| &nbsp;&nbsp;`{row['path']}` | {_n(row['bytes'])} | "
                        f"{_n(row['chars'])} | {_n(row['tokens'])} | "
                        f"{row['basis']} — imported by `{row['via']}` |"
                    )
        total = agent["total"]
        lines.append(
            f"| **total** | {_n(total['bytes'])} | {_n(total['chars'])} | "
            f"{_n(total['tokens'])} | {total['basis']} |"
        )
        lines.append("")
    return "\n".join(lines)


def _session_lines(session):
    """The session's table: one line per file of the pair, each import under
    its importer, then the core hook's row and the total."""
    lines = [
        "## session",
        "",
        "What a session started in this tree reads before its first prompt: "
        "the `CLAUDE.md` pair with the files its `@` lines import, and the core "
        "the plugin's `SessionStart` hook prints where the repository holds a "
        "`seal/` root. No subagent receives the hook's output, so no agent's "
        "table below carries it.",
        "",
        "| File | Bytes | Chars | Tokens | Basis |",
        "|---|---|---|---|---|",
    ]
    for row in session["files"]:
        name = f"`{row['path']}`"
        if "via" in row:
            name = f"&nbsp;&nbsp;{name}"
        if row.get("missing"):
            why = (
                " — no `skills/core/SKILL.md` in this tree, so no hook prints one"
                if row["share"] == "hook"
                else ""
            )
            lines.append(f"| {name} | 0 | 0 | 0 | missing{why} |")
            continue
        note = ""
        if "via" in row:
            note = f" — imported by `{row['via']}`"
        elif row["share"] == "hook":
            note = (
                " — what the `SessionStart` hook prints: its first line, the "
                "core below its frontmatter and its closing line"
            )
        lines.append(
            f"| {name} | {_n(row['bytes'])} | {_n(row['chars'])} | "
            f"{_n(row['tokens'])} | {row['basis']}{note} |"
        )
    total = session["total"]
    lines += [
        f"| **total** | {_n(total['bytes'])} | {_n(total['chars'])} | "
        f"{_n(total['tokens'])} | {total['basis']} |",
        "",
    ]
    return lines


def _file_line(row):
    if row.get("missing"):
        return f"| `{row['path']}` | 0 | 0 | 0 | missing — named by `skills:`, not in the tree |"
    note = ""
    if "shadow" in row:
        note = (
            f" — shadowed on this machine by `{row['shadow']['path']}` "
            f"({_n(row['shadow']['bytes'])} B)"
        )
    return (
        f"| `{row['path']}` | {_n(row['bytes'])} | {_n(row['chars'])} | "
        f"{_n(row['tokens'])} | {row['basis']}{note} |"
    )


# --- entry --------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", default=plugin_root())
    parser.add_argument("--agent", action="append", default=[])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    data = measure(
        os.path.abspath(args.root),
        os.path.expanduser("~"),
        agents=tuple(args.agent),
        config=os.environ.get("CLAUDE_CONFIG_DIR"),
    )
    if not data["agents"]:
        print(f"seal payload: no agents/*.md under {args.root}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(render(data))
    return 0


if __name__ == "__main__":
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    sys.exit(main())
