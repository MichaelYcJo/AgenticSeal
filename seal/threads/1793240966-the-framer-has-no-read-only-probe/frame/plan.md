# Implementation Plan: 1793240966-the-framer-has-no-read-only-probe

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 to 3.

## Summary

The framer's definition neither provides for nor forbids running a command
to see how something behaves, so a question a command answers either went to
the build as an `a measurement` row or stayed open. #1047 counts 40 such rows
across 0.22.x, 13 still open when their work item shipped (the issue's
figures, executed by its author and not re-derived here). This work gives
`agents/framer.md` one rule that provides for a read-only probe. The rule
bounds where the probe runs and what it may leave, sends its answer to
`frame/design.md`'s `## Grounding` labelled `executed`, and keeps a
measurement row only for a question no probe can run in the framer's
environment. A fifth framer case pins the outcome, and one paid run shows the
case red on the old definition and green on the new one.

## Technical context

- `agents/framer.md` (189 lines, 10,334 bytes at `c48cd5e3`, executed with
  `wc -l` and `wc -c`). The sentences this work amends are at `:23-25`
  (*Job*), `:76` (step 5), `:86-88` (step 8), `:107-108` (*Never*) and
  `:136-137` (the residue rule). The new rule goes after
  **What the tree can answer, you answer.** (`:120-127`).
- Every sentence the existing cases pin stays. Step 8's "is `executed`" and
  "no check of the repository's" are read by
  `tests/text/test_a_question_says_who_can_answer_it.py:188-205`.
  "You ask nobody anything", "has no `AskUserQuestion`", "`routing.md` is not
  one of them" and "a thing to report, never a thing to write" are read by
  `tests/behaviour/test_waiver_decided_at_start.py:602-650`. The *Never*
  line about reference roots is read by
  `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py:118`.
- `tests/text/test_no_passage_is_pasted_into_a_second_file.py` refuses a run
  of `WINDOW` consecutive words two rule files share. The new rule takes the
  clone pattern from `agents/proofer.md` *Rules* and must word it afresh.
- `seal rules` (`tests/github/test_rules.py`) refuses a `check:` line naming
  a path that does not exist. The case directory therefore lands in phase 1,
  before phase 2's rule names it.
- `evals/scripts/rule_cases.py:432-505` builds the framer cases from
  `FRAMER_ISSUES` through `framer_case(index, slug, issue)`. The item id is
  `179000002{index}-{slug}`, so the fifth case is `1790000025-sharp-s`.
  `shape_regex` and `behaviour.grader` take `match="not_contains"` as an
  extra field, as `evals/scripts/behaviour.py#report_shape` passes it to
  `#report_regex`. The generator
  reproduces today's framer and crafter cases byte for byte (executed, see
  `frame/design.md` *Grounding*).
- The rule change parses. Executed at `c48cd5e3`:
  `skills/settle/scripts/rule_changes.py#parse` over this design returns one
  `change` op with no errors, and `#pattern` of its `from` matches inside
  `docs/the-agent-set.md`'s section *One contract every agent receives, and
  one definition each*, lines 7 to 52.
- `evals/scripts/noninferiority.py run` takes `--case GLOB`, `--rev`,
  `--suite-rev`, `--runs` and `--max-cost-usd`
  (`evals/scripts/noninferiority.py:1557-1567`). So one case runs alone on
  the old tree with the new suite.

**The chosen approach's failure scenario.** In six months a framer meets a
question whose probe would be slow or costly, such as a generator over a
large tree or a `gh` query over hundreds of pull requests. The rule says
"run it", and the framer spends minutes a row would have deferred. That cost
shows in the segment's `seal cost` reading and in the flow log
(`docs/measuring-a-run.md`). It is the trade this issue asks for: a probe
spent at framing replaces a row that waits for the build. A second failure:
the harness gives a framer no scratchpad. The rule then has the framer say so
and not probe in the tree, which brings back the row this work removes, for
that environment only.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Keep the definition silent and let framers probe as #955's did | #1033's framer counted with `awk` instead of running the reader, and routed the question to the build, where it was still open when the record went. Each framer decides alone, and the same question gets a probe in one frame and a row in the next. | Rejected. The structure kept is the silence, and its premise, that framers probe anyway, is false on the issue's own record. |
| A2. Allow any probe in the tree, read-only by instruction | A reader or a generator run in the worktree writes `__pycache__`, a cache or its output under `evals/`. The frame's `git add` of its directory misses it, and the next `git status` shows a dirty tree nobody can attribute. | Rejected. A command that only reads runs in the tree. Anything that writes runs under `<scratchpad>/<work-item-id>/frame/`, and the repository's code runs from a clone there. |
| A3. The chosen rule: reads against the tree, writes and runs of the code under the work item's scratch directory, answer in `## Grounding` labelled `executed`, a row only where no probe can run here | See the failure scenario above. | Chosen. |
| A4. Also let the framer run a test module, a linter or a typechecker as a probe | A frame then rests on a verdict the build owns, and contract rule 2's line between the slice an agent touched and the broad run gets a third party that touched nothing. Step 8's "no check of the repository's" stops being true. | Rejected. A question about the suite is answered from `.test_durations` and the cases' text, which are read. |
| A5. Replace the `a measurement` answerer: every measurement becomes the framer's, or `the work` | A CI leg on Windows or Linux cannot run on a framer running on macOS, and a harness behaviour no subagent can trigger has no other owner. Folding those into `the work` hides that the answer is a run nobody in the chain can make. | Rejected. The premise that keeps the value is checked: #947 reads three CI legs, ubuntu, Windows and macOS (read: the issue's *Before* table), and this framer runs on darwin (read: the session's environment). |
| A6. Label a probe's answer with a new word such as `probed` | A fourth label beside `executed`, `read` and `unverified` that no reader checks, and a frame using it is a frame the sealer cannot grade by contract rule 4. | Rejected. `executed` is what a probe's fact is. |
| A7. Put the probe rule in the contract, for every agent | The crafter, the proofer and the tracer already have probe rules of their own, and rule 7 already binds every agent's leavings. A contract rule that one agent needs is a per-role rule in the universal file, which the contract's preamble refuses. | Rejected. |
| A8. Restate the `a measurement` definition in `skills/implement/SKILL.md` *3. The SDD file set* to name the framer | Two files then state when a framer opens the row, and the first edit to one leaves the other stating the old rule. The skill's sentence names no party and stays true. | Rejected. `agents/framer.md` is the one source. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `evals/scripts/rule_cases.py`: a fifth `FRAMER_ISSUES` entry, `sharp-s`, whose issue asks what `shout` returns for `straße` without giving the answer. `framer_case` takes a case's extra graders, and `sharp-s` has two: `shape-answers-by-probe`, a regex over `frame/design.md` matching inside `## Grounding` only, for a line holding both `executed` and `STRASSE`; and `shape-no-measurement-row`, a `not_contains` regex over `frame/questions.md` for a cell holding `a measurement`. The docstring's framer line says five issues. `evals/behaviour/framer/rule-framer-sharp-s/` is the generator's output, committed | `python3 evals/scripts/rule_cases.py` regenerates the tree, and `git status --short` then lists only `evals/behaviour/framer/rule-framer-sharp-s/` and the script. `bin/test` over `tests/evals/test_rule_cases.py`, `tests/behaviour/test_evals_layout.py` and `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py`, in one command. Each new grader's regex is shown matching a hand-written frame that answers in `## Grounding` and failing one that leaves the answer as a row, run once in a `test_tmp_*` file and deleted | |
| 2 | `agents/framer.md`: the new rule in `## Rules` with its `check:` line naming `evals/behaviour/framer/rule-framer-sharp-s/` and `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`, and the five amendments `frame/design.md` *Data & interfaces* lists. The new case in `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py` for `<scratchpad>/<work-item-id>/frame/`, with the module docstring's class line naming the framer | S4: the new case run against `agents/framer.md` at `c48cd5e3` and seen red, then green after the sentence. S6 and S7: `bin/test` over every module `git grep -l -e framer.md -e '"agents"' -- tests/` lists, in one command, `tests/github/test_rules.py` among them. `agents/framer.md`'s byte count before and after, recorded in the phase record for the pull request body | |
| 3 | The new case run on Q1's default, two runs on each side: `evals/scripts/noninferiority.py run --agent framer --case 'rule-framer-sharp-s' --rev c48cd5e3 --suite-rev <phase 2 commit> --runs 2 --max-cost-usd 20`, and the same with `--rev <phase 2 commit>`. Both side files are committed under `seal/threads/1793240966-the-framer-has-no-read-only-probe/evals/` | S8: each side file's grader results for `shape-answers-by-probe` and `shape-no-measurement-row`, quoted in the phase record with the spend each side recorded. Red on the old side, green on every new run, or Q2's default where the old side passes | |

## Operational impact

None for a deployer. No migration, no environment variable and no dependency
is added. A framer spawned after this work may run commands and write a
probe under `<scratchpad>/<work-item-id>/frame/`, which it removes before it
hands back. `agents/framer.md` grows by the new rule, and the release table's
preload row shows it. The pull request body states the bytes before and
after, as `docs/release-checklist.md` *Read the release table before the
merge* asks. The changelog fragment carries a `### Process changes` row,
because the framer's way of answering questions changes for every later work
item.
