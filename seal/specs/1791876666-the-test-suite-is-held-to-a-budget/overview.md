# 1791876666-the-test-suite-is-held-to-a-budget — overview

<!-- The closing memo (implement skill, step 4). Only what the diff cannot
show; each part written when it happened. Opened at phase 1. -->

📋 implement applied
· spec:     spec.md (Scope, The removal criterion, S1–S4, S6, Removes); plan.md (Technical context, phase 1, Test rows); questions.md Q4, Q6; templates/sdd-phase.md
· tests:    the cases phases/phase-1.md and phases/phase-2.md name, each with the mutation it was seen red by
· verified: phases/phase-1.md, which labels each figure executed or read

## Why this work exists

The suite only grew. This work cuts the commit-gate test file and the sealer
file's junit twins by removals a mutation table proves redundant, lowers the
budget rows those cuts moved, and puts the Python floor in one launcher. The
per-case check it built in phases 2 and 3 left again in phase 4, by the
owner's decision of 2026-10-15; what a case owes, and the rest of the
cleanup, are #942's and #923's.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| 191 parametrized ids of `test_s2_a_commit_bash_makes_into_an_undeclared_repository_does_not_land` removed, phase 1 | `spec.md` §Removes: "nothing — the frame names no unit … every removed function is a divergence row". The function stays; 191 of its 226 parameter rows leave | the removal | phase 1's mutation table: m1–m5 each still red after, and the counts of killers that are not S2 rows unchanged |
| S3 "the sample's rows all land in `main` or `u` without hooks" | read as true on every leg. On Windows `env -i` finds no git, and the `env -i` rows are the only S2 killers of m4 and m5 | two `env -i` rows kept, skipping on Windows by a named limit (`NO_GIT_UNDER_ENV_I`), as `stdbuf` already did; every other row fails rather than skips | the S9 case's own comment (#692's Windows pass) and `.test_durations`' low-band price of every `env -i` row |
| The battery, m1–m4 | `plan.md` names m1–m4; Q6 asks phase 1 to draw the battery from the docstrings | m1–m5: m5 breaks the stub's lease check (`hooks/githooks.py#_P2`), the shell half of the route m4 breaks in Python | Q6's default lets the work extend the battery |
| `test_every_sampled_name_is_a_corpus_row` removed, phase 2 (NAME NOT IN TREE) | `spec.md` §Removes names no unit; phase 1 planted it as T3 | the removal | the regrowth check reads phase 1's pins as changed functions, and T3's mutant, a misspelt `SAMPLE` name, is killed by S2's own row for that name, so no line could prove it; `mutation-check` with the name misspelt is red without T3 (`phases/phase-2.md`) |
| A case names what it guards, and the regrowth check runs that line | the frame approved on 2026-10-14: a `Kills:` line per function, two runs of the file per function, and `tests/unguarded-files.txt` holding the files that owe lines | no line, no list: the check derives each case's mutants from the lines it runs alone, the units it names and the changed shipped lines; one run of the cases that ran a mutant's line; a case its file's only killer of one mutant, or named; survivors of changed code reported; a five-minute bound. Left in phase 4 with the check | the owner's decisions of 2026-10-14: nobody annotates a case, a check derives what it needs, one run per mutant read for its killers, the proof within five minutes |
| The draw ranked and capped, after CI run 38498393195 | `plan.md` phase 2: mutants "drawn from the lines each runs and its siblings do not, the units of its file it names, and the shipped lines the range changed" | ranked by how many siblings run a line, a line only a sibling ran never drawn, 12 at most; the case's own ids run first; four operators added (an operand of `and`/`or` dropped, `in`/`is` flipped, an element removed). Left in phase 4 with the check | the orchestrator's ask: redesign the draw, not the bound; the CI run drew 400 and more per case and ran 23 |
| `mutation-check --baseline-passed` | the frame names no change to `mutation-check` | an option that skips the run against the file as it is, for a caller that ran it; a bare call is unchanged | without it one run per mutant still costs two file runs, and the five-minute bound would name files the model can afford |
| `bin/test` outside the launcher, round 1 | `spec.md` §Scope item 4 as framed: "every `bin/` wrapper and its `.cmd` twin runs its script through it" | every wrapper but `bin/test` and its twin, which hand `run_tests.py` to the interpreter themselves; `spec.md` names the exception now | round 1's 🔴 1: on `/usr/bin/python3` 3.9.6 the launcher refused `run_tests.py` with exit 2 before it could build the 3.12+ virtualenv it exists to build, and the `Broad gate` row runs `bin/test -q` |
| A census of what runs before any floor, round 1 | `spec.md` §Removes: the census of constructs above the floor leaves, on the grounds that the floor rose to 3.12 | the census over every shipped file stays removed; a narrower one replaces it, over the files a hook, a git hook or a `bin/` wrapper hands an interpreter with no floor checked and every module they load, derived from `hooks/hooks.json`, `hooks/githooks.py` and `bin/`; `ruff.toml` lints that set at 3.9 through `per-file-target-version`, and the census reads its version there | round 1's 🟡 2: hooks run on the harness's `python3`, 3.9 on a stock macOS, and `ruff.toml`'s B905 and UP017 at `py312` push toward `zip(strict=)` and `datetime.UTC`; the Stop hook loads `seal_stamp.py` on 3.9 since its guard left |
| A fourth phase-3 case, and a `tryfirst` wrapper | `plan.md` phase 3 names three end-to-end rows, and round 3's paste-ready wrapper is a plain `hookwrapper` | the three rows, and `test_a_traced_run_that_times_out_hands_back_nothing_it_traced` beside them; the wrapper `tryfirst` | no case reached `traced_run`'s timeout branch, so a five-element return there survived `mutation-check`, and the case is red under two mutants of it; `tests/conftest.py`'s own `makereport` wrapper is registered after the tracer and would otherwise read the report after it, against `spec.md`'s *after every other implementation* (`phases/phase-3.md`) |
| `mutation-check --baseline-passed` removed, phase 4 | the brief: "Keep `mutation-check` (its wrapper and script)"; `plan.md` phase 4: "`mutation-check` stays" | the option, `mutation_run`'s `baseline` parameter and the case that pinned them leave; the tool stays with the options it had on the base | phase 2 added the option for `case_check.py` alone, its docstring named that file as the caller, and nothing else in the tree passes it; the brief also removes "everything that stood only on them" (`phases/phase-4.md`) |
| The Windows command-line case moved, phase 4 | the frame names the test module as removed whole | `test_a_windows_command_line_keeps_the_backslashes_of_its_paths` moves to `tests/test_arm_check.py` and loads nothing of its own | it calls `arm_check.py#command_words`, which stays, and the changelog's `Fixed` entry ships its fix; seen red there under `lexer.escape = ""` removed (`phases/phase-4.md`) |
| The `CONTRIBUTING.md` paragraph removed, not rewritten, phase 4 | `plan.md` phase 4: "rewritten in place to the rule that stands … or removed" | removed | the rule that would replace it — a success and a failure case per function, the placement check, the smith's and warden's test rules — is in #942 and #923 and nowhere in the tree, so a rewritten paragraph would carry no `Enforced by:` target and raise `unenforced:CONTRIBUTING.md` past its ceiling; the paragraph was this branch's own, so removal leaves the base's text |

## Not verified

| Item | Who must answer |
|---|---|
| closed Whether each of the 35 sampled rows lands in `main` or `u` without hooks on ubuntu-latest. Only macOS was executed, and Windows was read from `.test_durations`; G4 records 145 rows landing on Linux in 2026-10, not which ones | PR #939's CI run 38477955404 at 480bea69 (now cb8e236e): every ubuntu job passed; three rows failed on macOS and Windows and were fixed at 249bd6d2 (`phases/phase-1.md`) |
| closed That on `macos-latest` and `windows-latest` the fixed sample lands where 249bd6d2 says: `shape: nice` and `#686: cd $W unset` run, and `#686: builtin cd` skips on Windows by `NO_CD_INTO_AN_UNQUOTED_PATH` | CI run 38498393195 at b2564df7 (now 61725f42): macOS passed; on Windows `#686: cd $W unset` landed nowhere, because the image's bash 5.3 refuses `cd ""`. Seen red locally under a bash 5.3 built from source; 3485af38 skips it by `NO_EMPTY_CD` wherever the bash refuses an empty cd |
| closed The phase-1 file's Windows seconds after the sample | #937 made every run's Windows shards measure `.test_durations`, and the refresh #972 committed carries the module's 178 rows |
| closed What the `cases` job says on a CI runner after the end-to-end paths became one case (853f2f28) and the silent-run case left with the value it guarded (f564f644). CI run 38518943105 at 0f2b8a33 (now 341f4941) proved 16 and named 6 in 297 s. Locally at 06f499d3 (now f564f644), `-n 4`, load 4–10: 14 of 14 proved in 298 s, exit 0 | CI run 38658107547 at 692cef31, its `cases` job's log read: 19 proved, 0 named, in 299 s of the 5-minute bound, the job green |
| closed That on `windows-latest` the case file passes now that a mutant keeps each line's own end (cc931b37). CI run 38518943105 failed six end-to-end cases there, every mutant refused against CRLF bytes. macOS gives the same output with a CRLF fixture, and passes after the fix | CI run 38658107547 at 692cef31: all four `windows-latest` shards passed, and the four shards hold every id (`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`), so the case file passed there; read from the jobs' conclusions, its own ids not named in the quiet logs |
| closed What the `cases` job says on a CI runner at phase 3's tip. Locally at d0429bfd, `-n auto`: 22 proved, 0 named, in 299 s, exit 0 | moot: phase 4 removed the job and its script by the owner's decision of 2026-10-15, so no run of it remains to read (`phases/phase-4.md`) |

## Not done

The owner closed this item at phase 2 on 2026-10-15. Phases 3–6 of the plan
as it stood then went to #942; the reframe after round 3 gave the number 3 to
the stopped-short rule. With them went:

- the three enumeration files (`test_a_signer_declares_its_pact.py`,
  `test_one_table_walker_reads_what_gfm_renders.py`,
  `test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py`), each
  cut by a battery of one mutation per kind and a sampled set per kind (Q4);
- the 249 byte-identical helper twins, moved to `tests/conftest.py` on the
  hash, and the `git init` bodies that are twins;
- the sealer file: the inventory of its `run_gate` call sites (Q5; the first
  count is in `phases/phase-2.md`), the battery over `broad_gate.py`'s words
  run after the cut, and whatever the inventory shows can share a run;
- every test file this item did not open, under `spec.md` §*The removal
  criterion*;
- the rows the frame proposed for `seal/budgets.md` — `test-cases`,
  `test-lines`, `test-cases:<file>`, `test-lines:<file>` — with their
  measurers in `budget_check.py`, a per-file table for them, and their
  ceilings;
- the cases that plan's T8 and T9 would have been, which pinned those
  measurers and the per-kind sample.

`unguarded-files` is not among them: the list it would have counted was
dropped by the owner's decisions of 2026-10-14, and nothing owes a line.

## Fed back into the spec

none
