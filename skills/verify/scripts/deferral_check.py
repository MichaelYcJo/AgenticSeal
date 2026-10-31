#!/usr/bin/env python3
"""seal deferrals — resolve the answerer named in an `unverified` row.

Condition 4 lets a claim go out unproven as long as it says *who or what
answers it*. Nothing checked that the answerer existed. The measured failure:
a session narrowed its run to one domain and deferred the rest to CI. That
repository's workflows assigned reviewers, deployed on push to the default
branch, and checked a migration graph. None ran the test suite, the default
branch had no protection, and the pre-commit hooks were lint and typecheck
only. The deferral named something that was not there, which reads exactly
like a deferral that was honoured.

So this resolves the common answerer. Given a repo and a kind of check, it
reads the command lines of the CI files and the pre-commit hook, and
separates three outcomes that a reader otherwise collapses into one:

  ci       a CI file holds a runner; whether it runs before the change
           merges is its trigger, which the reader opens
  local    a pre-commit hook runs it on the committer's machine only
  nothing  no one runs it

It reads no trigger. A workflow's `on:` key is YAML, no YAML parser ships
with the plugin's stdlib-only scripts, and a scan of it by hand misread
shapes YAML reads otherwise (#1167). The agent that opens the named file
reads the trigger better than a scan would. `KNOWN_LIMITS` states the
rest of what the command text leaves out.

Exit codes: 0 a CI file holds a runner for every requested kind · 1 for at
least one kind none does · 2 the path or arguments were unusable.
"""

import argparse
import os
import re
import sys

# A runner token is matched against the text of a command line. Word-boundary
# anchored so `pytest-cov` in a dependency list is not read as a test run.
RUNNERS = {
    "tests": [
        r"\bpytest\b",
        r"\bgo test\b",
        r"\bcargo test\b",
        r"\bnpm (?:run )?test\b",
        r"\b(?:pnpm|yarn) (?:run )?test\b",
        r"\bjest\b",
        r"\bvitest\b",
        r"\brspec\b",
        r"\bmvn (?:\S+ )*test\b",
        r"\bgradle (?:\S+ )*test\b",
        r"\bdotnet test\b",
        r"\bphpunit\b",
        r"\btox\b",
        r"\bmake test\b",
        r"\bpython3? -m unittest\b",
        r"\brails test\b",
        r"\bbin/test\b",
    ],
    "lint": [
        r"\bruff\b",
        r"\beslint\b",
        r"\bflake8\b",
        r"\bpylint\b",
        r"\bgolangci-lint\b",
        r"\bcargo clippy\b",
        r"\brubocop\b",
        r"\bmake lint\b",
        r"\bbiome\b",
    ],
    "typecheck": [
        r"\bmypy\b",
        r"\bpyright\b",
        r"\btsc\b",
        r"\bmake typecheck\b",
        r"\bgo vet\b",
    ],
}
KINDS = tuple(RUNNERS)

KNOWN_LIMITS = (
    "reads command text, not a YAML graph: a runner reached through a "
    "composite action, a reusable workflow, or a script this cannot see "
    "reads as absent; no trigger is read, so a file named here may run only "
    "after the change merges"
)

# The one line under the CI files a kind names: their trigger is not read.
TRIGGER = (
    "  trigger   not read: open each ci file above for whether it runs "
    "before the change merges"
)


def runners_in(text, kind):
    """Command lines in `text` that run `kind`, deduped, in file order."""
    found = []
    # exempt from splitlines: YAML keys
    for line in text.splitlines():
        stripped = line.strip().lstrip("-").strip()
        # exempt from heading_rule: a YAML or shell comment in a workflow's run lines
        if not stripped or stripped.startswith("#"):
            continue
        for pattern in RUNNERS[kind]:
            if re.search(pattern, stripped):
                cmd = re.sub(r"^(?:run|entry|script)\s*:\s*", "", stripped)
                if cmd not in found:
                    found.append(cmd)
                break
    return found


def workflow_files(root):
    d = os.path.join(root, ".github", "workflows")
    if not os.path.isdir(d):
        return []
    return [
        os.path.join(d, n)
        for n in sorted(os.listdir(d))
        if n.endswith((".yml", ".yaml"))
    ]


def other_ci_files(root):
    """CI systems whose config is a single known path."""
    out = []
    for rel in (
        ".gitlab-ci.yml",
        ".circleci/config.yml",
        "Jenkinsfile",
        "azure-pipelines.yml",
        ".drone.yml",
        ".travis.yml",
    ):
        p = os.path.join(root, rel)
        if os.path.isfile(p):
            out.append(p)
    d = os.path.join(root, ".buildkite")
    if os.path.isdir(d):
        out += [
            os.path.join(d, n)
            for n in sorted(os.listdir(d))
            if n.endswith((".yml", ".yaml"))
        ]
    return out


def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def inspect(root, kind):
    """(verdict, lines) for one kind. The verdict, the exit-code decision,
    is whether a CI file holds a runner. No trigger is read: each such file
    is named with its command lines, and `TRIGGER` leaves its trigger to
    the reader to open."""
    in_ci, local_only = [], []
    for path in workflow_files(root) + other_ci_files(root):
        cmds = runners_in(read(path), kind)
        if cmds:
            in_ci.append((os.path.relpath(path, root), cmds))

    pc = os.path.join(root, ".pre-commit-config.yaml")
    if os.path.isfile(pc):
        cmds = runners_in(read(pc), kind)
        if cmds:
            local_only.append((".pre-commit-config.yaml", cmds))

    lines = [f"  ci        {name} — {'; '.join(cmds)}" for name, cmds in in_ci]
    for name, cmds in local_only:
        lines.append(
            f"  local     {name} (the committer's machine only) — {'; '.join(cmds)}"
        )

    if in_ci:
        lines.append(TRIGGER)
        return True, lines
    if not lines:
        lines.append("  nothing runs it")
    return False, lines


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="seal deferrals",
        description="Resolve the answerer named in an `unverified` row.",
    )
    ap.add_argument("path", nargs="?", default=".")
    ap.add_argument(
        "--kind",
        default="tests",
        choices=(*KINDS, "all"),
        help="which check is being deferred (default: tests)",
    )
    args = ap.parse_args(argv)

    root = os.path.abspath(args.path)
    if not os.path.isdir(root):
        print(f"seal deferrals: no such path: {args.path}", file=sys.stderr)
        return 2

    kinds = KINDS if args.kind == "all" else (args.kind,)
    unresolved = []
    for kind in kinds:
        ok, lines = inspect(root, kind)
        print(f"{kind}: {'a runner in CI' if ok else 'NO RUNNER IN CI'}")
        for line in lines:
            print(line)
        if not ok:
            unresolved.append(kind)

    print(f"\nlimit: {KNOWN_LIMITS}")
    if unresolved:
        print(
            f"\nDeferring {', '.join(unresolved)} to CI names an answerer "
            f"that is not there. Run it, or say it is unanswered."
        )
        return 1
    return 0


if __name__ == "__main__":
    # A console that cannot encode what this prints kills it with stdout
    # empty, which is how a hook says "nothing to see here". `hooks/lib/console.py`
    # owns the reasoning and the three decisions behind these lines.
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    sys.exit(main())
