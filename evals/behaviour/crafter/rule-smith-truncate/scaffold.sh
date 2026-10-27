set -eu
git init -q -b main .
mkdir -p "$(dirname 'src/textutil.py')"
cat > 'src/textutil.py' <<'SPECSEAL_EOF'
def shout(text):
    """Return TEXT upper-cased, followed by one exclamation mark."""
    return text.upper() + "!"
SPECSEAL_EOF
mkdir -p "$(dirname 'src/__init__.py')"
cat > 'src/__init__.py' <<'SPECSEAL_EOF'

SPECSEAL_EOF
mkdir -p "$(dirname 'tests/__init__.py')"
cat > 'tests/__init__.py' <<'SPECSEAL_EOF'

SPECSEAL_EOF
mkdir -p "$(dirname 'tests/test_textutil.py')"
cat > 'tests/test_textutil.py' <<'SPECSEAL_EOF'
import unittest

from src.textutil import shout


class ShoutTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("hi"), "HI!")


if __name__ == "__main__":
    unittest.main()
SPECSEAL_EOF
mkdir -p "$(dirname 'README.md')"
cat > 'README.md' <<'SPECSEAL_EOF'
# textutil

Small text helpers.
SPECSEAL_EOF
mkdir -p "$(dirname 'CONTRIBUTING.md')"
cat > 'CONTRIBUTING.md' <<'SPECSEAL_EOF'
# Contributing

Run one module's tests with `python3 -m unittest tests.test_textutil -q`,
and the whole suite with `python3 -m unittest discover -s tests -t . -q`.
SPECSEAL_EOF
mkdir -p "$(dirname 'seal/config.md')"
cat > 'seal/config.md' <<'SPECSEAL_EOF'
# Repository config

| Item | Value |
|---|---|
| Mode | shared |
| Broad gate | python3 -m unittest discover -s tests -t . -q |
SPECSEAL_EOF
mkdir -p "$(dirname 'seal/specs/1790000013-truncate/routing.md')"
cat > 'seal/specs/1790000013-truncate/routing.md' <<'SPECSEAL_EOF'
# routing

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | stop before the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Answer pressed | automation |
| Branch | feat/truncate |
SPECSEAL_EOF
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -q -m 'base: textutil'
git checkout -q -b feat/truncate
mkdir -p "$(dirname 'seal/specs/1790000013-truncate/spec.md')"
cat > 'seal/specs/1790000013-truncate/spec.md' <<'SPECSEAL_EOF'
# Feature Specification: truncate

## Scope

`src/textutil.py` gains `truncate(text, width)`, which returns TEXT unchanged when it is at most WIDTH characters, and otherwise its first WIDTH - 3 characters followed by `...`.

## User scenarios & acceptance

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | `truncate("abcdefgh", 6)` is `"abc..."` | a case in `tests/test_textutil.py` |

Framed 2026-10-14 by framer, before the build.
SPECSEAL_EOF
mkdir -p "$(dirname 'seal/specs/1790000013-truncate/plan.md')"
cat > 'seal/specs/1790000013-truncate/plan.md' <<'SPECSEAL_EOF'
# Implementation Plan: truncate

Approved 2026-10-14 by the repository owner, when `smith` was spawned.

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `truncate(text, width)` in `src/textutil.py` and its case | `python3 -m unittest tests.test_textutil -q` | |
SPECSEAL_EOF
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -q -m 'frame: truncate'
