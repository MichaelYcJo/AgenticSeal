# 1792619407-the-replay-scaffold-and-reader-misread-rounds — review round 5

target: c64c8845, fixes ad78bfb6..c64c8845

## Findings

### 1. The spec names the docstring as the home of the floor rule and states the rule itself in two places

severity: should
location: `seal/specs/1792619407-the-replay-scaffold-and-reader-misread-rounds/spec.md:89-91`, `seal/specs/1792619407-the-replay-scaffold-and-reader-misread-rounds/spec.md:241-246`
evidence: read `seal/specs/1792619407-the-replay-scaffold-and-reader-misread-rounds/spec.md:82-96`, `seal/specs/1792619407-the-replay-scaffold-and-reader-misread-rounds/spec.md:237-248`, `evals/scripts/noninferiority.py:298-330`
verdict: open

c64c8845 rewrote the frame to point at the `finding_rows` docstring as the one statement of the floor rule. Under
that rule, a record the check cannot read or split gives one empty row per raw finding-level heading line. Both of
the spec's own sentences still state the rule in full beside the pointer. Scope item 1 says "The rule for both is the
docstring of `noninferiority.py#finding_rows`: one empty row for each raw line at the finding heading level, fenced
and commented lines included". *Data & interfaces* gives the condition and the count in full, then adds "as the
`noninferiority.py#finding_rows` docstring states". So the value stands in three places, and the spec names one of
them as the rule. The three agree today. The owner's direction binds this review:
`skills/writing-style/SKILL.md` §*에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* says a value stands in one
place, because otherwise one copy gets fixed and the reader has to choose between them. `CLAUDE.md` *The rule a
mechanism is kept against* says the same. This rule has moved three times in four rounds, so the next change is
likely to edit one copy. The spec's two sentences name the docstring as the authority, and the next reader would
then have to decide which copy wins.

The fix keeps *Data & interfaces* as the spec's one statement, since that section is the spec's place for a
function's contract. It drops the restatement from scope item 1. The docstring, which the code holds, stays. That
gives the spec one statement and one pointer, as plan row R3 already does by naming "the floor U4 sets".

```markdown
   refuses (`rounds/round-4.md`). What such a record gives is stated in
   *Data & interfaces*, under *The finding rows of a text*. Every such
   row is false, and no `truth-` grader over the record finds anything in
   that run. The count errs toward more false rows and
```

and in *Data & interfaces*, the closing pointer goes, since this section is the statement:

```markdown
`chain_check.py#FINDING_LEVEL`. An empty row matches no `truth-` pattern,
so `grade` finds no truth in such a run with no branch of its own.
```

answer:

## Confirmations

confirms: round-4#1
`finding_rows` (`evals/scripts/noninferiority.py:298-330`) now splits first and returns the floor where
`finding_spans` returns an error or `unclosed` refuses. The floor is one empty row per raw `FINDING_LEVEL` line. A
record with a `## Findings` section and no finding heading still gives no rows, because the split returns no error
for it (read). `test_a_record_the_check_cannot_split_counts_every_finding_false` holds both of round 4's shapes, a
second `## Findings` section and `## Findings (3)`. Each gives three empty false rows, and no truth passes even where
the eval recorded one. With the earlier reader cases, 14 passed under `bin/test` (executed). The plan row R3 that
round 4 named now reads "Chosen" with no limit left. The changelog states the rule for both kinds of record.

confirms: none
The rewritten frame sentences were read against the owner's three rules. Each sentence describes and orders nobody,
so the who-acts rule has nothing to apply to. No symbol stands in prose as syntax: the `#` and `:` sit inside code
identifiers and coordinates, as elsewhere in the tree. The one-value rule is finding 1. What each sentence states
matches the code at c64c8845 (read).

Carried from round 4 rather than re-established: the shapes `unclosed` refuses, and the behaviour of every record
the check accepts. The fix diff changes neither, since the condition only widens.

## Not judged

| What | Location | Who answers |
|---|---|---|
| `tests` run 39694379127 at c64c8845 | the branch | the orchestrator |
| The full suite, the repository-wide lint and the typecheck at c64c8845, labelled `unverified` here | the branch | the orchestrator, at its one broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist -k "cannot_split or cannot_read or never_closes or closed_fence or opener_inside or never_close_nested or fenced_fix or checks_split or shape_the_check_refuses or outside_every_finding"` in the scratch clone at c64c8845 | 14 passed, 119 deselected, exit 0 |
