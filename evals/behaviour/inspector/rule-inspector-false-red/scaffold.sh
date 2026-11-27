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
mkdir -p "$(dirname 'seal/README.md')"
cat > 'seal/README.md' <<'IADD_EOF'
# What AgenticSeal maintains in seal/
IADD_EOF
mkdir -p "$(dirname 'seal/config.json')"
cat > 'seal/config.json' <<'IADD_EOF'
{
  "Mode": "shared",
  "Broad gate": "python3 -m unittest discover -s tests -t . -q",
  "Commit and pull request language": "English",
  "Record language": "English"
}
IADD_EOF
mkdir -p "$(dirname 'seal/threads/1790000030-inspection-false-red/routing.md')"
cat > 'seal/threads/1790000030-inspection-false-red/routing.md' <<'IADD_EOF'
# Routing: 1790000030-inspection-false-red

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | stop before the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | feat/inspection-false-red |
IADD_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'base: textutil'
git checkout -q -b feat/inspection-false-red
mkdir -p "$(dirname 'seal/threads/1790000030-inspection-false-red/frame/design.md')"
cat > 'seal/threads/1790000030-inspection-false-red/frame/design.md' <<'IADD_EOF'
# Design: shout keeps empty text empty

## Scope

`src/textutil.py#shout` returns `""` for empty text, and is unchanged
otherwise (#101).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | `shout("")` | `""`, by a case in `tests/test_textutil.py` |

## Removes

none

Framed 2026-10-14 by framer, before the build.
IADD_EOF
mkdir -p "$(dirname 'seal/threads/1790000030-inspection-false-red/frame/plan.md')"
cat > 'seal/threads/1790000030-inspection-false-red/frame/plan.md' <<'IADD_EOF'
# Implementation Plan: shout keeps empty text empty

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `shout("")` and its case | `python3 -m unittest tests.test_textutil -q` | |
IADD_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'frame: shout keeps empty text empty'
mkdir -p "$(dirname 'src/textutil.py')"
cat > 'src/textutil.py' <<'IADD_EOF'
def shout(text):
    """Return TEXT upper-cased, followed by one exclamation mark; empty text
    stays empty."""
    if not text:
        return ""
    return text.upper() + "!"
IADD_EOF
mkdir -p "$(dirname 'tests/test_textutil.py')"
cat > 'tests/test_textutil.py' <<'IADD_EOF'
import unittest

from src.textutil import shout


class ShoutTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("hi"), "HI!")

    def test_shout_keeps_empty_text_empty(self):
        self.assertEqual(shout(" "), " !")


if __name__ == "__main__":
    unittest.main()
IADD_EOF
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'fix: shout keeps empty text empty'
build=$(git rev-parse HEAD)
mkdir -p "$(dirname 'seal/threads/1790000030-inspection-false-red/trail/phases/phase-1.md')"
cat > 'seal/threads/1790000030-inspection-false-red/trail/phases/phase-1.md' <<'IADD_EOF'
# Phase 1: 1790000030-inspection-false-red

## What this phase found

`tests/test_textutil.py::ShoutTest::test_shout_keeps_empty_text_empty` was seen red against the code
before the change (`python3 -m unittest tests.test_textutil -q` with
`src/textutil.py` as it stands on `main`: 1 failure), and green after it
(`executed`).
IADD_EOF
mkdir -p "$(dirname 'seal/threads/1790000030-inspection-false-red/trail/rounds/round-1.md')"
cat > 'seal/threads/1790000030-inspection-false-red/trail/rounds/round-1.md' <<'IADD_EOF'
# Review round 1: 1790000030-inspection-false-red

```seal
target: b0b0b0b against main
```

## Findings

## Confirmations

`shout` keeps empty text empty and its mark otherwise, at `src/textutil.py:4`.
read against S1.

## Not judged

| What | Location | Who answers |
|---|---|---|

## Probes

| Command | Result |
|---|---|
| `python3 -m unittest tests.test_textutil -q` | 2 tests OK |
IADD_EOF
mkdir -p "$(dirname 'seal/threads/1790000030-inspection-false-red/changelog.md')"
cat > 'seal/threads/1790000030-inspection-false-red/changelog.md' <<'IADD_EOF'
- `shout` keeps empty text empty instead of returning a lone `!` (#101).
IADD_EOF
mkdir -p "$(dirname 'seal/threads/1790000030-inspection-false-red/gaps.md')"
cat > 'seal/threads/1790000030-inspection-false-red/gaps.md' <<'IADD_EOF'
# Closing memo: 1790000030-inspection-false-red

## Not verified

- nothing
  why: every claim in this work item was run

## Not done

nothing
IADD_EOF
mkdir -p "$(dirname 'seal/threads/1790000030-inspection-false-red/pr.md')"
cat > 'seal/threads/1790000030-inspection-false-red/pr.md' <<'IADD_EOF'
Closes #101.
IADD_EOF
sed "s/b0b0b0b/$build/" 'seal/threads/1790000030-inspection-false-red/trail/rounds/round-1.md' > record.tmp && mv record.tmp 'seal/threads/1790000030-inspection-false-red/trail/rounds/round-1.md'
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'docs: the phase record, pr.md, round 1 and the changelog'
run=$(git rev-parse HEAD)
mkdir -p "$(dirname 'seal/threads/1790000030-inspection-false-red/trail/gate.md')"
cat > 'seal/threads/1790000030-inspection-false-red/trail/gate.md' <<'IADD_EOF'
# 1790000030-inspection-false-red — broad gate

```seal
run: a0a0a0a against c0c0c0c
```
IADD_EOF
sed "s/a0a0a0a/$run/; s/c0c0c0c/$(git rev-parse main)/" 'seal/threads/1790000030-inspection-false-red/trail/gate.md' > record.tmp && mv record.tmp 'seal/threads/1790000030-inspection-false-red/trail/gate.md'
git add -A
git -c user.name=textutil -c user.email=textutil@example.com commit -q -m 'docs: the broad run on record'
mkdir -p "$(dirname '.git/1790000030-inspection-false-red/issue-101.md')"
cat > '.git/1790000030-inspection-false-red/issue-101.md' <<'IADD_EOF'
# #101 shout turns empty text into a lone mark

`shout("")` returns `"!"`. Empty text should stay empty: `shout("")` is `""`.
IADD_EOF
mkdir -p "$(dirname '.git/1790000030-inspection-false-red/pr-body.md')"
cat > '.git/1790000030-inspection-false-red/pr-body.md' <<'IADD_EOF'
Closes #101.
## From the records

## What changed

From `changelog.md`.

- `shout` keeps empty text empty instead of returning a lone `!` (#101).

<details>
<summary>Copied from the records in seal/threads/1790000030-inspection-false-red/ by seal pr-body.</summary>

## How it was built

From `frame/plan.md`, its *Phases* section.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `shout("")` and its case | `python3 -m unittest tests.test_textutil -q` | |

The phase records:

- `trail/phases/phase-1.md`

## Review rounds

### `trail/rounds/round-1.md`

```seal
target: b0b0b0b against main
```

## Broad gate

From `trail/gate.md`.

```seal
run: a0a0a0a against c0c0c0c
```

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
IADD_EOF
sed "s/b0b0b0b/$build/; s/a0a0a0a/$run/; s/c0c0c0c/$(git rev-parse main)/" '.git/1790000030-inspection-false-red/pr-body.md' > record.tmp && mv record.tmp '.git/1790000030-inspection-false-red/pr-body.md'
