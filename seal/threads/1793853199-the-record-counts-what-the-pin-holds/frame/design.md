# Design: 1793853199-the-record-counts-what-the-pin-holds

Line coordinates in this file are at `a5bad40fd`, before the build. `trail/phases/phase-1.md` maps each D2 row to its line after the build.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "Nothing is kept beside the tree to stay in step with it, such as a stored count or coordinate." A count of the properties a pair of cases holds, and a count of passing cases, are both stored counts. "History goes to git, the release notes and the work record." A list of mutations measured in a past run is history. Together they decide D1 |
| `skills/agent-contract/SKILL.md` rule 14 (read) | "A fix that changes what a person sees documents it and pins it." The update notice is text a person reads at session start, so a pin over it stays. This is the premise that keeps the exact pin (plan A5) |
| Milestone `release: 0.32.4` (read: `gh api repos/MichaelYcJo/AgenticSeal/milestones/88`, relayed by the spawn and opened) | Docstrings and comments under `tests/` state only what the tree holds now. Text that costs lines with nothing to catch its drift is removed before it is corrected. The item carried is "#238's sentence that counts what a pin holds" |
| #1355's frame, `seal/threads/1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds/frame/design.md` D1 (read) | A sentence of provenance goes. The grounds of a decision a person may change stay in one short sentence or an issue number (`#N`). D1 below applies the same split |
| MichaelYcJo/SpecSeal#134 (executed: `gh issue view 134 --repo MichaelYcJo/SpecSeal --json title,state`, "docs: the update notice names the expensive move and not the cheap one the repository measured", CLOSED; its reasoning read in #238's body and in the cheap-move case's docstring, `tests/hooks/test_version_check.py:81-92`) | #134 abandoned predicates over the notice's prose for an exact pin, after four predicates were each blind one word over. This frame keeps that decision (plan A4) |
| #238 (executed: `gh issue view 238 --repo MichaelYcJo/AgenticSeal --json body,comments,title`; no comments, as the spawn's line also says) | The issue names three places that say the pair of cases holds exactly one property across a rewording, the scope qualifier. Its measurement found a second one: the notice names a reload at all. Its repair is one word in each place plus `evidence-check --reverify` |
| Where the issue's three places stand today (executed: `git grep`, `git log --diff-filter=D`, `git ls-tree f51e634d^`, `git show f51e634d^:<round-3 path>`) | `tests/test_version_check.py:108` is now `tests/hooks/test_version_check.py:107-111` (moved by `e391ea04`). The ledger row S1·S2·S3 and `seal/specs/1788789330-the-update-notice-names-the-expensive-move/rounds/round-3.md` left the tree at `f51e634d` (#497/#504, 2026-09-23). Round 3's line 35 at `f51e634d^` is a finding on `tests/test_version_check.py:101`, verdict `deferred #238`. So one of the three places is in the tree |
| The ledger tool (executed: `ls bin`; `git grep -n -i "evidence-check\|evidence ledger" -- tests`) | `bin/` holds `seal`, `seal.cmd`, `test`, `test.cmd`, and no `evidence-check`. `tests/behaviour/test_release_hygiene.py:1317` holds "the evidence ledger does not come back", from #944. The issue's `--reverify` step has nothing to run |
| What the module's assertions refuse once a reworded notice brings its golden string along (executed: a read-only probe under the scratchpad, `python3 -I test_tmp_pin_probe.py <clone>`, against a `git clone --no-local` of this branch at `a5bad40f`; it imported `hooks/version-check.py#notice` and evaluated every assertion of `tests/hooks/test_version_check.py` that reads the notice, other than the exact equality, against eight variants of the text; clone and probe removed after the run) | As the text stands, nothing refuses it. `/reload-plugins` replaced by `a plugin reload`: refused by the agreement case's reload assertion (`:299`). The scope qualifier dropped from the reload's sentence: refused by its qualifier assertion (`:300-304`). The word `restart` dropped: refused by `test_accepts_a_warning_that_names_both_commands_in_order` (`:66`). An overclaim appended to the reload's sentence, the restart named before the reload, and the `measured` and `skill bodies` labels dropped: refused by nothing. A flipped gap was refused only where the variant also dropped `restart`. So the pair holds two properties across a rewording, as #238 measured, and the module holds more (both versions named at `:57`, the two commands in order at `:63-65`, `restart` at `:66`). The count depends on which case the sentence counts over, and it moves whenever any case's assertion on the notice changes |
| The module's size (executed: `grep -c` of test definitions in `tests/hooks/test_version_check.py`) | 21 test functions, plus `test_census`. The docstring's "Every one left the module at `18 passed`" is a count of a past run that this tree no longer reproduces, and nothing reads it |
| `seal/follow-up.md` (executed: `grep -n "238\|version"`) | No row names this work or the notice |
| Process changes (executed: `gh release view` for `v0.32.3`, no `### Process changes` heading; the ten fragments under `seal/threads/` that hold one, rows filtered for `pin`, `docstring`, `count`, `golden` and read) | No row changes how a pin or a test docstring is written. The 2026-11-03 row on `skills/core/SKILL.md` *The first value* (text no agent acts on stands in a docstring) is consistent with keeping the instruction in the docstring and the assertion message |
| Policy root `docs/` (executed: `git grep -n "reload-plugins" -- docs skills templates README.md`; `git grep` of the two case names outside `seal/threads/`) | No policy document states what the pin holds. The case names appear outside the module only in `.test_durations`, as durations. `README.md:75` is #1382's sentence and states nothing about the pin |
| `routing.md` (read, committed at `a5bad40fd`) | Planning framer, Implementation crafter, Review through the review chain, Destination open the pull request, Automation yes. Nobody is asked anything in this run |

**D1. The paragraph that counts is cut to a statement with no count, and the measurement it carried goes to #238.** The paragraph is `tests/hooks/test_version_check.py:100-111`, in the docstring of `Test_main.test_accepts_a_warning_that_names_the_cheap_move_before_the_expensive_one`, from "What this does NOT do is check a REWORDING." to "an instruction to a person rather than a check." It holds three things:

- a list of mutations measured in #238's run and the pass count `18 passed`, which is history and a stored count;
- "The one property the pair still holds across a rewording is the scope qualifier", the count #238 found wrong;
- the conclusion a reader acts on: a rewording that brings the golden string along passes the pin, so the person changing the notice is the check, and the assertion message is the instruction to that person.

Correcting the count, as the issue proposed, leaves a count that moves each time an assertion on the notice changes, and nothing reads it (plan A1). Removing the paragraph whole leaves `:94-98`, which says only that "a legitimate rewording fails this case". A reader would then take the pin to guard a rewording, the opposite error (plan A2). So the paragraph keeps its conclusion and loses the other two:

- It says that a rewording which brings this text along passes this case, with `#238` as the grounds.
- It says that what still refuses a reworded notice is the assertions of the other cases in the module that read the notice. It names no number of properties and no number of cases.
- It keeps the sentence that the rest is carried by the assertion message, an instruction to a person rather than a check.
- It names no measured mutation and no pass count.

The text is the phase's (`frame/questions.md` Q1).

**D2. Each other sentence of the class is read, and it stays.** The class is every sentence in the tree that states what the exact pin or its partner case holds. It was listed by taking apart the module's text: the module docstring, each paragraph of the two cases' docstrings, the comment above the agreement case, and the assertion message. A `git grep` of the two case names outside `seal/threads/` added only `.test_durations`. The two records #238 names left the tree at `f51e634d`. The list is closed, and each entry was read:

| Coordinate | What it states | Disposition |
|---|---|---|
| `tests/hooks/test_version_check.py:1-8` | the hook's three limits | stays: it states no property of the pin |
| `:71-79` | what run 6 of `docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.md` measured | stays: the grounds of the notice's wording. The cited file stands |
| `:81-92` | why the message is pinned exactly: four predicates, each blind one word over | stays: the grounds of #134's decision, which this frame keeps. It states no fact of the present tree that can drift (plan A7) |
| `:94-98` | a rewording that does not bring the golden string along fails this case | stays: true, and D1's paragraph follows it |
| `:100-111` | the count | D1 |
| `:129-133` | the assertion message, the instruction to the person who changes the notice | stays |
| `:274-279` | why the notice and the hook's docstring must agree | stays |
| `:280-285` | this case checks the presence half, the scope qualifier; the absence half is pinned in the case above | stays. The reload assertion at `:299` is the precondition of finding the claim the qualifier is read in, and its message says so ("names no reload for the docstring to disagree with"). "Pinned" is true of the text as it stands, and D1's paragraph, which this sentence sends the reader to, says a rewording passes the pin |
| `:287-289` | why the docstring is read whitespace-normalised | stays |

## Scope

In scope:

1. **The counting paragraph.** `tests/hooks/test_version_check.py:100-111` is rewritten as D1 says. No other line of the module changes.
2. **The record of the class.** The phase record lists D2's rows and the rewritten paragraph's text, so a reviewer can read the class against the diff.

Out of scope:

- The two seal records #238 names: the ledger row S1·S2·S3 and round 3 of `1788789330-the-update-notice-names-the-expensive-move`. Neither is in the tree since `f51e634d`, and records keep what they said when written (#1355's frame, *Out of scope*). `evidence-check --reverify` goes with them, since the tool is gone (*Grounding*).
- The issue's larger question, whether a pin over prose can carry the notice's properties at all. This frame weighs it only as far as the sentence needs it: the exact pin stays (plan A4, A5), and the docstring says what it does not check.
- The `# Left for #923, under its name: …` comments at `tests/hooks/test_version_check.py:272` and `tests/hooks/test_question_gate.py:431`. Both were added by `cbf97bf5` on 2026-10-24, and #923 closed on 2026-10-16 (executed: `gh issue view 923`, `git show -s cbf97bf5`), so what they say may no longer hold. They state a hand-off between issues, not what the pin holds. `tests/hooks/test_question_gate.py` is outside this item. The orchestrator may file it under the milestone's principle.
- The hook's own module docstring, `hooks/version-check.py:15-21`, which tells what an old note said. The milestone covers `tests/` and `.github/scripts/`.
- The `:81-92` paragraph's length. Cutting it to one sentence and `#134` would apply #1355's G disposition, and the owner's scope names the counting sentence alone (plan A7).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. The paragraph counts nothing | Given the phase's commit, when the cheap-move case's docstring is read, then it names no number of properties, no number of cases or passes, and no measured mutation. It says a rewording that brings the text along passes this case, cites `#238`, and says the other cases' assertions on the notice and the assertion message are what remain | the docstring read in the diff |
| S2. Only the paragraph changes | Given the phase's commit, when the diff against the base is read, then every changed line of `tests/hooks/test_version_check.py` lies inside that docstring, and no other file of the tree changes outside the work item's directory | `git diff -U0 <base> -- tests/ hooks/`, each `+` and `-` line read |
| S3. The module still holds | Given the phase's commit, when the module runs narrow, then it passes, its `test_census` included | `bin/test tests/hooks/test_version_check.py`, its exit code read (contract rule 1) |
| S4. The class is accounted for | Given the phase record, when it is read, then it lists D2's rows and the paragraph's new text | the phase record against D2 |

## Data & interfaces

No interface changes. No assertion, fixture or hook changes.

## Rule changes

- nothing
  why: The rule this work applies, that a stored count and history do not stand beside the tree, is in `skills/core/SKILL.md` *The rule a mechanism is kept against*, which every party receives. No policy document states what the pin holds, so none changes.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the list of mutations measured in #238's run, with the `18 passed` count | `tests/hooks/test_version_check.py#Test_main.test_accepts_a_warning_that_names_the_cheap_move_before_the_expensive_one`, the docstring's paragraph opening "What this does NOT do" | #238's body holds the measurement, and the rewritten paragraph cites it |
| the sentence counting the one property the pair holds across a rewording | the same paragraph | nothing: the rewritten paragraph names where what remains is held, with no count |

This work adds no mechanism, so no row names a return.

Framed 2026-11-05 by framer, before the build.
