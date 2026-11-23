# Phase 2: 1795411585-five-checks-block-on-a-reading-guessed-from-words

## What this phase found

**The frame holds against the tree at `6e1e8cd00`, with one coordinate off
by a line.** `git diff --stat 22803718e 6e1e8cd00` over `skills/verify/`,
`lib/sibling.py` and the three test files of the plan row printed
`pact_check.py` alone (executed), so every coordinate of
`frame/design.md` G6 reads at HEAD as the framer read it. Each stands where
G6 gives it but one: the `nothing runs it` line of `inspect` stands at
`deferral_check.py:189` at `22803718e` (executed: `git show
22803718e:skills/verify/scripts/deferral_check.py | grep -n`), and G6 gives
`:188`, the `if not lines:` above it. Because these files did not change,
each red run below, made at `6e1e8cd00` before the fix, ran the bytes
`22803718e` holds.

**No transcript fixture of `tests/skills/test_session_cost.py` moves
family under the union.** The framer left this question to the phase. A
probe, `test_tmp_families.py` in this phase's scratch directory, loaded
`session_cost.py` from `22803718e` and from the working tree and charged
every string constant of five test modules with each `family` (executed,
6380 strings). The modules were `tests/skills/test_session_cost.py`,
`tests/skills/test_seal.py`,
`tests/text/test_a_segment_feeds_the_flow_log.py` and
`tests/text/test_the_handoff_before_round_one.py`; the fifth path given,
`tests/test_session_cost_post.py`, does not exist, and the first run
raised on it before it printed anything, so the probe ran a second time
without it. Five strings moved, all of them
in the new case `test_reads_the_runner_words_seal_deferrals_holds` (its
four commands and its docstring). The probe reads an f-string by its
literal parts, so a command assembled at run time is outside what it read;
the suite's run of both modules after the fix passed, so no assertion moved.
No case was re-pinned, which `frame/design.md` *Scope* item 3 allowed for.

**The union is one fragment per word, anchored at a word boundary.**
`frame/design.md` *Scope* item 3 asks each fragment to be anchored as one
of the two lists anchors it today. Where both lists held a word with
different anchors, the fragment takes `RUNNERS`' `\b`, which accepts every
command `session_cost.py`'s `(^|[\s./\\])` accepted, since each character
that anchor allows before the word is not a word character. Two fragments
come out of that: `\b(?:make|just|task|npm|yarn|pnpm|gradlew?)\s+(?:run\s+)?test\b`
in place of `RUNNERS`' three `make`, `npm` and `pnpm|yarn` fragments and
`FAMILIES`' group, and `\b(?:bin|scripts)[/\\]test\b` in place of
`RUNNERS`' `\bbin/test\b` and `FAMILIES`' path group. Each matches every
command either list matched, so neither reader loses a match. Each also
matches a few shapes neither matched, such as `"just test"` after a quote
(judged against `frame/design.md` *Scope* item 3 and
`skills/core/SKILL.md` *The rule a mechanism is kept against*: a fact has
one source). `\bmvn (?:\S+ )*test\b` already holds `FAMILIES`' `mvn test`,
so that word took no fragment of its own.

**The `nothing runs it` line goes, and the headline says what it said.**
`frame/design.md` *Scope* item 2 has the headline, the `nothing runs it`
line and the closing sentence say that no CI or hook line matched. Where
no line matched, the headline now reads `tests: no CI or hook line matched
a runner word`, so a second line saying the same would print one fact
twice. `inspect` no longer appends the line; the closing sentence and the
`limit:` line, which names a composite action, a reusable workflow and a
script, carry the rest. Where only the pre-commit hook matched, the
headline reads `tests: no CI line matched a runner word` above the `local`
line. The headline where a CI line matched stays `a runner in CI`, since
*Scope* item 2 names only the headline of a kind with no matching line
(judged against `frame/design.md` *Scope* item 2 and *Data & interfaces*,
which keeps the outcome lines' order).

**`session_cost.py` now loads `lib/sibling.py` at import, so a copy of it
taken alone exits 2.** `FAMILIES` is built at import, so the load of
`deferral_check.py` stands there too. Before this phase `session_cost.py`
imported `sibling` inside `lib_module` alone, and a copy run without its
siblings read a transcript. It now guards the import with the sentence
`pact_check.py` and `payload_meter.py` spell for the same case, and
`Test_module.test_a_script_copied_alone_exits_2_and_names_what_it_misses`
pins it, after S4 of #1482. The frame does not name this; it is the cost
of *Scope* item 3's load, and the comment over the guard and the
`lib_module` docstring state it (judged against
`lib/sibling.py`'s module docstring, which gives the absent file its one
sentence and exit 2).

**A false comment over `RUNNERS` went.** It said the word-boundary anchor
keeps `pytest-cov` in a dependency list from reading as a test run, and
`re.search(r"\bpytest\b", "pytest-cov")` matches (executed). The new
comment states what the anchor does keep out, `pytest` inside
`mypytests`, and names `session_cost.py` as the list's second reader.

**`test_missing_path_exits_two` is renamed
`test_refuses_a_missing_path_at_exit_2`.** The phase boundary run failed
`tests/behaviour/test_this_repository_passes_its_own_checks.py::Test_seal_layout::test_accepts_this_repositorys_tests`,
because `seal layout --check tests` refuses a `Test_main` with no
`test_refuses_` case once the refusing case of a tree with no CI became a
report. The command still refuses a path that is not there, so the case
that holds that refusal now says so. Its body is unchanged, which is the
*Names or places only* row of `skills/verify/SKILL.md` *The narrow command
still has to be able to fail*: the case ran green at its new name, and
`git grep -n missing_path_exits_two -- ':!seal/threads'` printed nothing
(executed).

**Seen red (executed, at `6e1e8cd00` before the fix, one command, 13
failed).**

- S5, `test_reports_a_suite_run_through_a_script_as_no_match_and_exits_0`:
  failed on `assert 1 == 0`, the old exit 1, with `NO RUNNER IN CI` in its
  output.
- S6's first case,
  `test_names_a_runner_word_session_cost_charged_before_this_list_held_it[tests-nox -s tests]`,
  failed on exit 1 with `NO RUNNER IN CI`: no word of the old `RUNNERS`
  matched `nox`. Its four other ids failed the same way.
- S6's second case, `test_reads_the_runner_words_seal_deferrals_holds`,
  failed on `pylint src`, `'other' == 'lint/type'`.
- `test_a_script_copied_alone_exits_2_and_names_what_it_misses` failed on
  `assert 0 == 2`: the copy printed its usage and exited 0.
- The five re-pinned cases of `seal deferrals`' outcomes each failed on
  their exit code.
- The `npm  test` id, added after the first `seal mutate` round, was seen
  red by the mutant that puts back `RUNNERS`' single space (below).

**Mutation (executed, `bin/seal mutate`, 25 runs, 24 red, 1 SURVIVED and
then pinned).** The tree was clean after each call.

- `deferral_check.py`, with the cases of the outcome lines: the final
  `return 0` as `return 1 if unmatched else 0`; `if lines:` in `headline`
  as `if False:`; the no-match headline respelt; `if unmatched:` as
  `if True:`.
- `deferral_check.py#RUNNERS`, with the cases of both files that name
  runner words: each word the union adds broken in turn, `nox`, `bun test`,
  `deno test`, `scripts`, `bin`, `test.sh`, `just`, `gradlew`, `black`,
  `lint-imports`, `pylint`, `go vet`, the optional `3` of `python3?` and
  the goals of `mvn`. The run of whitespace before `test`, as a single
  space, SURVIVED: no case of either file wrote two spaces. The
  `npm  test` id was added, committed as `6d9c06ca5`, and the same mutant
  then went red.
- `session_cost.py`, with `-k reads_the_runner_words`: `lint/type` built
  from `RUNNERS["lint"]` alone, from `RUNNERS["typecheck"]` alone, and
  `test` from `pytest` alone. With `-k copied_alone`: the guard's exit 2 as
  1, and its sentence without `Nothing was read.`

**Search 5 of `frame/design.md` prints nothing** (executed after the fix).

**The phase boundary set (executed, one `bin/test -q` command, run twice).**
It held the plan row's three files, the changed test files, the test files
outside `tests/text/` and `tests/behaviour/` that name `deferral_check`,
`session_cost` or `skills/verify/SKILL.md`
(`tests/github/test_roll_flow_measurement_issue.py`,
`tests/skills/test_broad_gate.py`, `tests/skills/test_seal.py`,
`tests/test_run_tests.py`), `tests/test_censuses.py`, and the two
tree-wide directories. The first run failed the one layout case above. The
run after the rename passed: 2356 passed, 10 skipped. Its five warnings are
citations that pending rule changes of other work items excuse, none in a
file this phase changed.
