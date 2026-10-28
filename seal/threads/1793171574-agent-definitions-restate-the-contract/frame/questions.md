# Questions for the planner: 1793171574-agent-definitions-restate-the-contract

## Judgments the ticket left open that the tree answered

Listed so nobody reopens them. Each one's grounds are in `frame/design.md` or
in `frame/plan.md`'s Alternatives table.

1. **The crafter's rule 9 bullet goes, although a test calls it the
   crafter's half.** `tests/text/test_edits_go_through_the_edit_tool.py:8-11`
   and `:111-123` hold `agents/crafter.md:70-71` as the crafter's own
   application of rule 9. Contract rule 9 names the same forms ("a `sed -i`,
   a redirection or a script"), so the bullet adds nothing that is the
   crafter's. #1040 lists it, and the ticket ranks above the code. The case
   and the docstring sentence go with the bullet (`frame/design.md`
   *Removes*).
2. **Which bold leads change.** The crafter's and the proofer's lead, *The
   broad gate is not yours, and its label is.*, stay. #1040 does not list
   them, their second half names the narrowing, and
   `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:881` finds
   the crafter's paragraph by its lead. The sealer's lead is part of a
   sentence #1040 lists, so it is replaced by one that names the narrowing.
3. **Four glosses stay, because the tree holds each one as a definition's
   own application.**
   - `agents/tracer.md:64-66`, "a probe you do run leaves nothing behind
     (rule 7)": `tests/behaviour/test_a_probe_that_commits_says_so.py:93-104`
     holds it as the tracer's pointer at rule 7.
   - `agents/proofer.md:160-164`, the probe paragraph:
     `tests/behaviour/test_a_probe_that_commits_says_so.py:51-64` and
     `tests/text/test_edits_go_through_the_edit_tool.py:95-108` hold it as
     the proofer's application of rules 7 and 9.
   - `agents/crafter.md:51-57`, step 10's `unverified` label and declined
     instruction: `tests/text/test_broad_gate_rule.py:124-157` holds it as
     where the crafter's two answers land.
   - `agents/sealer.md:104-105`, step 6's three labels:
     `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:1013-1028`
     holds them because the sealer does not preload `verify`.

   Whether the owner wants them gone too is P1 below.
4. **A removed assertion is not turned into an absence assertion.**
   `frame/plan.md` Alternatives row E.
5. **The paste check's `BASELINE` is not lowered.** Its comment says a change
   that drains a pair may lower its entry and nothing has to, and these
   sentences are not the pastes it counts.
6. **`## Rule changes` holds the no-change block.** `docs/the-record-layout.md`
   and `docs/the-agent-set.md` already state the rule this work applies.
7. **The parallel work items own no file this work edits.** This work edits
   `agents/crafter.md`, `proofer.md`, `sealer.md`, `framer.md`, `tracer.md`,
   `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`,
   `tests/behaviour/test_the_sealer_guarantees.py`,
   `tests/text/test_edits_go_through_the_edit_tool.py` and this work item's
   `changelog.md`. #1039 edits
   `tests/behaviour/test_the_hook_surface_git_offers.py`. #1058 edits
   `tests/conftest.py` and the modules that clear a `GITHUB_*` variable by
   hand, and none of the three test modules above names one (executed,
   `grep -n GITHUB_`). #913 edits the pact files, `hooks/lib/config.py`,
   `templates/setup/`, `skills/implement/orchestration.md` and the READMEs.
   #1041 edits `agents/crafter.md` after this work, at lines this work does
   not touch.
8. **One phase.** `frame/plan.md` Alternatives row F.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| P1 | **Whether the four glosses of head item 3 leave the definitions too.** Each one says, beside its rule number, a few words of what that rule says. The tests that hold them are code, which ranks below the ticket, and #1040 lists 13 sentences and none of these four. Whether this work's scope reaches past the ticket's own list is the owner's call, not a fact the tree holds | **a person**: the repository owner | **(a)** They stay. This work removes the 13 sentences #1040 lists, and the four glosses keep the cases that hold them. **(b)** They go too. Each gloss shrinks to its narrowing and its rule number, and four more cases are re-pointed: `test_the_fact_finder_reads_first_and_leaves_nothing`, `test_the_reviewer_still_says_a_probe_file_is_an_edit`, `test_the_crafter_puts_both_answers_in_the_hand_back` and `test_the_sealer_carries_the_four_conditions_in_its_own_words`. Under (b) the sealer loses the conditions its own definition carries in place of `verify` | (a); the frame is built on it | open |
| W1 | **The wording of the three shortened paragraphs and of the sealer's new lead.** `frame/design.md` *Scope* item 2 fixes what each keeps and that each cites `rule 2`. The sentences themselves are written where they are built | **the work**: phase 1 | Any wording that keeps the item 2 narrowing, cites `rule 2` in lower case, names no party from `RUNNERS` in the crafter's paragraph (`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:863`), and shares no 15-word run with a contract section (S5). The choice goes into `trail/phases/phase-1.md` | the shortest paragraph that meets those four conditions | open |
