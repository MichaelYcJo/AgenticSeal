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
mkdir -p "$(dirname 'iadd/threads/1790000015-rename/routing.md')"
cat > 'iadd/threads/1790000015-rename/routing.md' <<'IADD_EOF'
# Routing: 1790000015-rename

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | stop before the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | refactor/exclaim |
IADD_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'base: textutil'
git checkout -q -b refactor/exclaim
mkdir -p "$(dirname 'README.md')"
cat > 'README.md' <<'IADD_EOF'
# textutil

Small text helpers.

- `shout(text)` returns TEXT upper-cased, followed by one `!`.
IADD_EOF
mkdir -p "$(dirname 'iadd/threads/1790000015-rename/frame/design.md')"
cat > 'iadd/threads/1790000015-rename/frame/design.md' <<'IADD_EOF'
# Design: shout is renamed exclaim

## Scope

`shout` is renamed `exclaim` everywhere it is named: its definition in
`src/textutil.py`, its case in `tests/test_textutil.py`, and `README.md`.
What it returns does not change.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | `exclaim("hi")` is `"HI!"`, and no file names `shout` | the case in `tests/test_textutil.py` |

Framed 2026-10-14 by framer, before the build.
IADD_EOF
mkdir -p "$(dirname 'iadd/threads/1790000015-rename/frame/plan.md')"
cat > 'iadd/threads/1790000015-rename/frame/plan.md' <<'IADD_EOF'
# Implementation Plan: exclaim

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `shout` renamed `exclaim` in `src/textutil.py`, `tests/test_textutil.py` and `README.md`, with what it returns unchanged | `python3 -m unittest tests.test_textutil -q` | |
IADD_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'frame: exclaim'
