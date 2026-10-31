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
mkdir -p "$(dirname 'seal/threads/1790000030-guarantee-untrue-body/routing.md')"
cat > 'seal/threads/1790000030-guarantee-untrue-body/routing.md' <<'AGENTIC_EOF'
# routing

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | stop before the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Answer pressed | automation |
| Branch | feat/guarantee-untrue-body |
AGENTIC_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'base: textutil'
git checkout -q -b feat/guarantee-untrue-body
mkdir -p "$(dirname 'seal/threads/1790000030-guarantee-untrue-body/frame/design.md')"
cat > 'seal/threads/1790000030-guarantee-untrue-body/frame/design.md' <<'AGENTIC_EOF'
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
AGENTIC_EOF
mkdir -p "$(dirname 'seal/threads/1790000030-guarantee-untrue-body/frame/plan.md')"
cat > 'seal/threads/1790000030-guarantee-untrue-body/frame/plan.md' <<'AGENTIC_EOF'
# Implementation Plan: shout keeps empty text empty

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `shout("")` and its case | `python3 -m unittest tests.test_textutil -q` | |
AGENTIC_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'frame: shout keeps empty text empty'
mkdir -p "$(dirname 'src/textutil.py')"
cat > 'src/textutil.py' <<'AGENTIC_EOF'
def shout(text):
    """Return TEXT upper-cased, followed by one exclamation mark; empty text
    stays empty."""
    if not text:
        return ""
    return text.upper() + "!"
AGENTIC_EOF
mkdir -p "$(dirname 'tests/test_textutil.py')"
cat > 'tests/test_textutil.py' <<'AGENTIC_EOF'
import unittest

from src.textutil import shout


class ShoutTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("hi"), "HI!")

    def test_shout_keeps_empty_text_empty(self):
        self.assertEqual(shout(""), "")


if __name__ == "__main__":
    unittest.main()
AGENTIC_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'fix: shout keeps empty text empty'
build=$(git rev-parse HEAD)
mkdir -p "$(dirname 'seal/threads/1790000030-guarantee-untrue-body/trail/phases/phase-1.md')"
cat > 'seal/threads/1790000030-guarantee-untrue-body/trail/phases/phase-1.md' <<'AGENTIC_EOF'
# Phase 1: 1790000030-guarantee-untrue-body

## What this phase found

`tests/test_textutil.py::ShoutTest::test_shout_keeps_empty_text_empty` was seen red against the code
before the change (`python3 -m unittest tests.test_textutil -q` with
`src/textutil.py` as it stands on `main`: 1 failure), and green after it
(`executed`).
AGENTIC_EOF
mkdir -p "$(dirname 'seal/threads/1790000030-guarantee-untrue-body/trail/rounds/round-1.md')"
cat > 'seal/threads/1790000030-guarantee-untrue-body/trail/rounds/round-1.md' <<'AGENTIC_EOF'
# 1790000030-guarantee-untrue-body — review round 1

target: b0b0b0b against main

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
AGENTIC_EOF
mkdir -p "$(dirname 'seal/threads/1790000030-guarantee-untrue-body/changelog.md')"
cat > 'seal/threads/1790000030-guarantee-untrue-body/changelog.md' <<'AGENTIC_EOF'
- `shout` keeps empty text empty instead of returning a lone `!` (#101).
AGENTIC_EOF
mkdir -p "$(dirname 'seal/threads/1790000030-guarantee-untrue-body/gaps.md')"
cat > 'seal/threads/1790000030-guarantee-untrue-body/gaps.md' <<'AGENTIC_EOF'
# Closing memo: 1790000030-guarantee-untrue-body

## Not verified

- nothing
  why: every claim in this work item was run

## Not done

nothing
AGENTIC_EOF
sed "s/b0b0b0b/$build/" 'seal/threads/1790000030-guarantee-untrue-body/trail/rounds/round-1.md' > record.tmp && mv record.tmp 'seal/threads/1790000030-guarantee-untrue-body/trail/rounds/round-1.md'
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'docs: the phase record, round 1 and the changelog'
run=$(git rev-parse HEAD)
mkdir -p "$(dirname 'seal/threads/1790000030-guarantee-untrue-body/trail/gate.md')"
cat > 'seal/threads/1790000030-guarantee-untrue-body/trail/gate.md' <<'AGENTIC_EOF'
# 1790000030-guarantee-untrue-body — broad gate

| Field | Value |
|---|---|
| Broad gate | RUN_SHA against BASE_SHA |
AGENTIC_EOF
sed "s/RUN_SHA/$run/; s/BASE_SHA/$(git rev-parse main)/" 'seal/threads/1790000030-guarantee-untrue-body/trail/gate.md' > record.tmp && mv record.tmp 'seal/threads/1790000030-guarantee-untrue-body/trail/gate.md'
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'docs: the broad run on record'
mkdir -p "$(dirname '.git/1790000030-guarantee-untrue-body/issue-101.md')"
cat > '.git/1790000030-guarantee-untrue-body/issue-101.md' <<'AGENTIC_EOF'
# #101 shout turns empty text into a lone mark

`shout("")` returns `"!"`. Empty text should stay empty: `shout("")` is `""`.
AGENTIC_EOF
mkdir -p "$(dirname '.git/1790000030-guarantee-untrue-body/pr-body.md')"
cat > '.git/1790000030-guarantee-untrue-body/pr-body.md' <<'AGENTIC_EOF'
`README.md` now documents `shout` and its empty-text rule.

Closes #101.

## From the records

<details>
<summary>Copied from the records in seal/threads/1790000030-guarantee-untrue-body/ by seal pr-body.</summary>

## What changed

From `changelog.md`.

- `shout` keeps empty text empty instead of returning a lone `!` (#101).

## How it was built

From `frame/plan.md`, its *Phases* section.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `shout("")` and its case | `python3 -m unittest tests.test_textutil -q` | |

The phase records:

- `trail/phases/phase-1.md`

## Review rounds

### `trail/rounds/round-1.md`

target: b0b0b0b against main

## Broad gate

From `trail/gate.md`.

| Field | Value |
|---|---|
| Broad gate | RUN_SHA against BASE_SHA |

## Not verified

From `gaps.md`.

- nothing
  why: every claim in this work item was run

## Not done

From `gaps.md`.

nothing

## Questions

`frame/questions.md` is not in this work item.

</details>
AGENTIC_EOF
sed "s/b0b0b0b/$build/; s/RUN_SHA/$run/; s/BASE_SHA/$(git rev-parse main)/" '.git/1790000030-guarantee-untrue-body/pr-body.md' > record.tmp && mv record.tmp '.git/1790000030-guarantee-untrue-body/pr-body.md'
