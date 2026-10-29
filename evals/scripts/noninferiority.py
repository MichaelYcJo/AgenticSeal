#!/usr/bin/env python3
"""Run the behaviour suite on one side, and judge a new side against a baseline.

  noninferiority.py run --agent A (--rev REV | --tree DIR) --out FILE.json
      [--runs 2] [-j 4] [--max-cost-usd USD] [--case GLOB] [--suite-rev HEAD]
  noninferiority.py run --from-raw FILE.raw --out FILE.json
  noninferiority.py compare --agent A --phase N --old OLD.json --new NEW.json
      --out RECORD.md
  noninferiority.py check RECORD.md
  noninferiority.py model RECORD.md
  noninferiority.py regrade --side IN.json --suite-rev REV --out OUT.json

`run` copies the plugin tree at REV (or DIR) into a temporary directory,
puts the suite at SUITE-REV's `evals/behaviour/` into it, and runs
`claude plugin eval` over `evals/behaviour/<A>/` there. **What the runs paid
for is saved before anything reads it**: the eval's JSON, every run's trace
and the measured preload go to `<out>.raw/` beside `--out`, and only then is
each directory the eval kept removed. `--out` is the saved side with these
additions under `agentic`: the preload's hashes and bytes, each run's
`report_text` (the round record its session printed, whole, with what
the `real_identifiers` census in `tests/censuses.py` refuses masked), cost (its trace's
`result` event: `total_cost_usd`, `duration_ms`, `modelUsage`) and tool
calls (every `tool_use` block in its trace), and whether the side was cut
short. `run --from-raw` writes `--out` again from a saved side, with no
eval run.

A side is read whenever it is compared or regraded. Each run's finding rows
are the `### ` sections of the one `## Findings` section of its
`report_text`, split by `chain_check.py#finding_spans` over the lines the
check's shared reader leaves (`finding_rows`), so a correction to that
reader applies to every side that keeps its text. A `truth-` grader over a
round record is read from those rows, for recall and for the false count
alike. `compare` and `regrade` refuse, with exit 2, a side any run of which
keeps no `report_text`: such a side was read by the reader before #986 and
cannot be read again.

`regrade` writes a saved side again under the `truth-` graders of the suite
at REV, with no eval run: each run's truth result is the grader's regex
searched over its finding rows, and the scores follow. It refuses a side
whose own suite does not give back, from each run's whole `report_text`,
the truth results it recorded, and a suite at REV that differs from the
side's in anything but `truth-` graders or holds other cases.
`compare` writes the record the
five pass rules judge, outcome first and then cost, each against the
baseline: recall not fallen, except by one find where every truth grader
that lost it is still found by at least one new run, the false-finding rate
within `FALSE_MARGIN`
of the baseline's, the shape and reach graders both sides ran passing,
pooled, no fewer runs on the new side than on the baseline, with none of
them failing every new run where the baseline passed it, the preload's
bytes below the baseline's, and either the tokens read across every model
or those tokens per tool call within `TOKEN_MARGIN` of the baseline's.
Tokens per true find, spend and wall seconds are written and judge nothing.
`check` recomputes a record's verdict from its numbers.
`model` reads a record whose `--old` was the Opus side and `--new` the
Sonnet side, and prints `sonnet` only where no truth, shape or reach grader
passes on the Sonnet side less often and its spend is lower, else `opus`;
then one line saying why. The record's own verdict does not decide it.

Exit codes: 0 written, the record's verdict holds, or a model was decided ·
1 the record's verdict is not `pass`, or it disagrees with its numbers · 2
nothing ran (arguments, a missing tool, an unreadable input), `model` was
handed a record that disagrees with its numbers or ran two suites,
`compare` or `regrade` refused a side read before #986, naming its file, or
`regrade` refused a side, naming the case.
"""

import argparse
import copy
import functools
import hashlib
import importlib.util
import io
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import replay_targets as rt

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
SUITE = "evals/behaviour"
AGENTS = ("proofer", "crafter", "framer", "sealer", "tracer")
CLT_GIT = "/Library/Developer/CommandLineTools/usr/bin/git"
# The end of a round record's path: `round-N.md`, or `<...>-report.md` on a
# run taken before 0.22.0. A side keeps the record a session printed from
# such a path, and a `truth-` grader over such a path is read from it.
RECORD_PATH = r"(?:-report|/round-\d+)\.md"
# The census module whose `real_identifiers` every committed file is held
# to, which masks the record a side keeps (`masked`).
SCAN = os.path.join(ROOT, "tests", "censuses.py")
UNREAD = (
    "keeps no report_text, so the side was read by the reader before #986 "
    "and cannot be read again"
)
FALSE_MARGIN = 0.05
# Rule 5's margin on both of its figures, the total tokens and the tokens
# per tool call. Two takes of one `writing-style` text differed by 6.8 points
# of tokens per tool call, *Not done* of
# 0ed5dd3b:seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md
# and 0.07 is the smallest whole percent that covers that spread.
TOKEN_MARGIN = 0.07
# The three counts of a model's `modelUsage` entry a run read.
READ_COUNTS = ("inputTokens", "cacheCreationInputTokens", "cacheReadInputTokens")
COST_FIELDS = (
    "old_spend",
    "new_spend",
    "old_tokens",
    "new_tokens",
    "old_calls",
    "new_calls",
    "old_seconds",
    "new_seconds",
    "old_bytes",
    "new_bytes",
)
VERDICTS = ("pass", "fail", "no result")


# --- the preload a side measured -------------------------------------------


def preload_files(tree, agent):
    """The files AGENT's spawn preloads in TREE: its definition and every
    skill its `skills:` frontmatter lists.

    A definition with no frontmatter stops the run."""
    rel = f"agents/{agent}.md"
    with open(os.path.join(tree, rel), encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"---\n(?P<head>.*?)\n---\n", text, re.S)
    if not m:
        raise SystemExit(f"{rel} has no frontmatter")
    skills = re.search(
        r"^skills:\n(?P<items>(?:[ \t]+- .*\n?)+)", m["head"] + "\n", re.M
    )
    names = re.findall(r"- (\S+)", skills["items"]) if skills else []
    return [rel, *(f"skills/{n}/SKILL.md" for n in names)]


def preload_hashes(tree, agent):
    """`{path: sha256}` of AGENT's preload in TREE.

    A missing file stops the run."""
    out = {}
    for rel in preload_files(tree, agent):
        with open(os.path.join(tree, rel), "rb") as f:
            out[rel] = hashlib.sha256(f.read()).hexdigest()
    return out


def preload_bytes(tree, agent):
    """The bytes of AGENT's preload in TREE, every file summed.

    A missing file stops the run."""
    return sum(
        os.path.getsize(os.path.join(tree, rel)) for rel in preload_files(tree, agent)
    )


# --- run --------------------------------------------------------------------


def git_bytes(*args):
    """`git -C ROOT <args>`'s stdout as bytes.

    A non-zero exit stops the run."""
    run = subprocess.run(["git", "-C", ROOT, *args], capture_output=True)
    if run.returncode != 0:
        raise SystemExit(
            f"git {' '.join(args)}: {run.stderr.decode('utf-8', 'replace')}"
        )
    return run.stdout


def extract(rev, paths, into):
    """Write REV's PATHS (the whole tree when empty) under INTO.

    A member that would land outside INTO stops the run."""
    data = git_bytes("archive", "--format=tar", rev, *paths)
    with tarfile.open(fileobj=io.BytesIO(data)) as tar:
        tar.extractall(into, filter="data")


def side_path(tree, base_path):
    """The PATH a side runs under: the tree's `bin/`, its `.shims/`, then
    BASE_PATH without any installed plugin's `bin/`.

    An entry is compared in the platform's own spelling, so a Windows entry
    under `\\.claude\\plugins\\cache\\` is dropped as a POSIX one is."""
    cache = os.path.normcase(os.path.join(os.sep, ".claude", "plugins", "cache", ""))
    kept = [
        p for p in base_path.split(os.pathsep) if p and cache not in os.path.normcase(p)
    ]
    return os.pathsep.join(
        [os.path.join(tree, "bin"), os.path.join(tree, ".shims"), *kept]
    )


def write_git_shim(tree):
    """Where `/usr/bin/git` is Xcode's stub, which the eval's sandbox stops,
    put a `git` under the tree's `.shims/` that runs the Command Line Tools'
    binary directly.

    No such binary writes no shim."""
    if sys.platform != "darwin" or not os.path.isfile(CLT_GIT):
        return
    shims = os.path.join(tree, ".shims")
    os.makedirs(shims, exist_ok=True)
    path = os.path.join(shims, "git")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f'#!/bin/sh\nexec {CLT_GIT} "$@"\n')
    os.chmod(path, 0o755)


@functools.cache
def identifier_scan():
    """`tests/censuses.py` as a module, loaded by its path. It imports
    nothing from `tests/conftest.py`, which needs pytest, and a side's run
    has no pytest.

    A census module that will not load stops the run."""
    spec = importlib.util.spec_from_file_location("agentic_identifier_scan", SCAN)
    scan = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scan)
    return scan


def masked(text):
    """TEXT with what the identifier scan refuses in a committed file
    replaced, line by line as the scan reads a file and by the scan's own
    functions: each user path by its fixture path, then each host by its
    fixture host; then `apart`, for what the scan refuses only in the
    side's JSON form.

    A `location:` value never starts with `/` and names no host, so no
    finding row changes."""
    scan = identifier_scan()
    lines = []
    for line in text.split("\n"):
        for refused, fixture in (
            (scan.refused_user_paths, scan.ALLOWED_USER_PATH),
            (scan.refused_domains, scan.FIXTURE_DOMAIN),
        ):
            for m in reversed(refused(line)):
                line = line[: m.start()] + fixture + line[m.end() :]
        lines.append(line)
    return apart("\n".join(lines), scan)


def apart(text, scan):
    """TEXT with one space set beside each character a side's JSON writes
    as an escape, where the scan's functions refuse a host or a user path
    in that JSON form and the refused match takes in part of the escape.
    The space goes after the character where the match starts inside its
    escape, a host whose first letter the scan reads from the escape, and
    before it where the match runs into the escape, a user path whose name
    the scan reads from the escape's backslash. The JSON form is the one
    `write_side` writes, with `ensure_ascii` off.

    A refusal no escape is part of is left as it is, and no more spaces are
    set than TEXT has characters."""
    for _ in range(len(text) + 1):
        spans, at = [], 0
        for ch in text:
            width = len(json.dumps(ch, ensure_ascii=False)) - 2
            spans.append((at, at + width))
            at += width
        form = json.dumps(text, ensure_ascii=False)[1:-1]
        found = sorted(
            [*scan.refused_domains(form), *scan.refused_user_paths(form)],
            key=lambda m: m.start(),
        )
        hit = next(
            (
                i + 1 if a < m.start() else i
                for m in found
                for i, (a, b) in enumerate(spans)
                if b - a > 1 and a < m.end() and b > m.start()
            ),
            None,
        )
        if hit is None:
            break
        text = text[:hit] + " " + text[hit:]
    return text


def finding_rows(text):
    """One row for each finding of the round record TEXT: the finding's
    `location:` lines joined by a newline, or the empty string where it has
    none. A finding is a `### ` section of the one `## Findings` section,
    split by `chain_check.py#finding_spans` over the lines its shared reader
    leaves, so a line in a fence is no line and a comment is text (#1012). A
    section the check would refuse is still one row.

    A record the check cannot read or cannot split is one production reads
    as no finding: one holding a fence that never closes
    (`chain_check.py#unclosed`), after whose opener no reading is certain to
    find every finding, and one with no `## Findings` section or with two,
    which `finding_spans` refuses. It gives one empty row for each raw line
    at the finding heading level, a fenced one included, so every one is
    false, the count errs toward more false rows, and an empty row finds no
    truth."""
    check, reader = rt.record_reader()
    lines = reader.readable(text)
    _section, spans, error = check.finding_spans(reader, lines)
    if error or check.unclosed(reader, text, ""):
        return [
            ""
            for line in reader.gfm_lines(text)
            if reader.heading_level(line) == check.FINDING_LEVEL
        ]
    return [
        "\n".join(
            line
            for line in lines[first:stop]
            if check.label_of(line) == check.LOCATION_ROW
        )
        for first, stop in spans
    ]


def text_of(case, i, run):
    """The record run I of CASE kept, `report_text`.

    A run that keeps none raises ValueError naming the case and the run."""
    text = (run.get("agentic") or {}).get("report_text")
    if not isinstance(text, str):
        raise ValueError(f"{case}, run {i}, {UNREAD}")
    return text


def reads_record(grader):
    """True for a `truth-` grader whose regex reads a round record, the file
    `finding_rows` reads; a truth over another file keeps the eval's
    result."""
    config = grader.get("config") or {}
    path = (config.get("target") or {}).get("path") or ""
    return (
        kind(grader["name"]) == "truth"
        and grader.get("type") == "regex"
        and re.search(rf"{RECORD_PATH}$", path) is not None
    )


def report_text(trace_path):
    """The round record the run's session printed with `cat <…/round-N.md>`
    (`<…-report.md>` on a run taken before 0.22.0), the last such print
    winning, `masked`.

    Only an event whose `message` is an object with a list `content` holds
    tool calls; a line that is not a JSON object, a `message` that is a
    string (a `permission_denied` event's) and a string `content` are
    skipped. A run that printed no record keeps the empty string."""
    commands, last = {}, ""
    with open(trace_path, encoding="utf-8") as f:
        for line in f:
            try:
                event = json.loads(line)
            except ValueError:
                continue
            if not isinstance(event, dict) or event.get("parent_tool_use_id"):
                continue
            message = event.get("message")
            content = message.get("content") if isinstance(message, dict) else None
            for block in content if isinstance(content, list) else []:
                if not isinstance(block, dict):
                    continue
                if block.get("type") == "tool_use" and block.get("name") == "Bash":
                    commands[block.get("id")] = block.get("input", {}).get(
                        "command", ""
                    )
                if block.get("type") == "tool_result":
                    command = commands.get(block.get("tool_use_id"), "")
                    if re.match(
                        rf"\s*cat \S+{RECORD_PATH}\s*$", command
                    ) and not block.get("is_error"):
                        content = block.get("content")
                        if isinstance(content, list):
                            content = "\n".join(
                                c.get("text", "")
                                for c in content
                                if isinstance(c, dict)
                            )
                        last = content or ""
    return masked(last)


def run_cost(trace_path):
    """`{"total_cost_usd", "duration_ms", "modelUsage"}` from the session's
    last `result` event in the run's trace, or None where it has none.

    `modelUsage` holds every model's tokens, the spawned agent's among
    them; the event's `usage` counts the case session alone and is not
    read. A subagent's event, one carrying `parent_tool_use_id`, is not the
    session's; a line that is not a JSON object is skipped; a field the
    event lacks is None, never zero."""
    cost = None
    with open(trace_path, encoding="utf-8") as f:
        for line in f:
            try:
                event = json.loads(line)
            except ValueError:
                continue
            if not isinstance(event, dict) or event.get("parent_tool_use_id"):
                continue
            if event.get("type") != "result":
                continue
            cost = {
                k: event.get(k) for k in ("total_cost_usd", "duration_ms", "modelUsage")
            }
    return cost


def tool_calls(trace_path):
    """The tool calls a run made: every `tool_use` block in its trace, the
    case session's and the spawned agent's alike, a block an event repeats
    counted once by its id; or None where the trace cannot be read or holds
    none.

    Rule 5 reads this count with the total tokens. A run's tokens are about
    its calls times the context each call carries, and the rewrite controls
    the context while how many calls an agent makes is its behaviour, which
    the outcome rules judge. So rule 5 fails a side only where its total and
    its tokens per call both rose: fewer calls raise the figure per call and
    more calls raise the total, and the count moves the verdict in neither
    direction. Tokens per true find was weighed and not chosen: its
    divisor is the recall, which moves by a find or two between runs of the
    same agent (owner, 2026-10-17). A line that is not a JSON object is
    skipped; no count is never zero calls."""
    seen, count = set(), 0
    try:
        with open(trace_path, encoding="utf-8") as f:
            for line in f:
                try:
                    event = json.loads(line)
                except ValueError:
                    continue
                message = event.get("message") if isinstance(event, dict) else None
                content = message.get("content") if isinstance(message, dict) else None
                for block in content if isinstance(content, list) else []:
                    if not isinstance(block, dict) or block.get("type") != "tool_use":
                        continue
                    ident = block.get("id")
                    if ident is not None:
                        if ident in seen:
                            continue
                        seen.add(ident)
                    count += 1
    except OSError:
        return None
    return count or None


def tokens_read(model_usage):
    """The tokens a run read across every model of MODEL_USAGE: input,
    cache creation and cache read, summed.

    No model, a model that is not an object, or a model missing one of the
    three counts gives None, never a smaller figure."""
    if not isinstance(model_usage, dict) or not model_usage:
        return None
    total = 0
    for model in model_usage.values():
        if not isinstance(model, dict):
            return None
        counts = [model.get(k) for k in READ_COUNTS]
        if not all(isinstance(c, int) and not isinstance(c, bool) for c in counts):
            return None
        total += sum(counts)
    return total


def kept_root(trace_path):
    """The directory a kept run lives in, or None when the trace sits
    anywhere but `<tmp>/e-*/out/` or `<tmp>/claude-eval-*/out/`."""
    root = os.path.dirname(os.path.dirname(trace_path))
    name = os.path.basename(root)
    if os.path.basename(os.path.dirname(trace_path)) != "out":
        return None
    if not (name.startswith("e-") or name.startswith("claude-eval-")):
        return None
    return root


def remove_kept(root):
    """Remove a kept run's directory, which the eval leaves read-only.

    Each directory is opened before it is walked; a path already gone is
    skipped."""
    for path in (root, os.path.join(root, "sealed")):
        try:
            os.chmod(path, stat.S_IRWXU)
        except OSError:
            pass
    for directory, dirs, _files in os.walk(root, topdown=True):
        for d in dirs:
            try:
                os.chmod(os.path.join(directory, d), stat.S_IRWXU)
            except OSError:
                pass
    shutil.rmtree(root, ignore_errors=True)


def runs_of(result):
    """`[(key, run)]` for every run of an eval result, KEY its position."""
    out = []
    for c, case in enumerate(result.get("cases", [])):
        for arm, runs in sorted(case.get("arms", {}).items()):
            out += [(f"{c}|{arm}|{i}", run) for i, run in enumerate(runs)]
    return out


def saved_dir(out):
    """The directory a side's paid output is saved in, beside OUT."""
    return os.path.splitext(out)[0] + ".raw"


def save_side(raw, saved, meta):
    """Save what a side's runs paid for into SAVED, then remove each kept
    run: the eval's JSON byte for byte, every trace under `traces/`, and
    META with the trace each run's position maps to.

    A run whose trace is missing maps to none."""
    os.makedirs(os.path.join(saved, "traces"), exist_ok=True)
    shutil.copyfile(raw, os.path.join(saved, "raw.json"))
    with open(raw, encoding="utf-8") as f:
        result = json.load(f)
    traces, kept = {}, []
    for n, (key, run) in enumerate(runs_of(result)):
        trace = run.get("tracePath") or ""
        if trace and os.path.isfile(trace):
            rel = f"traces/{n:03d}.jsonl"
            shutil.copyfile(trace, os.path.join(saved, rel))
            traces[key] = rel
            kept.append(kept_root(trace))
    meta = dict(meta, traces=traces)
    with open(os.path.join(saved, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=1)
        f.write("\n")
    for root in kept:
        if root:
            remove_kept(root)


def annotate(saved):
    """The side SAVED holds, with `agentic` added: the preload's hashes and
    bytes, each run's `report_text`, cost and tool calls read from its saved
    trace, and whether the side was cut short.

    A run with no saved trace keeps the empty string and no cost, and a
    run's error makes the side cut short."""
    with open(os.path.join(saved, "raw.json"), encoding="utf-8") as f:
        result = json.load(f)
    with open(os.path.join(saved, "meta.json"), encoding="utf-8") as f:
        meta = json.load(f)
    cut = bool(result.get("partial"))
    for key, run in runs_of(result):
        rel = meta["traces"].get(key)
        trace = os.path.join(saved, rel) if rel else None
        run["agentic"] = {
            "report_text": report_text(trace) if trace else "",
            "cost": run_cost(trace) if trace else None,
            "tool_calls": tool_calls(trace) if trace else None,
        }
        if run.get("error"):
            cut = True
    result["agentic"] = {
        "agent": meta["agent"],
        "preload": meta["preload"],
        "preload_bytes": meta.get("preload_bytes"),
        "cut_short": cut,
        "rev": TREE_REV if os.path.isabs(meta["rev"]) else meta["rev"],
        "suite_rev": meta["suite_rev"],
        "suite_tree": meta.get("suite_tree"),
    }
    return result


def write_side(saved, out):
    """Write OUT from the side SAVED holds."""
    result = annotate(saved)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=1, ensure_ascii=False)
        f.write("\n")
    return 0


def call_eval(command, env):
    """Run `claude plugin eval` as COMMAND under ENV.

    A machine with no `claude` stops the run before anything is spent."""
    if not shutil.which("claude", path=env.get("PATH")):
        print("claude is not on PATH", file=sys.stderr)
        raise SystemExit(2)
    subprocess.run(command, env=env)


# What a `--tree` side records as its `rev`. A machine path would put the
# account name into a committed record, and the preload's hashes already name
# the content; a side saved with an absolute path reads back as this too.
TREE_REV = "tree"


def run_side(a):
    """`run`: one side of one agent's suite, or `--from-raw` a saved side.

    An eval that writes no JSON stops the run."""
    if a.from_raw:
        return write_side(a.from_raw, a.out)
    if not a.agent:
        raise SystemExit("run needs --agent, or --from-raw")
    work = tempfile.mkdtemp(prefix="agentic-")
    try:
        tree = os.path.join(work, "tree")
        if a.rev:
            os.makedirs(tree)
            extract(a.rev, [], tree)
        else:
            shutil.copytree(a.tree, tree, ignore=shutil.ignore_patterns(".git"))
        shutil.rmtree(os.path.join(tree, SUITE), ignore_errors=True)
        extract(a.suite_rev, [SUITE], tree)
        write_git_shim(tree)
        raw = os.path.join(work, "raw.json")
        command = [
            "claude", "plugin", "eval", tree,
            "--eval-dir", f"{SUITE}/{a.agent}",
            "--runs", str(a.runs), "-j", str(a.concurrency),
            "--ablation", "none", "--trust-plugin", "--scaffold", "--keep-temp",
            "--allow-tools", "Bash", "Write", "Edit",
            "--no-publish", "--max-cost-usd", str(a.max_cost_usd),
            "--json", raw,
            "--output-dir", os.path.join(work, "results"),
            "--report", os.path.join(work, "report.html"),
        ]  # fmt: skip
        if a.case:
            command += ["--case", a.case]
        meta = {
            "agent": a.agent,
            "preload": preload_hashes(tree, a.agent),
            "preload_bytes": preload_bytes(tree, a.agent),
            "rev": a.rev or TREE_REV,
            "suite_rev": git_bytes("rev-parse", a.suite_rev).decode("utf-8").strip(),
            "suite_tree": suite_tree(a.suite_rev, a.agent),
        }
        env = dict(os.environ, PATH=side_path(tree, os.environ.get("PATH", "")))
        call_eval(command, env)
        if not os.path.isfile(raw):
            raise SystemExit("claude plugin eval wrote no JSON")
        saved = saved_dir(a.out)
        save_side(raw, saved, meta)
        print(f"saved the side's paid output under {saved}", file=sys.stderr)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    return write_side(saved, a.out)


# --- compare: the numbers a record holds ------------------------------------


def kind(name):
    """A grader's kind, from its name's prefix, or None."""
    head = name.split("-", 1)[0]
    return head if head in ("reach", "shape", "truth") else None


def side_numbers(result):
    """`{"graders": {(case, grader): [kind, passed, runs]}, "rows", "false",
    "runs": {case: n}, "cut", "preload", "id", "spend", "tokens", "calls",
    "seconds", "bytes"}` for one side, the last five pooled over every run,
    the tokens read across every model and the calls every `tool_use` block.

    Rows and false rows are each run's `finding_rows` of its `report_text`,
    a row false where no `truth-` grader's regex finds it. A `truth-`
    grader that `reads_record` passes a run where `grade` finds it in those
    rows; every other grader keeps the result the eval recorded. A grader
    whose name carries no kind prefix is not counted. Each of spend, tokens,
    calls and seconds is None where any run lacks it, a run with no cost
    lacking the first, second and fourth, and bytes is None where the
    preload's bytes were not recorded.

    A run that keeps no `report_text`, or a grader that reads a record and
    `grade` cannot read, raises ValueError naming the case."""
    graders, runs_per_case = {}, {}
    rows = false = 0
    costs, calls = [], []
    for case in result.get("cases", []):
        name = case["name"]
        truths = [
            re.compile(g["config"]["pattern"], re.M)
            for g in case.get("graders", [])
            if kind(g["name"]) == "truth" and g.get("type") == "regex"
        ]
        read = {g["name"]: g for g in case.get("graders", []) if reads_record(g)}
        runs = case_runs(case)
        runs_per_case[name] = len(runs)
        for g in case.get("graders", []):
            k = kind(g["name"])
            if k:
                graders[(name, g["name"])] = [k, 0, len(runs)]
        for i, run in enumerate(runs):
            found = finding_rows(text_of(name, i, run))
            for g in run.get("graders", []):
                key = (name, g["name"])
                if g["name"] in read:
                    try:
                        passed = grade(read[g["name"]], found)["passed"]
                    except ValueError as e:
                        raise ValueError(f"{name}: {e}") from None
                else:
                    passed = g.get("passed")
                if key in graders and passed:
                    graders[key][1] += 1
            for row in found:
                rows += 1
                if not any(t.search(row) for t in truths):
                    false += 1
            costs.append((run.get("agentic") or {}).get("cost") or {})
            calls.append((run.get("agentic") or {}).get("tool_calls"))
    seconds = pooled(c.get("duration_ms") for c in costs)
    meta = result.get("agentic") or {}
    started = result.get("startedAt", "")
    digest = hashlib.sha256(json.dumps(result, sort_keys=True).encode()).hexdigest()[
        :12
    ]
    return {
        "graders": graders,
        "rows": rows,
        "false": false,
        "runs": runs_per_case,
        "cut": bool(meta.get("cut_short")) or bool(result.get("partial")),
        "preload": meta.get("preload", {}),
        "id": f"{started} {digest}",
        "suite": {"rev": meta.get("suite_rev"), "tree": meta.get("suite_tree")},
        "spend": pooled(c.get("total_cost_usd") for c in costs),
        "tokens": pooled(tokens_read(c.get("modelUsage")) for c in costs),
        "calls": pooled(calls),
        "seconds": seconds / 1000 if seconds is not None else None,
        "bytes": meta.get("preload_bytes"),
    }


def pooled(values):
    """The sum of VALUES, or None where there are none or any one is None."""
    values = list(values)
    if not values or any(v is None for v in values):
        return None
    return sum(values)


def suite_tree(rev, agent):
    """The git tree hash of `evals/behaviour/<agent>/` at REV: the suite's
    identity, which a commit that leaves the cases alone does not move.

    A REV or a directory git does not resolve stops the run."""
    return git_bytes("rev-parse", f"{rev}:{SUITE}/{agent}").decode("utf-8").strip()


def suite_name(suite):
    """`<commit> <tree>` for a side's suite, the form a record carries."""
    return f"{suite['rev']} {suite['tree']}"


def verdict(numbers):
    """`(verdict, [reason])` the five pass rules give NUMBERS, the merged
    `{(case, grader): (kind, old passed, old runs, new passed, new runs)}`
    under `graders` beside `old_rows`, `old_false`, `new_rows`, `new_false`,
    `old_cut`, `new_cut` and every name in `COST_FIELDS`.

    Each rule reads the new side against the baseline: 1 recall not fallen,
    except by one find where every truth grader that lost it is still found
    by at least one new run, 2 the false-finding rate within `FALSE_MARGIN`
    of the baseline's, 3 the shape and reach graders both sides ran passing,
    pooled, no fewer runs, none of them failing every new run where the
    baseline passed it, and one the baseline lacks passing every new run, 4
    the preload's bytes below the baseline's, 5 either the tokens read
    across every model or those tokens per tool call within `TOKEN_MARGIN`
    of the baseline's, so a side fails it only where both rose by more
    (`tool_calls` says why both). A missing key raises. A side cut short, a
    case the baseline ran and the new side did not, whatever its graders, a
    case run a different number of times, and a side whose tokens, tool
    calls or preload bytes are None, or whose tool calls are none, are no
    result; tokens per true find, spend and wall seconds are never judged."""
    if numbers["old_cut"] or numbers["new_cut"]:
        sides = [
            s
            for s, key in (("baseline", "old_cut"), ("new", "new_cut"))
            if numbers[key]
        ]
        return "no result", [f"the {' and '.join(sides)} side was cut short"]
    g = numbers["graders"]
    # A case the baseline ran and the new side did not is no result whatever
    # graders it carries: a case of shape and reach graders alone would
    # otherwise leave no trace in any rule below (#957 round 1, finding 2).
    old_case, new_case = {}, {}
    for (case, _name), (_k, _op, old_runs, _np, new_runs) in g.items():
        old_case[case] = max(old_case.get(case, 0), old_runs)
        new_case[case] = max(new_case.get(case, 0), new_runs)
    unrun = sorted(c for c in old_case if old_case[c] and not new_case[c])
    if unrun:
        return "no result", [
            f"the new side did not run {', '.join(unrun)}, which the baseline ran"
        ]
    # Inside a case both sides ran, a shape or reach grader one side lacks is
    # the record's shape moving between the two sides (0.22.0's round record
    # dropped two), not a case run a different number of times; rule 3 below
    # judges one the baseline lacks on the new side alone, and one the new
    # side lacks not at all.
    if any(
        old_runs != new_runs
        for k, _op, old_runs, _np, new_runs in g.values()
        if not (k in ("shape", "reach") and 0 in (old_runs, new_runs))
    ):
        return "no result", ["the two sides ran a case a different number of times"]
    unknown = [
        s
        for s, side in (("baseline", "old"), ("new", "new"))
        if any(numbers[f"{side}_{k}"] is None for k in ("tokens", "calls", "bytes"))
        or not numbers[f"{side}_calls"]
    ]
    if unknown:
        return "no result", [
            f"the {' and '.join(unknown)} side records no tokens across every "
            "model or no tool calls for every run, or no preload bytes"
        ]
    reasons = []
    truths = {key: v for key, v in g.items() if v[0] == "truth"}
    old_found = sum(v[1] for v in truths.values())
    new_found = sum(v[3] for v in truths.values())
    if new_found < old_found:
        lost = sorted(key for key, v in truths.items() if v[3] < v[1])
        noise = old_found - new_found == 1 and all(truths[key][3] >= 1 for key in lost)
        if not noise:
            names = ", ".join(f"{c}/{n}" for c, n in lost)
            reasons.append(
                f"recall fell from {old_found} to {new_found} finds: {names}"
            )
    old_rate = (
        numbers["old_false"] / numbers["old_rows"] if numbers["old_rows"] else 0.0
    )
    new_rate = (
        numbers["new_false"] / numbers["new_rows"] if numbers["new_rows"] else 0.0
    )
    if new_rate > old_rate + FALSE_MARGIN + 1e-9:
        reasons.append(f"false-finding rate rose from {old_rate:.3f} to {new_rate:.3f}")
    # Rule 3 judges the agent, not one run (#966): the passes of every shape
    # and reach grader both sides ran are pooled into one total a side, and
    # a grader the new side failed on every run, where the baseline passed
    # it at least once, is named whatever the totals say. Each grader in the
    # totals ran as many times on both sides, or the check above returned.
    common = sorted(
        (key, v) for key, v in g.items() if v[0] in ("shape", "reach") and v[2] and v[4]
    )
    old_total = sum(v[1] for _key, v in common)
    new_total = sum(v[3] for _key, v in common)
    runs = sum(v[4] for _key, v in common)
    if new_total < old_total:
        fell = ", ".join(
            f"{c}/{n} {v[3]}/{v[4]} against {v[1]}/{v[2]}"
            for (c, n), v in common
            if v[3] < v[1]
        )
        reasons.append(
            f"shape and reach graders passed {new_total}/{runs} runs on the new "
            f"side, fewer than the baseline's {old_total}/{runs} (rule 3): {fell}"
        )
    for (case, name), (k, op, oruns, np_, nruns) in common:
        if op and not np_:
            reasons.append(
                f"{k} grader {case}/{name} failed every new run (0/{nruns}) where "
                f"the baseline passed it {op}/{oruns} (rule 3)"
            )
    for (case, name), (k, _op, oruns, np_, nruns) in sorted(g.items()):
        if k in ("shape", "reach") and nruns and not oruns and np_ < nruns:
            reasons.append(
                f"{k} grader {case}/{name}, which the baseline lacks, failed on "
                f"the new side ({np_}/{nruns}) (rule 3)"
            )
    if numbers["new_bytes"] >= numbers["old_bytes"]:
        reasons.append(
            f"the new preload is {numbers['new_bytes']} bytes, not below the "
            f"baseline's {numbers['old_bytes']} (rule 4)"
        )
    # Rule 5 fails a side only where both figures rose past the margin: the
    # total, which more calls raise, and the figure per call, which fewer
    # calls raise, so the call count moves the verdict in neither direction.
    # Cross-multiplied, so a baseline of no tokens divides by no zero, and
    # the 1e-9 lets a figure exactly at the margin pass, as in rule 2.
    old_t, new_t = numbers["old_tokens"], numbers["new_tokens"]
    old_c, new_c = numbers["old_calls"], numbers["new_calls"]
    bar = 1 + TOKEN_MARGIN + 1e-9
    if new_t > old_t * bar and new_t * old_c > old_t * new_c * bar:
        reasons.append(
            f"the new side read {new_t} tokens across every model over {new_c} "
            f"tool calls, {new_t / new_c:.1f} a call, against the baseline's "
            f"{old_t} over {old_c}, {old_t / old_c:.1f} a call: the total and "
            f"the figure per call both rose by more than {TOKEN_MARGIN:.0%} "
            "(rule 5)"
        )
    return ("fail" if reasons else "pass"), reasons


def merged(old, new):
    """The numbers `verdict` reads, from two sides' `side_numbers`, spend
    rounded to four places and seconds to one, the precision a record
    carries, so a record reads back to the numbers it was judged on.

    A grader one side lacks counts zero runs there."""
    keys = sorted(set(old["graders"]) | set(new["graders"]))
    graders = {}
    for key in keys:
        o = old["graders"].get(key)
        n = new["graders"].get(key)
        k = (o or n)[0]
        graders[key] = (
            k,
            o[1] if o else 0,
            o[2] if o else 0,
            n[1] if n else 0,
            n[2] if n else 0,
        )
    return {
        "graders": graders,
        "old_rows": old["rows"],
        "old_false": old["false"],
        "new_rows": new["rows"],
        "new_false": new["false"],
        "old_cut": old["cut"],
        "new_cut": new["cut"],
        **{
            f"{prefix}_{key}": rounded(s[key], places)
            for prefix, s in (("old", old), ("new", new))
            for key, places in (
                ("spend", 4),
                ("tokens", 0),
                ("calls", 0),
                ("seconds", 1),
                ("bytes", 0),
            )
        },
    }


def rounded(value, places):
    """VALUE at PLACES decimals, an integer at none; None stays None."""
    if value is None:
        return None
    return int(value) if places == 0 else round(float(value), places)


# --- the record ---------------------------------------------------------------

HEADER = "| Kind | Case | Grader | Old passed | Old runs | New passed | New runs |"
COST_ROWS = (
    ("spend", "spend USD", "{:.4f}", float),
    ("tokens", "tokens read, every model", "{:d}", int),
    ("calls", "tool calls", "{:d}", int),
    ("seconds", "wall seconds", "{:.1f}", float),
    ("bytes", "preload bytes", "{:d}", int),
)


def per(value, divisor, shown):
    """VALUE over DIVISOR in SHOWN's format, `unknown` where either is None
    or the divisor is none."""
    if value is None or not divisor:
        return "unknown"
    return shown.format(value / divisor)


def cost_rows(numbers):
    """The record's header rows for both sides' cost, `unknown` where a
    number is None, then the two derived rows a reader compares by: tokens
    per tool call, whose figure rule 5 reads together with the total from
    the rows above it, and tokens per true find, which judges nothing. Neither derived row is read back."""
    lines = []
    for key, label, shown, _parse in COST_ROWS:
        for side, name in (("old", "Baseline"), ("new", "New")):
            value = numbers[f"{side}_{key}"]
            cell = "unknown" if value is None else shown.format(value)
            lines.append(f"| {name} {label} | {cell} |")
    truths = [v for v in numbers["graders"].values() if v[0] == "truth"]
    found = {"old": sum(v[1] for v in truths), "new": sum(v[3] for v in truths)}
    for label, divisor, shown in (
        ("tokens per tool call", "calls", "{:.1f}"),
        ("tokens per true find", "found", "{:.0f}"),
    ):
        for side, name in (("old", "Baseline"), ("new", "New")):
            by = found[side] if divisor == "found" else numbers[f"{side}_{divisor}"]
            cell = per(numbers[f"{side}_tokens"], by, shown)
            lines.append(f"| {name} {label} | {cell} |")
    return lines


def render(agent, phase, old, new):
    """The record `compare` writes."""
    numbers = merged(old, new)
    result, reasons = verdict(numbers)
    lines = [
        f"# {agent} — phase {phase} non-inferiority",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Agent | {agent} |",
        f"| Phase | {phase} |",
        f"| Baseline run | {old['id']} |",
        f"| New run | {new['id']} |",
        f"| Baseline suite | {suite_name(old['suite'])} |",
        f"| New suite | {suite_name(new['suite'])} |",
        f"| Baseline cut short | {'yes' if numbers['old_cut'] else 'no'} |",
        f"| New cut short | {'yes' if numbers['new_cut'] else 'no'} |",
        f"| Baseline report rows | {numbers['old_rows']} |",
        f"| Baseline false rows | {numbers['old_false']} |",
        f"| New report rows | {numbers['new_rows']} |",
        f"| New false rows | {numbers['new_false']} |",
        *cost_rows(numbers),
        "",
        "## Graders",
        "",
        HEADER,
        "|---|---|---|---|---|---|---|",
    ]
    for (case, name), (k, op, oruns, np_, nruns) in sorted(numbers["graders"].items()):
        lines.append(f"| {k} | {case} | {name} | {op} | {oruns} | {np_} | {nruns} |")
    lines += ["", "## New preload", "", "| File | sha256 |", "|---|---|"]
    lines += [f"| {p} | {h} |" for p, h in sorted(new["preload"].items())]
    lines += ["", f"Verdict: {result}", ""]
    lines += [f"- {r}" for r in reasons] or ["- every pass rule holds"]
    return "\n".join(lines) + "\n"


def table(text, heading):
    """The body rows of the first table under `## HEADING`, as cell lists.

    A missing heading gives no rows."""
    m = re.search(
        rf"^## {re.escape(heading)}\n(?P<body>.*?)(?=^## |\Z)", text, re.M | re.S
    )
    rows = []
    for line in (m["body"] if m else "").split("\n"):
        if line.startswith("|") and not re.match(r"^\|[-| ]+\|$", line):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows[1:]


def header_field(text, name):
    """A `| NAME | value |` row of the record's header table, or None.

    A missing row is None."""
    m = re.search(rf"^\| {re.escape(name)} \| (?P<v>[^|]*) \|$", text, re.M)
    return m["v"].strip() if m else None


def parse_record(text):
    """`(numbers, stated verdict, new preload)` read back from a record.

    A count that is not an integer raises ValueError; a cost row that is
    missing or says `unknown` reads as None."""
    graders = {}
    for row in table(text, "Graders"):
        k, case, name, op, oruns, np_, nruns = row
        graders[(case, name)] = (k, int(op), int(oruns), int(np_), int(nruns))
    numbers = {
        "graders": graders,
        "old_rows": int(header_field(text, "Baseline report rows") or 0),
        "old_false": int(header_field(text, "Baseline false rows") or 0),
        "new_rows": int(header_field(text, "New report rows") or 0),
        "new_false": int(header_field(text, "New false rows") or 0),
        "old_cut": header_field(text, "Baseline cut short") != "no",
        "new_cut": header_field(text, "New cut short") != "no",
    }
    for key, label, _shown, parse in COST_ROWS:
        for side, name in (("old", "Baseline"), ("new", "New")):
            cell = header_field(text, f"{name} {label}")
            numbers[f"{side}_{key}"] = (
                None if cell in (None, "unknown") else parse(cell)
            )
    m = re.search(r"^Verdict: (?P<v>.+)$", text, re.M)
    stated = m["v"].strip() if m else None
    preload = {row[0]: row[1] for row in table(text, "New preload") if len(row) == 2}
    return numbers, stated, preload


def differ(old, new):
    """The sentence that two sides ran different suites, naming both."""
    return (
        f"the two sides ran different suites: the baseline at {old} and the new "
        f"side at {new} (`<commit> <tree of {SUITE}/<agent>>`); a changed suite "
        "needs a new baseline"
    )


def suite_problem(text):
    """The problem with a record's two suites, or None: a side naming none,
    or two different trees."""
    old, new = header_field(text, "Baseline suite"), header_field(text, "New suite")
    if not old or not new:
        return "the record names no suite for one of its sides"
    if old.split()[-1] != new.split()[-1]:
        return differ(old, new)
    return None


def read_record(text):
    """`(numbers, computed verdict, reasons, [problem])` for a record, the
    problems being what makes it unsound whatever its verdict: its suites,
    and a stated verdict its numbers do not give.

    A record that does not parse is a problem, and its first three are
    None, None and no reasons."""
    try:
        numbers, stated, _preload = parse_record(text)
    except (ValueError, TypeError) as e:
        return None, None, [], [f"the record does not parse: {e}"]
    computed, reasons = verdict(numbers)
    problems = [p for p in (suite_problem(text),) if p]
    if stated != computed:
        problems.append(f"it says `{stated}` and its numbers give `{computed}`")
    return numbers, computed, reasons, problems


def check_record(text):
    """`[problem]` for a record: what `read_record` finds unsound, and
    anything but `pass`."""
    numbers, computed, reasons, problems = read_record(text)
    if numbers is not None and computed != "pass":
        problems.append(f"its numbers give `{computed}`: " + "; ".join(reasons))
    return problems


def cheaper_model(numbers):
    """`(model, reason)` from a record whose baseline is the Opus side and
    whose new side is Sonnet: `sonnet` only where no grader, truth, shape or
    reach, passes on the Sonnet side less often and its spend is lower.

    A side cut short, or any other no result, is `opus`; so is a spend
    either side does not record, and a record that carries no truth grader,
    since it measured no outcome and `sonnet` would rest on cost alone. A
    truth grader one side lacks is already a no result: that side ran its
    case a different number of times."""
    result, reasons = verdict(numbers)
    if result == "no result":
        return "opus", "; ".join(reasons)
    if not any(v[0] == "truth" for v in numbers["graders"].values()):
        return "opus", "the record carries no truth grader, so no outcome was measured"
    lost = [
        f"{k} grader {case}/{name} passed {np_}/{nruns} on Sonnet, {op}/{oruns} on Opus"
        for (case, name), (k, op, oruns, np_, nruns) in sorted(
            numbers["graders"].items()
        )
        if np_ * oruns < op * nruns
    ]
    if lost:
        return "opus", "; ".join(lost)
    old, new = numbers["old_spend"], numbers["new_spend"]
    if old is None or new is None or new >= old:
        return "opus", f"Sonnet spent {new} USD, not below Opus's {old}"
    return "sonnet", f"every grader holds and Sonnet spent {new} USD, below {old}"


def compare(a):
    """`compare`: write the record of one agent's phase.

    A side `side_numbers` cannot read is refused with exit 2, naming the
    side's file; a file that is not JSON stops the run."""
    sides = []
    for path in (a.old, a.new):
        with open(path, encoding="utf-8") as f:
            result = json.load(f)
        try:
            sides.append(side_numbers(result))
        except ValueError as e:
            print(f"{path}: {e}", file=sys.stderr)
            return 2
    old, new = sides
    for s in (old, new):
        if not s["suite"]["rev"]:
            print(
                "a side records no suite_rev, so its suite is unknown", file=sys.stderr
            )
            return 2
        if not s["suite"]["tree"]:
            s["suite"]["tree"] = suite_tree(s["suite"]["rev"], a.agent)
    if old["suite"]["tree"] != new["suite"]["tree"]:
        print(
            differ(suite_name(old["suite"]), suite_name(new["suite"])), file=sys.stderr
        )
        return 2
    text = render(a.agent, a.phase, old, new)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(text)
    print(re.search(r"^Verdict: .*$", text, re.M)[0])
    return 0


def check(a):
    """`check`: recompute a record's verdict.

    A record that does not parse is reported and exits 1."""
    with open(a.record, encoding="utf-8") as f:
        text = f.read()
    problems = check_record(text)
    for p in problems:
        print(p)
    old, new = header_field(text, "Baseline suite"), header_field(text, "New suite")
    if old and new and old.split()[-1] != new.split()[-1]:
        return 2
    return 1 if problems else 0


def model(a):
    """`model`: print the sealer's model a record decides, then its reason.

    A record that cannot be read, does not parse, or is unsound exits 2."""
    try:
        with open(a.record, encoding="utf-8") as f:
            numbers, _computed, _reasons, problems = read_record(f.read())
    except OSError as e:
        problems = [f"the record cannot be read: {e}"]
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 2
    print("\n".join(cheaper_model(numbers)))
    return 0


# --- regrade: a side read again under another suite's truths ----------------

# One scalar of the front matter `behaviour.grader` writes: single-quoted, a
# quote doubled inside, or a bare word up to the next `,` or `}`.
SCALAR = r"'(?:[^']|'')*'|[^,}]+"
REGEX_FLAGS = {"m": re.M, "i": re.I, "s": re.S}
# The float error two sums of the same scores in another order can leave.
SCORE_ERROR = 1e-9


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


def grader_at(rev, path):
    """The grader file REV:PATH, read by `grader_from`."""
    return grader_from(path, git_bytes("show", f"{rev}:{path}").decode("utf-8"))


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


def suite_files(rev, agent):
    """`{case dir: {path: blob}}`: every file of every case of AGENT's suite
    at REV."""
    out = {}
    listing = git_bytes("ls-tree", "-r", "-z", rev, "--", f"{SUITE}/{agent}/")
    for entry in listing.decode("utf-8").split("\0"):
        if entry:
            mode_type_blob, path = entry.split("\t", 1)
            case = "/".join(path.split("/")[:4])
            out.setdefault(case, {})[path] = mode_type_blob.split()[2]
    return out


def is_truth_file(path):
    """True for a case's `graders/truth-*` file."""
    parts = path.split("/")
    return len(parts) > 1 and parts[-2] == "graders" and parts[-1].startswith("truth-")


def truths_at(rev, files):
    """`{case dir: [truth grader]}` of the suite at REV, FILES its
    `suite_files`."""
    return {
        case: [grader_at(rev, p) for p in sorted(paths) if is_truth_file(p)]
        for case, paths in files.items()
    }


def grade(grader, rows):
    """A run's entry for the truth GRADER: its regex searched over ROWS
    joined by newlines, the run's `finding_rows` where a side is counted or
    graded on another suite, and its whole `report_text` where `regrade`
    checks a side against the suite it ran.

    A grader that is not a regex the report must contain, or that carries a
    flag this module does not know, raises ValueError."""
    config = grader.get("config") or {}
    if grader.get("type") != "regex" or config.get("match") != "contains":
        raise ValueError(f"{grader['name']} is not a regex the report must contain")
    flags = 0
    for letter in config.get("flags", ""):
        if letter not in REGEX_FLAGS:
            raise ValueError(f"{grader['name']} carries the flag {letter!r}")
        flags |= REGEX_FLAGS[letter]
    found = re.search(config["pattern"], "\n".join(rows), flags) is not None
    return {
        "name": grader["name"],
        "passed": found,
        "weight": grader.get("weight", 1),
        "explanation": "regraded from the kept report text: "
        + ("found" if found else "not found"),
        "withOnly": False,
        "scored": True,
    }


def mean(values):
    """The mean of VALUES, or 0 where there are none."""
    values = list(values)
    return sum(values) / len(values) if values else 0


def case_runs(case):
    """Every run of CASE, arm by arm."""
    return [r for arm in case.get("arms", {}).values() for r in arm]


def regraded(result, truths, whole=False):
    """RESULT with each case's truth graders TRUTHS[case dir], every run
    graded on them from its `finding_rows`, or from its whole `report_text`
    where WHOLE is set, and the scores recomputed the way the eval writes
    them: a run's score is its passed graders' weight over every scored
    grader's, passing at the suite's threshold; a case's score and pass
    rate are its runs' means; the side's are its cases' means, and its cases
    passed are those whose every run passed.

    A run that keeps no `report_text`, or a truth grader `grade` cannot
    read, raises ValueError naming the case."""
    out = copy.deepcopy(result)
    threshold = (out.get("suite") or {}).get("threshold", 1)
    cases = out.get("cases", [])
    for case in cases:
        new = truths[case["dir"]]
        kept = [g for g in case.get("graders", []) if kind(g["name"]) != "truth"]
        case["graders"] = kept + new
        runs = case_runs(case)
        for i, run in enumerate(runs):
            text = text_of(case["name"], i, run)
            rows = [text] if whole else finding_rows(text)
            others = [g for g in run.get("graders", []) if kind(g["name"]) != "truth"]
            try:
                run["graders"] = others + [grade(g, rows) for g in new]
            except ValueError as e:
                raise ValueError(f"{case['name']}: {e}") from None
            scored = [g for g in run["graders"] if g.get("scored", True)]
            weight = sum(g.get("weight", 1) for g in scored)
            passed = sum(g.get("weight", 1) for g in scored if g.get("passed"))
            run["score"] = passed / weight if weight else 0
            run["passed"] = run["score"] >= threshold
        if runs:
            case["aggregates"] = dict(
                case.get("aggregates", {}),
                score=mean(r["score"] for r in runs),
                passRate=mean(r["passed"] for r in runs),
            )
    rated = [c["aggregates"] for c in cases if "aggregates" in c]
    out["aggregates"] = dict(
        out.get("aggregates", {}),
        casesTotal=len(cases),
        casesPassed=sum(1 for g in rated if g["passRate"] >= 1),
        overallScore=mean(g["score"] for g in rated),
        overallPassRate=mean(g["passRate"] for g in rated),
    )
    return out


def differs(recorded, again, keys):
    """The KEYS whose values RECORDED holds and AGAIN does not give, a
    number to `SCORE_ERROR`."""
    out = []
    for key in keys:
        if key not in recorded:
            continue
        a, b = recorded[key], again.get(key)
        same = (
            abs(a - b) <= SCORE_ERROR
            if isinstance(a, (int, float)) and isinstance(b, (int, float))
            else a == b
        )
        if not same:
            out.append(f"{key} {a!r}, not {b!r}")
    return out


def unreproduced(result, again):
    """`[problem]`, each naming its case: where AGAIN, RESULT graded once
    more on the suite it ran over each run's whole `report_text`, the file
    the eval searched, does not give what RESULT recorded, its truth
    graders, each run's truth results and scores, and its aggregates."""
    problems = []
    for case, mine in zip(result.get("cases", []), again["cases"], strict=True):
        name = case["name"]

        def truths(graders):
            return sorted(
                (g["name"], g.get("type"), g.get("weight", 1), g.get("config"))
                for g in graders
                if kind(g["name"]) == "truth"
            )

        if truths(case.get("graders", [])) != truths(mine["graders"]):
            problems.append(f"{name}: its truth graders are not its suite's files")
            continue
        pairs = zip(case_runs(case), case_runs(mine), strict=True)
        for i, (run, re_run) in enumerate(pairs):
            was = {
                g["name"]: bool(g.get("passed"))
                for g in run.get("graders", [])
                if kind(g["name"]) == "truth"
            }
            now = {
                g["name"]: g["passed"]
                for g in re_run["graders"]
                if kind(g["name"]) == "truth"
            }
            if was != now:
                problems.append(
                    f"{name}, run {i}: it recorded {was} and its report text gives {now}"
                )
            off = differs(run, re_run, ("score", "passed"))
            if was == now and off:
                problems.append(f"{name}, run {i}: it recorded " + ", ".join(off))
        off = differs(
            case.get("aggregates", {}),
            mine.get("aggregates", {}),
            ("score", "passRate"),
        )
        if off:
            problems.append(f"{name}: its aggregates are " + ", ".join(off))
    off = differs(
        result.get("aggregates", {}),
        again["aggregates"],
        ("casesTotal", "casesPassed", "overallScore", "overallPassRate"),
    )
    if off:
        problems.append("the side's aggregates are " + ", ".join(off))
    return problems


def regrade(a):
    """`regrade`: write the side A.side holds, graded on the `truth-` graders
    of the suite at A.suite_rev from each run's `finding_rows`, with no eval
    run.

    Refused with exit 2, naming the side's file, where a run keeps no
    `report_text`; and, naming the case, where the side's own suite does
    not give back from each run's whole `report_text` what it recorded,
    where the target suite and the side's differ in a case's files other
    than its `truth-` graders, or where the two hold different cases. A REV
    git does not resolve stops the run."""
    with open(a.side, encoding="utf-8") as f:
        result = json.load(f)
    try:
        for case in result.get("cases", []):
            for i, run in enumerate(case_runs(case)):
                text_of(case["name"], i, run)
    except ValueError as e:
        print(f"{a.side}: {e}", file=sys.stderr)
        return 2
    meta = result.get("agentic") or {}
    agent, own = meta.get("agent"), meta.get("suite_rev")
    if agent not in AGENTS or not own:
        print(
            "the side records no agent or no suite_rev, so its suite is unknown",
            file=sys.stderr,
        )
        return 2
    target = git_bytes("rev-parse", f"{a.suite_rev}^{{commit}}").decode("utf-8").strip()
    mine, theirs = suite_files(own, agent), suite_files(target, agent)
    ran = {c["dir"]: c["name"] for c in result.get("cases", [])}
    at = f"the suite at {target[:8]}"
    problems = [
        f"{d}: {at} holds this case, and the side never ran it"
        for d in sorted(set(theirs) - set(ran))
    ]
    for d in sorted(ran):
        if d not in theirs:
            problems.append(f"{ran[d]}: {at} does not hold this case")
        elif d not in mine:
            problems.append(
                f"{ran[d]}: the suite it ran, at {own[:8]}, does not hold it"
            )
        elif {p: b for p, b in mine[d].items() if not is_truth_file(p)} != {
            p: b for p, b in theirs[d].items() if not is_truth_file(p)
        }:
            problems.append(
                f"{ran[d]}: {at} changes more than its truth- graders, so the "
                "side's runs did not answer it"
            )
    try:
        if not problems:
            again = regraded(result, truths_at(own, mine), whole=True)
            problems = unreproduced(result, again)
        if not problems:
            out = regraded(result, truths_at(target, theirs))
    except ValueError as e:
        problems.append(str(e))
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 2
    out["agentic"] = dict(
        out.get("agentic", {}),
        suite_rev=target,
        suite_tree=suite_tree(target, agent),
        # The suite the runs answered, kept through any number of regrades.
        regraded_from=meta.get("regraded_from") or own,
    )
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
        f.write("\n")
    numbers = side_numbers(out)
    print(f"graded on {target[:8]}: {numbers['rows']} rows, {numbers['false']} false")
    return 0


def main(argv=None):
    """Parse the arguments and run one subcommand.

    An unusable argument is argparse's exit 2."""
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = p.add_subparsers(dest="command", required=True)
    r = sub.add_parser("run")
    r.add_argument("--agent", choices=AGENTS)
    src = r.add_mutually_exclusive_group(required=True)
    src.add_argument("--rev")
    src.add_argument("--tree")
    src.add_argument("--from-raw")
    r.add_argument("--suite-rev", default="HEAD")
    r.add_argument("--out", required=True)
    r.add_argument("--runs", type=int, default=2)
    r.add_argument("-j", "--concurrency", type=int, default=4)
    r.add_argument("--max-cost-usd", type=float, default=100.0)
    r.add_argument("--case")
    c = sub.add_parser("compare")
    c.add_argument("--agent", choices=AGENTS, required=True)
    c.add_argument("--phase", type=int, required=True)
    c.add_argument("--old", required=True)
    c.add_argument("--new", required=True)
    c.add_argument("--out", required=True)
    k = sub.add_parser("check")
    k.add_argument("record")
    m = sub.add_parser("model")
    m.add_argument("record")
    g = sub.add_parser("regrade")
    g.add_argument("--side", required=True)
    g.add_argument("--suite-rev", required=True)
    g.add_argument("--out", required=True)
    a = p.parse_args(argv)
    commands = {
        "run": run_side,
        "compare": compare,
        "check": check,
        "model": model,
        "regrade": regrade,
    }
    return commands[a.command](a)


if __name__ == "__main__":
    sys.exit(main())
