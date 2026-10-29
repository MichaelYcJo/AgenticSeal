# Phase 3: 1793240966-the-framer-has-no-read-only-probe

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 80a3f439 |

## What this phase was asked

Build `frame/plan.md` *Phases* row 3 on `frame/questions.md` Q1's default
(a): the new case alone, two runs on each side, capped with
`--max-cost-usd 20`. One side runs the definition at `c48cd5e3` and the
other phase 2's, both with the suite at phase 2's commit, `e8051ef0`. Both
side files are committed under the work item's `evals/`. The phase record
quotes each side's results for the two new graders and its spend. Q2's
default (a) applies where the old side passes, and Q3's default is that the
crafter runs the sides itself.

## What this phase found

**Q3 resolved to (a).** The crafter's own environment started
`claude plugin eval` through `noninferiority.py run`, and both sides
completed with exit 0.

**The sides (executed).** Each side's file records `cut_short: false`, two
runs and no run error.

| Side | `--rev` | `shape-answers-by-probe` | `shape-no-measurement-row` | Spend |
|---|---|---|---|---|
| old | `c48cd5e3` | failed 2 of 2: "pattern not found in file seal/threads/1790000025-sharp-s/frame/design.md" | failed 2 of 2: "pattern found (expected absent)" | 5.20 USD (2.71 and 2.49), 336 s |
| new | `e8051ef0` | passed 2 of 2 | run 0 failed, run 1 passed | 4.81 USD (2.38 and 2.43), 339 s |

The two sides spent 10.01 USD together. Q1 caps the spend at 20 USD, so
the new side ran with `--max-cost-usd 14.8`, which is 20 USD less the old
side's spend, rather than 20. The preload the side files record is 22,458
bytes on the old side and 24,013 on the new.

**The case filter is a glob over the case's name.** The plan's command
passes `--case 'rule-framer-sharp-s'`. `claude plugin eval --help` says the
filter is a "name glob", and the case's name is `framer
rule-framer-sharp-s`. Both sides ran with `--case '*rule-framer-sharp-s'`,
and each side file's `suite.caseFilter` records that filter and one case.

**The old framers probed, and put the answer elsewhere (executed, read from
the saved traces).** Both old-side runs ran `shout("straße")` through
`python3 -c` and wrote `STRASSE!` into the frame: run 0 in `## Scope`, the
scenario table and `plan.md`, run 1 in the scenario table, a list in
`frame/design.md` and `plan.md`. Neither
wrote it on a `## Grounding` line labelled `executed`. So the case does not
separate probing from not probing. It separates writing the probe's answer
where the new rule says from writing it somewhere else. Both new-side runs
probed from a `git clone --no-local` under the scratchpad and wrote the
answer into `## Grounding` labelled `executed`.

**`shape-no-measurement-row` fired only on a row the new rule keeps, and is
removed (`7ac24a06`).** Each of the three rows it caught asked whether
issue #105's comments change the request. Each row said `gh` was not
authenticated in the runner's environment and the clone has no remote. The
old side's run 1 first wrote that row as `a person` and then edited it to
`a measurement`. The new side's run 0 wrote "`gh issue view 105
--comments` was refused in the framer's environment for lack of GitHub auth,
so no probe could read them here", with the orchestrator as the party to run
it. The new rule writes such a row "only where no probe can run in your
environment", and the reason says which, so that row obeys the rule. In four
runs the grader caught no row about `shout`, and it failed one new-side run
for a correct row. Contract rule 18 says to fix a check that refuses correct
behaviour. The grader, its pattern and its case in
`tests/evals/test_rule_cases.py` are gone, and `shape-answers-by-probe`
alone holds S8. The no-row half of the rule is read by the proofer at
review, as S5 already is. `gaps.md` records the divergence.

**S8 holds on the grader that remains.** `shape-answers-by-probe` fails
every old-side run and passes every new-side run. Q2's default was not
needed.

**The side files come from the saved paid output, and nothing was paid
twice.** Each side ran with `--out` under the scratchpad, so its `.raw/`
directory with the traces stayed outside the tree. `noninferiority.py run
--from-raw` then wrote each side file into
`seal/threads/1793240966-the-framer-has-no-read-only-probe/evals/`, and
`python3 -m json.tool` of each matched the scratchpad copy (`cmp` exit 0).
The four directories the eval kept, `/private/tmp/e-Uvsapi`,
`/private/tmp/e-lcUxMP`, `/private/tmp/e-I7xAu2` and
`/private/tmp/e-Kpu3X9`, were gone after each side, removed by the
runner's `save_side`, and so was each side's `agentic-*` work directory.

**The narrow run after the removal (executed).** `bin/test
tests/evals/test_rule_cases.py tests/behaviour/test_evals_layout.py
tests/text/test_no_case_tells_the_agent_it_is_evaluated.py
tests/github/test_rules.py -q` exited 0, 90 passed. `bin/test
tests/test_censuses.py -q`, run with the side files staged, exited 0.
`uvx ruff check` and `uvx ruff format --check` over the two Python files
exited 0.
