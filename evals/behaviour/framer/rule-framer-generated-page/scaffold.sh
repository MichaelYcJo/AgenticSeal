set -eu
git init -q -b main .
mkdir -p "$(dirname 'src/textutil.py')"
cat > 'src/textutil.py' <<'IADD_EOF'
def shout(text):
    """Return TEXT upper-cased, followed by one exclamation mark."""
    return text.upper() + "!"
IADD_EOF
mkdir -p "$(dirname 'src/__init__.py')"
cat > 'src/__init__.py' <<'IADD_EOF'

IADD_EOF
mkdir -p "$(dirname 'tests/__init__.py')"
cat > 'tests/__init__.py' <<'IADD_EOF'

IADD_EOF
mkdir -p "$(dirname 'tests/test_textutil.py')"
cat > 'tests/test_textutil.py' <<'IADD_EOF'
import unittest

from src.textutil import shout


class ShoutTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("hi"), "HI!")


if __name__ == "__main__":
    unittest.main()
IADD_EOF
mkdir -p "$(dirname 'README.md')"
cat > 'README.md' <<'IADD_EOF'
# textutil

Small text helpers.
IADD_EOF
mkdir -p "$(dirname 'CONTRIBUTING.md')"
cat > 'CONTRIBUTING.md' <<'IADD_EOF'
# Contributing

Run one module's tests with `python3 -m unittest tests.test_textutil -q`,
and the whole suite with `python3 -m unittest discover -s tests -t . -q`.
IADD_EOF
mkdir -p "$(dirname 'iadd/README.md')"
cat > 'iadd/README.md' <<'IADD_EOF'
# What IADD keeps in iadd/
IADD_EOF
mkdir -p "$(dirname 'iadd/config.json')"
cat > 'iadd/config.json' <<'IADD_EOF'
{
  "Mode": "shared",
  "Broad gate": "python3 -m unittest discover -s tests -t . -q"
}
IADD_EOF
mkdir -p "$(dirname 'iadd/threads/1790000026-generated-page/routing.md')"
cat > 'iadd/threads/1790000026-generated-page/routing.md' <<'IADD_EOF'
# Routing: 1790000026-generated-page

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | stop before the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | feat/generated-page |
IADD_EOF
mkdir -p "$(dirname 'scripts/helpers_page.py')"
cat > 'scripts/helpers_page.py' <<'IADD_EOF'
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
IADD_EOF
mkdir -p "$(dirname 'docs/helpers.md')"
cat > 'docs/helpers.md' <<'IADD_EOF'
# Helpers

## shout

Return TEXT upper-cased.
IADD_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'base: textutil'
git checkout -q -b feat/generated-page
