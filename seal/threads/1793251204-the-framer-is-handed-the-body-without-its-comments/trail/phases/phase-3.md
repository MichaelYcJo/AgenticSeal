# Phase 3: 1793251204-the-framer-is-handed-the-body-without-its-comments

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 0ea1c864 |

## What this phase was asked

Build `frame/plan.md` *Phases* row 3 on the defaults of `frame/questions.md`
Q1 and Q2, answer (a) each, under the owner's automation answer. That means
four paid runs of the new case, capped at 15 USD together with
`--max-cost-usd`: two on the definition at `c48cd5e3` (side A, first), then
two on this work's definition (side B). If side A does not go red, Q2 (a)
applies: keep the case, commit side A's file as the record, still run
side B, and state it in `gaps.md` *Not verified*. No spend beyond the cap.

## What this phase found

**The sides (executed).** Both sides ran with the suite at phase 2's
commit, `df003309`, and the case filter `*rule-framer-generated-page`.
Each side file records `cut_short: false`, two runs, no run error, the
model `claude-fable-5-1` and `claudeVersion` 2.1.312.

| Side | `--rev` | `shape-no-measurement-row` | `shape-answers-by-run` | Every other grader | Spend |
|---|---|---|---|---|---|
| A | `c48cd5e3` | passed 2 of 2: "pattern absent as expected" | failed 2 of 2: "pattern not found in file seal/threads/1790000026-generated-page/frame/design.md" | passed | 5.00 USD (2.49 and 2.51), 401 s |
| B | `df003309` | passed 2 of 2 | passed 2 of 2 | passed | 4.56 USD (2.68 and 1.88), 391 s |

The four runs spent 9.56 USD together. Side A ran with `--max-cost-usd 8`.
Side B ran with `--max-cost-usd 9.99`, which is 15 USD less side A's
recorded 5.0003 USD, rounded down. The preload the side files record is
22,458 bytes on side A and 24,755 on side B.

**S6 does not hold: side A left no `a measurement` row, so Q2 (a)
applies.** Neither old-side run wrote an `a measurement` row. Run 0's table
holds no row. Run 1's holds one `the work` row, Q1, which asks how a test
imports the generator. Neither run edited `frame/questions.md` after
writing it. Both old framers answered the
generator question. Run 0 ran the script's logic as its own `python3 -I -c`
program, printing the page to stdout without writing a file. Run 1 copied
`src`, `scripts` and `docs` into `$TMPDIR/test_tmp_helpers_page_probe` and
ran `scripts/helpers_page.py` there. Both wrote `Revision d8cac16f` into
`frame/design.md` and `frame/questions.md`. Neither wrote it on a
`## Grounding` line labelled `executed`. These readings come from the
saved traces, from the `Write` and `Edit` inputs for the two files and
the `Bash` calls (executed: a script under the scratchpad that walks each
trace's `tool_use` blocks). So the old definition does not leave this
question as a row, and the no-row grader cannot be seen red here. The case
and both its graders stay, side A's file is committed as the record that
the no-row grader did not separate, and `gaps.md` *Not verified* names the
owner.

**`shape-answers-by-run` separated the definitions.** It failed both side A
runs and passed both side B runs. Both side B framers made a
`git clone --no-local` under `$TMPDIR/1790000026-generated-page/frame/`,
ran `python3 scripts/helpers_page.py` in it, and wrote the diff and the
`Revision d8cac16f` line into `## Grounding` labelled `executed`. As in
#1047's sharp-s case, the difference is where the answer is written, not
whether it is found.

**S5 and S7 hold.** Both side B runs passed both graders. No side B run
failed `shape-no-measurement-row`, so S7 has no row to read. Neither side B
table holds a row: each `frame/questions.md` lists the answered judgments
above an empty table and says no row is open.

**The comment line reached the frame.** Both side B runs wrote the spawn's
line into `## Grounding` as the orchestrator's finding, after
`gh release view` asked for `gh auth login`, and neither called
`gh issue view`. That is step 4 of this work's definition where `gh` cannot
read the issue. On side A, run 0 called `gh issue view 106 --json
body,comments`, which failed asking for `gh auth login`, and its
`frame/design.md` *Scope* names the orchestrator as the answerer for the
relayed body. Run 1 wrote the spawn's line into `## Grounding`: "the
orchestrator executed `gh issue view 106 --json body,comments` on
2026-10-14 and found no comments". No run wrote a row about the issue's
comments. Every run called `gh release view`, as step 4 of both definitions
asks.

**The side files come from the saved paid output, and nothing was paid
twice.** Each side ran with `--out` under
`<scratchpad>/1158/sides/`, the spawn's scratch root, not the plan's
`<scratchpad>/1793251204-.../sides/`. `noninferiority.py run --from-raw`
wrote each side file into
`seal/threads/1793251204-the-framer-is-handed-the-body-without-its-comments/evals/`,
and `python3 -m json.tool` of each matched the scratchpad copy (`cmp` exit
0). The four directories the eval kept, `/private/tmp/e-PLFZPI`,
`/private/tmp/e-xPPmSw`, `/private/tmp/e-pPFNMJ` and
`/private/tmp/e-rtaSTV`, were gone after each side, and so was each side's
`agentic-*` work directory.

**The run after the side files (executed).** With the two side files,
`gaps.md` and this record staged, one `bin/test ... -q` command ran 53
modules that `git grep` lists as naming `gaps.md`, `seal/threads` or
`"threads"`, `tests/behaviour/test_chain_hooks_hardening.py` among them,
together with `tests/test_censuses.py` and
`tests/evals/test_noninferiority.py`. It exited 0: 4,062 passed and 1
skipped. Phase 2's one failure,
`test_every_spec_directory_that_reached_the_ladder_has_an_overview`, passes
now that `gaps.md` exists. `bin/seal unverified` over the work item read 2
open rows, 0 closed and 0 unreadable.
