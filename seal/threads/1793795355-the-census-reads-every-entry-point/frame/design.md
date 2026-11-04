# Design: the census reads every entry point (#1255)

Issue #1255, in milestone `release: 0.32.0`. The framer read its body with
`gh issue view 1255 --json body,comments` on 2026-11-04 (executed). It has
no comments. The issue's measure was taken at `813665f0` and `bf9efcba`.
This frame reads every coordinate at `215ad6020`, the branch's HEAD, so the
line numbers below are HEAD's.

An entry point, in this frame, is a tracked `.py` file whose module body
holds an `if __name__ == "__main__":` block, the shape
`tests/censuses.py#is_main_guard` reads. Its answer is the
`(stream, errors)` pairs it puts into UTF-8 before it does its work.
`hooks/lib/console.py#STREAMS` holds the one answer every entry point owes:
`stdin` with `replace`, `stdout` with `replace`, and `stderr` with
`backslashreplace`.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `routing.md` (read) | Planning `framer`, Implementation `crafter`, Review through the review chain, Destination open the pull request, Automation `yes`, branch `feat/1255-the-census-reads-every-entry-point`. Nobody is asked anything during the run, so the question #1255 leaves to the owner is defaulted in `frame/questions.md` Q1, and the build follows the default |
| The orchestrator's spawn (the orchestrator's finding) | The milestone also holds #1254, which edits `evals/README.md`, `evals/scripts/noninferiority.py`, `tests/evals/test_noninferiority.py` and `.claude-plugin/plugin.json`, and #1256, which edits `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `docs/` *The dependency rule*. Each is built on its own branch at the same time. This work item is not the release's first, so it leaves `.claude-plugin/plugin.json` alone (`grep version` prints `0.31.2`, executed) |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "A script holds a gate only on a fact it reads exactly: an exit code, a parser's result". The census reads each answer through `ast`: which call a block makes, and which pairs a loop's literal names. It compares them with `STREAMS` for equality. It guesses at nothing, such as whether a file reads `stdin`. "Nothing is kept beside the tree to stay in step with it". So the census parses `STREAMS` out of `hooks/lib/console.py` and keeps no copy of it, and its corpus is every tracked `.py` rather than a list of directories |
| `skills/core/SKILL.md` *The rule a mechanism is kept against*, "A change rewrites the text it amends in place, and in the same commit removes what stood on the old fact" (read) | The `CONTRIBUTING.md` sentence, its pin, `hooks/lib/console.py`'s open-question sentence, the stale exemption in `hooks/dispatch.py` and the run-time case for three release scripts each change or go in this work item (`## Removes`) |
| `hooks/lib/console.py` docstring, lines 40 to 64 (read) | "The call sites are each entry point's `__main__`, not this module's import", and each entry point "carries the call rather than relying on `dispatch.py` having made it". Some entry points spell the loop inline, and the docstring gives the reasons for `chain_check.py`, the three release scripts and `dispatch.py`. "What must not diverge is the ANSWER". Line 54 says "Which entry points owe the answer is #1255's". So the census reads a loop as an answer, as it reads the call, and this work item writes the answer at line 54 |
| `.github/scripts/run_tests.py` docstring, lines 14 to 18 (read) | "The plugin ships from the repository root, so a user's cache holds `.github/scripts/` and `tests/` beside `bin/`". Shipped code is therefore every tracked file. The issue's "each `__main__` of shipped code" is every entry point the tree holds |
| The measure: `569780eff:seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-3.md` *The decisions* row C9, *Command C9* and *Instances C9*, and `48d035aa6:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md` *The table* row K12, *Command entry* and *Instances K12* (read, with `git show`) | At `813665f0`, 47 entry points: 26 gave `STREAMS`' answer, 3 gave `stderr` `replace`, 5 left out `stdin`, and 13 gave none. The 3 drifted answers each stood in 15 to 23 release tags. That is the catch record the widened census is kept against. K12 counted the 5 that leave out `stdin` as not drifted because none of them reads `stdin` |
| *Command C9* re-run at HEAD (executed: the command's script, saved under the scratch directory, with `python3 -I c9.py <worktree> HEAD`) | 48 entry points. 17 hold the text `console.to_utf8()`, 13 have a loop giving `STREAMS`' pairs, 5 have a loop without `stdin`, and 13 give none. `.github/scripts/release_report.py`, `release_seal.py` and `rules.py` give `STREAMS`' pairs at HEAD, so #1235 (closed, `release: 0.27.3`, executed: `gh issue view 1235`) repaired the issue's out-of-scope item before this branch was cut |
| An `ast` probe over every tracked `.py` at HEAD (executed: a script under the scratch directory that parses each file, finds its module-level `__main__` blocks, and reads the first block's statements) | 221 tracked `.py` files, and 48 have a module-level `__main__` block. No file under `tests/` or `evals/behaviour/` has one. In the first block: 12 open with `console.to_utf8()`, 11 open with a loop over `STREAMS`' pairs, 5 open with a loop over `stdout` and `stderr` alone (`skills/code-review/scripts/pr_body.py:90`, `skills/verify/scripts/arm_check.py:1300`, `core_check.py:274`, `pact_check.py:834`, `payload_meter.py:1134`), 2 have the loop after other statements (`skills/verify/scripts/broad_gate.py:3252`, after 2; `skills/verify/scripts/seal_stamp.py:1512`, after 1), and 18 hold no answer |
| The 18 with no answer in the first block (executed: the same probe, and `grep -n 'to_utf8'`) | Five call `console.to_utf8()` inside `main()` and not in the block: `.github/scripts/finding_counts.py:175`, `plugin_directory_check.py:289`, `publish_release_note.py:845`, `tag_release.py:183` and `tracker_labels.py:159`. `.github/scripts/issue_claims_check.py` makes the call once, as its block's first statement (`:324`), and is among the 12 that open with it. The other 13 make no call anywhere: `.github/scripts/close_issues_on_release.py`, `durations_union.py`, `label_merged_on_release_branch.py`, `release_completeness_check.py`, `roll_flow_measurement_issue.py`, `run_tests.py`; `evals/scripts/noninferiority.py`, `replay_targets.py`, `rule_cases.py`, `seed_defects.py`; `hooks/lib/launch.py`, exempted at `:105`; `skills/verify/scripts/mutation_check.py` and `test_layout.py` |
| Two files hold two module-level `__main__` blocks (executed: the probe) | `skills/code-review/scripts/chain_check.py` at `:131` and `:2047`, and `pr_body.py` at `:88` and `:784`. The first block gives the loop before the file loads its readers, and the second calls `main()`. A module body runs top to bottom, so the streams are set when the second block runs. The census reads the first block of a file and no later one |
| Where the 17 without an answer run (executed: `git grep` over `.github/workflows`, `bin`, `docs`, `evals/README.md` and `skills/implement/scripts/seal.py`) | `bin/test` and `bin/test.cmd` run `run_tests.py` on a contributor's machine, Windows among them (`bin/test:30`, `bin/test.cmd:7`). `seal.py:142` and `:175` run `mutation_check.py` and `test_layout.py` for `seal mutate` and `seal layout`. A person types `finding_counts.py`, `plugin_directory_check.py` and `tracker_labels.py --check` (`docs/releasing/release-checklist.md:77`, `:235`; `tracker_labels.py:152-158`), and runs the four under `evals/scripts/` (`evals/README.md:11`, `:22`). Seven run only from a workflow on `ubuntu-latest`: `close_issues_on_release.py`, `durations_union.py`, `label_merged_on_release_branch.py`, `release_completeness_check.py`, `roll_flow_measurement_issue.py`, `publish_release_note.py` and `tag_release.py`. So "this runs only on CI's UTF-8 runner" is false for ten of the seventeen, and for the other seven it is a claim no check reads (`frame/plan.md` *Alternatives considered* A2') |
| `hooks/dispatch.py:613` and `hooks/lib/launch.py:105` (read; executed: `git grep -n 'exempt from entry_point'`) | The two exemptions the census holds at HEAD. `dispatch.py`'s says "its own reconfigure loop, held by test_dispatch". Once the census reads a loop as an answer, it excuses nothing, and `tests/censuses.py#_held` refuses an exemption that excuses nothing. `launch.py`'s reason, "the launcher imports nothing before its floor check", stands |
| `tests/hooks/test_console.py:102-128` (read; executed: `git log -S`, first added by `81414aaeb`, #1273) | `test_a_release_script_run_on_its_own_gives_the_answer_streams_holds` holds the loops of `release_report.py`, `release_seal.py` and `rules.py` to `STREAMS` at run time. Its docstring gives its reason: those scripts spell the loop inline, and no check read `.github/scripts/`. The widened census reads every loop's pairs against `STREAMS`, so the case goes (`## Removes`, `frame/plan.md` A8) |
| `CONTRIBUTING.md` *House rules*, lines 419 to 428, and `tests/text/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py:23-24` (read) | The sentence "Every hook entry point also opens its `__main__` with `console.to_utf8()`" and the sentence the issue quotes state the rule this work changes. The pin asserts "The `encoding` and `entry_point` censuses in `tests/censuses.py`" and "opens its `__main__` with `console.to_utf8()`". Both sentences and the second assertion change in the same commit (contract rule 19) |
| `CONTRIBUTING.md` *What a change to a gate must carry* (read) | The pull request body carries a test seen red, the failure direction, a prompt budget, platform honesty, what it removes and what it reads. `frame/plan.md` *Operational impact* gives each one for the orchestrator |
| The policy root (executed: `git grep -n -i 'census'` and `git grep -n -i 'entry.point\|to_utf8'` over `docs/`) | No `docs/` document states the entry-point rule. `docs/running/the-agent-set.md:41` names `tests/censuses.py` as a check of another rule. The rule stands in `CONTRIBUTING.md`, outside the policy root, so `## Rule changes` holds the no-change block, and the pull request rewrites the sentence in place, as the issue says |
| Unsettled designs' `## Rule changes` (executed: `grep -l -i -E 'entry_point\|to_utf8\|console\.py\|censuses'` over every `frame/design.md` under `seal/threads/`) | One design names `tests/censuses.py`: `1793787547-each-statement-is-corrected-to-the-tree`, for `floor_syntax`. None touches the entry-point rule, and this work moves no `docs/` section, so it re-points nothing |
| `seal/follow-up.md` (read) | The row on `console.to_utf8()` left the file when #1038 kept this check. No row left is this work's |
| The latest release `v0.31.2`'s body and the fragments under `seal/threads/` (executed: `gh release view --json body` and `awk` over each `changelog.md`'s `### Process changes`) | No process row touches the censuses or the console module. This diff changes none of the files `docs/layout/the-record-layout.md` *A change to the way of working writes its process row in its own fragment* names, so the fragment carries no `### Process changes` table |
| The census's added cost (executed: one `ast.parse` of each of the 221 tracked `.py` files, timed) | 0.51 s on this machine. `tests/test_censuses.py` ran in 20.32 s at `bf9efcba` (row K12, read) |
| `seal/config.md` (read) | No `Record language` row, so the records are English. No `seal/parity.md` exists |

## Scope

In scope:

1. **The corpus.** `tests/censuses.py#entry_point` reads every tracked
   `.py`, and no longer only those under `hooks/`. In each file it reads the
   first module-level `__main__` block and no later one.
2. **What it accepts.** The block's first statement gives `STREAMS`'
   answer in one of two forms. The first form is the call
   `console.to_utf8()`, read by `tests/censuses.py#calls_to_utf8`. The second form is a `for` loop
   whose target is two names, whose iterable is a literal tuple of pairs
   equal to `STREAMS`, and whose body calls `.reconfigure(encoding="utf-8",
   errors=<the target's second name>)` on the stream `getattr(sys, <the
   target's first name>, ...)` returns. Every loop under `__main__` at HEAD
   has this shape (`## Grounding`, the `ast` probe row). The census parses
   `STREAMS` out of `hooks/lib/console.py` under `ROOT` with
   `ast.literal_eval`, and keeps no copy of it.
3. **What it refuses, and at which line.** An answer statement is a
   top-level statement of the first block that is the call of the first
   form, or a `for` statement whose body calls `.reconfigure`. The census
   reads the first answer statement of the block. Each refusal is one line
   in the census's form, `<rel>:<line>: entry_point: <what and the repair>`,
   and each can be exempted by `# exempt from entry_point: <why>` on its own
   line above the line it names.
   - The block holds no answer statement: at the block's `if` line. The
     repair names both forms.
   - The answer statement is not the block's first statement: at the line
     of the block's first statement. An exemption there excuses only the
     order. The answer statement's own line is still read, and a removal of
     the answer is still refused at the `if` line.
   - The answer statement is a `for` statement that is not of the loop
     form, or whose pairs are not `STREAMS`' pairs: at the `for` line. The
     repair says to name `STREAMS`' pairs or to call `console.to_utf8()`.
4. **Its cases**, in `tests/test_censuses.py` *Test_entry_point*, each seen
   red against the census at `215ad6020` and with only its own guard
   removed (contract rule 15):
   - a block without an answer outside `hooks/`, under `.github/scripts/`,
     `evals/scripts/` and `tests/`, is refused at its `if` line;
   - a loop over `STREAMS`' pairs as the first statement is accepted, under
     `hooks/` and outside it;
   - a loop over `stdout` and `stderr` alone, and a loop that gives
     `stderr` `replace`, are each refused at the `for` line;
   - a loop of another shape is refused at the `for` line: an iterable that
     is not a literal, such as `console.STREAMS`, and a `reconfigure` call
     with another encoding or a constant `errors`;
   - a loop after one statement is refused at that statement's line; an
     exemption above that statement excuses it, and a loop with drifted
     pairs is still refused at its `for` line under the same exemption;
   - a second module-level `__main__` block without an answer is not read
     where the first block gives one;
   - a loop whose target is not two names (one name, three names, a nested
     tuple) is refused at the `for` line;
   - the census's pairs are those `hooks/lib/console.py#STREAMS` holds,
     loaded from the file.
   The case `test_refuses_a_block_without_the_call_and_one_with_it_after_main`
   keeps its point. Its `hooks/after.py` arm is refused at the block's
   first statement, the second of the three lines item 3 names, in place
   of the `if` line, because the block now gives an answer after `main()`
   (phase record).
5. **Every entry point gives the answer or carries its reason** (Q1's
   default, `frame/questions.md`):
   - The 13 that make no call give one, except `hooks/lib/launch.py`, whose
     exemption stays. A file that puts `hooks/lib/` on `sys.path` at import,
     as `close_issues_on_release.py:76` and `rule_cases.py:52` do, imports
     `console` and calls `console.to_utf8()`; a file that reaches
     `hooks/lib/` only through a sibling script it loads, as
     `label_merged_on_release_branch.py` and
     `release_completeness_check.py` do, spells the loop (phase 2 record,
     `gaps.md` *Not done*). Any other file spells the loop
     in the form of item 2, as the files under `skills/*/scripts/` do.
   - The five that call `console.to_utf8()` inside `main()` move the call to
     the first statement of their `__main__` block, with the comment above it
     where one stands, and `main()` no longer makes it.
   - The five loops over `stdout` and `stderr` gain `("stdin", "replace")` as
     their first pair.
   - `broad_gate.py` and `seal_stamp.py` each carry an exemption above the
     first statement of their block. Its reason is the one the comment
     there already states: the file asks how stdout was found before the
     loop moves it to UTF-8.
   - `hooks/dispatch.py:613`'s exemption goes.
   The census over the tree then prints no line.
6. **`CONTRIBUTING.md` *House rules*** is rewritten in place in the bullet
   **Every file read or written names its encoding.** It says that every
   entry point, each tracked `.py` with a `__main__` block, opens its first
   such block with the answer `hooks/lib/console.py#STREAMS` gives, as the
   call or as a loop over its literal pairs in the one form
   `tests/censuses.py#loop_pairs` reads. It says that the `encoding` and
   `entry_point` censuses enforce both over every tracked `.py`.
   `tests/text/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`
   pins three facts of the bullet in the same commit, and its docstring stops saying
   "the hook entry points'".
7. **`hooks/lib/console.py`'s docstring**: its open question, "Which entry
   points owe the answer is #1255's.", becomes the answer, which opens the
   paragraph on the call sites, and that paragraph is rewritten whole
   (phase 2 record): every entry point owes it, and an entry
   point that cannot give it carries its reason at its line, read by
   `tests/censuses.py#entry_point`. `tests/censuses.py#entry_point`'s
   docstring says what the census now reads; phase 1 rewrote it with the
   code it describes.

Out of scope:

- The three drifted answers, which #1235 repaired before this branch was
  cut (`## Grounding`, the *Command C9* row).
- Whether the loops under `skills/*/scripts/` other than `chain_check.py`'s,
  which state no reason, should load `hooks/lib/console.py` instead. They give `STREAMS`' answer,
  and the census reads the answer, not the form (`frame/plan.md` A3).
- A `python3 -c` line in a skill or a workflow. `CONTRIBUTING.md` already
  says it is outside the censuses' reach.
- Whether a script reaches a console at all. The census reads code, and a
  script that never prints still gives the answer (Q1).
- The files #1254 and #1256 edit, except the one `__main__` block of
  `evals/scripts/noninferiority.py` (`frame/plan.md` *Operational impact*).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A new script outside `hooks/` gives no answer | Given `.github/scripts/x.py` whose `__main__` block calls `main()` alone, when the census reads it, then it prints one line at the `if` line that names both forms and the exemption | Scope 4's first case, red at `215ad6020`, where the census returns nothing for a file outside `hooks/` |
| A loop drifts from `STREAMS` | Given a loop that gives `stderr` `replace`, when the census reads it, then it refuses at the `for` line | Scope 4's third case, red with the pair comparison removed |
| An entry point must ask the console before the loop | Given `broad_gate.py` with its exemption removed, when the census reads it, then it refuses at the block's first statement; with the exemption in place, a drifted loop below it is still refused | Scope 4's fifth case, and the census over `broad_gate.py` with the exemption deleted (the crafter's probe, named in the phase record) |
| The tree at the phase's commit | Given the tree after Scope 5, when `tests/test_censuses.py` sweeps every tracked file, then no `entry_point` line is printed, and `git grep -n 'exempt from entry_point'` lists `hooks/lib/launch.py`, `broad_gate.py` and `seal_stamp.py` alone | The widened census run over the tree before Scope 5 prints 25 lines (17 without an answer, 5 drifted loops, 2 out of order, and `dispatch.py`'s exemption excusing nothing). After Scope 5 it prints none |
| A contributor reads the rule | Given `CONTRIBUTING.md` *House rules*, when a contributor reads the encoding bullet, then it says that the census reads every tracked `.py` and names the two forms of the answer | The text pin, red with the old sentence in place |
| Each entry point gives the answer | Given the tree at the pull request, when a probe parses each tracked `.py` and reads the first statements of its first `__main__` block, then each of the 48 entry points gives `STREAMS`' answer there, except `hooks/lib/launch.py`, and `broad_gate.py` and `seal_stamp.py` give it after the statements their exemption names | A probe written apart from the census, such as the proofer's, so that the census is not the only reader of its own result |

## Data & interfaces

- `tests/censuses.py#entry_point(rel, root=None)` keeps its signature and
  its place in `CENSUSES`. It drops `under=("hooks/",)` from its `_python`
  call.
- `tests/censuses.py#calls_to_utf8(statement)` reads the first form in
  one statement, in place of `opens_with_to_utf8`. One helper reads the loop form and returns its pairs, or `None`
  where the statement is not of that shape. Its name and the reader of
  `STREAMS` are the crafter's to choose.
- The census reads `hooks/lib/console.py` under `ROOT`, the repository it
  runs in, and not under a case's `root`, so a case plants no copy of the
  console module.
- Each message is pinned by a case (contract rule 14). The three messages
  are new text a contributor reads.

## Rule changes

- nothing
  why: The rule this work changes stands in `CONTRIBUTING.md` *House rules*, outside the policy root, and no `docs/` document states it (executed: `git grep` over `docs/`). The pull request rewrites the sentence in place, as #1255 says, because `skills/settle/scripts/rule_changes.py#parse` reads the policy root alone.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The census's restriction to `hooks/` | `tests/censuses.py#entry_point`, `under=("hooks/",)` | The census reads every tracked `.py` (Scope 1) |
| The exemption "its own reconfigure loop, held by test_dispatch" | `hooks/dispatch.py:613` | The census reads the loop as an answer, so the exemption excuses nothing and `tests/censuses.py#_held` would refuse it |
| The run-time case for three release scripts' loops | `tests/hooks/test_console.py#Test_module.test_a_release_script_run_on_its_own_gives_the_answer_streams_holds` | The census reads each loop's pairs against `STREAMS`, for these three and for every other loop. The case's own reason was that no check read `.github/scripts/` (`frame/plan.md` A8) |
| The arm that accepts a `__main__` block outside `hooks/` without an answer | `tests/test_censuses.py#Test_entry_point.test_accepts_the_call_first_a_module_and_a_file_outside_hooks`, the `tests/x.py` plant | Its behaviour is reversed. Scope 4's first case refuses that file, and the case's other two arms stay |
| `console.to_utf8()` called inside `main()` | `.github/scripts/finding_counts.py:175`, `plugin_directory_check.py:289`, `publish_release_note.py:845`, `tag_release.py:183`, `tracker_labels.py:159` | The first statement of each file's `__main__` block, where `hooks/lib/console.py`'s docstring puts the call and the census reads it |
| The open question "Which entry points owe the answer is #1255's." | `hooks/lib/console.py`'s docstring | The answer, written in its place (Scope 7) |
| The clauses "Every hook entry point" and "the second over `hooks/`", and the pin "opens its `__main__` with `console.to_utf8()`" | `CONTRIBUTING.md` *House rules*, lines 423 to 426; `tests/text/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py:24` | The rewritten sentence and its pin (Scope 6) |

This work widens a check and adds no new mechanism. It adds two exemption
lines, in `broad_gate.py` and `seal_stamp.py`, and removes one, in
`dispatch.py`. The widened reading is kept against the catch record of
*The decisions* row C9: three drifted answers each stood in 15 to 23
release tags, and the widened census refuses each of them. Round 1 of work
item `1790076050` also found `tracker_labels.py` without the call
(`813665f0:seal/follow-up.md:49`, read in *Instances C9*). Its cost is one
more parse of each tracked `.py`, 0.51 s (`## Grounding`, the cost row),
and the cases of Scope 4.

Framed 2026-11-04 by framer, before the build.
