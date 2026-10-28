# Overview: 1793171929-the-suite-tells-the-agent-it-is-evaluated

## Why this work exists

The behaviour suite told the agent under test that it was being evaluated, through a commit author, an input directory and the plugin's temporary directory; now none of the three says so, and a case refuses the words.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| `evals/README.md` changes in phase 2 too | `plan.md`'s phase 2 row: "`prefix="agentic-"` at `noninferiority.py#run_side`, and a case in `tests/evals/test_noninferiority.py` *Test_run_side*", with no README change. Phase 2 added one sentence to the paragraph phase 1 wrote, naming *Test_run_side* | The code | `frame/design.md` *Scope* item 6: "One paragraph in `evals/README.md` *The behaviour suite* states the rule and names the case." The rule covers the directory name too, and the paragraph would otherwise state only part of it |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck at this branch's head | the orchestrator, through `seal gate` |
| `questions.md` Q2: whether `claude plugin eval` loads the plugin in place, so the skill preamble's base directory is the run's temporary directory | the orchestrator, by reading one saved trace's `Base directory for this skill:` line |
| Whether an agent behaves differently without the words: no side was run on the new suite | the repository owner, at the next paid comparison of any of the four agents |

## Not done

The issue's third done-when line asks that the tree the agent's `PATH` reaches hold no `truth-*.md` grader. That half is not done. The truth graders stay under `evals/behaviour/` in the tree `claude plugin eval` loads, because the command reads cases only from inside that tree. This is `questions.md` Q1's default (a), which the orchestrator chose under the automation answer; the owner has not answered Q1. Only the temporary directory's name changed (phase 2).

## Fed back into the spec

- A replay or seeded case file that its generator no longer writes is reported as such first, at line 0, with the instruction to write the case again with `--case NAME`. It keeps no exemption, so every refused word in it is reported after that, its copied values included (inferred during implementation, and the report's first line from review round 1's finding 1). `frame/design.md` *Data & interfaces* says the generator's own text is not exempt. It does not say what happens to a file that is not that text. `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py#test_a_word_in_the_generators_text_is_refused_and_one_it_copied_is_not` holds it.
