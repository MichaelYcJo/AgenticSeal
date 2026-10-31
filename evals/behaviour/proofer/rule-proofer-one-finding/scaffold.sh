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
mkdir -p "$(dirname 'seal/threads/1790000001-shout-ends-with-one-exclamation-mark/routing.md')"
cat > 'seal/threads/1790000001-shout-ends-with-one-exclamation-mark/routing.md' <<'AGENTIC_EOF'
# routing

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | stop before the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Answer pressed | automation |
| Branch | feat/shout-exclaims |
AGENTIC_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'base: textutil'
git checkout -q -b feat/shout-exclaims
mkdir -p "$(dirname 'seal/threads/1790000001-shout-ends-with-one-exclamation-mark/frame/design.md')"
cat > 'seal/threads/1790000001-shout-ends-with-one-exclamation-mark/frame/design.md' <<'AGENTIC_EOF'
# Feature Specification: shout ends with one exclamation mark

## Scope

`src/textutil.py#shout` returns its text upper-cased followed by exactly one
`!`, and `shout_twice(text)` returns `shout(text)` twice, joined by a space.

## User scenarios & acceptance

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | `shout("hi")` | `"HI!"` |
| S2 | `shout_twice("hi")` | `"HI! HI!"` |

Framed 2026-10-14 by framer, before the build.
AGENTIC_EOF
mkdir -p "$(dirname 'seal/threads/1790000001-shout-ends-with-one-exclamation-mark/frame/plan.md')"
cat > 'seal/threads/1790000001-shout-ends-with-one-exclamation-mark/frame/plan.md' <<'AGENTIC_EOF'
# Implementation Plan: shout_twice

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `shout_twice(text)` in `src/textutil.py` | `python3 -m unittest tests.test_textutil -q` | |
AGENTIC_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'frame: shout_twice'
mkdir -p "$(dirname 'src/textutil.py')"
cat > 'src/textutil.py' <<'AGENTIC_EOF'
def shout(text):
    """Return TEXT upper-cased, followed by one exclamation mark."""
    return text.upper() + "!"


def shout_twice(text):
    """Return shout(TEXT) twice."""
    return shout(text) + shout(text)
AGENTIC_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'feat: shout_twice'
