# Phase 1: 1793769283-each-form-a-script-does-not-decide-on-goes-to-plain-words

## What this phase found

**The frame holds for this phase.** I checked it against the tree before the first edit.

- `skills/core/SKILL.md` and `skills/agent-contract/SKILL.md` at `acda3da5e` are byte-identical to the base `c186a59ac` and to the installed 0.31.0 copies (executed: `git diff c186a59ac HEAD --stat`, which lists only the work item's records, and `diff` against the plugin cache, exit 0 for each file).
- Each coordinate R1 to R27 gives is the paragraph it names at those line numbers (read).
- R11's home holds: `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each* already states "A rule that would need a per-role exception is not universal. That is the test the shared file applies to itself" (read).
- R19's home holds: `docs/checks/the-routing-check.md` *The edit check* states which tools the gate refuses, that a shell write calls no edit tool, and that the pull request's trailer arm is what remains at a shared root (read).
- R12's home section exists, and it did not state rule 1's reason before this phase (read).

**No case under `tests/` pinned a removed sentence.** I ran `git grep -n -F` over the whole tree, outside `seal/threads/`, on each removed sentence's words: "sits above them", "separate agents because", "targets differ", "per-role exception", "is not universal", "failure is a habit", "as easy to copy", "Both forms are written out", "Two reasons point", "routing check sees only", "invisible to it", "trailer arm is left" (executed). Each hit was in the preload file being edited or in a home the frame names, with one exception. That exception is the module docstring of `tests/text/test_edits_go_through_the_edit_tool.py`, which said the contract states the routing check as rule 9's reason. The docstring now says that rule 9 states that reason in one clause citing *The edit check*, where the fact stands whole. This corrects a statement and removes nothing, so the frame's `## Removes` needs no row for it.

**How each row was built.** All 27 rows were built as the design's *The reason census* decides. The rows marked kept were left as they stand.

- R2: the clause ", which is why it sits above them" is cut. The sentence now ends "The value decides between two designs that break no rule below."
- R4: the clause "They are separate agents because their targets differ, and" is cut. The paragraph now reads "Each reaches its result without leaning on another's verdict, so one agent's mistake does not pass through the next unread."
- R11: the preamble keeps "This file's rules bind every agent, and nothing here is one agent's own." The test sentence leaves it.
- The citation the design's paragraph after the table asks for: one preamble sentence, "A person changing a rule finds the reasons no agent weighs in `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each*." It stands right after R11's kept sentence, so it covers R11 and R12 (plan row A3).
- R12: the sentence leaves rule 1. It now stands in the agent-set section as its own paragraph after the per-role test, led by "**Contract rule 1 writes out the wrong command form beside the right one, because the failure is a habit.**" Decision: the paragraph ends with `check: tests/text/test_the_agent_contract_holds_the_universal_rules.py`. That module's `FACTS[1]` pins both command forms inside rule 1's body, so it is the case that holds the rule the paragraph states. Grounds: `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test*, which says a rule ends with a `check:` line naming its case. `bin/seal rules --check` reads the new line, among all 226 lines in 70 rule files, and all hold (executed, exit 0).
- R17: "Two reasons point the same way." is cut.
- R18: kept, rewrapped only.
- R19: the paragraph leaves rule 9. Rule 9 keeps the one clause "The routing check sees only the edit tools (`docs/checks/the-routing-check.md` *The edit check*)." Decision: the clause states the reason and its citation together, so an agent with no edit tool still learns that a shell write escapes a gate, and the section it cites holds the mechanism. Grounds: R19's row ("Rule 9 keeps one clause that cites that section").

**The cuts left two lines past the wrap limit, and the boundary run found them.** `tests/behaviour/test_docs_line_wrap.py` named `skills/core/SKILL.md:52` (89 columns) and `skills/agent-contract/SKILL.md:21` (103 columns) at `4d06f7760`, where the limit is 88 (executed). Neither module is in the plan row's Verified by cell, so the six-module narrow run passed over them. `2cac08a35` reflows the two paragraphs. `git diff 4d06f7760 2cac08a35 --word-diff=porcelain -- skills` lists no changed word (executed).

**The S5 check at `2cac08a35`.** `git grep -n -F HEAD` outside `seal/threads/` gives these results (executed):

- "sits above them", "separate agents because", "Two reasons point" and "only the pull request's trailer arm is left" print nothing.
- "would need a per-role exception" and "failure is a habit" print only their line in `docs/running/the-agent-set.md`.
- "routing check sees only the edit tools" prints rule 9's kept clause and the corrected docstring.

**Other statements of the reworded rules, a sample.** Contract rule 19 asks for these, so I searched by words and by `check:` target. I ran `git grep -n -i -E` on "contract's (own) preamble", "right form", "wrong form", "two reasons", "second reason", "separate agents", "targets differ" and "sits above", and `git grep -n` on "rule 9", "contract rule 1" and "rule 1's" (executed). Each place I found still holds at HEAD:

- `docs/checks/the-routing-check.md:76` cites rule 9 as the reason every agent edits through the `Edit` tool.
- `docs/running/the-agent-set.md:28` cites the preamble for retired numbers, and the preamble still lists them.
- `agents/proofer.md:169` cites rule 9 for its probe edits.
- `tests/behaviour/test_a_commit_names_its_repository.py:59` reads `skills/implement/SKILL.md`'s commit rule, not rule 9.

The other citations of rules 1 and 9 under `tests/` name the rule and not the removed sentences. This list is a sample: a paraphrase of a removed reason in words these searches do not contain is not reached. Such a paraphrase would stand in prose under `docs/`, `skills/` or `agents/`, which the review reads.

**Seen red and mutation.** No unit adds behaviour in this phase. The edits are prose in two preload files and one `docs/` file, plus one docstring, which is the *Prose only* and *A comment or docstring inside source* rows of `skills/verify/SKILL.md` *The narrow command still has to be able to fail*. So no case was written new and no `seal mutate` run is owed. The docstring's module still imports and passes (executed: the narrow run below).

**Narrow run.** I ran the six modules of the plan row's Verified by cell in one `bin/test ... -q -p no:xdist` after the edits: 242 passed (executed, exit 0). `uvx ruff check` and `uvx ruff format --check` on `tests/text/test_edits_go_through_the_edit_tool.py` exited 0 (executed).

**Phase boundary run.** This is the *Phase boundary* row of `skills/verify/SKILL.md` *Scope: cheap and often, broad and once*, run as one `bin/test ... -q` over 43 modules. It took the plan row's six, and every module under `tests/` that names `agent-contract`, `core` or the agent-set document (executed: `git grep -l`). It also took the modules that read the tree's own `docs/`, `skills/` and `seal/threads/` markdown: the wrap, cited-section, heading, check-line (`tests/github/test_rules.py`), record-word, cited-commit, release-hygiene, line-liveness, reference-root, unverified-row, chain-check and census modules. The first run at `835b3ad83` had three failures. Two were the wrap lines above. The third was `tests/test_censuses.py`, on a real user path in this record's measurement command, which now writes `<repo>`. The second run, over the tree at `2cac08a35` with this record's edits, gave 2225 passed and 9 skipped (executed, exit 0). The selection is my reading of "a module that reads a path the phase changed". A module that reads those files through a helper none of these searches name is not in it, and the broad run covers that.

**The base measurement, design *Scope* item 2 at `c186a59ac`.** Each figure comes from `git -C <repo> show c186a59ac:<path> | LC_ALL=en_US.UTF-8 wc -lm`, with `<repo>` the clone's absolute path (executed). The measured files are each agent's definition, and the two files every agent's `skills:` list names (`core`, `agent-contract` for all five, read at the base). The session's preload is `skills/core/SKILL.md` alone.

| File | Lines | Characters |
|---|---|---|
| `skills/core/SKILL.md` | 140 | 9177 |
| `skills/agent-contract/SKILL.md` | 225 | 12469 |
| `agents/crafter.md` | 213 | 11985 |
| `agents/framer.md` | 233 | 13401 |
| `agents/proofer.md` | 170 | 9716 |
| `agents/sealer.md` | 176 | 9752 |
| `agents/tracer.md` | 68 | 2670 |
| `templates/records/process.md` | 5 | 246 |
| `templates/records/sdd-design.md` | 31 | 722 |
| `templates/records/sdd-gaps.md` | 15 | 342 |
| `templates/records/sdd-guarantee.md` | 23 | 920 |
| `templates/records/sdd-phase.md` | 5 | 262 |
| `templates/records/sdd-plan.md` | 29 | 914 |
| `templates/records/sdd-questions.md` | 5 | 188 |
| `templates/records/sdd-round.md` | 50 | 914 |
| `templates/records/sdd-routing.md` | 16 | 403 |

| Party's preload at `c186a59ac` | Lines | Characters |
|---|---|---|
| crafter (definition, core, contract) | 578 | 33631 |
| framer | 598 | 35047 |
| proofer | 535 | 31362 |
| sealer | 541 | 31398 |
| tracer | 433 | 24316 |
| session (core) | 140 | 9177 |

The table lists every file under `templates/records/` at the base (executed: `git ls-tree --name-only c186a59ac templates/records/`). For phase 4, as context and not as its figure: at `2cac08a35` the same command gives 139 lines and 9085 characters for the core, and 218 lines and 12072 characters for the contract (executed).

**What phase 2 needs.**

- The preload phase 2's crafter receives through `skills:` is the installed 0.31.0 copy, not this branch's (`CLAUDE.md`). Its rule 9 and preamble still read as at the base.
- This phase edited none of the files design G15 names for #1346.
- This phase touched no eval scaffold or grader (design C4).
