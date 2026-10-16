# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — review round 10

target: 555d1c06, fixes 0c16e9bb..555d1c06

A verifying round over round 9's fix pass (cacbf43c, 229cad2f, ae548748,
480bf163, e8c6b7ec) and the framer's spec sync (304db5d8, 555d1c06). Under
the cap rule the fix pass shipped, the count runs from phase 5d-v, approved
after round 8, so this is the second round of that count and carries no
extension line. Round 9's fix pass answered no regression, so this round
is an ordinary verifying round.

All four closes hold, and this round opens nothing. Each fix states the
rule its finding asked for in every carrier the finding named, and the
carriers the finding did not name were searched for the same sentence.
Each new or widened pin was red against the texts before the fix (probe 2
below). The spec sync brings the five `spec.md` places the two new
`overview.md` rows name into line, and the two docs checks the framer did
not run pass over the tree.

Findings from reading and from execution are labelled in each entry. The
full suite was not run. It is `unverified`, and the sealer answers it.

## Findings

This round opens nothing that needs a fix.

## Confirmations

confirms: round-9#1
The trigger sentence now asks who made the defect. In
`docs/the-review-record.md:268-294` a finding takes its regression line
only where a fix pass's own commits added or changed its unit "and those
commits introduced its defect", and a `fixed` commit that left the defect
standing, in the unit that commit changed or in another, takes a reopens
line. `agents/warden.md:136-150` and `templates/sdd-round.md:51-59` say the
same, and the template's regression comment now sends the left-standing
case to `reopens:` in so many words. The carriers the answer called
already keyed on the defect's origin were read and are:
`docs/the-review-record.md:70-77` and `:236-243`,
`skills/code-review/SKILL.md:187-192`, `agents/warden.md:116-124` and
`:219-225`, the orchestration's `Job` row at
`skills/code-review/orchestration.md:96`, and
`skills/code-review/scripts/chain_check.py:167-171`. A search of the tree
outside the work items for "added or changed" and "did not fix it" finds
no other trigger sentence. The work item's `changelog.md:11-14` states the
split the same way. `spec.md` S9, its `warden` row and the relations
sentence of §*What a round records* were brought into line at 304db5d8;
the rows that keep "a `fixed` commit that did not fix it", the grounding
row on round 8 and the `Fix of a fix` row, give that case `reopens:` and
never `regression:`, so they do not reopen the conflict. The pin
`tests/test_the_rules_have_one_owner.py::test_a_regression_is_a_defect_a_fix_passs_own_commit_made`
holds the document, the warden and the template to both phrases.
read: the coordinates above at 555d1c06. executed: the pin in the module
run, and red against the pre-fix texts (probe 2).

confirms: round-9#2
The cap counts from the last design change, and both routes a regression
takes now have a round to go on to. `docs/the-review-record.md:246-266`
states the owner's three rulings as `phases/phase-5d.md` §*Round 9 fix
pass* records them: the count starts again at the first finding round that
reviews a reframe or a new phase the owner approved; a regression routed to
a fix pass is followed by one verifying round, whatever the count, that is
not an extension; and the loop guard stands, with what else that round
leaves open past the cap taking the ladder. The extension line's example
names where the count started. The same rule stands in
`templates/sdd-round.md:23-29`, `skills/code-review/orchestration.md:108-113`
and the redesign row at `:155`, `README.md:90-95`, `README.ko.md:78-83` and
`agents/framer.md:310-313`, where round N is now the record whose
regression was routed to the framer. The remaining mentions of the cap,
`skills/verify/SKILL.md:387`, `agents/smith.md:281`, `agents/warden.md:152-155`
and `skills/implement/orchestration.md:636`, point at §*The run* or state
what still holds. The `spec.md` places `overview.md`'s row *Where the round
cap counts from* names, the cap row of §*What leaves, what stays*, S26 and
§*Data & interfaces*, now say the same; S9 and S27 state no cap. The pin
`tests/test_the_rules_have_one_owner.py::test_the_cap_counts_from_the_last_design_change`
holds the document, the orchestration, both READMEs, the template and the
framer, and `bin/rules --check` resolves its new `Enforced by:` target.
Round 9's own extension line, written under the old rule, stays as the fix
pass left it, since a fix pass writes only the verdict, answer and location
lines; `phases/phase-5d.md` §*Round 9 fix pass* says why it was not
needed. read: the coordinates above at 555d1c06. executed: the pin in the
module run, red against the pre-fix texts (probe 2), and `bin/rules --check`.

confirms: round-9#3
The run-end sentence names both of the check's conditions.
`skills/code-review/orchestration.md:125-132` ends the run only on a round
whose record holds no `open`, `fixed` or `rejected` finding and whose
target commit is HEAD or is followed only by the work item's own records,
as `docs/the-review-record.md:164-171` states the check, and adds that a
fix committed after that round, a first-rung fix at the cap among them, is
followed by one more verifying round. T44,
`tests/test_the_rules_have_one_owner.py::test_a_close_that_does_not_hold_reopens_it`,
now holds the section to the second condition, and its first phrase stays
contiguous. `spec.md` S26 already named both conditions and still does.
read: the coordinates above at 555d1c06. executed: T44 in the module run,
and red against the pre-fix sentence (probe 2).

confirms: round-9#4
A bare reference line is read as its label and refused at its line.
`skills/code-review/scripts/chain_check.py:111-114` takes the value of
both reference labels as optional, as the confirms and target patterns
already did, and `finding_of`'s `one()` at `:813-817` reads a missing
value as empty (`:813-818`), so `reference_of` and `reopened_of` refuse
it by line. The verdict and location patterns keep their required space:
a bare line of either reads as no such line, which `one()` refuses because
both are required, so the class has no other member. The only callers of
the two patterns are `finding_of`'s two calls at `:857-858`, so no reader
meets a value of `None`. The case
`tests/test_chain_check.py::TestFindings::test_a_reference_label_with_nothing_after_it_is_refused`
pins the line and that the refusal names the label. executed: the case in
the module run, and red against the pre-fix reader (probe 2). Probe 1
reached the edges the case does not: a bare regression line before or
after a reopens line is refused for its empty value and then at the second
of the two lines as a finding holding both, which is what `spec.md` S24
and its relations sentence state; two bare reopens lines are refused as
two; a bare line inside a fence is no line; a bare reopens line under
`## Confirmations` is refused as out of place; one with trailing spaces is
refused by line; and in a pair of records a bare reopens line on round 2
leaves round 1's `fixed` finding refused as unnamed.

confirms: none
The spec sync matches the fix pass. 304db5d8 rewrites S9, S24, S26, the
`warden` row, the relations sentence of §*What a round records*, the cap
row of §*What leaves, what stays* and §*Data & interfaces*' extension line,
and each now states what the fix pass built; 555d1c06 marks the two
`overview.md` rows' sentences brought into line, and the commit each row
names is the one that changed them. read: `git diff 0c16e9bb..555d1c06` of
`spec.md` and `overview.md`. executed: `tests/test_docs_line_wrap.py` and
`tests/test_no_passage_is_pasted_into_a_second_file.py` over the tree,
exit 0.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The single-carrier mutations the fix pass's answers report from `mutation-check`. This round reverted all of a fix's carriers at once instead (probe 2), which shows each pin can fail but not that each carrier is held alone | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/rounds/round-9.md:109`, `:184`, `:219`, `:299` | the sealer, if it samples them |
| The full suite | the tree at 555d1c06 | the sealer |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the worktree into `<scratchpad>/923-r10/clone`, checked out at 555d1c06, with `origin/release/v0.22.0` fetched from the worktree | every run below ran there. The worktree was only read, apart from this file |
| probe 1: `python3 -I <scratchpad>/923-r10/test_tmp_r10_bare.py <clone>`, `findings` over a round-2 record per edge, `round_of` and `channel` over a pair | exit 0. A bare regression line beside `reopens: round-1#1`, before or after it: refused at its own line for the empty value, and at the second line as holding both. Both lines bare: three refusals by line. Two bare reopens lines: refused as two. A bare line in the fix fence: read as no line. A bare reopens line under `## Confirmations`: refused as out of place. Trailing spaces: refused by line. The pair: round 2's bare line refused, and round 1's `fixed` finding refused as unnamed. The file was deleted |
| probe 2: `git checkout 0c16e9bb --` of the eight files the fix pass changed outside `tests/` and `seal/specs/`, then each of the four new or widened pins alone with `bin/test <case> -q -p no:xdist`, then `git checkout 555d1c06 -- .` | each exit 1, 1 failed: the bare reopens line read into a finding; the document lacks "those commits introduced"; the orchestration lacks the second condition; §*The run* lacks "counted from the last design change". `git status --short` was empty after the restore |
| `bin/test tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py -q` | exit 0, 45 passed |
| `bin/test tests/test_chain_check.py tests/test_the_rules_have_one_owner.py tests/test_chain_hooks_hardening.py::test_the_cycle_is_bounded_and_ends_at_a_pull_request -q` | exit 0, 73 passed |
| `bin/rules --check --root <clone>` | exit 0: all 429 `Enforced by:` targets in 60 rule files resolve |
| `chain_check.py --baseline origin/release/v0.22.0 --root <clone>`, before this file | exit 0. The pull request's state is unknown, so nothing was judged as ready. Owed: a verifying round for round 9's four `fixed` findings and for cacbf43c after its target, and `broad-gate.md` and `guarantee.md`, the sealer's |
| this file committed in the clone by a Python `subprocess` call, then `chain_check.py --baseline origin/release/v0.22.0 --root <clone>` and `--worktree`; `bin/test tests/test_no_real_identifiers.py tests/test_docs_line_wrap.py tests/test_one_word_one_meaning.py -q`; an emoji scan of the file | exit 0 for both: round 9's four findings and cacbf43c no longer owe a round, nothing in this record's shape is refused, and only `broad-gate.md` and `guarantee.md` are owed, to the sealer. Tests exit 0, 64 passed. No emoji character |
| the full suite | not run: `unverified`, the sealer's |
