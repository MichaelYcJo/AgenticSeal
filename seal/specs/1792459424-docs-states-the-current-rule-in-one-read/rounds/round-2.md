# 1792459424-docs-states-the-current-rule-in-one-read — review round 2

target: 93671fc2, fixes 75ac6203..93671fc2

## Findings

### 1. A check label behind a heading's `#`, a task box or a table cell's `|` is still neither read nor refused

severity: should
location: `.github/scripts/rules.py:58-65`, `skills/settle/SKILL.md:93-98`, `tests/test_the_rules_command_reads_each_rule_off_its_test.py:362`
evidence: executed `python3 -I probe/fixes.py <clone>`, `python3 -I probe/wider.py <clone>`, `bin/rules --check`
verdict: fixed 3b01852d
reopens: round-1#4

The close at bc260d09 does not hold for the whole class. Round 1's finding
named that class as a block marker in front of the label, and gave the
ordered-list number and the blockquote as its examples. The fix covers
exactly those two. Run against `NEAR` at 93671fc2, `1. check:`, `1) check:`,
`> check:`, `>> - check:` and `-check:` are all read and refused. Three
spellings of the same class still pass unread: `## check: tests/x.py` (a
heading's `#`), `- [ ] check: tests/x.py` (a task box) and
`| check: tests/x.py |` (a table cell). A check line written behind any of
them names a target nobody resolves. The code review skill says an
enumeration over an open set of spellings narrows a finding and does not
close it. So either the remaining markers are read, or the limit is stated
where the grammar is stated, and neither has happened. The wider pattern
below matches no shown line of any rule file that the current one misses
(`probe/wider.py`: "newly refused in the tree: 0"). `bin/rules --check`
still reads 240 lines and exits 0 at 93671fc2.

```python
NEAR = re.compile(
    r"^\s*(?:(?:[-+*]|[0-9]{1,9}[.)]|>|\[[ xX]\]|#{1,6}|\|)\s*)*[*_]*\s*"
    r"(?:checks?|enforced\s+by)\s*[*_]*\s*:",
    re.IGNORECASE,
)
```

The comment above it changes in the same edit, to: "any run of block
markers (a list bullet, an ordered-list number, a task box, a blockquote's
`>`, a heading's `#` or a table cell's `|`) or emphasis". In
`skills/settle/SKILL.md` *A rule has one shape*, the refused list reads "a
list bullet, an ordered-list number, a task box, a blockquote's `>`, a
heading's `#`, a table cell's `|` or emphasis in front". Three rows go into
`test_every_other_spelling_is_refused_at_its_line`:

```python
        (f"## check: {HELD}", f"`## check: {HELD}` is no check line: {EXPECTED}"),
        (f"- [ ] check: {HELD}", f"`- [ ] check: {HELD}` is no check line: {EXPECTED}"),
        (f"| check: {HELD} |", f"`| check: {HELD} |` is no check line: {EXPECTED}"),
```

Their ids are `"a heading marker"`, `"a task box"` and `"a table cell"`.
Each is seen red against bc260d09's pattern first. A heading row also ends
the walk's current heading in `shown_lines`, so the case checks that the
refusal names its own line. The changelog fragment's list follows the
skill's.

answer: holds, and is closed as a class rather than as three more markers, on the orchestrator's direction. `rules.py` keeps the markup in one constant, `BLOCK_MARK` (a heading's `#` run, a list bullet or number, a task box, a blockquote's `>`, a table's `|`), and `NEAR` refuses any line whose only content before the label is that markup, spaces or emphasis; only the exact shape is read. `skills/settle/SKILL.md` *A rule has one shape* states the class in one sentence instead of listing markers, and the changelog fragment follows. The round-1 rows for `1.` and `>` moved out of the spelling list into one parametrized case, `test_a_label_behind_block_markup_is_refused_at_its_line`, with `##`, `- [ ]` and `|`; each asserts a single refusal at line 6, so a heading row cannot move it. With the pattern at bc260d09 the three new shapes were red, and `mutation-check` reducing `BLOCK_MARK` to a bare bullet turned all five red. `bin/rules --check` reads 240 lines, exit 0, so no standing line is newly refused.

## Confirmations

confirms: round-1#1
The close at 0398a18b holds (executed). Re-run at 93671fc2,
`bin/test tests -q -p no:xdist -k test_the_durations_file_prices_the_suite`
reports 1 passed, 7287 deselected, exit 0. 0398a18b changes only
`.test_durations`, which the finding's `location:` names.

confirms: round-1#2
The close at ca5cf133 holds (executed, `probe/fixes.py`).
`rule_changes.py#parse` at 93671fc2 refuses a second `- nothing` at line 5,
both with an unknown field and with a clean `why:`, naming "`- nothing` is
the section's one item". At 75ac6203 the same bodies returned
`nothing='a'` with no error. A single block still reads `nothing='a'`. A
block beside an operation is still refused at the operation's line, in
either order. A bad item still fails first at its own line. The new case
`test_a_second_block_is_refused_at_its_own_line` finds the second block by
its index, not by its text, so it pins the line. The answer explains why it
is a function rather than a row of the parametrized list, and that holds
(read, `tests/test_settle_applies_rule_changes_in_place.py:249-260`).

confirms: round-1#3
The close at c283eb3d holds (read, `docs/one-root-by-lifetime.md:33`,
`docs/one-root-by-lifetime.md:48`, `docs/one-root-by-lifetime.ko.md:33`,
`docs/one-root-by-lifetime.ko.md:46`). All four name the line a round
record opens with, `target:`. The class sweep also stands (executed): `git grep` for
`Target SHA` within 30 characters of "round" now finds only
`templates/seal-README.md:94`, which is lowercase prose in a tree drawing
that #940's scope covers. The two test comments the fix pass found were
corrected in the same commit. `tests/test_both_editions_carry_the_same_folds.py`
and `tests/test_docs_line_wrap.py` pass.

confirms: round-1#5
The close at 027ea445 holds (executed). `git grep -nE '#[0-9]+'` over `docs/`
outside `docs/experiments/` finds only `#51`, the live log the rule
describes, and the `Closes #N` syntax examples. The sentence about the
original design being kept stands without the number
(`docs/issues-and-milestones.md:301-304`).

confirms: none
The new units read as code. The widened `NEAR` nests `\s*` inside a starred
group. Every pass of that group consumes at least one marker character, so a
long run of marker characters costs polynomial time, never exponential. The
reader check `reader != reader.strip()` refuses a leading space more and a
tab. A trailing space never reaches it, because `check_lines` strips the
line first. The `parse` change keeps the order of refusals: an item outside
the grammar is still named before the one-item rule (executed,
`probe/fixes.py`). Ruff check and format pass on the six Python files the
fix range touched. The four changed test modules and the two docs modules
pass: 227 passed (executed).

confirms: none
93671fc2 replaces the list of refused spellings in S5 with a pointer to
`skills/settle/SKILL.md` *A rule has one shape*. That leaves one statement
of the list, which the fix commits extended. The scenario's verification
column, one case per spelling seen red, is unchanged. This describes the
build and does not bend the frame (read,
`seal/specs/1792459424-docs-states-the-current-rule-in-one-read/spec.md:115`).

confirms: none
No rule an agent needs is lost from the release and tracker group
(`docs/branch-and-release.md`, `docs/release-checklist.md`,
`docs/issues-and-milestones.md`), the runs, broad gate and pact group
(`docs/measuring-a-run.md`, `docs/the-broad-gate.md`, `docs/the-pact.md`)
or the review and records group (`docs/the-review-record.md`,
`docs/the-record-layout.md`, `docs/the-reader-registry.md`,
`docs/the-agent-set.md`). Two probes were read against the base text at
ac83bdf3 (executed, `probe/leads.py` and `probe/sentences.py`). The first
takes each bold-opened rule paragraph at base whose lead is absent at HEAD.
The second takes each base sentence carrying a normative word whose
content words are mostly absent from every HEAD paragraph of the same
document. Seven leads were missing in the release and tracker group, and
every one is reworded in place. The two rulesets stand at
`docs/branch-and-release.md:171`, the release-preparation branch at `:184`
and `docs/release-checklist.md:46`, and the missing formal closing link at
`docs/branch-and-release.md:266`. An unclaimed issue refusing the release
stands at `docs/issues-and-milestones.md:213`. The rest were history: "used
to", "this section used to stop here". The other two groups lost no lead.
Of their sentence candidates, the fold-marker wrap exemption left with the
markers under `## Removes`. The contract's numbering rule lives in
`skills/agent-contract/SKILL.md`, which `docs/the-agent-set.md` links. The
remaining candidates stand reworded in the same document (`one table, one
shape` at `docs/measuring-a-run.md:35`, `fits one read` at
`docs/the-record-layout.md:25`). The same probes over the commit gate
group and the guard flagged only reader mechanics and their measurements.
Their rules stand: the token rule at `docs/worktree-guard-spec.md:418`, the
exact `git` word at `:273`, the choice marker at `:252`, and "two answers,
not three" and "no standing waiver" at
`docs/the-review-and-parity-arms.md:73` and `:82`.

confirms: none
The history left in the three groups is either grounds that a test names
as deliberate, or the fact a limit rests on. "The release that shipped the
framer" and "the release that replaced the deleted checklist with a gate"
(`docs/issues-and-milestones.md:25-30`) are pinned as deliberate by
`tests/test_a_release_is_sized_by_a_criterion.py#test_the_two_releases_are_cited_without_a_version_number`.
"Through 0.18.x a signer was called a signatory" (`docs/the-pact.md:21`)
names the old header that `pact-check` still reads. The rest are the dated
reading behind the directory listing's limit
(`docs/release-checklist.md:276`) and the screenshot behind the stamp's
limit (`docs/the-review-record.md:399`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at 93671fc2: `unverified` | the branch | the orchestrator, at `broad-gate` once the rounds settle |
| Cross-platform run 39370135810 at 93671fc2, which this round did not read | CI | the orchestrator |
| Whether "two hook processes racing for one record" is behaviour the tree cannot observe, carried from round 1 unanswered | `docs/commit-review-gate-spec.md`, the backlog row closed on *Registration* | the framer, through the orchestrator |
| A rule stated without a bold lead or a normative word, which neither probe reads; the documents were not read whole line against line | the ten documents of the three groups | the sealer, where it samples `docs/` |

## Probes

| Command | Result |
|---|---|
| `python3 -I probe/fixes.py <clone>` (the parsers at 75ac6203 and at HEAD, loaded from git in memory) | `parse`: a second block refused at line 5 at HEAD, passed at 75ac6203; `NEAR` at HEAD reads ordered-list, blockquote and bare-dash spellings; `## check:`, `- [ ] check:` and `\| check: \|` still not read |
| `python3 -I probe/wider.py <clone>` | the wider pattern reads the three remaining spellings; newly refused in the tree: 0 |
| `bin/rules --check` | exit 0, all 240 check lines in 61 rule files hold |
| `bin/test` over the four changed test modules and the two docs modules | 227 passed |
| `bin/test tests -q -p no:xdist -k test_the_durations_file_prices_the_suite` | 1 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over the six changed Python files | all checks passed, 6 files already formatted |
| `python3 -I probe/leads.py` and `probe/sentences.py` over the three groups, then over the commit gate group and the guard | release group: 7 leads reworded in place; the other two groups: 0 leads missing, 4 sentence candidates, all accounted for |
