# Phase 2: 1793171929-the-suite-tells-the-agent-it-is-evaluated

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 1fbae5ae |

## What this phase was asked

Change `noninferiority.py#run_side` to `prefix="agentic-"`. Before that,
see its *Test_run_side* case red with the old prefix. Q1 is built on its
default (a): the truth graders stay in the loaded tree, and only the
temporary directory is renamed. #992 edits `evals/README.md` and
`noninferiority.py` next, so only what the frame names changes there.

## What this phase found

**The case was seen red with the old prefix.**
`bin/test tests/evals/test_noninferiority.py -q -p no:xdist -k Test_run_side`
exited 1, naming the component `agentic-eval-tu4vxl8p` (executed). After
the change, the plan's command over `tests/evals/test_noninferiority.py`
and the text case exited 0, with 253 passed (executed). `seal mutate` with
the prefix `agentic-grader-` went red (executed).

**The case takes the word list from the text case.** It imports `REFUSED`
from `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py`, which
`tests/conftest.py` puts on `sys.path`. The case drives `run` with
`call_eval` replaced by a stand-in that records the tree and writes no
JSON. It reads the path below `tempfile.gettempdir()`.

**The random part of the name is read too.** `mkdtemp` adds eight random
characters from lower-case letters, digits and `_`. A stem can land in them
after a digit, an underscore or the prefix's `-`, so the case can go red by
chance. The odds are about one run in 400,000 (computed, not measured).

**`evals/README.md` gained one sentence in this phase.** The paragraph
phase 1 wrote names the text case. This phase adds that the loaded tree's
path holds none of the words, and names *Test_run_side*. The plan's phase 2
row names no README change; `gaps.md` records it.
