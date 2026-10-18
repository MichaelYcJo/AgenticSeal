# 1792129100-the-mechanics-leave-before-the-agents-are-rewritten — phase 1

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 74083e67 |


## What this phase was asked

The tree green and the evaluation harness reading the 0.22.0 record. The
Windows failure of
`tests/test_a_rewritten_definition_proved_non_inferior.py::test_a_side_runs_the_tree_it_measures_and_no_installed_plugin`
(run 38852872472 and #963's run) fixed where the defect is, the test's
expectation or `noninferiority.py#side_path`, decided by reading the code
and said why here. `evals/scripts/replay_targets.py` reading what the
0.22.0 round record carries (`docs/the-review-record.md`,
`templates/sdd-round.md`), and the four replay cases regenerated through
the generator's `--case`. `evals/README.md:34-35`'s sentence about a
`--list` flag that does not exist rewritten to the generators' real usage.
The plan's Verified-by column for the phase, and its Status cell filled
with the closing commit.

## What this phase found

**The Windows case was wrong in both places, so both changed (94b027cc).**
The case handed `side_path` a `:`-separated PATH, and the function splits
on `os.pathsep`, which is `;` on Windows. Nothing was split, the one entry
contained the cache path, and the whole PATH was dropped, which is the
`['/w/tree\\bin', '/w/tree\\.shims']` of the CI log. Reading the function
for that found the second defect: its filter was the literal
`"/.claude/plugins/cache/"`, which a Windows PATH entry
(`C:\Users\x\.claude\plugins\cache\…`) never contains, so a Windows side
would have run the installed plugin, the one thing the function exists to
prevent. The filter now compares `os.path.normcase` of the entry with
`normcase(join(sep, ".claude", "plugins", "cache", ""))`, which is the
same string on POSIX and the backslashed, lowercased one on Windows. The
case is parametrised over `posixpath` and `ntpath` with a stand-in `os`, so
all three legs run both spellings; the Windows row also carries a
forward-slashed, capitalised cache entry. Seen red: `mutation-check` with
the old literal filter restored, `red` on the `windows` row (executed), and
with `normcase` dropped, `red` on the same row (executed).

**The replay generator had two defects, not one (74083e67).** The first is
the one the plan named: it read only the table record, so all ten of #923's
rounds were left out as `Target SHA (none) does not resolve` (`--list`,
executed before the change). It now reads a labelled record through
`chain_check.py`'s own readers (`round_of`, `finding_spans`, `TARGET_LABEL`,
`LOCATION_LABEL`, `FIXED`), so the grammar has no fifth statement here; a
record the check refuses is left out naming the refusal, and a next record
it refuses confirms nothing. The base comes from the `target:` line: a fix
range's first commit, an `against <sha>` commit, or the merge-base with
`origin/<base>`. A labelled record carries no asked paragraph, so its
prompt carries none, which is the plan's "or none". After the change,
`--list` keeps #923's rounds 3, 9, 7 and 1 with 2, 4, 4 and 5 truths, the
numbers its `confirms:` lines give (executed).

The second was found by trying the plan's own verification: `--case` could
not regenerate any of the four committed replay cases. Their records sit
at `v0.21.0` alone, and the generator read the tree and the last two tags,
which became `v0.22.0` and `v0.21.1` when 0.22.0 was tagged. The same
window held `seed_defects.py` (last three tags): none of the four committed
`seeded-*` names was on its `--list` (executed). That is the class, and both
members are fixed the same way: `--case` reads every release tag for the
named items or commits alone, so a committed case regenerates after any
later release, and `--list` and `--count` keep their window. The four
replay and the four seeded cases were then regenerated in place through
`--case` and came out byte-identical (`diff -r` exit 0 for each, executed;
`git status` clean after). Their graders were read against
`templates/sdd-round.md` by #923's phase 5d and are unchanged; the
`shape-findings` pattern and the `^location: ` truths read the template's
`## Findings`, `### <n>. ` and `verdict:` lines (read).

**For phase 3.** `replay_targets.py` is now a reader of `chain_check.py`'s
label constants (`TARGET_LABEL`, `LOCATION_LABEL`, `FIXED`) and of
`round_of` and `finding_spans`. Phase 3 removes the constants from
`SEVERITY` to `DEFERRED_VALUE`, so it re-points these four reads at the
grammar table; the cases
`test_a_truth_of_a_labelled_record_is_a_fixed_finding_the_next_round_confirms`
and `test_a_labelled_record_the_check_refuses_gives_no_truth` go red with an
`AttributeError` if it does not.

**The README** now says `replay_targets.py` and `seed_defects.py` take
`--list`, `--count N` and `--case NAME`, and `rule_cases.py` takes no
selection (`--help` of all three, executed).

**The cases this phase added or changed, and how each was seen red.** The
plan said phase 1 writes no new case; the generator gained readers, so it
gained cases (`overview.md`'s divergence row). In
`tests/test_a_rewritten_definition_proved_non_inferior.py`, each seen red
by one `mutation-check` break, all executed, all `red`:

| Case | Break |
|---|---|
| `test_a_side_runs_the_tree_it_measures_and_no_installed_plugin[windows]` | the old `/`-literal filter; `normcase` dropped |
| `test_a_truth_of_a_labelled_record_is_a_fixed_finding_the_next_round_confirms` | `fixed` read as not fixed; `confirms:` of every round counted; `labelled` read as "no `Target SHA` row" |
| `test_a_labelled_record_the_check_refuses_gives_no_truth` | the check's refusals ignored |
| `test_a_labelled_target_names_its_base` | `origin/` not prefixed; the fix-range branch removed |
| `test_records_read_only_the_named_items` | the item filter always true |
| `test_a_named_case_is_read_at_every_release_tag[replay_targets]`, `[seed_defects]` | each generator's `--case` back on its old window |
| `test_a_seeded_case_is_looked_for_among_the_named_commits_alone` | the prefix filter removed |
| `test_a_record_with_no_asked_paragraph_ends_the_spawn_at_the_report` | the space before the paragraph written always |

**Verification.** `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_evals_layout.py -q`:
exit 0, 58 passed, at 74083e67 (executed). `bin/test tests/test_a_reader_declares_its_input_class.py tests/test_docs_line_wrap.py -q`:
exit 0, 113 passed (executed). `uvx ruff check` and `uvx ruff format --check`
on `evals/scripts/` and the test module: exit 0 (executed). CI on the three
legs at this phase's commit is not run from here; it is `overview.md`'s
first row.
