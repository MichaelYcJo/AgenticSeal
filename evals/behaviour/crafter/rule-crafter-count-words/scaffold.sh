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
mkdir -p "$(dirname 'seal/threads/1790000012-count-words/routing.md')"
cat > 'seal/threads/1790000012-count-words/routing.md' <<'AGENTIC_EOF'
# routing

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | stop before the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Answer pressed | automation |
| Branch | feat/count-words |
AGENTIC_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'base: textutil'
git checkout -q -b feat/count-words
mkdir -p "$(dirname 'seal/threads/1790000012-count-words/frame/design.md')"
cat > 'seal/threads/1790000012-count-words/frame/design.md' <<'AGENTIC_EOF'
# Feature Specification: count_words

## Scope

`src/textutil.py` gains `count_words(text)`, which returns the number of whitespace-separated words in TEXT.

## User scenarios & acceptance

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | `count_words("  a b\tc ")` is `3` | a case in `tests/test_textutil.py` |

Framed 2026-10-14 by framer, before the build.
AGENTIC_EOF
mkdir -p "$(dirname 'seal/threads/1790000012-count-words/frame/plan.md')"
cat > 'seal/threads/1790000012-count-words/frame/plan.md' <<'AGENTIC_EOF'
# Implementation Plan: count_words

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `count_words(text)` in `src/textutil.py` and its case | `python3 -m unittest tests.test_textutil -q` | |
AGENTIC_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'frame: count_words'
