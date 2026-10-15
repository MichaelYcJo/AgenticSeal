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
mkdir -p "$(dirname 'seal/specs/1790000030-broad-run-failing-test/routing.md')"
cat > 'seal/specs/1790000030-broad-run-failing-test/routing.md' <<'SPECSEAL_EOF'
# routing

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | stop before the pull request |
| Planning | framer |
| Implementation | smith |
| Automation | yes |
| Answer pressed | automation |
| Branch | feat/broad-run-failing-test |
SPECSEAL_EOF
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -q -m 'base: textutil'
git checkout -q -b feat/broad-run-failing-test
mkdir -p "$(dirname 'seal/specs/1790000030-broad-run-failing-test/spec.md')"
cat > 'seal/specs/1790000030-broad-run-failing-test/spec.md' <<'SPECSEAL_EOF'
# Feature Specification: the shout case names its expectation

## Scope

`tests/test_textutil.py` states what `shout` returns.

Framed 2026-10-14 by framer, before the build.
SPECSEAL_EOF
mkdir -p "$(dirname 'seal/specs/1790000030-broad-run-failing-test/overview.md')"
cat > 'seal/specs/1790000030-broad-run-failing-test/overview.md' <<'SPECSEAL_EOF'
# 1790000030-broad-run-failing-test — overview

## Why this work exists

The shout case states what `shout` returns.

## Where spec and implementation diverged

none

## Not verified

none — every claim in this work item was run

## Not done

none

## Fed back into the spec

none
SPECSEAL_EOF
mkdir -p "$(dirname 'seal/specs/1790000030-broad-run-failing-test/plan.md')"
cat > 'seal/specs/1790000030-broad-run-failing-test/plan.md' <<'SPECSEAL_EOF'
# Implementation Plan: the shout case

Approved 2026-10-14 by the repository owner, when `smith` was spawned.

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | the case in `tests/test_textutil.py` | `python3 -m unittest tests.test_textutil -q` | |
SPECSEAL_EOF
mkdir -p "$(dirname 'tests/test_textutil.py')"
cat > 'tests/test_textutil.py' <<'SPECSEAL_EOF'
import unittest

from src.textutil import shout


class ShoutTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("hi"), "HI!!")


if __name__ == "__main__":
    unittest.main()

# the branch's change
SPECSEAL_EOF
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -q -m 'feat: the build'
target=$(git rev-parse HEAD)
mkdir -p "$(dirname 'seal/specs/1790000030-broad-run-failing-test/rounds/round-1.md')"
cat > 'seal/specs/1790000030-broad-run-failing-test/rounds/round-1.md' <<'SPECSEAL_EOF'
# 1790000030-broad-run-failing-test — review round 1

| Field | Value |
|---|---|
| Target SHA | TARGET_SHA against main |

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | `shout` keeps its mark | `src/textutil.py:3` | confirmed | read |

## Paste-ready fixes

## Executed probes

| What was run | Result |
|---|---|
SPECSEAL_EOF
sed "s/TARGET_SHA/$target/" 'seal/specs/1790000030-broad-run-failing-test/rounds/round-1.md' > round.tmp && mv round.tmp 'seal/specs/1790000030-broad-run-failing-test/rounds/round-1.md'
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -q -m 'review: round 1'
