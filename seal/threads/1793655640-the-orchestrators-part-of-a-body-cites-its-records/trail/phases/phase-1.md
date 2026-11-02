# Phase 1: 1793655640-the-orchestrators-part-of-a-body-cites-its-records

## What this phase found

**The frame held against the tree.** Each coordinate *Scope* items 1 to 5 name was opened at `b7d913795` and stood where the design says (read). The sentence "Your part restates no record" stood at `skills/code-review/orchestration.md:369-370`, the Korean copy at `skills/writing-style/outside-the-review.md:27-29`, the clause at `skills/commit-pr-convention/SKILL.md:240-242`, the last sentence of the row at `skills/implement/acts.md:75`, and the comment at `evals/scripts/rule_cases.py:826-828`. The S3 command printed those three lines of `orchestration.md`, `SKILL.md` and `outside-the-review.md` before the edit, and nothing, exit 1, after it (executed).

**Two wordings depart from the frame's, and neither changes what a sentence asks.**

- *Scope* item 1 says "a decision given to a person". The rewritten sentence says "a decision attributed to a person". "Given to" can read as a decision handed to a person to make. The case it names, "the owner asked", is a decision a sentence says a person made, which design G6 calls "an attribution to a person". Judged against `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*, which asks for one reading.
- *Scope* item 1's fourth point is two sentences. The rewritten text joins them with a colon: "A copied sentence carries its record's claim and no more: the sealer reads the record against the tree, so the sentence adds no claim of its own." The words are the frame's.

**The Korean pointer names both halves of the sentence it replaces.** The removed sentence said what the orchestrator writes above the line and how it states a record's fact. The pointer says that `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* decides both, because that section holds the list of what no record holds and the rewritten rule. It states neither, as *Scope* item 2 asks. Judged against `skills/core/SKILL.md` *The rule a mechanism is kept against* ("A fact has one source, and every other place links to it").

**The comment in `rule_cases.py` shortens the rule change's `to:` text.** It says the orchestrator's part holds what no record holds, "and a record's fact only as that record's own sentence or with the coordinate that holds it". The `to:` text names the row, heading, finding or line. The comment describes a fixture whose part holds only a `Closes` line, so the list of what a coordinate is adds nothing for its reader. Judged against contract rule 19 and *Scope* item 5.

**No case was written and no `seal mutate` ran.** The phase changes prose and one comment, and adds no behaviour. `skills/verify/SKILL.md` *The narrow command still has to be able to fail* gives prose the row "Whatever actually parses those files", and `frame/plan.md` phase 1's Verified by cell names no new case. The modules of the narrow run that open each changed file, found with `git grep -l` over `tests` (executed):

- `skills/code-review/orchestration.md`: 11 modules, `test_docs_line_wrap.py`, `test_every_orchestrator_act_names_its_delivery.py` and `test_the_rules_have_one_owner.py` among them.
- `skills/commit-pr-convention/SKILL.md`: `test_the_chain_section_has_one_shape.py`, `test_the_pull_request_language_is_the_repositorys.py`, `test_docs_line_wrap.py`, `test_chain_hooks_hardening.py` and `test_a_signer_declares_its_pact.py`.
- `skills/writing-style/outside-the-review.md`: `test_a_language_section_of_writing_style_opens_alone.py`.
- `skills/implement/acts.md`: `test_every_orchestrator_act_names_its_delivery.py`, `test_docs_line_wrap.py`, `test_broad_gate_rule.py` and `test_no_passage_is_pasted_into_a_second_file.py`.
- `evals/scripts/rule_cases.py`: `tests/evals/test_rule_cases.py`, `test_seed_defects.py`, `test_evals_layout.py`, `test_the_sealer_guarantees.py` and `test_a_rewritten_definition_proved_non_inferior.py`.

**The edit leaves #883's paragraph alone (S5).** `git diff -U0 85a238c6 -- skills/code-review/orchestration.md` prints one hunk, `@@ -369,2 +369,11 @@`, so no line from 371 on changed (executed). The merge with #883's branch was probed by the framer (design G11) and was not run again here.

**Other places stating the rule (contract rules 12 and 19).** After the commit, `git grep -n -i` ran outside `seal/threads/` for `restate`, `no record holds`, `names the record's path`, `record's path`, `기록에 없는` and `기록의 경로` (executed). Beyond the five edited places, these stand, each for the reason given:

- `docs/the-review-record.md:270` is the policy. `frame/design.md` `## Rule changes` changes it at the settle, and a pull request does not edit the policy root.
- `docs/the-record-layout.md:9` and `:338`, and `docs/the-review-record.md:23`, say that a record cites another record's fact and does not restate it. They are about the records, not the orchestrator's part, and agree with the new rule.
- `skills/code-review/scripts/pr_body.py:8-9` tells #1044's history in the docstring and states no rule for the part.
- `skills/writing-style/outside-the-review.md:64` asks that a phase record's verification be cited by path. Design G10 judged it in agreement, and it stays.

This is a search for wordings, so it is a sample in the sense of contract rule 12. Design G10 built its list from the readers of the body's dividing line, and this search adds nothing to that list. A document that describes the part in other words is not reached by either method.

**`frame/questions.md` Q1 is the work's to answer, and the phase-boundary run answers it for the narrow set.** No module of the run turned red, so no module of the set reads a rewritten sentence in a way the edit broke. The suite beyond the set is the broad gate's, as Q1's default says, and `gaps.md` carries it.

**The phase-boundary run (executed).** One `bin/test -q` call took 40 modules. They were the 22 modules `frame/plan.md` phase 1's `git grep -l` lists, `tests/text/test_a_moved_rule_leaves_its_definition.py`, and 17 more. Sixteen of those walk `skills/`, `evals/` or the tracked files, found with `git grep` for `glob(`, `rglob(`, `os.walk` and `ls-files` and judged from each matching line. The seventeenth, `tests/text/test_the_rules_claude_md_names_have_one_home.py`, came from the `restate` search above. It gave 1349 passed and 9 skipped, exit 0, with the build at `6b7c9a08e` and `gaps.md` written but not committed. The same command, run again with this record, `gaps.md` and the plan's Status cell written and not yet committed, gave the same counts, exit 0. `uvx ruff check` and `uvx ruff format --check` on `evals/scripts/rule_cases.py` exited 0. No file under `tests/` changed, so `bin/seal layout --check tests` was not run.
