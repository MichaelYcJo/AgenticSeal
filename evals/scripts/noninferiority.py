#!/usr/bin/env python3
"""Run the behaviour suite on one side, and judge a new side against a baseline.

  noninferiority.py run --agent A (--rev REV | --tree DIR) --out FILE.json
      [--runs 2] [-j 4] [--max-cost-usd USD] [--case GLOB] [--suite-rev HEAD]
  noninferiority.py run --from-raw FILE.raw --out FILE.json
  noninferiority.py compare --agent A --phase N --old OLD.json --new NEW.json
      --out RECORD.md
  noninferiority.py check RECORD.md
  noninferiority.py model RECORD.md

`run` copies the plugin tree at REV (or DIR) into a temporary directory,
puts the suite at SUITE-REV's `evals/behaviour/` into it, and runs
`claude plugin eval` over `evals/behaviour/<A>/` there. **What the runs paid
for is saved before anything reads it**: the eval's JSON, every run's trace
and the measured preload go to `<out>.raw/` beside `--out`, and only then is
each directory the eval kept removed. `--out` is the saved side with these
additions under `agentic`: the preload's hashes and bytes, each run's cost
(its trace's `result` event: `total_cost_usd`, `duration_ms`, `modelUsage`)
and tool calls (every `tool_use` block in its trace), and whether the side
was cut short. `run --from-raw` writes `--out` again from a saved side,
with no eval run.

`compare` writes the record the three pass rules judge, a smoke run for
gross breakage of the agent's output, each against the baseline: the shape
and reach graders both sides ran pass, pooled, no fewer runs on the new side
than on the baseline, none of them fails every new run where the baseline
passed it, and one the baseline lacks passes every new run. Every grader,
a `truth-` grader among them, counts the result the eval recorded. A pass
claims nothing about whether a rewrite is worse or means the same. The
truth graders, the tokens, the tool calls, spend, wall seconds and the
preload's bytes are written and judge nothing.
`check` recomputes a record's verdict from its numbers.
`model` reads a record whose `--old` was the Opus side and `--new` the
Sonnet side, and prints `sonnet` only where no truth, shape or reach grader
passes on the Sonnet side less often and its spend is lower, else `opus`;
then one line saying why. The record's own verdict does not decide it.

Exit codes: 0 written, the record's verdict holds, or a model was decided ·
1 the record's verdict is not `pass`, or it disagrees with its numbers · 2
nothing ran (arguments, a missing tool, an unreadable input), or `model`
was handed a record that disagrees with its numbers or ran two suites.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
SUITE = "evals/behaviour"
AGENTS = ("proofer", "crafter", "framer", "sealer", "tracer")
CLT_GIT = "/Library/Developer/CommandLineTools/usr/bin/git"
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


def git_bytes(*args, index=None, stdin=None):
    """`git -C ROOT <args>`'s stdout as bytes, reading INDEX as its index
    where given and STDIN on its standard input.

    A non-zero exit stops the run."""
    env = None if index is None else {**os.environ, "GIT_INDEX_FILE": index}
    run = subprocess.run(
        ["git", "-C", ROOT, *args], capture_output=True, env=env, input=stdin
    )
    if run.returncode != 0:
        raise SystemExit(
            f"git {' '.join(args)}: {run.stderr.decode('utf-8', 'replace')}"
        )
    return run.stdout


def extract(rev, paths, into):
    """Write REV's PATHS (the whole tree when empty) under INTO, every file,
    whatever `.gitattributes` marks `export-ignore`: `git archive` leaves a
    marked path out and exits 0, so REV is read into an index of its own and
    checked out from there.

    A REV git does not resolve, a PATH REV does not hold, and a file already
    standing where one is written stop the run. So does a member that would
    land outside INTO, since `read-tree` refuses a tree entry that leaves
    it.

    INTO reaches git spelt with `/`: `checkout-index` creates each missing
    directory of a path at its `/` and at no other separator, so a Windows
    INTO spelt with `\\` that does not yet exist is never created."""
    with tempfile.TemporaryDirectory() as work:
        index = os.path.join(work, "index")
        git_bytes("read-tree", rev, index=index)
        names = git_bytes(
            "ls-files", "-z", "--error-unmatch", "--", *paths, index=index
        )
        prefix = os.path.join(os.path.abspath(into), "").replace(os.sep, "/")
        git_bytes(
            "checkout-index", "-z", "--stdin", f"--prefix={prefix}",
            index=index, stdin=names,
        )  # fmt: skip


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

    The record writes this count and the tokens per tool call, and neither
    is judged. A line that is not a JSON object is skipped; no count is
    never zero calls."""
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
    bytes, each run's cost and tool calls read from its saved trace, and
    whether the side was cut short. The round record a run's session
    printed stays in its trace and is not copied into the side.

    A run with no saved trace keeps no cost and no tool calls, and a run's
    error makes the side cut short."""
    with open(os.path.join(saved, "raw.json"), encoding="utf-8") as f:
        result = json.load(f)
    with open(os.path.join(saved, "meta.json"), encoding="utf-8") as f:
        meta = json.load(f)
    cut = bool(result.get("partial"))
    for key, run in runs_of(result):
        rel = meta["traces"].get(key)
        trace = os.path.join(saved, rel) if rel else None
        run["agentic"] = {
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
        shutil.rmtree(os.path.join(tree, *SUITE.split("/")), ignore_errors=True)
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


def case_runs(case):
    """Every run of CASE, arm by arm."""
    return [r for arm in case.get("arms", {}).values() for r in arm]


def side_numbers(result):
    """`{"graders": {(case, grader): [kind, passed, runs]}, "runs": {case:
    n}, "cut", "preload", "id", "spend", "tokens", "calls", "seconds",
    "bytes"}` for one side, the last five pooled over every run, the tokens
    read across every model and the calls every `tool_use` block.

    Every grader, a `truth-` grader among them, keeps the result the eval
    recorded, and a run's `report_text`, which a side written before #1487
    carries, is not read. A grader whose name carries no kind prefix is not
    counted. Each of spend, tokens, calls and seconds is None where any run
    lacks it, a run with no cost lacking the first, second and fourth, and
    bytes is None where the preload's bytes were not recorded."""
    graders, runs_per_case = {}, {}
    costs, calls = [], []
    for case in result.get("cases", []):
        name = case["name"]
        runs = case_runs(case)
        runs_per_case[name] = len(runs)
        for g in case.get("graders", []):
            k = kind(g["name"])
            if k:
                graders[(name, g["name"])] = [k, 0, len(runs)]
        for run in runs:
            for g in run.get("graders", []):
                key = (name, g["name"])
                if key in graders and g.get("passed"):
                    graders[key][1] += 1
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
    """`(verdict, [reason])` the three pass rules give NUMBERS, the merged
    `{(case, grader): (kind, old passed, old runs, new passed, new runs)}`
    under `graders` beside `old_cut` and `new_cut`.

    Each rule reads the new side's shape and reach graders against the
    baseline: 1 those both sides ran pass, pooled, no fewer runs, 2 none of
    them fails every new run where the baseline passed it, and 3 one the
    baseline lacks passes every new run. A missing key raises. A side cut
    short, a case the baseline ran and the new side did not, whatever its
    graders, and a case run a different number of times are no result.
    No truth grader, token, tool call, spend, second or preload byte is
    judged, and an unknown one gives no `no result`."""
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
    reasons = []
    # The rules judge the agent, not one run (#966): rule 1 pools the passes
    # of every shape and reach grader both sides ran into one total a side,
    # and rule 2 names a grader the new side failed on every run, where the
    # baseline passed it at least once, whatever the totals say. Each grader
    # in the totals ran as many times on both sides, or the check above
    # returned.
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
            f"side, fewer than the baseline's {old_total}/{runs} (rule 1): {fell}"
        )
    for (case, name), (k, op, oruns, np_, nruns) in common:
        if op and not np_:
            reasons.append(
                f"{k} grader {case}/{name} failed every new run (0/{nruns}) where "
                f"the baseline passed it {op}/{oruns} (rule 2)"
            )
    for (case, name), (k, _op, oruns, np_, nruns) in sorted(g.items()):
        if k in ("shape", "reach") and nruns and not oruns and np_ < nruns:
            reasons.append(
                f"{k} grader {case}/{name}, which the baseline lacks, failed on "
                f"the new side ({np_}/{nruns}) (rule 3)"
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
    number is None, then the derived row a reader compares by, tokens per
    tool call. No row judges anything, and the derived row is not read
    back."""
    lines = []
    for key, label, shown, _parse in COST_ROWS:
        for side, name in (("old", "Baseline"), ("new", "New")):
            value = numbers[f"{side}_{key}"]
            cell = "unknown" if value is None else shown.format(value)
            lines.append(f"| {name} {label} | {cell} |")
    for side, name in (("old", "Baseline"), ("new", "New")):
        cell = per(numbers[f"{side}_tokens"], numbers[f"{side}_calls"], "{:.1f}")
        lines.append(f"| {name} tokens per tool call | {cell} |")
    return lines


def render(agent, phase, old, new):
    """The record `compare` writes."""
    numbers = merged(old, new)
    result, reasons = verdict(numbers)
    lines = [
        f"# {agent} — phase {phase} smoke run",
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

    A side naming no suite, and two sides that ran different suites, are
    refused with exit 2; a file that is not JSON stops the run."""
    sides = []
    for path in (a.old, a.new):
        with open(path, encoding="utf-8") as f:
            sides.append(side_numbers(json.load(f)))
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
    a = p.parse_args(argv)
    commands = {
        "run": run_side,
        "compare": compare,
        "check": check,
        "model": model,
    }
    return commands[a.command](a)


if __name__ == "__main__":
    # A console that cannot encode what this prints kills it with stdout
    # empty; `lib/console.py` owns the reasoning behind these lines.
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    sys.exit(main())
