# Implementation Plan: nothing in the tree says that less text means nothing said twice (#1192)

## Technical context

The sentence goes into `skills/core/SKILL.md` *The rule a mechanism is kept against* (line 99), after the sentence that ends on line 106, "A fact has one source, and every other place links to it." The paragraph is wrapped near 75 columns, and the builder wraps the new sentence to the same band; whether `tests/behaviour/test_docs_line_wrap.py` covers the core is the builder's to read. The core reaches a session through `hooks/core-start.py`, which prints `hooks/lib/core.py#output` under the 10,000-character `CAP`; P1 in `frame/design.md` *Grounding* measured 6,653 characters with the sentence. An agent receives the installed plugin's copy through `skills:`, so the sentence reaches agents once 0.25.2 is installed, and a session in this repository from the merge on.

The enumeration that answers the first *Done when*'s second half is in `frame/design.md` *Data & interfaces*: fifteen lines, none a criterion on a change's size. The build changes no other shipped text.

The failure scenario of the chosen approach, six months on: a later work item adds a limit that bounds a change rather than a reader, such as "a fix pass adds no more than N lines", and a proofer reads the sentence as forbidding it. The sentence says what it rules out, a change's added lines against its removed lines held as a criterion, so that limit has to argue against the core in its own design, which is the place the argument belongs.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. One sentence after "A fact has one source", scoped to a change's added lines against its removed lines | A later limit on a change's size has to argue against the core (*Technical context*) | Chosen |
| B. A, and a test that pins the sentence by a phrase only it writes | The pin is a mechanism with no catch record: no sentence of the core is pinned for its wording today, and the one pin on the core, `tests/text/test_the_rules_claude_md_names_have_one_home.py#LINKED`, holds a link and not a wording. Contract rule 14 asks a pin of text a person sees and acts on, such as a message or a verdict. A rewording would cost an edit to the test and nothing else | Rejected |
| C. A test that refuses line-count phrasings anywhere in shipped text | It blocks on words. `skills/core/SKILL.md` *The rule a mechanism is kept against* allows a reading guessed from words to report and never to block, and the pattern of *Data & interfaces* matches fifteen lines today, none of them a criterion | Rejected |
| D. A check that reports those phrasings at every run | A new mechanism with nothing caught yet. The issue asks for the phrasings listed in the work item, and the listing in `frame/design.md` *Data & interfaces* answers it once, where the crafter and the proofer can rerun the command | Rejected |
| E. Replace the structure: rewrite "A fact has one source, and every other place links to it." in place so that one sentence carries both claims | One sentence would state where a fact lives and what that means for a change's size, two points that `skills/writing-style/SKILL.md` *English prose rules* ("Short sentences over connector chains", "One paragraph, one point") splits. The premise that keeps the anchor sentence as it is, checked: it is cited by three frames at fixed commits and by no shipped file (`git grep -n -F 'A fact has one source'`, executed), so rewriting it would break nothing; it stays because it states a different claim, and the new sentence follows it | Rejected |
| F. The issue's example sentence word for word, "a line count is reported as context, never held as a criterion" | A proofer reading it literally raises findings against `hooks/lib/core.py#CAP` and its test, the `Stop` hook cap in `docs/the-review-record.md` line 493 and the 806,241-token bound in `skills/code-review/orchestration.md` line 30, each a size held as a criterion by design. That is the misreading #1148's run paid for, one class over | Rejected |
| G. The sentence in `skills/writing-style/SKILL.md`, `agents/framer.md` or `agents/proofer.md` as well as, or instead of, the core | A second home for one fact. The core reaches every party and every repository, and the issue names it | Rejected |
| H. Amend #1148's records (S10, round 1's finding 6, Q2, `gaps.md` *Not done*) to the new reading | The records are not amended after the guarantee; the owner's comment of 2026-10-31 is their answer, and they leave at the settle after 0.25.1 | Rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2 and 3, in one commit | S1: `git grep -n -F 'Less text means nothing said twice' -- skills/core/SKILL.md` gives one line, after the anchor. S3: the enumeration command of `frame/design.md` *Data & interfaces* at HEAD lists the fifteen recorded lines and the new sentence. S4 and S5: a narrow run of `tests/hooks/test_core.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/text/test_the_rules_claude_md_names_have_one_home.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/hooks/test_version_check.py`, `tests/github/test_publish_release_note.py` and the other modules contract rule 2 names for the three paths, with the broad suite `unverified` and the orchestrator its answerer. S2 is the proofer's reading | |

## Operational impact

`.claude-plugin/plugin.json` moves to `0.25.2`, the first move into `release/v0.25.2`; `skills/implement/orchestration.md` lines 318-325 put that move in the commit that adds the fragment. No migration, no environment variable, no dependency. After the merge the orchestrator deletes its local memory `compact-not-net-negative` (the issue's second *Done when*).
