# Guarantee: 1794271936-the-korean-edition-lacks-two-passages

Audited on 2026-11-10 by the sealer, at `14912f374` against the base
`origin/release/v0.37.1`, which resolved to `8657297d5`. The gate record
`trail/gate.md` names `run: f58f89546 against 8657297d5`. `f58f89546` is an
ancestor of HEAD, and the one commit after it, `14912f374`, touches only
`trail/gate.md` (`executed`: `git log --no-merges --name-only
f58f89546..HEAD ^8657297d5`). `seal pr-body <item> --body <file> --check`
exited 0 with both the installed plugin's `seal` and the tree's `bin/seal`
(`executed`). The repository declares no `seal/parity.json` (`executed`:
`git ls-files seal/parity.json` printed nothing), so no comparison with an
original is owed. The route is straight to the pull request, so
`trail/rounds/` holds no record and no round is a party.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| S1 was seen red before the build: the backtick-span diff printed `` `pr.<lang>.md` `` and `` `seal pr-body` `` and exited 1 | `trail/phases/phase-1.md:16-20` | In a scratch clone at HEAD with `docs/layout/one-root-by-lifetime.ko.md` and `skills/settle/rule-changes.md` restored from `8657297d5`: `grep -o` of every backtick span in each edition, `sort -u`, `diff` | Holds. The diff printed exactly those two English-only spans and exited 1 |
| S1 is empty after the build, and the issue's *Done when* (a) holds: the two editions' backtick tokens differ nowhere | `trail/phases/phase-1.md:20`; `changelog.md` *Fixed*, its last sentence | The same comparison on the tree at HEAD | Holds. `diff` printed nothing and exited 0 over 70 spans |
| The cases S4 and S5 name pass at HEAD | `frame/plan.md` *Phases*, row 1 | `bin/test` over `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `test_a_phase_hands_the_next_one_a_record.py`, `test_both_editions_carry_the_same_folds.py`, `test_docs_line_wrap.py`, `test_first_setup_asks_once.py`, `test_settle_applies_rule_changes_in_place.py`, `test_the_pull_request_language_is_the_repositorys.py`, `test_the_rules_command_reads_each_rule_off_its_test.py` and `tests/lib/test_config.py`, `-q` | Holds. 350 passed, exit 0. The line-wrap case was shown able to fail: in the scratch clone, one line of the new paragraph widened to 119 columns made `test_prose_stays_within_the_wrap_limit[skills/settle/rule-changes.md]` fail with `skills/settle/rule-changes.md:76 is 119 columns (limit 88)` |
| Every added English line is at most 76 display columns, and every added Korean line at most 78 | `trail/phases/phase-1.md:42-45` | `git diff -U0 8657297d5...HEAD -- docs skills`, each added line measured by East Asian width | Holds. 76 and 78 |
| The one design the 0.35.0 to 0.36.0 settle removed that named the document carried operations on the English edition alone | `frame/design.md` *Grounding* G5; `changelog.md` *Fixed*; `pr.md`, its second quote | `git show --diff-filter=D --name-only e5370691d`; `git grep -n 'file: docs/layout/one-root-by-lifetime' 'e5370691d^' -- seal/threads`; `git show --stat e5370691d -- docs/layout/` | Holds. Of the eleven designs removed, only `1794188289` names the document, at its lines 187 and 202, both the English edition. The settle changed `one-root-by-lifetime.md` and not its Korean edition |
| No heading and no `check:` line changed in the Korean edition | `trail/phases/phase-1.md:49-51` | `git diff 8657297d5...HEAD -- docs/layout/one-root-by-lifetime.ko.md` | Holds (`read` of the diff). Both additions sit inside their paragraphs; passage A ends before the paragraph's unchanged `check:` line |
| Item C stands as the design wrote it | `trail/phases/phase-1.md:42` | `frame/design.md` *Data & interfaces* item C read against `skills/settle/rule-changes.md:74-86` | Holds (`read`). The text is the same, rewrapped |
| `## Removes` holds nothing, and the changelog names no removal | `frame/design.md` *Removes*; `changelog.md` | Read of both against the diff | Holds (`read`). The diff deletes no line except the two last lines of the Korean paragraphs it extends |

Passages A and B were read sentence for sentence against
`docs/layout/one-root-by-lifetime.md:231-237` and `:250-253` (`read`). Each
English statement of passage A has its Korean sentence, in order: the two
keys are required; first setup and the batch before a work item's first
edit ask for them, with the recent titles' language shown; `seal pr-body`
refuses without them; where nobody answers, the orchestrator writes the
titles' language and `routing.md` says so; no commit is refused for them.
Passage B says the body opens with `pr.<lang>.md`, the quotes of `pr.md` in
the team's language, and `pr.md` follows, so the records keep one language
and the team reads the body in theirs.

The broad gate's pass is the orchestrator's account in its spawn prompt;
the sealer read `trail/gate.md` at HEAD and did not run the gate
(`read`, contract rule 2).

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Translate passages A and B into the two Korean paragraphs, and end `skills/settle/rule-changes.md` *Rule changes* with item C; `## Rule changes` and `## Removes` hold nothing | The issue's decision (a) and its *Done when* (a); the diff; G5 as re-run | none |
| the build | `2ba8bb052` changes those two files only, as *Scope* items 1 to 3 ask, with the Korean wording improved where `phase-1.md` names each change; `phase-1.md` stands for phase 1, the one phase whose Status holds a commit | The design; the token comparison and the cases re-run above | none |
| the last round | No round ran: `routing.md` answers `straight to the PR` | The route the orchestrator chose under `agentic`. Its *Why this way* calls the diff two translated passages and one paragraph of the settle's grammar, and the diff is exactly that | none |
| the changelog | *Fixed*: the Korean edition says what the English edition says about the two keys, and the editions hold the same backtick spans. *Changed*: an operation on a document with a `.ko.md` edition carries one on that edition, and the settling session writes the other edition's section at step 4 | The diff; the token comparison; G5 as re-run; `skills/settle/SKILL.md` *The settling session's procedure* step 4, where each group's section is written | none |
| the orchestrator's part of the pull request body | Six quotes of `changelog.md`, the title judgment `docs:` from `frame/plan.md` *Judgments of the run*, and `Closes #1491.` | Each quote stands verbatim at the coordinate it names; the `docs:` row stands in `frame/plan.md`; the diff changes no executed line | none |

```seal
target: 14912f374967e858073ddb91252b97cd02e08d49 against 8657297d5918bf74edc0cfd784ac8764684145ad
Verdict: sealed
```
