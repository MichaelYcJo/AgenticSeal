# Implementation Plan: 1794372899-two-skills-tell-the-framer-to-ask

## Technical context

The tree as read at `b578ffb77`.

The only text that sends a party to either skill is `agents/framer.md` step 5 (`:96-103`), and every other line naming them is a list, a test or a record (`frame/design.md` G3). Neither skill is preloaded (G5), and no transcript holds a framer opening one (G4). The work is one commit's worth of text: a rewritten step, two removed directories, one row in each README edition, and the test units that read the removed files. A commit that removed the directories without the README rows would leave `#test_the_skills_row_lists_the_on_demand_skills_without_a_count` red (G9), and one that removed them without the test units would leave `read("skills", "feature-planner", "SKILL.md")` failing, so the five *Scope* items go in together.

Failure scenario of the chosen approach, in six months: a framer applies D1's three assumptions where the frame rests on none of them, and spends a search or a probe on a settled question. D1 limits the settling to an assumption "the frame rests on", and each is answered by reading or one probe, which the step already asks for behaviours. The other failure is a framer reading the third assumption as a demand for a reproducing probe where the code read already shows the cause; D1 names both routes.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. Fold the three readiness checks the step already named into step 5 (D1), and remove both skills with every text and case that names them | `agents/framer.md` grows by 187 B (G6) for checks most frames answer in a line | Chosen. It is the owner's decision as made (G2), and the three checks have no other home in the framer's texts (D2) |
| 2. Remove both skills and fold nothing; step 5 keeps its first sentence alone | A framer recalls a library's API from memory, or adds what the tree already holds, and nothing it preloads says otherwise: *A question a command answers is answered by running it* covers a behaviour, not a duplicate or an API recalled. It also departs from the decision's "the few checks a frame uses move into `agents/framer.md`" | Rejected |
| 3. Keep the skills as a structure and rewrite only their two sentences that ask (G1) | Two skills of 5,540 B stay to be kept in step with the framer for a reader that does not open them. The premise that keeps a structure, a reader that uses it, was checked and does not hold (G4). The owner chose fold and remove | Rejected |
| 4. Fold the checks as a new paragraph under *Rules* and leave step 5 its first sentence | Step 5 and the new rule both say how the framer settles what it assumes, and a later edit to one leaves the other; contract rule 19 asks for the rewrite in place | Rejected |
| 5. Fold feature-planner's steps as well: requirements, existing code, ordered tasks, scope lock, phasing past ten files | Each restates a home the framer already has (D2), so the definition carries two statements of the template's sections, and the ten-file line brings back a file count the ladder dropped | Rejected |
| 6. Add a case pinning D1's words, or the absence of the two names | A case on the absence of two names catches only a skill re-added under the same name, and the review reads D1 once against the diff (S1, S3); the case would be a mechanism with nothing in its record to catch | Rejected |
| 7. Keep the test units of *Scope* items 4 and 5 and point them at something else, such as "no skill stands down for a definition" | The property they read was where each skill was called from and whom its `NOT for` clause names; with no such skill the retargeted case asserts a property of an empty set | Rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 5, in one commit, then the records | S1 to S5 by their commands at the build commit; S6 and S7 by the crafter's narrow run of the four modules S7 names | `7ffcf1ab9` |

## Overlap with the release

The spawn names #1475 as the release's other open item; #1471, #1472, #1473, #1474 and #1503 are merged at the base (`frame/design.md` G13). #1475 has no branch and no frame, so it is read from its issue.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1475 | `agents/framer.md`: this work rewrites step 5 (`:96-103`), and #1475 deletes the definition's `check:` lines, at `:143`, `:169`, `:200`, `:206`, `:230`, `:235` and `:243` at the base, none of them in step 5. This work adds no `check:` line and removes no test file a `check:` line names: it removes test functions, and `tests/behaviour/test_chain_hooks_hardening.py`, which `agents/crafter.md:97` names, stays | #1480 | The milestone's order and the spawn put #1475 last, because it touches every definition. The two diffs touch different lines of `agents/framer.md`, so the later merge meets no conflict there, and #1475's count of the lines it deletes is the same before and after this work. Merging this first leaves #1475 to read the final definitions once |

## Operational impact

A person who typed `/agentic:feature-planner` or `/agentic:confidence-check`, or a session that loaded either by its description, finds no such skill after the update. The crafter's `changelog.md` names both under *Removed*, so the release notes carry it. No migration, environment variable or dependency changes. `.claude-plugin/plugin.json` reads `0.37.3` at the base (read), and this work moves no version.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-11 | The title takes `fix:`, as the issue's title does | The two skills told their one reader, the framer, to ask a person, which `agents/framer.md` and the core forbid, and the diff removes that instruction with the skills that carried it. `feat:` would fit a removal its users must work around; the only measurement, the owner's transcripts, found no call of either command, so no user is known to lose one, and the changelog's *Removed* names both for any who did | `skills/commit-pr-convention/SKILL.md` *Commit messages*; `frame/design.md` G11 |
