# Phase 2: 1793171930-no-check-reads-a-citation-of-most-files

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | aafe184b |

## What this phase was asked

Build S9, the warning for a citation in the policy root that a pending
`## Rule changes` item corrects, and S10, the sentence and `check:` line in
`skills/writing-style/SKILL.md`. Answer `frame/questions.md` Q1 by running the
S9 fixture once under `bin/test -q` and recording the result. Build Q2 on its
default; the orchestrator handles any rebase.

## What this phase found

**Q1, measured: (a).** One probe, `tests/behaviour/test_tmp_q1_warning.py`,
ran S9's excusing fixture through `assert_resolved` with nothing capturing
the warning. It ran under `bin/test tests/behaviour/test_tmp_q1_warning.py -q`,
which started xdist workers. The run ended `1 passed, 1 warning`, exit 0.
Under its warnings summary, pytest printed the whole message as a
`UserWarning`: the citing file and line `docs/a.md:9`, the citation of
`manual/b.md`, and the work item `seal/threads/1-x/`. The fixture then
cited the one-word section *Old*; it cites *Old name* since. The probe was
deleted after that one run. The record `seal gate --record`
writes holds no test output at all: `skills/verify/scripts/broad_gate.py#write_gate_file`
writes one row, `<tree> against <base>` (read). The gate's panel prints
pytest's counts without a warnings category (`#suite_counts`, read). The
gate keeps the full output in a file under `--keep-output`, and the warning
should stand there as it did in the probe's output. No gate run measured
that. S9 reports through `warnings.warn` as framed, so no divergence row is
owed. `frame/questions.md` is not a file the crafter writes, so its Q1
Status cell is the orchestrator's to fill.

**S9's red run.** S9's cases were written first, against a reader that
excused nothing. The two excusing variants failed and the refusing ones
passed, exit 1. With `corrections` and `excuser` written, the module passed,
exit 0.

**What decides an excuse.** An item excuses a citation when its `file` is
the citing file, its `from` holds `*<cited text>*`, and its `to` does not.
Both fields are compared with whitespace collapsed, because `field_values`
joins a continued field with a line break. A `remove` with no `from`
excuses a citation inside the section it names, measured with
`rule_changes.section_lines`. An `add` excuses nothing, even when it names
the citation's section. A missing section leaves `section_lines` with no
span, and no excuse follows. Nothing in the case tests whether the citing
file is in the policy root. `rule_changes.parse` refuses an item whose
`file` is not a top-level file of that root, so such an item never reaches
`excuser`. The fixture for a file outside the root pins that.

**The fixtures grew to give each condition a case.** The excusing set
covers a `from` holding the citation, a `from` wrapping it onto a
continuation line, a removal of its section, and a policy root that
`seal/config.md` names (`policy/`). The refusing set covers a design with
no `## Rule changes`, a `- nothing` block, an item naming another file, a
`from` that lacks the citation, a `to` that keeps it wrapped, a removal of
another section, a removal of a section the file lacks, an `add` to its
section, a section `parse` refuses, and a citing file outside the policy
root. S9's 14 mutants all went red against these two cases.

**S10.** The citation sentence of `skills/writing-style/SKILL.md` now says
the italic text is the cited file's heading or the bold sentence that opens
one of its rules. Its `check:` line ends with the new module.
`bin/seal rules --check` holds all 266 check lines, exit 0. A mutant naming
the module one letter short failed that command, which `seal mutate` read as
red.

**Five other places state the citation shape by heading alone, and they
stand.** These are `tests/censuses.py:889` (the `section_sign` census's
message, pinned at `tests/test_censuses.py:729`),
`templates/records/sdd-design.md:29`,
`tests/behaviour/test_a_declared_label_reaches_the_tracker.py:54` and
`tests/text/test_broad_gate_rule.py:80`. Citing by heading text stays
correct, and none of them says a bold lead cannot be cited, so none of them
states the old fact. `tests/text/test_broad_gate_rule.py` is #1040's file.

**`stacklevel=2`** is passed to `warnings.warn`, as ruff's B028 asks. The
warning then points at the case that called `assert_resolved`.
