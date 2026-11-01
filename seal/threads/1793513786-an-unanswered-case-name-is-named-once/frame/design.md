# Design: 1793513786-an-unanswered-case-name-is-named-once

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| Issue #1228, body and its one comment (read: `gh issue view 1228 --comments`, and `--json title,body`) | The request. Each generator names an unanswered `--case` name once, however often the name is given. Each test module gains a run that gives one name twice and counts one line. The comment carries #1150's round 4 fix, which reads the names once in `say_unanswered`, and the two runs to add to the cases. |
| `seal/threads/1793457435-replay-targets-reads-both-layouts/trail/rounds/round-4.md` finding 1 (read, lines 17-57) | Where the defect came from. #1150's fix wrote "A name given twice is one name." into both module docstrings and made it hold only for the exit code. The finding was closed `deferred #1228`, and its answer says the two module docstrings keep the sentence and #1228 makes it true. No caller reads the count `say_unanswered` returns beyond its truth, so the count changes no exit. |
| The defect at `eb97d23e`, the base of this branch (executed: a probe in a `git clone --no-local` of the worktree at `eb97d23e`, with `origin` set to the GitHub URL, running each generator with one unanswered name given twice) | `replay_targets.py --list --case replay-1-r1 --case replay-1-r1` and the same run with `--out out` each exited 1 and printed `replay_targets: replay-1-r1 not written: no record of its work item was read` twice. `seed_defects.py --list --case seeded-12345678 --case seeded-12345678` and the same run with `--out out` each exited 1 and printed `seed_defects: seeded-12345678 not written: no shipped commit read has 12345678 as its first eight digits` twice, then the line saying no shipped commit read holds a round 1 record. #1224 (#1239) did not change this: `say_unanswered` still reads `unanswered = [name for name in names if name not in answered]` (read: `evals/scripts/replay_targets.py:979`, `evals/scripts/seed_defects.py:394`). |
| The fix this design chooses, run in the same clone (executed: the line `a.case = list(dict.fromkeys(a.case))` added after `a = p.parse_args(argv)` in each `main`, by a script that asserted each replacement matched once) | The four runs above exited 1 as before and printed each name's line once. The seeded runs still printed the no-round-1 line after it. |
| Every reader of `a.case` in the two `main`s (executed: `git grep -n 'a\.case'` over `evals`, `tests`, `.github` and `bin`) | `say_unanswered` is the only reader that walks the names in order and prints per name. The others build a set (`replay_targets.py:1021`, `seed_defects.py:456` through `named` at `:455`), test membership (`replay_targets.py:1051`, `seed_defects.py:472`), or test truth (`replay_targets.py:1020`, `:1068`, `seed_defects.py:454`, `:499`). `evals/scripts/noninferiority.py:648-649` passes its own `--case` to `claude plugin eval` and runs neither generator. No test calls `say_unanswered` directly. |
| `docs/` (the policy root; `seal/config.md` has no `Policy root` row) and the unsettled designs' `## Rule changes` (executed: `git grep` for "given twice", "named twice" and "named once"; read: the five unsettled designs' `## Rule changes`) | No policy sentence says how a generator answers a repeated `--case` name. `docs/the-review-record.md` *What the check reads at the pull request* and #1150's change to it concern which check reads a record, which this work leaves alone. So this work states no rule change. |
| `docs/the-record-layout.md` *A change writes fragments, never a shared file* and *A commit after the build brings its changelog fragment along*; `docs/branch-and-release.md` *Work accumulates on a release branch* ("Feature pull requests write their entry to `seal/threads/<work-item-id>/changelog.md`") (read) | The work owes its own fragment, `seal/threads/1793513786-an-unanswered-case-name-is-named-once/changelog.md`, written by the crafter. The release note is built from every fragment the release's commits added, each as it stands at the tag. |
| #1150's fragment, `seal/threads/1793457435-replay-targets-reads-both-layouts/changelog.md` line 7 (read), and its release (executed: `git tag --contains 5fd6b88c` prints no tag) | #1150 merged into `release/v0.27.1` and no release holds it yet, so its fragment goes into the same release note as this work's. It ends its third entry with "an unanswered name given twice is still named twice (#1228)". After this work that clause is false in the note that ships it. `skills/core/SKILL.md` *The rule a mechanism is kept against* and contract rule 19 say a change rewrites the text it amends in place. So the clause goes, and this work's fragment states the fact once. No release ever printed the name twice: v0.27.0 named no unanswered name at all, since #1150 is what added the naming. |
| `tests/evals/test_replay_targets.py:907-936` and `tests/evals/test_seed_defects.py:409-484` (read) | The two cases the runs join. Their docstrings say "A name given twice is one name" about the exit of a run that wrote its case (`test_replay_targets.py:914-916`, `test_seed_defects.py:425-427`). The comment's line numbers were taken at #1150's head. At `eb97d23e` the replay case's first assertion is at `:920-924`, and the seeded case's `assert case(nothing) == 1` and its `readouterr` are at `:479-480`. |
| `seal/follow-up.md` (executed: `grep` for `replay`, `seed_defects` and `--case`) | No row names either generator, so no follow-up item joins this scope. |
| The latest GitHub Release's `### Process changes` and the fragments under `seal/threads/` (executed: `gh release view`; `grep -l 'Process changes'`) | No row concerns the generators. This work changes no file that owes a process row, so its fragment holds none. |

## Scope

In:

1. In `evals/scripts/replay_targets.py#main` and `evals/scripts/seed_defects.py#main`, the `--case` names are read once each, in the order first given, right after the arguments are parsed. Every later reader of the names in `main` then sees each name once. `say_unanswered` keeps its code and its docstring in both modules.
2. `tests/evals/test_replay_targets.py#test_names_each_named_case_it_did_not_write_with_its_reason` gains a run that gives `replay-1-r1` twice and asserts one stderr line. `tests/evals/test_seed_defects.py#test_names_each_named_case_no_shipped_commit_answers_with_its_reason` gains a run that gives `nothing` twice under `--list` and asserts `unshipped + empty`. Each run is placed where the issue's comment places it, and each is seen red against `eb97d23e`'s two scripts (contract rule 15).
3. Each of those two cases' docstrings extends its "A name given twice is one name" sentence: the same holds for a name no case answers, which was named once per time it was given (#1228), and the run was seen red against that.
4. This work's fragment, `seal/threads/1793513786-an-unanswered-case-name-is-named-once/changelog.md`, holds one `### Fixed` entry: since #1150, an unanswered `--case` name given twice was named on stderr once per time it was given, and it is now named once, as each module docstring says. In #1150's fragment the clause "; an unanswered name given twice is still named twice (#1228)" is removed, and the sentence it ends stays as it is.

Out:

- The module docstrings' sentence "A name given twice is one name." (`evals/scripts/replay_targets.py:52-53`, `evals/scripts/seed_defects.py:51`) stays word for word. The fix makes it true for stderr as well as for the exit code, and #1150's round 4 closed its finding on that reading.
- `replay_targets.py#main` calls `origin_url()` before it names an unanswered name, so on a clone whose `origin` is not a GitHub URL a `--case` run that writes nothing stops with the `origin` message and names no name (executed: the first probe run, before `origin` was set). `origin_url`'s docstring says a URL of another shape stops the run, the issue does not ask about it, and no generator run in CI reads a non-GitHub origin. It is left as it is, and the orchestrator decides whether it is worth an issue.
- `seal/threads/1793457435-replay-targets-reads-both-layouts/guarantee.md:32` and `:34`, and #1237's records that quote the drifted sentence, are records of what stood at their commits, and stay.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 An unanswered replay name given twice | Given a tree where no record of work item `1` is read, when `replay_targets.py --case replay-1-r1 --case replay-1-r1` runs, then it exits 1 and stderr holds exactly one line, `replay_targets: replay-1-r1 not written: no record of its work item was read`. | Scope item 2's replay run, red at `eb97d23e`'s `replay_targets.py` and green after item 1. |
| S2 An unanswered seeded name given twice under `--list` | Given the case's shipped commits, when `seed_defects.py --list --case seeded-12345678 --case seeded-12345678` runs, then it exits 1 and stderr holds the `not written` line once, followed by the no-round-1 line. | Scope item 2's seeded run, red at `eb97d23e`'s `seed_defects.py` and green after item 1. |
| S3 What already passed still passes | Given the runs the two cases already hold, a written name given twice among them, when they run after the fix, then every assertion they make holds unchanged. | `bin/test tests/evals/test_replay_targets.py tests/evals/test_seed_defects.py -q`, run by the crafter as the phase's narrow run. |
| S4 The release note says what ships | Given the fragments of `release/v0.27.1`, when the note is built, then no sentence in it says an unanswered name given twice is still named twice, and this work's entry says it is named once. | The proofer and the sealer read both fragments against the diff. |

## Data & interfaces

No interface changes. The flags, the exit codes and the line `say_unanswered` prints keep their shapes. Only how many times a repeated name's line is printed changes, from once per time the name is given to once. The count `say_unanswered` returns is now the number of distinct unanswered names. Both `main`s read that count only for its truth (`replay_targets.py:1042`, `:1067-1069`; `seed_defects.py:490`, `:499-500`).

## Rule changes

- nothing
  why: No policy sentence says how a generator answers a `--case` name given twice. The sentence lives in each module's docstring, and this work makes the code meet it.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The clause "; an unanswered name given twice is still named twice (#1228)" | `seal/threads/1793457435-replay-targets-reads-both-layouts/changelog.md`, the third `### Fixed` entry | The fact it stated stops being true with this work, in the release that ships both. This work's own fragment states what ships instead (Scope item 4). |

This work adds no mechanism. It adds one statement to each `main` and two runs to existing cases.

Framed 2026-11-01 by framer, before the build.
