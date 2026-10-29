set -eu
git init -q -b main .
mkdir -p "$(dirname 'src/textutil.py')"
cat > 'src/textutil.py' <<'AGENTIC_EOF'
def shout(text):
    """Return TEXT upper-cased, followed by one exclamation mark."""
    return text.upper() + "!"
AGENTIC_EOF
mkdir -p "$(dirname 'src/__init__.py')"
cat > 'src/__init__.py' <<'AGENTIC_EOF'

AGENTIC_EOF
mkdir -p "$(dirname 'tests/__init__.py')"
cat > 'tests/__init__.py' <<'AGENTIC_EOF'

AGENTIC_EOF
mkdir -p "$(dirname 'tests/test_textutil.py')"
cat > 'tests/test_textutil.py' <<'AGENTIC_EOF'
import unittest

from src.textutil import shout


class ShoutTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("hi"), "HI!")


if __name__ == "__main__":
    unittest.main()
AGENTIC_EOF
mkdir -p "$(dirname 'README.md')"
cat > 'README.md' <<'AGENTIC_EOF'
# textutil

Small text helpers.
AGENTIC_EOF
mkdir -p "$(dirname 'CONTRIBUTING.md')"
cat > 'CONTRIBUTING.md' <<'AGENTIC_EOF'
# Contributing

Run one module's tests with `python3 -m unittest tests.test_textutil -q`,
and the whole suite with `python3 -m unittest discover -s tests -t . -q`.
AGENTIC_EOF
mkdir -p "$(dirname 'seal/README.md')"
cat > 'seal/README.md' <<'AGENTIC_EOF'
# What AgenticSeal maintains in seal/
AGENTIC_EOF
mkdir -p "$(dirname 'seal/config.md')"
cat > 'seal/config.md' <<'AGENTIC_EOF'
# Repository config

| Item | Value |
|---|---|
| Mode | shared |
| Broad gate | python3 -m unittest discover -s tests -t . -q |
AGENTIC_EOF
mkdir -p "$(dirname 'seal/threads/1790000026-generated-page/routing.md')"
cat > 'seal/threads/1790000026-generated-page/routing.md' <<'AGENTIC_EOF'
# routing

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | stop before the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Answer pressed | automation |
| Branch | feat/generated-page |
AGENTIC_EOF
mkdir -p "$(dirname 'scripts/helpers_page.py')"
cat > 'scripts/helpers_page.py' <<'AGENTIC_EOF'
"""Write docs/helpers.md from the docstrings in src/textutil.py."""

import ast
import os
import zlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    with open(os.path.join(ROOT, "src", "textutil.py"), encoding="utf-8") as f:
        tree = ast.parse(f.read())
    lines = ["# Helpers", ""]
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            lines += [f"## {node.name}", "", ast.get_docstring(node) or "", ""]
    page = "\n".join(lines)
    revision = format(zlib.crc32(page.encode("utf-8")), "08x")
    with open(os.path.join(ROOT, "docs", "helpers.md"), "w", encoding="utf-8") as f:
        f.write(f"{page}\nRevision {revision}\n")


if __name__ == "__main__":
    main()
AGENTIC_EOF
mkdir -p "$(dirname 'docs/helpers.md')"
cat > 'docs/helpers.md' <<'AGENTIC_EOF'
# Helpers

## shout

Return TEXT upper-cased.
AGENTIC_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'base: textutil'
git checkout -q -b feat/generated-page
