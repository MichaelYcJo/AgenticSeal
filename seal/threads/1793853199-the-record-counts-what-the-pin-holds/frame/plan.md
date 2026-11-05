# Implementation Plan: 1793853199-the-record-counts-what-the-pin-holds

## Technical context

The notice is `hooks/version-check.py#notice` (`:148-161`). Two cases read it in `tests/hooks/test_version_check.py`. `Test_main.test_accepts_a_warning_that_names_the_cheap_move_before_the_expensive_one` (`:68-133`) compares the whole message with a golden string. `test_the_notice_agrees_with_the_docstring_about_what_a_reload_re_reads` (`:273-304`) finds the first sentence naming `/reload` and looks for a scope qualifier in it. Two more cases read the notice: `test_accepts_a_newer_release_and_warns` (`:53-57`) and `test_accepts_a_warning_that_names_both_commands_in_order` (`:59-66`). The paragraph this work rewrites is `:100-111`, inside the first case's docstring. Nothing reads a docstring of this module, apart from `test_census`, which reads the whole file for old names and vacated paths.

The failure scenario of the chosen approach: in six months someone rewords the notice, brings the golden string along, and adds an overclaim. The pin passes, as the rewritten paragraph says it will. The defence is the person and the review that read the assertion message, and no checker. That is the state today, and this work only stops the docstring from understating or misstating it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. The issue's repair: "one property" becomes "two properties", the reload added, in the one place still in the tree | The count moves the next time any case's assertion on the notice changes, and nothing reads it. The paragraph would also keep "Every one left the module at `18 passed`", where the module now holds 21 test functions and `test_census` (design *Grounding*). The probe also shows the module, beyond the pair, refuses a dropped `restart`, so "the pair" against "the module" is one more distinction the count has to carry | rejected: correcting a count that drifts with nothing to catch it is what the milestone says to remove first (design D1) |
| A2. Remove the paragraph `:100-111` whole | `:94-98` is left saying "a legitimate rewording fails this case". A reader takes the pin to guard a rewording, which overstates it. #238 called the current error the safe direction; this would be the unsafe one | rejected |
| A3. Cut the paragraph to a statement with no count: a rewording that brings the text along passes (#238), the other cases' assertions on the notice and the assertion message are what remain | It goes stale only if the pin stops being exact, or if no other case reads the notice. Either change edits this module, and the paragraph stands in the case that changes | chosen (design D1) |
| A4. A form that survives a rewording: predicates over the notice's properties, the issue's second option | #134 tried four predicates and each was blind one word over (`:81-92`; #238's body). A fifth meets the next spelling, and a script that reads meaning from words is what `skills/core/SKILL.md` *The first value* says a script does not do | rejected, standing on #134 |
| A5. Replace the structure: drop the exact pin, keep the property cases | A change to the notice lands with no test touched, and a person reads the new text at every session start. Contract rule 14 asks that a fix changing what a person sees pins it. The premise that keeps the pin is that rule, read in `skills/agent-contract/SKILL.md` rule 14 | rejected: the pin stays |
| A6. Correct the two seal records the issue names | Both left the tree at `f51e634d`, and a record keeps what it said when written (#1355's frame, *Out of scope*). There is no file in the tree to edit | rejected |
| A7. Also cut `:81-92`, the four-predicate history, to one sentence and `#134` | It applies #1355's G disposition to a paragraph that states no fact of the present tree that can drift, and the owner's scope names the counting sentence alone | not taken in this item; open to a later one under the milestone's principle |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope 1, Scope 2 | S1 and S2, the diff read line by line; S3, `bin/test tests/hooks/test_version_check.py` narrow, its exit code; S4, the phase record against design D2 | |

## Operational impact

None. One test docstring changes. No hook, no assertion, no fixture and no shipped instruction changes.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
