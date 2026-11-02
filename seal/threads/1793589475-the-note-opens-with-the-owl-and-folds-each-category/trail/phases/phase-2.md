# Phase 2: 1793589475-the-note-opens-with-the-owl-and-folds-each-category

## What this phase found

### The frame, checked before the build

The frame holds for phase 2. Every coordinate `frame/design.md` gives for
this phase was opened at `ef978e65f` and stood as stated (read). The guard is
at `.github/scripts/release_seal.py:506-513`. `alt_text` is at `:171-208`, the
`LABELS` comment at `:100-109` and the module docstring's guard sentence at
`:27-37`. `glance` and `sealed_glance` are at
`.github/scripts/publish_release_note.py:595-633`, and the workflow comment is
at `.github/workflows/publish-release.yml:24-36`. `frame/questions.md` Q1 is
built on its default: the image keeps the width `draw` answers.

### What the code writes now

The design leaves the functions' names to the crafter (*Data & interfaces*).
Four functions in `publish_release_note.py` replace `glance`,
`sealed_glance` and `GLANCE_HEADING`:

- `counts` returns the counts' lines: `7 pull requests merged`,
  `4 issues closed`, and `2 outside contributors` where there are any. A count
  of one is singular. Both headers call it, as the design asks.
- `table` writes the HTML table of one row. A cell's lines are parted by
  `<br>`, and no line inside the table is blank.
- `header` is `publish`'s one-cell table of `counts`. `release_body` writes
  it first, then the theme where there is one, then the folds. A note with no
  pull request to read has no header, as before.
- `sealed_header` is the two-cell table. The first cell holds the image. The
  second holds `<b>SEALED</b>` and the sealed version line, the lines of
  `counts`, and the stamp's other results. The URL, the alt text and every
  line are escaped with `html.escape`.

In `release_seal.py`, `results` replaces `alt_text`. It returns the sealed
version line (`v1.2.3 at aaa11111 on main`) and the lines for the suite, the
work items, the capped count and the deferred issues, in the phrases the alt
sentence used. A row not read says so in its line, as before. `seal_release`
finds `header`'s text exactly once, or refuses with a sentence that now names
"a run of this job already replaced it". It sets the alt text to
`The <version> release seal`. The `[`, `]` and line-break filter went with
`alt_text`, and with it the module's only use of `re`; the lint hook removed
the import when the file was saved.

### Decision: the pull request and issue lines come from `counts`, not from the rows

`release_rows` also carries the pull request and issue counts, and
`alt_text` read them back out of the rows. The design says one function's
phrases serve both headers (*Data & interfaces*). So `results` leaves those
two rows out, and `sealed_header` takes `work`, `closed` and `people` and
calls `counts`. The numbers are the same either way, because `seal_release`
builds both rows from `len(work)` and `len(closed)`. Judged against
`frame/design.md` *Data & interfaces*.

### Decision: `publish_release_note.py` gets its own `plural`

`release_seal.py#plural` already exists. `counts` needs the same rule in the
publisher, and the publisher cannot import from the seal, which it does not
load. The seal could have called the publisher's copy instead. That would
make `release_rows` depend on the publisher, which the seal loads only when
first asked (`release_seal.py#module`), and the row cases call `release_rows`
directly. So each script keeps a one-line `plural`. Judged against
`release_seal.py`'s comment over `module` and `skills/core/SKILL.md` *The rule
a mechanism is kept against* ("A fact has one source"). The rule here is a
pluralisation rule and not a fact of the release. `gaps.md` *Not done* names it.

### The cases, and how each was shown red

| Scenario | Case | Seen red at phase 1's code |
|---|---|---|
| S2 | `tests/github/test_publish_release_note.py#Test_main::test_the_note_opens_with_a_header_of_its_counts`, in place of `test_the_glance_counts_the_release` | at its first assertion: the note opened with the theme |
| S2 | `#Test_main::test_the_theme_follows_the_notes_header`, in place of `test_the_note_opens_with_the_releases_theme` | at its opening assertion: the note opened with the theme |
| S2 | `#Test_main::test_without_a_theme_the_note_has_no_theme_line_and_the_job_goes_on`, three cases | at its opening assertion: the note opened with the glance heading |
| S2, S3 | `#Test_module::test_the_header_is_built_by_one_function_and_its_sealed_twin_by_another`, in place of the glance case | `AttributeError`: no `header` |
| S3 | `tests/github/test_release_seal.py#Test_main::test_accepts_a_published_note_and_replaces_its_header` | at `published.count(HEADER) == 1`: the old note held no header |
| S3 | `#Test_module::test_the_results_are_the_stamps_rows_in_words`, in place of the alt text case | failed; the line was not read, and the old module has no `results` (read) |
| S4 | `#Test_main::test_a_second_run_finds_no_header_to_replace_and_writes_nothing`, new | at its `::warning::` line: the old guard refused with the glance sentence |
| S5 | `#Test_main::test_a_hand_edited_note_is_left_alone_and_nothing_is_uploaded`, rewritten to the header | at `edited != note()`: the old note held no header to edit |
| S5 | `#Test_main::test_refuses_on_any_failure_and_leaves_the_note_as_published[the header is not there]` | at `len(warnings) == 1`: the old code sealed the note and printed no warning |
| S3 | `#Test_main::test_a_dry_run_draws_and_prints_and_writes_nothing` | failed; the line was not read, and the old dry run printed the alt sentence (read) |

The red run was taken in a scratch clone at `ef978e65f` made with
`git clone --no-local`, with the two new test modules copied in. It exited 1
with 12 failed and 83 passed (executed), and the clone was removed afterwards.
The failing line of ten of the twelve was read from that run's log. The log
was cut at twenty lines, so two failing lines were not read, and the table
says which.
S6's case, `test_with_nothing_to_summarise_the_note_is_the_theme_and_the_fragments`,
is unchanged and passed there and after the build.

After the build commit `7744a4564`, `seal mutate` ran nine mutants, one
command each. Each verdict was `red` with exit 0, and the tree was clean after
each restore (executed):

| Mutant | Case run | Failing line |
|---|---|---|
| `if body.count(table) != 1:` in `seal_release` made `if False:`, the exact-header guard alone removed | S4's case | `assert hub.writes("upload") == [] and hub.writes("edit") == []`: the second run uploaded and edited |
| `counts` writes the contributors' line with no contributor | S2's header case | the singular header assertion |
| `plural` always adds `s` | S2's header case | the singular header assertion |
| the theme written before the header | S2's header case | the opening assertion |
| the lines of `sealed_header` not escaped | the header module case | the escaping assertion |
| the sealed version line not escaped | the header module case | the escaping assertion |
| the alt text other than `The <version> release seal` | S3's case | `body == published.replace(HEADER, sealed)` |
| `capped not read` written as `capped` | the results case | the not-read assertion |
| the image and the result lines in one cell | S3's case | `body == published.replace(HEADER, sealed)` |

### Pins changed beyond the frame's *Removes*

*Removes* lists the cases that pin the glance, the type headings and the
alt sentence. Four more cases read the old note and changed in the build
commit, each only as far as the new note requires:

- `test_the_note_opens_with_the_releases_theme` asserted that the theme was
  the note's first line. It is now `test_the_theme_follows_the_notes_header`.
- `test_without_a_theme_the_note_has_no_theme_line_and_the_job_goes_on`
  asserted that the note opened with the glance heading. It now asserts the
  header, followed by the first fold.
- `test_a_release_with_no_outside_contribution_thanks_nobody` looked for
  `Outside contributors`. It now looks for `outside contributor`, the header's
  words, so a contributors' line with no contributor still fails it.
- `test_a_dry_run_draws_and_prints_and_writes_nothing` looked for the old alt
  sentence. It now looks for the new alt text and the `SEALED` line.

`.test_durations` still holds the old ids of the renamed cases. That file
is the cache the test runner rewrites (`tests/censuses.py`, the comment over
`OLD_NAME_RECORDS`), and this phase did not edit it.

### The phase-boundary run

The plan's command
`bin/test tests/github/test_publish_release_note.py tests/github/test_release_seal.py tests/behaviour/test_the_release_seal_is_drawn.py tests/behaviour/test_a_release_publishes_its_note.py tests/behaviour/test_the_gate_names_every_step_ci_runs.py tests/text/test_the_release_tail_does_not_end_at_the_tag.py tests/hooks/test_console.py tests/hooks/test_launch.py tests/skills/test_settle.py tests/test_censuses.py`
passed 447 cases (executed, exit 0). `bin/seal layout --check tests` refused
nothing (executed, exit 0). `bin/seal layout --pairs` exited 0 and named no
pair in the two changed test modules (executed). `uvx ruff check` and
`uvx ruff format --check` passed on the four changed Python files (executed,
exit 0 each).
