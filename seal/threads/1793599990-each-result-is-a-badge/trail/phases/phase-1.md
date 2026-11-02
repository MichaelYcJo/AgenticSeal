# Phase 1: 1793599990-each-result-is-a-badge

## What this phase found

**The frame holds, with two coordinates off.** Every path the frame names
exists, and the header helpers sit at
`.github/scripts/publish_release_note.py:611-669` as *Technical context*
states. Two of the case coordinates in `frame/design.md` *Grounding* are
wrong. The two `sealed_header` cases in
`tests/github/test_publish_release_note.py` sit under `Test_module`, which
opens at line 824, and not under `Test_main`. In
`tests/github/test_release_seal.py`, the dry run case ends at line 966 and
the `results` case opens at line 1011, not at the ranges given. I built to
the cases themselves, so neither error changed what was built.

**S3 is an assertion in S1's case, not a new case.** The frame asks for a
new case that reads every badge's alt text with `html.parser`. S1's case
already pins the whole header string, every `alt` attribute included, so a
separate case would cover nothing its group does not. That is the crafter
definition's rule *A new test starts from its group*. The reading is
therefore a second assertion in
`#Test_module::test_the_header_is_built_by_one_function_and_its_sealed_twin_by_another`,
through a parser `Unimaged` in the same module, and it also reads the odd
input back, so an escaped `&`, `<` and `"` come back as written.

**The badge's address is not HTML-escaped, which departs from *Scope* item
2's last sentence.** `seal mutate` left the case green with
`html.escape(url)` removed. The escape cannot change any output.
`urllib.parse.quote(text, safe="")` leaves only letters, digits, `_.-~` and
`%` in a label or a value, and the address template's own characters
(`:/?=`) mean nothing to HTML. A unit that stays green while broken has
nothing behind it (`skills/core/SKILL.md` *The rule a mechanism is kept
against*), so `ddbef6c1` removes it, and `badge`'s docstring states why the
address needs no escape. The alt text keeps its escape, and S1's odd input
pins that escape.

**`counts`' docstring is corrected, though *Scope* item 7 does not name it.**
It said "Both headers state them in these words (#1153)", and once the
sealed header carries badges that is false. Contract rule 19 asks for every
sentence that states an old fact to change in the same commit. It now says
`header` states the counts in words and `sealed_header` states them as
badges through `count_badges`.

**Decisions the frame left to the builder:**

- The new names in `publish_release_note.py` are `BADGE_LABEL_COLOUR`,
  `BADGE_VALUE_COLOUR`, `BADGE_URL`, `badge_text`, `badge` and
  `count_badges` (*Data & interfaces* says their names are the builder's).
- `tests/censuses.py#ALLOWED_DOMAINS` gains the badge service's image host
  exactly, not its parent domain. `refused_domains` allows any subdomain of
  an allowed entry, so the parent would allow every host under it, and
  *Scope* item 4 names one host.
- The label `outside contributors` stays the same whatever the count, so
  one contributor reads `outside contributors: 1`. A label names a kind of
  thing, as `pull requests: 1 merged` does, and *Data & interfaces* writes
  each label as one fixed string.
- The `skipped` badge's value is the count alone, taken from the suite
  row's second part. The suite always has both parts, because
  `release_seal.py#seal_release` raises `Refused` before `results` runs
  when the record cannot be read.

**A constraint met only by trying.** `hooks/lint-python.py` runs `ruff
--fix` on each save. An `import urllib.parse` added before its first use
was removed as unused, and the module then failed in `release_seal.py`'s
cases with `NameError`. The import went back in after the code that uses it.

**`.test_durations` is not edited.** It holds no row under the touched
cases' current names. Its only row for them is
`test_the_glance_block_is_built_by_one_function_and_its_sealed_twin_by_another`,
a name from before #1153. So the file is not kept in step with each rename,
and the renamed `results` case and the new S4 case add nothing it tracks.

**Seen red (contract rule 15).** I rewrote the cases first and ran them
against the tree at `b90e0158`. That run gave 12 failed and 2 passed. Red:
the two `sealed_header` cases, the new S4 case (`AttributeError`, no
`badge`), `test_accepts_a_published_note_and_replaces_its_header`, the six
parameters of `test_a_row_other_than_yes_attaches_nothing_and_puts_the_results_alone`,
the dry run case, and
`test_the_results_are_the_stamps_rows_as_labelled_values`. The 2 passes
were the two parameters of
`test_a_second_run_finds_no_header_to_replace_and_writes_nothing`, which
S7 keeps unchanged. `test_the_results_are_the_stamps_rows_in_words` is
renamed to `..._as_labelled_values`, because it now pins pairs, not words.

**Mutation (`bin/seal mutate`, at `eca0e549`).** There were three runs, one
per file:

- `publish_release_note.py`, against the two `sealed_header` cases and S4.
  Five mutants went red: the encoder without doubling, the badge without
  its `alt`, the outside contributors line dropped, the badges of a line
  joined with no space, and the value colour set to the label colour. The
  `html.escape(url)` removal survived and is the departure above.
- `release_seal.py#results`, against the `results` case and
  `test_accepts_a_published_note_and_replaces_its_header`. Six mutants went
  red: `skipped` left with its word, the not-read review badge dropped,
  `capped` and `deferred` each left unsplit, the branch badge dropped, and
  the review and work items values swapped.
- `tests/censuses.py`, with the badge host replaced in `ALLOWED_DOMAINS`.
  `test_publish_release_note.py::test_census` went red, naming the host at
  `publish_release_note.py:655` as a real-looking domain.

`seal mutate` reads a mutant that does not compile as red until #898 lands.
So before counting any red, I applied every mutant in memory and passed it
to `compile()`. The probe was
`compile_mutants.py` in the build's scratch directory, and all twelve
compiled. None of the mutants changes an import or a name bound at module
level, so each module still imports (read). The census red names the
census's own refusal, not an import error.

**The phase-boundary run.** One command through `bin/test` gave 470 passed,
exit 0. It ran `tests/github/test_publish_release_note.py`,
`tests/github/test_release_seal.py`, `tests/test_censuses.py`,
`tests/behaviour/test_a_release_publishes_its_note.py`,
`tests/behaviour/test_the_release_seal_is_drawn.py`,
`tests/behaviour/test_the_gate_names_every_step_ci_runs.py`,
`tests/hooks/test_console.py`, `tests/skills/test_settle.py` and
`tests/text/test_the_release_tail_does_not_end_at_the_tag.py`. These are
the modules that name a changed path. The run leaves out the other modules
that read `tests/censuses.py` through `conftest.py#census_case`, which is
nearly every module. The plan's *Verified by* cell narrows the census check
to `tests/test_censuses.py` and the touched modules' census cases. A
widened allowlist cannot refuse a file it accepted before, and the broad
gate runs them all.
