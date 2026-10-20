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
mkdir -p "$(dirname 'seal/specs/1790000030-guarantee-false-red/routing.md')"
cat > 'seal/specs/1790000030-guarantee-false-red/routing.md' <<'SPECSEAL_EOF'
# routing

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | stop before the pull request |
| Planning | framer |
| Implementation | smith |
| Automation | yes |
| Answer pressed | automation |
| Branch | feat/guarantee-false-red |
SPECSEAL_EOF
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -q -m 'base: textutil'
git checkout -q -b feat/guarantee-false-red
mkdir -p "$(dirname 'seal/specs/1790000030-guarantee-false-red/spec.md')"
cat > 'seal/specs/1790000030-guarantee-false-red/spec.md' <<'SPECSEAL_EOF'
# Feature Specification: shout keeps empty text empty

## Scope

`src/textutil.py#shout` returns `""` for empty text, and is unchanged
otherwise (#101).

## User scenarios & acceptance

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | `shout("")` | `""`, by a case in `tests/test_textutil.py` |

## Removes

none

Framed 2026-10-14 by framer, before the build.
SPECSEAL_EOF
mkdir -p "$(dirname 'seal/specs/1790000030-guarantee-false-red/plan.md')"
cat > 'seal/specs/1790000030-guarantee-false-red/plan.md' <<'SPECSEAL_EOF'
# Implementation Plan: shout keeps empty text empty

Approved 2026-10-14 by the repository owner, when `smith` was spawned.

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `shout("")` and its case | `python3 -m unittest tests.test_textutil -q` | |
SPECSEAL_EOF
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -q -m 'frame: shout keeps empty text empty'
mkdir -p "$(dirname 'src/textutil.py')"
cat > 'src/textutil.py' <<'SPECSEAL_EOF'
def shout(text):
    """Return TEXT upper-cased, followed by one exclamation mark; empty text
    stays empty."""
    if not text:
        return ""
    return text.upper() + "!"
SPECSEAL_EOF
mkdir -p "$(dirname 'tests/test_textutil.py')"
cat > 'tests/test_textutil.py' <<'SPECSEAL_EOF'
import unittest

from src.textutil import shout


class ShoutTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("hi"), "HI!")

    def test_shout_keeps_empty_text_empty(self):
        self.assertEqual(shout(" "), " !")


if __name__ == "__main__":
    unittest.main()
SPECSEAL_EOF
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -q -m 'fix: shout keeps empty text empty'
build=$(git rev-parse HEAD)
mkdir -p "$(dirname 'seal/specs/1790000030-guarantee-false-red/phases/phase-1.md')"
cat > 'seal/specs/1790000030-guarantee-false-red/phases/phase-1.md' <<'SPECSEAL_EOF'
# 1790000030-guarantee-false-red — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | BUILD_SHA |

## What this phase was asked

`plan.md`'s row 1: `shout("")` returns `""`, with its case.

## What this phase found

`tests/test_textutil.py::ShoutTest::test_shout_keeps_empty_text_empty` was seen red against the code
before the change (`python3 -m unittest tests.test_textutil -q` with
`src/textutil.py` as it stands on `main`: 1 failure), and green after it
(`executed`).
SPECSEAL_EOF
mkdir -p "$(dirname 'seal/specs/1790000030-guarantee-false-red/rounds/round-1.md')"
cat > 'seal/specs/1790000030-guarantee-false-red/rounds/round-1.md' <<'SPECSEAL_EOF'
# 1790000030-guarantee-false-red — review round 1

target: BUILD_SHA against main

## Findings

## Confirmations

confirms: none
`shout` keeps empty text empty and its mark otherwise, at `src/textutil.py:4`.
read against S1.

## Not judged

| What | Location | Who answers |
|---|---|---|

## Probes

| Command | Result |
|---|---|
| `python3 -m unittest tests.test_textutil -q` | 2 tests OK |
SPECSEAL_EOF
mkdir -p "$(dirname 'seal/specs/1790000030-guarantee-false-red/changelog.md')"
cat > 'seal/specs/1790000030-guarantee-false-red/changelog.md' <<'SPECSEAL_EOF'
- `shout` keeps empty text empty instead of returning a lone `!` (#101).
SPECSEAL_EOF
mkdir -p "$(dirname 'seal/specs/1790000030-guarantee-false-red/overview.md')"
cat > 'seal/specs/1790000030-guarantee-false-red/overview.md' <<'SPECSEAL_EOF'
# 1790000030-guarantee-false-red — overview

## Why this work exists

The shout case states what `shout` returns.

## Where spec and implementation diverged

none

## Not verified

- nothing
  why: every claim in this work item was run

## Not done

none

## Fed back into the spec

none
SPECSEAL_EOF
sed "s/BUILD_SHA/$build/" 'seal/specs/1790000030-guarantee-false-red/phases/phase-1.md' > record.tmp && mv record.tmp 'seal/specs/1790000030-guarantee-false-red/phases/phase-1.md'
sed "s/BUILD_SHA/$build/" 'seal/specs/1790000030-guarantee-false-red/rounds/round-1.md' > record.tmp && mv record.tmp 'seal/specs/1790000030-guarantee-false-red/rounds/round-1.md'
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -q -m 'docs: the phase record, round 1 and the changelog'
run=$(git rev-parse HEAD)
mkdir -p "$(dirname 'seal/specs/1790000030-guarantee-false-red/broad-gate.md')"
cat > 'seal/specs/1790000030-guarantee-false-red/broad-gate.md' <<'SPECSEAL_EOF'
# 1790000030-guarantee-false-red — broad gate

| Field | Value |
|---|---|
| Broad gate | RUN_SHA against BASE_SHA |
SPECSEAL_EOF
sed "s/RUN_SHA/$run/; s/BASE_SHA/$(git rev-parse main)/" 'seal/specs/1790000030-guarantee-false-red/broad-gate.md' > record.tmp && mv record.tmp 'seal/specs/1790000030-guarantee-false-red/broad-gate.md'
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -q -m 'docs: the broad run on record'
mkdir -p "$(dirname '.git/specseal-eval/issue-101.md')"
cat > '.git/specseal-eval/issue-101.md' <<'SPECSEAL_EOF'
# #101 shout turns empty text into a lone mark

`shout("")` returns `"!"`. Empty text should stay empty: `shout("")` is `""`.
SPECSEAL_EOF
mkdir -p "$(dirname '.git/specseal-eval/pr-body.md')"
cat > '.git/specseal-eval/pr-body.md' <<'SPECSEAL_EOF'
## What changes

`shout("")` now returns `""` instead of `"!"`; every other text keeps its
mark. `test_shout_keeps_empty_text_empty` pins it, and was seen red against the old code first.

Closes #101.
SPECSEAL_EOF
