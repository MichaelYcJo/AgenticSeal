# 1792366315-the-wardens-real-false-finding-rate-is-unknown — review round 2

target: b52e3d25, fixes f9f53f3c..b52e3d25

## Findings

This round verifies the fixes, reading `git diff f9f53f3c..b52e3d25`. All
four closes of round 1 hold, and each is named under *Confirmations*. One
new defect stands in a unit the fix pass added, the range branch of
`truths_with`, so it carries a `regression:` line.

What this round carried from round 1 rather than re-established:

- The S2 re-runs of the classing commands. The classing and `false-rows.md`'s
  rows did not change in this range (read: the diff of `false-rows.md` touches
  only the figures section).
- The AST check that `verdict` is unchanged. In this range
  `noninferiority.py` changes only the `regraded_from` line (read).

Everything else below was re-run at b52e3d25.

### 1. A range entry whose end is below its start writes a truth that matches no line, with no message

severity: should
location: `evals/scripts/replay_targets.py:450-456`, `tests/test_a_rewritten_definition_proved_non_inferior.py:1766-1784`
verdict: open
regression: round-1#2

The unit is `truths_with`'s range branch at `replay_targets.py:450-456`,
which 11ebe8f4 added. `spec.md` §*Data & interfaces* says an entry's
location is `path`, `path:line` or `path:first-last`, and the plan's phase 3
row has the generator stop on an entry the case cannot take. The fix reads
a range to its last line but never checks that the last line follows the
first. So a reversed range, a typing slip the next hand-added entry can make,
passes as a coordinate and writes an empty line list. That is the same
silent wrong truth round 1's finding 2 was about, made by the code that
closed it.

Grounds, executed. The round's probe called `truths_with` for
rule-warden-one-finding with `"locations": ["src/x.py:100-10"]`. It returned
`^location: .*(?:src\/x\.py:(?:)(?!\d))` with no message. That pattern
matched none of the rows naming `src/x.py` at lines 9, 10, 50 and 100. It
matched only a row whose path ends in a bare colon. Its grader would read
`not found` on every run, and recall's denominator would grow by a truth no
run can find.

Grounds, read. `lines_option(path, first, last)` builds
`range(max(1, first), last + 1)`. With `last` below `first`, that range is
empty, and nothing downstream refuses an empty line list.

```python
            last = re.search(r"[-\N{EN DASH}](\d+)$", location) if m["line"] else None
            if last:
                first, end = int(m["line"]), int(last[1])
                if end < first:
                    raise SystemExit(
                        f"{case}: {e['grader']} names `{location}`, a range that ends before it starts"
                    )
                options.append(lines_option(m["path"], first - window, end + window))
            else:
                options.append(truth_option(f"`{location}`", target, window))
```

```python
# test_an_entry_the_case_cannot_take_stops_the_generator, one more row and id
        ({"locations": ["src/x.py:100-10"]}, "ends before it starts"),
        "a-range-that-ends-before-it-starts",
```

answer:

## Confirmations

confirms: round-1#1
The close holds at 11ebe8f4 and 4116d2a5 (executed):

- At b52e3d25, truth-changelog-history accepts `changelog.md` lines 10-19.
  truth-old-phrase-kept accepts lines 5-9 of the changelog and lines 4-8 of
  the test docstring. No line is accepted by both.
- The new `test_no_two_truths_of_a_warden_case_accept_one_location` passes
  at b52e3d25. It fails with f9f53f3c's two r5 grader files put back,
  naming this pair at `changelog.md:3` and `:6`. So it pins the class
  across all nine cases.
- Phase 3's run 0 now passes truth-changelog-history by row 1 and
  truth-old-phrase-kept by no row. Every other credit of the pair comes
  from a row that names its own coordinate.
- The committed `971-warden-phase-3-11ebe8f4.md` shows truth-old-phrase-kept
  at 1 of 2, and the tables give phase 3 40/54. `compare` re-run over the
  two committed sides wrote the record byte for byte.

One limit stands on the test. Its `OPTION` reader parses only the
generator's own line-list and bare-path forms. So the one hand-written
pattern, rule-warden-one-finding's truth-shout-twice, is checked only as
the other side of a pair, never as the source of a probe line. No other
truth of that case shares its file, so nothing is missed today.

confirms: round-1#2
The close holds, executed. An entry with `"locations": []` stops with
`names no location`. A range is read to its last line. That holds for
`src/x.py:10-100` in the module's new case, for the committed entry's
`changelog.md:12-17`, and for an en-dash range in the probe.
`window` is refused for `True`, `-1` and `"2"`, and accepted for `0`, which
gives the exact line. The regenerated suite's bytes did not move for any
truth without a `window` (see the S6 entry below). The reversed range above
is a new defect in the branch that made this close, and it is finding 1.

confirms: round-1#3
The close holds, executed. Both committed sides at 11ebe8f4 hold
`regraded_from` af9c924b. Regrading each of them onto 11ebe8f4 again exited
0 and kept af9c924b. The added lines of
`test_a_side_regraded_onto_a_wider_truth_counts_the_row_it_now_matches`
pin it.

confirms: round-1#4
The close holds. The fragment now names #968's and #970's bodies passing
`--suite-rev af9c924b` and #985's measuring on af9c924b's suite (read).
That agrees with the bodies round 1 opened.

confirms: none
The figures follow from the suite as fixed (executed). The phase 1 join, the
S5 join and the figures check, each as written in its phase file at
b52e3d25, exited 0:

- The S5 join printed 19 of 55 and 12 of 47 false, and `problems: 0`.
  truth-old-phrase-kept now passes three runs.
- The figures check printed `figures: 11; not in the table: 0`.
- `regrade` of #957's two sides onto 11ebe8f4 wrote files byte for byte
  equal to the committed ones.
- `noninferiority.py check` over the new record exited 0.

confirms: none
S6 and S7 still hold, executed. In a `--shared` clone at b52e3d25, the
three generators regenerated all nine warden cases and every other agent's
fixture cases, and `git status --porcelain` was empty. Against 864798a4,
the only suite files 11ebe8f4 changes are the two r5 truth graders. Nothing
under `evals/behaviour/` changes after 11ebe8f4. `bin/test
tests/test_a_rewritten_definition_proved_non_inferior.py -q` passed 103.

confirms: none
The coordinator asked whether the edits to `phases/phase-3.md` and
`phases/phase-4.md` correct the record or rewrite history. I read them as a
correction of record. Each edit keeps the value recorded at the phase beside
the new one, and names review round 1 as the cause:

- the S5 join "exited 0 at 864798a4, and again at 11ebe8f4";
- the run counts "at 864798a4 were 4, 6 and 7";
- the figures check "exited 0 over the 864798a4 sides".

The edits are what keep the two commands runnable. The figures check names
side files that 4116d2a5 removed, so as first written it would now stop on
a missing file. Each phase's `What this phase was asked`, its `Commit`
field and `plan.md`'s Status column still name 864798a4 and 837ee9bc,
which is what each phase closed on (`git grep -n 864798a4`, executed).

One part is a rewrite. Phase 3's paragraph giving its own reason for
keeping the ±15 window was replaced, not kept beside the fix. That reason
survives in round 1's finding 1, which quotes it, in `overview.md`'s new
divergence row and in git. So nothing of it is lost from the work record,
and I raise no finding on it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Round 1's row on five credits from rows no entry's `from` names, unchanged by this range | `seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/rounds/round-1.md` | the repository owner |
| The finding wording behind every class, which only #971's first comment holds | `seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/evals/false-rows.md` | the repository owner |
| The full suite, the repository-wide lint and the typecheck over the branch. This round ran one module | the branch | the orchestrator, through `broad-gate` |

## Probes

| Command | Result |
|---|---|
| `test_tmp_round2.py`, one file at a `--no-local` clone's root at b52e3d25, run once and deleted | The phase 1 join, the S5 join and the figures check each exited 0. Regrading onto 11ebe8f4 gave files byte-equal to both committed sides, and a second regrade kept `regraded_from` af9c924b. The r5 pair's credits by row are as given under round-1#1. `truths_with` on a reversed range gave an empty line list (finding 1); on `True`, `-1` it stopped; on `0` it gave the exact line; on an en-dash range it gave the whole range. The overlap test failed with f9f53f3c's r5 graders and passed after they were restored |
| `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q` | 103 passed |
| `replay_targets.py --case` for the four replay cases, `seed_defects.py --case` for the four seeded cases and `rule_cases.py`, in a `--shared` clone at b52e3d25 | all exited 0; `git status --porcelain` empty |
| `noninferiority.py compare --agent warden --phase 3` over the two committed 11ebe8f4 sides, then `cmp` against the committed record; `noninferiority.py check` over it | `Verdict: pass`, byte-equal; check exit 0 |
| `git grep -n -e 864798a4 b52e3d25`, outside `rounds/` | only phase 3's and phase 4's records of what they did, and `plan.md`'s Status cell |
