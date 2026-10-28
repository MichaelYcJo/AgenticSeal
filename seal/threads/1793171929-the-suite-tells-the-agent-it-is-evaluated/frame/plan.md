# Implementation Plan: 1793171929-the-suite-tells-the-agent-it-is-evaluated

Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 and 2.

## Summary

Two phases. Phase 1 makes the suite's prompts and scaffolds say nothing that
names an evaluation: a new case in `tests/text/` refuses six words in every
`prompt.md` and `scaffold.sh`, seen red first, then the generators change
the author and the sealer's input directory, and the cases are written again
by their generators. Phase 2 renames the temporary directory
`noninferiority.py run` loads the plugin from, with its case. The truth
graders stay in the tree the eval loads, because the eval reads cases only
below that tree; `questions.md` Q1 asks the owner whether to change that.

## Technical context

- `evals/scripts/rule_cases.py` writes the 14 `rule-*` cases. The author is
  written out at `:205` (`base_project`), `:280` and `:288`
  (`proofer_case`), `:370` (`crafter_case`) and `:636` (`BY`, used by
  `sealer_case`). The sealer's input directory is `evidence =
  ".git/agentic-eval"` at `:660`. All 14 committed rule cases equal the
  generator's output today (executed: generated into a scratch directory and
  compared with `diff -rq`, every exit 0).
- `evals/scripts/seed_defects.py#scaffold` writes the amend at `:310` to
  `:313`. `seed_defects.py --case <name>` writes one committed case again.
  Run for all four `seeded-*` cases into a scratch directory, it differs from
  the committed case in one line each, the `git remote add origin` URL, which
  `replay_targets.py#origin_url` takes from this clone's `origin`
  (`https://github.com/MichaelYcJo/AgenticSeal.git`, executed).
- `evals/scripts/noninferiority.py#run_side` (`:603` to `:653`) makes
  `tempfile.mkdtemp(prefix="agentic-eval-")`, extracts the tree into
  `<it>/tree`, puts the suite at `--suite-rev` into that tree, and runs
  `claude plugin eval <tree> --eval-dir evals/behaviour/<agent>`.
  `side_path` puts `<tree>/bin` first on `PATH`.
- `claude plugin eval` 2.1.312 refuses an eval directory outside the plugin:
  `--eval-dir ../empty` exits 1 with `--eval-dir must stay inside the plugin
  root (no ..)`, and an absolute path exits 1 with `--eval-dir must be a
  relative path inside the plugin`. A symlink inside the plugin pointing out
  of it is accepted (executed, against an empty scratch plugin, no case run,
  the scratch removed after).
- `noninferiority.py#side_numbers` grades a `truth-` grader over a round
  record from the run's `report_text` and ignores the eval's result for it;
  a `truth-` grader over any other file, such as the sealer's
  `guarantee.md`, keeps the eval's result (`#reads_record`, read).
- `tests/behaviour/test_evals_layout.py#test_the_sealer_cases_are_the_generators_output`
  compares the sealer cases with the generator byte for byte. No case
  compares the crafter, framer or proofer rule cases, or the seeded cases,
  with their generators.
- `tests/evals/test_noninferiority.py#Test_run_side` already drives `run`
  with `call_eval` replaced by a fake (`run_one_side`, `:313`), which is
  the seam S6's case uses.
- `tests/conftest.py` puts every directory under `tests/` on `sys.path`, so
  `tests/evals/test_noninferiority.py` can import the word list from the new
  file in `tests/text/` (`CONTRIBUTING.md` *The test layout*, read).

**The failure scenario of the chosen approach.** In six months a new
generator template line, or a new record shape a scaffold copies, adds a
refused word, and the case goes red on a commit that only regenerated
cases. That is the case doing its job: the fix is a reworded template line,
or an exemption added to the case with its reason. The other failure is
quieter: the truth graders stay one directory listing away from the agent,
under the plugin root its skill preamble names. A run whose agent reads
them is not detected by anything this work adds.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep one tree that `claude plugin eval` loads and that is on `PATH`, rename its temporary directory, and leave the suite and its truth graders in it | An agent that lists the plugin root its skill preamble names finds `evals/behaviour/<agent>/<case>/graders/truth-*.md`. Nothing in the suite would show that it did | **Chosen.** It is the only layout `claude plugin eval` accepts with the graders read by the eval, which the issue asks to keep. The premise that keeps the tree whole is checked: the eval refuses `..` and absolute eval directories (executed). Every installed copy of the plugin ships the same `evals/` directory (read: the 0.23.1 cache), so its presence is not itself a cue. The residue is Q1 |
| Replace the structure: take `truth-*.md` out of the tree before the run, and grade every truth after it from what the side keeps | Proofer truths over a round record are already graded from `report_text`, so they lose nothing. The four sealer truths read `guarantee.md`, which no side keeps today. The sealer case would have to print the file and `report_text` would have to read it, which changes how the sealer is scored and edits `noninferiority.py`'s reader, where #992 works next | Rejected as the default, because the issue asks that the graders stay where `claude plugin eval` reads them and that scoring not change. Offered to the owner as Q1's other option |
| Two trees: `claude plugin eval` loads one with the suite, and a copy without it goes first on `PATH` | Claude Code puts the loaded plugin's `bin/` on `PATH` as well (`bin/seal`'s header, read), and the skill preamble names the loaded tree, so the graders stay as reachable as before. Two copies of one rev can also drift if a later edit touches only one | Rejected. It meets the letter of the done-when line and none of its purpose |
| A symlink at `<tree>/evals/behaviour` to a suite directory outside the tree | The eval accepts the link (executed), and a reader that follows `<tree>/evals/behaviour` reaches the graders through it exactly as before | Rejected. The tree would hold no grader file in name only |
| The word check as a `shape-` grader inside each case, scored by the eval | A grader cannot read the prompt it is graded against, and adding one moves rule 3's pooled pass counts for every later comparison | Rejected. The check reads committed text, so it belongs in `tests/`, where it costs nothing to run |
| One case file in `tests/behaviour/` holding both the word case and the directory case | The directory case runs `noninferiority.py`, whose cases stand in `tests/evals/test_noninferiority.py` under its `TARGET` (`CONTRIBUTING.md` *The test layout*). A second home for `run`'s cases splits them | Rejected. The text case stands in `tests/text/`, since it only reads text, and the directory case joins *Test_run_side*, importing the word list |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py` with its word list and exemptions (S4, S5), seen red against the suite as it stands; one author constant in `rule_cases.py` used at all five sites; the sealer's input directory `.git/<work-item-id>`; the seeded amend without `-c` flags; the 14 rule cases and 4 seeded cases written again by their generators; `tests/evals/test_rule_cases.py` reading the body path from the generator; the rule's paragraph in `evals/README.md` *The behaviour suite* | `bin/test tests/text/test_no_case_tells_the_agent_it_is_evaluated.py tests/evals/test_rule_cases.py tests/evals/test_seed_defects.py tests/behaviour/test_evals_layout.py -q`, and the seeded scaffold case once more with `HOME` set to an empty directory and `GIT_CONFIG_NOSYSTEM=1` (S2). Red shown twice: the new case against the suite before the generators change, and S5's planted template word | |
| 2 | `prefix="agentic-"` at `noninferiority.py#run_side`, and a case in `tests/evals/test_noninferiority.py` *Test_run_side* that refuses a temporary directory whose name holds a refused word (S6) | `bin/test tests/evals/test_noninferiority.py tests/text/test_no_case_tells_the_agent_it_is_evaluated.py -q`, the new case seen red with the old prefix | |

## Operational impact

- **No side compares across this change.** Every rule case's scaffold and
  the five sealer prompts change, so `suite_tree` moves for the crafter,
  framer, proofer and sealer suites. `noninferiority.py regrade` refuses a
  suite that differs in anything but `truth-` graders, so a side recorded
  before this lands is not regraded onto it. The next comparison of any of
  those agents takes both sides at the new suite. This work pays for none.
- **#1040** cites `evals/behaviour/sealer/rule-sealer-*` on its check lines.
  The case directory names do not change, so those lines still resolve.
- No new dependency, environment variable or migration.
