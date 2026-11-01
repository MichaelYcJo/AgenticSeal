# Implementation Plan: each wording pin is kept or removed (#1233)

## Technical context

The work edits test modules and the check lines that name them; it changes no script, hook or skill sentence. The list of what is ruled is *The listing* of `frame/design.md`, 506 asserts in 259 cases of 56 modules at `361ed0cb` (design G2). The criterion is #1111's reading of `docs/what-a-script-gates.md` *The checks* (design G1), and its model of a kept pin is `tests/text/test_the_agent_contract_holds_the_universal_rules.py#FACTS`, which names beside each kept spelling what the fact is and who reads it.

Three constraints shape the order. `.github/scripts/rules.py` (docstring `:37-46`) refuses a check line naming a missing file and excuses no pending `change`, so a module a `docs/` line names stays until the settle (design G4). `tests/github/test_rules.py` runs that check in the suite, so each phase that edits a check line runs it. `.test_durations` divides the Windows and macOS shards (`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`), so a removed case's row leaves in the commit that removes the case.

The 56 modules split into four groups of 113 to 147 listed asserts (design *The groups*). The split follows the size a fresh crafter reads in one phase and keeps each module inside one group. Groups A and B are `tests/text/` and the script modules, and C and D are `tests/behaviour/`. No group depends on another. They run in order because each phase edits `.test_durations` and may edit the same `agents/*.md` or `skills/*/SKILL.md` check lines.

The failure scenario of the chosen approach, six months on: a rule under `docs/` or `skills/` is deleted by a change whose review misses it, and no case turns red, because the case that pinned its lead sentence is gone. The rule's `check:` line still names a module, and that module reads the rule's facts, not its sentences. The proofer reading that diff is the reader left, which is the trade `docs/what-a-script-gates.md` *The checks* makes on purpose. The other half of the scenario is the one #1216 records: a wording pin that stays, outside this listing, turns red at a settle where the meaning did not move.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1 Read each case that holds a listed assert whole; keep each assert that pins a fact of *The criterion* with the fact and its reader in a comment above it, and remove the rest; state the two `docs/` line changes; leave the one module a `docs/` line names to a successor issue | the scenario under *Technical context* | chosen |
| A2 Rule the listed asserts alone, and leave every other assert of their cases as it stands | a case keeps the unlisted pins of the same paragraph: `tests/text/test_the_rules_have_one_owner.py#test_the_cap_counts_from_the_last_design_change` asserts four phrases through a loop variable, which the lister cannot see, beside the two it lists. Reworded, the rule still turns the case red, and the case pins half a paragraph | rejected |
| A3 Widen the scope to every case of the 56 modules that reads prose | 1411 cases hold no listed assert (design G2), most of them reading a script's behaviour; telling the prose readers among them apart is a search over unbounded spellings (contract rule 12), and the issue scopes the work to *Command K5*'s list | rejected; #1216 meets the rest at the next pull request that breaks one |
| A4 Keep the structure of each text module and turn each wording pin into an assert that its rule's heading still stands | a heading pin turns red only when a section goes, which `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and the citation readers already hold where a heading is cited. A pin added at the removal would be a mechanism with nothing caught to its name (`skills/core/SKILL.md` *The rule a mechanism is kept against*). The premise that keeps the modules, a fact only their pins hold, was checked for the 23 lines of design G5 and holds only where a fact assert is kept | rejected |
| A5 Name each kept fact in a module-level table, as #1111's `FACTS` does | 56 modules, most holding one to four kept asserts with different readers, each restructured into a table and a loop. The table fits a module whose pins share one shape and one reader. A comment above the assert keeps the fact beside what pins it without moving code; its risk is a comment that drifts from its assert, which the proofer reads together | rejected; the comment above the assert is A1's form |
| A6 Delete `tests/text/test_a_gate_that_fails_says_so.py` now, by widening `rules.py`'s excuse to a pending `change` | every pending `change` becomes leave to break a check line before its settle, for one 32-line module. #1197 weighed the same widening and rejected it (`v0.27.1:seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/plan.md` A3) | rejected |
| A7 Leave the deletion to the settle, or fold it into #1216 | the settle writes the policy root and removes released work item directories, and deletes no test module (`skills/settle/SKILL.md`); #1216 is a feature of 0.28.0 with its own scope, and a deletion folded into it has no frame stating it | rejected; a successor issue, as #1197 filed #1243 |
| A8 Leave `docs/the-review-record.md:428` naming `tests/text/test_the_rules_have_one_owner.py` | the module stays, but no case of it reads the cap once its one case goes; `seal rules --check` cannot tell a target that reads its rule from one that does not (`.github/scripts/rules.py`, *How it errs*) | rejected; the line names the reader of the rows the cap's decisions become (design G7) |
| A9 One phase for all 259 cases | one crafter reads 506 asserts and their cases in one context, and one review round reads a diff over 56 modules | rejected; four phases of 52 to 75 cases, each reviewed with the narrow run its own diff calls for |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope items 1 and 6, and items 8, 9, 10 and 11 for group A | S1 over group A, S2, S4 and S7 executed; S8 at review; the suite beyond *The narrow run* labelled `unverified`, answered by the orchestrator's broad gate | 899db781 |
| 2 | Scope items 2, 5 and 13, and items 8, 9, 10 and 11 for group B | S1 over group B, S2, S3, S4, S6 and S7 executed; S8 at review; the suite beyond *The narrow run* `unverified`, answered by the orchestrator's broad gate | 244e726f |
| 3 | Scope item 3, and items 8, 9, 10 and 11 for group C | S1 over group C, S2, S4 and S7 executed; S8 at review; the suite beyond *The narrow run* `unverified`, answered by the orchestrator's broad gate | |
| 4 | Scope items 4 and 12, and items 8, 9, 10 and 11 for group D | S1 over all four groups, S2, S4 and S7 executed; S8 at review; the suite beyond *The narrow run* `unverified`, answered by the orchestrator's broad gate | |

## Operational impact

None for a deployer: no migration, environment variable, dependency or compatibility break. The suite loses the cases the ruling removes and the shards lose their prices in the same commits. The orchestrator files one successor issue before `seal pr-body` runs (design Scope item 7). Where #1232 merges into `release/v0.27.3` before this work's last phase, the branch takes it by a merge; no listed assert reads a sentence #1232 changes (design G9).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
