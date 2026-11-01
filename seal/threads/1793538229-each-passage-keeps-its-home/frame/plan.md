# Implementation Plan: 1793538229-each-passage-keeps-its-home (#1231)

## Technical context

The work touches three files and the frame's one rule change. Every coordinate is at the base, `ec7adf84`.

- `agents/crafter.md:44-46`, step 5 of *Order of work*: "Build the phase as a vertical slice. Where a unit adds behaviour: each case first, seen red against the tree as it stands, then the code, then the case green." The second sentence is K2.6. Its home is `skills/implement/SKILL.md:229-231`, the bold sentence opening *2. Implement test-first, and let each rule name its test*. `tests/behaviour/test_chain_hooks_hardening.py:1084` finds step 5 by the words "Build the phase as a vertical slice", so that sentence stays as it is.
- `skills/implement/SKILL.md:53-56`, the paragraph opening "**It is independent of `Commit and pull request language`.**", is K2.8. Its home is `docs/one-root-by-lifetime.md:220-230`, the paragraph "**Two rows, because one cannot express the middle answer.**" under *What the repository decides for itself, and how it is read*.
- `skills/implement/SKILL.md:162-169`, the bullet opening "A spawn prompt's facts arrive under", is K2.9 from "A fact with no coordinate" onwards. Its home is `skills/agent-contract/SKILL.md:71-80`, contract rule 5. The bullet's first sentence is the route `tests/text/test_the_handoff_before_round_one.py` *test_the_implementer_documents_point_at_the_section* holds, and it stays.
- `tests/text/test_no_passage_is_pasted_into_a_second_file.py`: `shared_counts` at line 128, `BASELINE` at lines 188-222 with 16 entries, the docstring's *Why a ratchet* at line 38, and the two cases that read the tree's largest pair at lines 266 and 280.

**The failure scenario of the chosen approach, six months on.** A sentence two agent definitions share drifts in one of them, and nothing counts it. The measure's row K2 accepts that: each such passage states a fact about the file that holds it, and each agent reads only its own definition, so the two copies are two facts and not one fact said twice. The opening paragraph every definition carries is still pinned word for word by `tests/text/test_every_agent_reads_the_contract.py`. The second scenario is a definition gaining a passage that really is a shared rule, such as one of the contract's. That passage then stands in the contract too, and the pair of a definition with the contract is still counted, as is `tests/text/test_a_moved_rule_leaves_its_definition.py`'s own check.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **A1** Leave pairs of two definitions out in `shared_counts`, keep `BASELINE` to the two `README.md` entries, rebuild the two tree-reading cases on planted texts, and link the three passages to their homes | The scenario in *Technical context*: a sentence two definitions share drifts unread | Chosen. It answers the issue's four *Done when* clauses and removes fourteen stored counts |
| **A2** Keep the ten definition-pair entries as stored counts | Every edit to a sentence two definitions share re-measures the pairs by hand, as the `BASELINE` comment records for #968, #970 and #1177. A count that falls is never lowered, so an entry goes stale unseen, as `README.md` with `skills/parity-setup/SKILL.md` did (P1) | Rejected on `skills/core/SKILL.md` *The rule a mechanism is kept against*, "Nothing is kept beside the tree to stay in step with it" |
| **A3** Store the definitions' shared passages as text in the module, so a new copy fails and a known one passes | A copy kept beside the tree, and a pin of a definition's wording | Rejected by round 1 of `1793490088-each-kind-of-restatement-is-measured`, finding 1 (design G9); not argued again |
| **A4** Replace the structure now: remove `BASELINE` and the ratchet, so any shared run fails, and leave `README.md` out of the corpus until #1102 | A paste into `README.md`, the file a first reader opens, goes unseen for two releases, and #1102 has to remember to put `README.md` back. Linking the two `README.md` passages instead edits the file #1102 rewrites, which the issue rules out | Rejected. The premise for keeping the ratchet one more release was checked: both `README.md` entries are at their stored counts (P1), and #1102, which removes them, is open in `release: 0.29.0` (G10) |
| **A5** Leave every file under `agents/` out of the corpus, as `*.ko.md` is | A paste between a definition and a skill, K2.6's kind, goes unseen, and the issue's *Done when* case cannot pass | Rejected |
| **A6** Leave definition pairs out in `over_baseline`, the judge, and keep counting them in `shared_counts` | `shared_counts` and the judgment disagree about what is counted, and #1216's reader, which extends the module, would meet counts the check never judges | Rejected. The filter stands where the count is made |
| **A7** Make the skill K2.8's home, and change the policy document to link it | Policy outranks the skill (`skills/implement/SKILL.md` *1. Read the documents that outrank the code first*). The reasons would leave a document every reader of the config rows is sent to for a procedure only builders open | Rejected (design G3) |
| **A8** Make `skills/implement/SKILL.md` K2.9's home, and have the contract link it | The rule is true of every agent, and the contract is the one file every agent receives (design G4). The proofer, sealer and tracer never open the implement skill | Rejected |
| **A9** Make `agents/crafter.md` K2.6's home | A session that builds without a crafter reads the skill and not the definition, and would lose the cadence | Rejected (design G5) |
| **A10** Delete step 5's restated clause with no citation, since step 1 already opens the skill | Step 5 is where the crafter builds a unit, and it would then name neither the cadence nor where it stands. The issue asks for a link by path and section | Rejected. The citation costs one clause |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope items 1 to 7 | `tests/text/test_no_passage_is_pasted_into_a_second_file.py` green. S3's case seen red with the pair filter widened to every pair holding an `agents/` path. S4's case seen red against the module at the base. S5's two cases each shown able to fail by `seal mutate` of `over_baseline`'s comparison. The phase-boundary set of contract rule 2, which holds every module design G12 names | 43eaa555 |

One phase, because the parts depend on each other: the three linked pairs leave `BASELINE` only once their links land, and a second phase would cost a spawn and a record for about four files. Within the phase, the cases of Scope item 6 come before the module's filter, as `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test* states.

## Operational impact

None for a deployer: no migration, environment variable, dependency or compatibility break. A user's agents and sessions read `agents/crafter.md` and `skills/implement/SKILL.md` with the same instructions, each citing its home for what it no longer restates. A contributor to this repository meets the paste check no longer counting a pair of two agent definitions, and a `BASELINE` of two entries.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
