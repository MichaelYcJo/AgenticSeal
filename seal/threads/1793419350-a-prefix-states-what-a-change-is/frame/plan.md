# Implementation Plan: 1793419350-a-prefix-states-what-a-change-is (#1199)

## Technical context

The work edits one skill, one script, one workflow step's name and one test module. `skills/commit-pr-convention/SKILL.md` *Commit messages* holds the prefix table every writer of a title reads: the crafter, the orchestrator, and through `docs/issues-and-milestones.md` *An issue is titled like a commit*, whoever files an issue. `.github/scripts/release_completeness_check.py#main` already reads the release branch's subjects since its fork from `main` (`#subjects_since`, `#merge_base`) and the version from the head branch's name (`label_merged_on_release_branch.py#version_of`), so the new reading needs no new read. The step that runs it is in `.github/workflows/hygiene.yml`, job `release`, which the `main` ruleset requires.

The failure scenario of the chosen approach, six months on: a release pull request is opened, as the last four were, minutes before its merge, and goes red because a `feat:` squashed into a patch-numbered branch weeks earlier and nobody pushed the milestones at filing. The repair is the whole push at the release's end: rename the milestones, cut the branch again under the minor's name, a pull request moving `plugin.json`, and a new release pull request. That is the cost the push rule owes anyway, paid late. What keeps it rare is the earlier moment: an issue filed `feat:` into a patch milestone is pushed when it is filed, and the table stops `chore:` from hiding the `feat:` in the first place.

A second scenario: the refusal makes a writer lower a `feat:` to keep a release's number, which is the failure this issue exists for. The refusal adds no reason the push rule did not already give, and the rewritten table says the prefix is never chosen to fit a number.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1 The release pull request refuses a patch-numbered release whose own subjects carry `feat:` | Late red where the release pull request opens at the end, as above. A reverted `feat:` refuses a release that carries nothing new | **Chosen.** The reading is exact (`skills/core/SKILL.md` *The rule a mechanism is kept against*: a script blocks only on a fact it reads exactly). Its record: 14 of 37 patch releases carried a `feat:` subject, under a 2026-09-02 rule nothing held (`frame/design.md` *Grounding*). The repair is the policy's own act, so a refusal costs nothing the rule does not owe |
| A2 The same reading, reported at exit 0 | The line sits in a green job's log. The owner's one read before the merge is the `release-report` summary (`docs/release-checklist.md` *5. The release pull request*), not this log, so the push rule is again held by nothing, which is how the 2026-09-02 rule went | Rejected. The core keeps a report for a noisy or guessed reading, and this one is neither |
| A3 Refuse at each feature pull request into a patch-numbered `release/vX.Y.Z`, reading the pull request's title | The `release` ruleset requires no check, so a red feature pull request can still merge, and the title is read, not what the release ships. The issue's *Done when* names the release's own commit subjects | Rejected for this work. It is the earlier moment, and the filing-time push in `## Rule changes` covers the same ground with no new reader |
| A4 Both A1 and A3 | Two readers of one fact, each with its own cases, for one rule | Rejected (`skills/core/SKILL.md` *The rule a mechanism is kept against*: a fact has one source) |
| A5 Replace the structure: take the number out of the milestone's name and assign it when the release pull request opens (#653's second direction) | `release_completeness_check.py` and `label_merged_on_release_branch.py` find a release's milestone and label by `release: X.Y.Z` and `merged: X.Y.Z` (read), so both move first. A milestone named by purpose cannot be pushed, so the version is decided at the release, the worst moment #653 itself names | Rejected. The premise that keeps the numbered milestone is the owner's decision of 2026-10-31, "milestones keep their version numbers and their order" (issue #1199, read) |
| A6 A second rule that bumps on what an installing repository experiences (#653's first direction) | A judgment made at the release, not readable off the subjects, which #653 requires of any rule | Rejected as a separate rule. Folded into the classification: a refusal on a rule the change states is `feat:` (`frame/design.md` *Data & interfaces*, *#653*) |
| A7 State the prefix-to-version map in `skills/commit-pr-convention/SKILL.md` | The skill ships to repositories whose versioning is their own, so a user's writer reads this repository's release policy as theirs | Rejected. The map is this repository's and goes to `docs/branch-and-release.md` |
| A8 Tell each writer in its own file: `agents/crafter.md` step 8, `skills/implement/orchestration.md`, the review orchestration | Three copies of the table's rule, and #1167's later phases edit all three files | Rejected. Every writer already reads the skill, which is the one home |
| A9 A new script and step for the version reading | One more step, file and boundary case for a reading that uses the existing step's two reads | Rejected for A1's form inside `release_completeness_check.py` |
| A10 Classify #1167 as `refactor:`, the owner's lean | Items 11 and 12 add a record section and a reading, which the issue's own `feat:` line names ("a record format, a step, a reading"), so a writer applying the table to #1167 gets `feat:` and a second writer told "refactor" disagrees | Rejected. `feat:`, by the first fitting row (`frame/design.md` *The first cases*). The milestone does not move either way |
| A11 Keep the table's words and add a "chore is narrow" note | The words "behaviour that did not exist now does" and "same behaviour, different structure" do not separate #1167 from #1198 (the issue, read), so two writers still disagree | Rejected. The rows are rewritten in place |
| A12 Pull a milestone back where a minor ends with no `feat:` | Every later milestone is renamed for a release that adds nothing, and the owner's decision keeps numbers | Rejected. A milestone is never pulled back |

## Phases

One phase, because the three items are small and a round over all of them reads one table, one function and its cases. The round reads `frame/design.md` *Scope* items 1 to 3 and *Data & interfaces*.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2, 3 and 5 | `tests/github/test_release_completeness_check.py` with one case per scenario S1 to S7, each seen red with the refusal removed or the count inverted; `tests/text/test_a_release_cannot_ship_an_untrue_milestone.py`; the modules that read `skills/commit-pr-convention/SKILL.md` (`tests/behaviour/test_a_signer_declares_its_pact.py`, `tests/behaviour/test_chain_hooks_hardening.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`, `tests/text/test_the_chain_section_has_one_shape.py`, `tests/text/test_the_settings_have_a_front_door.py`); `seal mutate` over the new judging function | |

*Scope* item 4, the policy root's changes, has no phase: the settle after this release applies `frame/design.md` `## Rule changes`.

## Operational impact

No migration, environment variable or dependency. `plugin.json` is not moved here; #1167's last phase moves it to the release's version.

**A release pull request can now go red on its version.** The `::error::` line names the subjects and the push, so the person who meets it reads the repair there.

**After this lands in `release/v0.26.0`, the orchestrator applies the result once**, in this order, because the owner froze the milestones until then and asked for one application:

1. Re-read the open issues of milestones 74, 75, 76 and 70 against the rewritten table, by each body, and collect every title to change. 27 were open on 2026-10-31 (executed, `gh issue list --milestone`).
2. Retitle each, with a comment saying why (`docs/issues-and-milestones.md` *An issue is its body and its comments together*). #1167 and #1199 take `feat:` (`frame/design.md` *The first cases*).
3. Push once, from every patch-numbered milestone that now holds a `feat:`. #1198 makes 75 one, so 75, 76 and 70 become `0.27.0`, `0.27.1` and `0.28.0` at least, with every description rewritten for the new numbers. A `feat:` found in 76 by step 1 pushes from 76 as well, in the same act. No branch is cut again: none of those releases has a branch on `origin` (executed).
4. The pull request body carries `Closes #653` beside `Closes #1199`. The release closes both, and #653's answer is `frame/design.md` *#653*.
