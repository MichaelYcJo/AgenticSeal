# Implementation Plan: the pull request names each pin a rule change breaks (#1216)

## Technical context

The work builds on three readers and two test modules, each read at the branch's base `96f424ec`.

- `skills/settle/scripts/rule_changes.py#parse` reads a design's `## Rule changes` into `Op`, whose `lines` field (#1215) maps each field to its value's lines with their line numbers in the design. `#section_lines(text, section)` gives the span a section holds in a document, and `#pattern` is the whitespace-collapsed match the settle's dry run uses. The module loads `skills/verify/scripts/unverified_check.py` by path through `reader()`, and the new `passages.py` is loaded the same way.
- `skills/code-review/scripts/chain_check.py#rule_changes_read` parses each judged design and each design the pull request's own commits add or change, appends notices to the list `main` prints as `path:line  message`, and returns refusals. `#check_lines_in` is #1215's read of a `to`, and the new reading sits beside it. `#tracked_files` lists one directory's direct children at HEAD, so the new composition lists `tests/` and the corpus with one `git ls-files` each, and reads the files from disk, as `rules.py` resolves its targets.
- `tests/text/test_no_passage_is_pasted_into_a_second_file.py` holds the paste check: the corpus, the normalisation in `words`, `windows`, the counts per pair and the `BASELINE` ratchet. It imports `WINDOW` from `tests/text/test_a_moved_rule_leaves_its_definition.py`, whose docstring records why the value is 15.
- `ruff.toml` `[per-file-target-version]` lists every module `chain_check.py` loads at `py39`, and `tests/hooks/test_launch.py` holds that list against the loads.

The failure scenario of the chosen approach, six months on: the notices become noise nobody reads. On the record, 13 of 26 named pins did not fail (design G10), and at the base 4 of 4 would not fail (design G13). If the proofer learns to pass over them, the mechanism catches nothing and costs a second per run. The signal is a settle whose broad run fails on a pin the pull request had named. The answer then is to remove the reading, since `skills/core/SKILL.md` *The rule a mechanism is kept against* weighs it by what it caught. A second scenario: the paste check's normalisation changes in `passages.py` for the test's sake, and the notice changes with it. That is the point of one reader, and both callers' cases run on it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. At the pull request: `chain-check`'s rule-changes arm prints each pin and copy as a notice, from pure functions in `rule_changes.py` and the paste reader moved to `skills/settle/scripts/passages.py`; the proofer weighs each notice | Noise the proofer learns to skip (*Technical context*) | Chosen. The copy is answerable only before the merge, by rewording the `to`, and a pin of wording can leave in the same pull request by #1278's criterion (design E2). The proofer already runs the check on each round (design G15). |
| 2. In the settle's dry run only, the issue's other moment | A copy is found after the pull request that wrote it has merged, as at 0.27.1. #1278's handoff to "the next pull request whose design breaks one" has no receiver. The settling session already runs the broad run at step 8, which names every failing pin exactly, so the list saves one run and adds a sample beside it | Rejected. `skills/settle/scripts/settle.py` and `skills/settle/SKILL.md` are also #1217's next files. |
| 3. Both moments | Twice the cases and two outputs to keep in step, for a settle that runs the exact check anyway | Rejected. |
| 4. Replace the structure that causes the late meeting: let a pull request edit the policy root itself, so a pin breaks in the pull request's own suite | Two work items changing one section conflict in the tree, and the settle's merge-order grouping, which exists to write each section as its latest decision, has nothing left to read | Rejected. The premise that keeps the structure, checked: `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* states that a pull request does not edit the policy root, and the settle and the policy-in-force rule stand on it (read). Changing it is a decision far larger than this issue. |
| 5. Keep the structure and add nothing: the settle's broad run finds every pin, as at 0.27.1 | The four fact pins #1278 kept (design G12) and every later paste meet the suite only at the settle, and #1278's handoff (design E2) stays unmet | Rejected. The cost of the reading is about a second per judged run (design G14). |
| 6. Name a pin only where the test module's source names the document's file name | On the record it drops 6 of the 13 that did not fail and none of the 13 that did, and at the base it drops 3 of the 4 noise pins (executed: the framer's probe with `grep -F` of each document's base name in each module). It misses a module that reaches a document through a glob or a path built elsewhere | Rejected. It is a second guess of which file a test reads, and the notice refuses nothing, while each pull request sees only its own design's notices. |
| 7. A three-word floor for a literal | 44 named on the record against 26, with none of the 13 failing literals added (design G10) | Rejected. Four words, the floor #1278's lister used. |
| 8. `chain-check` loads the paste test module by path | It imports `pytest`, `conftest` and another test module, none of which a user's CI provides, and a test module is no interface of the plugin | Rejected. |
| 9. A second copy of the normalisation in shipped code, the test keeping its own | Two readers of one form drift, and the notice and the test disagree on what a copy is | Rejected. The issue asks for the test's reader. |
| 10. Apply the operations to a scratch copy of the policy root at the pull request and run the suite over it | Needs #1217's placement of each `to`, and runs a broad run per pull request, which contract rule 2 gives the orchestrator once | Rejected. |
| 11. A sentence in `agents/framer.md` that the framer runs the check over its own design, in place of the proofer's | The framer runs no check of the repository's (`agents/framer.md` *Job*), and a frame is read by the proofer at round 1 anyway | Rejected. The proofer reads the notices. |
| 12. No definition changes, the notices left to whoever reads the output | The proofer's step 7 tells it to correct what the check refuses in its own record, so a notice about the design has no named reader and catches nothing (design G15) | Rejected. One sentence in step 7. |
| 13. End the check at exit 2 for a test file that does not parse | A notice that refuses nothing would then block a pull request for a file unrelated to its design | Rejected. The file is named as not read, as #1167 names what a reader did not read (design E3). |
| 14. The check line names files, against a marker | `skills/settle/SKILL.md` *A rule has one shape*: a marker names the tests of a rule whose test drives a script that can fail a required pull-request job, which `chain_check.py` is | A marker, `a-rule-change-names-the-pins-and-copies-it-breaks`, as #1215 used one for its own arm. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Design *Scope* items 1 to 8 | Each new case in `tests/skills/test_passages.py`, `tests/skills/test_rule_changes.py` and `tests/skills/test_chain_check.py` seen red before it is planted, against the base or under the mutation the phase record names, and green after (contract rule 15). The two cases moved from the paste test pass in their new file. Design S7, run in a scratch directory over `git archive a92c358b^` and recorded in the phase record. Run narrowly, in one command at the phase boundary: those three modules, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`, `tests/hooks/test_launch.py`, `tests/github/test_rules.py`, `tests/skills/test_settle.py`, `tests/behaviour/test_settle_applies_rule_changes_in_place.py`, and each other module that `git grep -l` at the phase's base lists for `chain_check`, `rule_changes`, `agents/proofer.md`, `ruff.toml` or either moved test module's name. `bin/seal layout --check tests` and `uvx ruff check` over the changed `.py` files, both exit 0. `bin/seal rules --check` exit 0 once the marker's class exists | `abe82825a` |
| 2 | Design *Scope* item 9 | The fragment and its `### Process changes` row, read against `docs/the-record-layout.md` *A change writes fragments, never a shared file* and the other fragments under `seal/threads/`; `tests/behaviour/test_release_hygiene.py` and the modules that read the fragments, run narrowly at the phase's commit | |

Phase 1 is one slice. The reader, its move and the arm cannot be shown through `chain-check` apart, and the proofer's sentence names notices only the arm prints. Phase 2 is apart because the fragment states what phase 1 built. The orchestrator may hand both to one crafter spawn, as #1215's run did.

## Operational impact

- A pull request whose design changes a `from` that a test under `tests/` pins, or whose `to` repeats a passage of a rule document, gets notice annotations in CI and notice lines in every local `chain-check` run. No exit code changes, so nothing blocks more or allows more.
- Prompt budget: no question to a person.
- Each `chain-check` run that judges a design with operations reads every tracked `tests/**/*.py` through `ast` and the corpus once, about one second here (design G14). A run with no such design reads neither.
- In a user's repository the notice reads that repository's `tests/` and its files at the corpus paths, as the rule-changes arm already reads its designs. A repository whose tests are not Python under `tests/` gets no pin notice.
- No new dependency, environment variable, configuration row or migration. `.claude-plugin/plugin.json` stays at `0.28.0`.
- Platforms: the reading opens files by repository paths from `git ls-files` and reads them as UTF-8. The new cases run on every leg of `.github/workflows/test.yml`, Windows among them, with no skip.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-02 | One crafter spawn builds phases 1 and 2, departing from a fresh spawn per phase, as #1215's did | Phase 2 holds only the changelog fragment and its process row; a fresh spawn would re-read the frame and phase 1's record to write one file. This is the second work item of 0.28.0 to take this departure, which the settle reads against the rule | `skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer* |
