# Implementation Plan: 1793513786-an-unanswered-case-name-is-named-once

## Technical context

Each generator takes `--case` with `action="append"` (`evals/scripts/replay_targets.py:1015`, `evals/scripts/seed_defects.py:449`), so `a.case` holds a name as many times as it was given. `say_unanswered` (`replay_targets.py:976-984`, `seed_defects.py:386-406`) walks that list and prints one line per entry no case answers. That is the one reader of `a.case` that walks the names in order and prints per name. Every other reader builds a set, tests membership or tests truth (`frame/design.md` *Grounding*, the `a.case` row). The build adds `a.case = list(dict.fromkeys(a.case))` after `a = p.parse_args(argv)` in each `main`. `dict.fromkeys` keeps the first time each name was given and that order, so the lines of distinct names come out in the order they were given, as before.

The two cases run each generator's `main` in a fixture repository: `tagged_repo` and `two_layouts` for the replay case, `shipped_item` for the seeded one. The seeded case's `case(*names, run=("--list",))` helper already turns a list of names into `--case` pairs.

Failure scenario of the chosen approach, six months on: a new caller imports `say_unanswered` and passes a list with a name in it twice, and gets two lines, because the dedupe lives in `main` and not in the printer. Today no caller other than the two `main`s exists (executed: `git grep -n say_unanswered`), and the module docstring states the property of the command, which `main` is.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Read the names once at the parse, in each `main`: `a.case = list(dict.fromkeys(a.case))` (this changes the structure: the argument holds each name once, for every reader) | A future caller of `say_unanswered` outside `main` passes a repeated name and gets two lines. The module docstrings state a property of the command, so the command's entry point is where it is held. | Chosen. One statement per generator. It makes the docstrings' "A name given twice is one name." true for every reader of `a.case`, including a reader added later that walks the names, which the alternative below leaves open. Probed in a clone at `eb97d23e` (`frame/design.md` *Grounding*). |
| Keep the argument as argparse gives it and read the names once in `say_unanswered`: `unanswered = [name for name in dict.fromkeys(names) if name not in answered]` (#1150's round 4 fix, pasted in the issue's comment; it still applies verbatim at `eb97d23e`, `replay_targets.py:979`, `seed_defects.py:394`) | A later edit to `main` that walks `a.case` and prints or writes per name, such as a progress line per named case, repeats a name again. The fact "a name given twice is one name" would then be held at one printer and not at the argument the docstring describes. | Rejected. The premise that keeps the structure was checked: today `say_unanswered` is the only reader that walks the names in order (executed: `git grep -n 'a\.case'`). So this choice holds now as well as the chosen one, and fails sooner under the change described. |
| Make argparse drop repeats itself, with a custom `Action` that keeps a set or skips a name it holds | A set loses the order the names were given, which the stderr lines follow. A custom `Action` is a class added to each script to do what one statement does. | Rejected: more code for the same result, and the set form changes the order of the lines. |
| Leave #1150's fragment as it stands and let this work's fragment say the repeat is fixed | One release note says both "is still named twice (#1228)" and that it is named once. | Rejected. Both fragments ship in 0.27.1 (`frame/design.md` *Grounding*, the #1150 fragment row), and a change rewrites the text it amends in place (`skills/core/SKILL.md` *The rule a mechanism is kept against*). |
| Rewrite the module docstrings' `--case` sentence | None, beyond rewording a sentence that becomes true with the fix. | Not taken. #1150's round 4 closed its finding saying the docstrings keep the sentence and #1228 makes it true (`seal/threads/1793457435-replay-targets-reads-both-layouts/trail/rounds/round-4.md:57`). |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2, 3 and 4 | The two runs of Scope item 2 seen red with `eb97d23e`'s `evals/scripts/replay_targets.py` and `evals/scripts/seed_defects.py` put back, and green after. Then, in one command, `bin/test tests/evals/test_replay_targets.py tests/evals/test_seed_defects.py tests/evals/test_rule_cases.py tests/test_censuses.py tests/behaviour/test_a_rewritten_definition_proved_non_inferior.py tests/text/test_no_case_tells_the_agent_it_is_evaluated.py -q`, the modules that read the two changed scripts (executed: `git grep -ln 'replay_targets\|seed_defects' -- tests`). | |

## Operational impact

None. The scripts are maintainer tools that write proofer eval cases. No script in the tree runs either generator: `evals/scripts/noninferiority.py:85` and `evals/scripts/rule_cases.py:60` import `replay_targets` and call no `main` (executed: `git grep` over `evals/scripts`, `.github`, `bin`, `hooks` and `skills`). Both generators keep their flags and exit codes.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
