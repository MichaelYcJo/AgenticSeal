# Implementation Plan: the wording-pin module leaves (#1243)

## Technical context

The module is `tests/behaviour/test_one_word_one_meaning.py`, 999 lines at `18e3bd1a`. No file imports it, and one line outside it names one of its units (`frame/design.md` G5). The `check:` lines are read by `.github/scripts/rules.py`, whose `RULE_FILES` (`:68-76`) takes in `skills/*/SKILL.md`, so `skills/writing-style/SKILL.md:276` is the one line `seal rules --check` would refuse once the module goes. `tests/text/test_a_language_section_of_writing_style_opens_alone.py:157` asserts the section's three check lines equal `WRITING_RULE_CHECKS` (`:42-52`), so the pin moves with the line. `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#suite_modules` (`:220-223`) lists `tests/*.py` from the index, so the module's row in `APPLIES_THE_SHARED_GUARD` turns the case red once the deletion is staged and declines while it is not. `.test_durations` is one JSON object that the Windows and macOS shards are divided by (`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:9`), and its 24 rows sit at lines 816 to 839 with rows on both sides, so deleting them leaves every comma in place.

The failure scenario of the chosen approach, six months on: a skill or a README gains a sentence that calls the sealer's seal and the proofer's round record by one bare word, and nothing turns red. The proofer reading that diff is the one reader left. That is the trade `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest* makes on purpose: the module turned red where the wording moved and the meaning had not, and `docs/what-a-script-gates.md` *The checks* already gives prose to the proofer.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1 Delete the module whole, with every place that names it, in one change; the writing-style line names the proofer | the scenario under *Technical context*: an anonymous word lands and only a reader can find it | chosen. It is what #1167 decided and #1197 prepared (design G3); every fact a case held has another holder (G4) |
| A2 Keep the structure: trim the module to the cases whose facts no other holder reads, and keep the writing-style line on it | none of the 24 has such a fact: G4's table gives each a holder that reads the behaviour, or the proofer for a word's meaning, or none for the five cases that pin the module's own patterns. A trimmed module would keep sweeping wording, the kind of case that turns red where the meaning has not changed | rejected. The premise that would keep it, a fact only the module holds, was checked against the holders at `18e3bd1a` and is false |
| A3 Point the writing-style second rule's line at another test module instead of a reader | no module reads whether a word keeps one meaning without sweeping its spelling; the line would name a target that does not assert the rule, which `seal rules --check` cannot tell from one that does (`.github/scripts/rules.py`, its docstring, *How it errs*) | rejected; the third rule of the same section already ends `check: none reader: the proofer at review` |
| A4 Widen *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* to `README.md` and `README.ko.md`, so the line's reader reaches cases 2, 3 and 10 | the section's ground is that an agent cannot ask its writer back (`skills/writing-style/SKILL.md:252-255`), and the READMEs are human-facing (`CONTRIBUTING.md:435-437`); widening puts a person's install guide under rules for agent-read text, a reach nobody measured a catch for. Kept narrow, a README sentence misstating a grain is caught only by the proofer of the change that edits the README | rejected. The grains are behaviours with their own hook tests, and the README's prose is in every diff that changes it (design G8) |
| A5 Give *여럿이 가질 수 있는 것은 누구 것인지 밝힌다* a `check: none reader:` line of its own when its last paragraph is rewritten | a second line naming the same reader as the next section's second rule, which already sends readers of a shared word to this section; a mark added at the removal with nothing caught to its name (`skills/core/SKILL.md` *The rule a mechanism is kept against*) | rejected (design G7) |
| A6 Two phases: the writing-style line and its pin first, the deletion second | between the two the tree is consistent, but the split buys nothing: both phases run the same narrow set, and the issue's *Done when* asks for one change | rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope items 1 to 7 | S1, S2 and S5 executed; S3 and S4 seen red then green; S6 in one command over the modules `frame/design.md` *The narrow run* lists, with the module removed; the suite beyond that set labelled `unverified`, answered by the orchestrator's broad gate | b27b9835 |

## Operational impact

None for a deployer: no migration, environment variable, dependency or compatibility break. The suite loses 24 cases, and the shards lose their prices with them in the same commit, so no shard is sized by a case that does not run.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
