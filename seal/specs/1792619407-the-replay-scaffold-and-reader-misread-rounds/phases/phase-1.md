# 1792619407-the-replay-scaffold-and-reader-misread-rounds — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | ba469747 |

## What this phase was asked

Build the reader in `evals/scripts/noninferiority.py`. A finding row is one
`### ` section of the one `## Findings` section, split by
`chain_check.py#finding_spans` over the shared reader's lines and loaded as
`replay_targets.py#record_reader` loads them. `annotate` keeps `report_text`
in place of `report_rows`, masked as `questions.md` Q4 states. `side_numbers`,
`regraded`, `unreproduced` and `regrade` read rows and `truth-` passes from
it. `compare` and `regrade` refuse a side without `report_text` with exit 2.
`FINDING_ROW` and `report_rows` are removed. The cases are spec S1 to S7,
test-first in `tests/test_a_rewritten_definition_proved_non_inferior.py`,
with every case that builds a side by hand given `report_text`.
`evals/README.md` (the sentence on what a side records, and the `regrade`
paragraph) and the module docstring are rewritten in place.

## What this phase found

**The frame holds for this phase except at one point, and the build follows
the part that holds.** Scope item 3 reads every `truth-` grader from the
finding rows. The sealer suite's four `truth-` graders read
`seal/specs/1790000030-guarantee-*/guarantee.md`
(`evals/behaviour/sealer/rule-sealer-false-red/graders/truth-false-red.md`),
which no run prints as a round record, so its rows are empty. Read from the
rows, every sealer truth would fail on both sides of every comparison, and
rule 1 would pass on zero finds. That contradicts the spec's own Out item,
which says the other agents' suites are unchanged. The build reads a `truth-`
grader from the rows only where its target path ends as a round record's
path does (`noninferiority.py#reads_record`, the one `RECORD_PATH` pattern
the `cat` match also uses). Every other grader keeps the eval's result. The
divergence row is in `overview.md`.

**How the Q4 mask loads the scan.** `noninferiority.py#identifier_scan` parses
`tests/test_no_real_identifiers.py`, drops its `from conftest import` line,
and runs the rest as a module. `conftest` imports pytest, and a side's run is
plain `python3` with no `tests/` on its path; only the scan's cases and its
walk of the tree read the dropped names. The scan's allow logic lived inline
in its two walks, so it moved into `refused_domains(line)` and
`refused_user_paths(line)` in the same file, and both walks call them. The
mask calls the same two functions and reads `ALLOWED_USER_PATH` and the new
`FIXTURE_DOMAIN` constant from the module. No pattern is copied.
`test_the_scan_loads_in_a_process_that_cannot_import_a_test_module` runs the
mask in an isolated interpreter.

**A side's JSON needs one more step than the scan's per-line reading.** A
side writes `report_text` as one JSON string, so a line break before a host
becomes the two characters backslash and `n`. The scan then reads the `n` as
the host's first letter. `nexample.com` is refused even though
`example.com` is allowed. So `masked` puts one space after a control
character wherever a host would follow it. No `location:` line or heading
can open with a host, so no row changes.
`test_a_kept_record_is_masked_where_the_identifier_scan_refuses_it` writes
the side and scans every line of the file.

**`regrade` reads a run two ways, and the spec names both.** Its own-suite
check grades each truth over the whole `report_text`, the file the eval
searched. Grading on a suite reads the finding rows.
`test_regrade_checks_a_side_against_the_file_the_eval_searched` holds the
two apart: a truth found by the eval only on a fenced line is accepted and
then graded not found.

**Seen red.** Against 2751c7c7 with the cases written,
`bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist`
exited 1 with 16 failed and 98 passed. The failures were S1 to S7, the Q4
case and the fixtures moved to `report_text`. FINDING_ROW over S1's record
matches two lines, the finding's own and the fenced one. The two cases added
after 74fc5807 and the `-report.md` assertion were each shown red by
reverting their unit with `mutation-check`.

**Mutation.** 16 runs of `bin/mutation-check`, one per unit added, each exit
0 `red`. The units were `finding_rows` (readable lines, and a section with no
`location:` line kept), `masked` (unmasked text, and the escape gap),
`identifier_scan`'s `conftest` filter, `text_of`'s refusal, `reads_record`,
`regraded`'s `whole` both ways, the side's file named in `compare`'s
refusal, `regrade`'s refusal before any suite is read, the truth pass taken
from the eval again, `annotate`'s `report_text`, `RECORD_PATH`'s
`-report.md` alternative, and the scan's `refused_user_paths` and
`refused_domains`. The first run of mutation 14 survived, and the
`-report.md` assertion of the S6 case was added for it.

**S7 executed.** `python3 evals/scripts/noninferiority.py compare --agent
warden --phase 3 --old
seal/specs/1792368015-every-finding-carries-an-evidence-line/evals/baseline-warden.json
--new .../warden-phase-3.json --out <scratch>` exited 2. It printed the
side's path, then `warden replay-1791382684-r2, run 0, keeps no
report_text, so the side was read by the reader before #986 and cannot be
read again`. `regrade --side` over the same file exited 2 with the same
line.

**S13's `git grep`.** `git grep -n -e report_rows -e FINDING_ROW --
':!seal'` finds two lines, both in the test module and both naming the old
field on purpose. One asserts that a side no longer carries the field. The
other builds a side as a run before #986 kept it, for S7. The grep is not
bent to pass. `.test_durations` named the renamed S6 case, and its key is
renamed in place.

**Phase boundary, executed at ba469747.** The touched and meta modules
named in the spawn ran in one `bin/test` call: 408 passed, 2 skipped, exit
0. `bin/rules --check` exit 0, `bin/settle --released-at HEAD` exit 0,
`bin/unverified-check seal/specs/` exit 0. `ruff check` and `ruff format
--check` on each touched `.py` file: exit 0 each.
