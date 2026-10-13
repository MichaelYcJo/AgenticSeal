# 1791852615-whether-a-ledger-line-is-live-has-seven-rules — review round 1

| Field | Value |
|---|---|
| Target SHA | f8c96c3be0965760a9fd053dfb93bbd29ca007cd |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #918 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `9b5239c6ded482c279f11e28f32479f3289f277a..e224390fb4ad6438dc3c2eaf658c68344ff127d7`, 1 commit |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1, 🟡 2 and 🟡 3: the statement's excusing headline, the statement's account of how the rider check parts from the checker, and the two `passed` direction words in the holding group. |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 1 of #872, target f8c96c3b against `origin/release/v0.21.1` at 321e9de1, over the whole build, phases 1–3. The reviewer was asked to judge the smith's divergences — `hidden_lines`' direction stated as it behaves, the corpus grown from six shapes to eight, three declarations changed from the frame's proposals, the W1 and W2 ledger rows reshaped after MALFORMED, a surviving mutation on the rider's `and not walked.uncertain[index]` left in Not verified — to check every `Reads:` line against its unit's code, and to hold the statement in `docs/the-evidence-ledger.md` against each of the seven readers.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | the excusing bullet's headline "is not taken on doubt" and its sentence "nothing is excused or declared by a line nobody wrote live" are false for `hidden_lines` on a row below a comment opener nobody closed, which the same bullet says it declares and the table pins as read | `docs/the-evidence-ledger.md:629` | **fixed** `e224390f` | fixed at e224390f; read: the bullet at lines 629 to 640; `hooks/blocks.py:366` makes the line uncertain; the table pins `read` at `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:202` |
| 🟡 2 | the statement names one shape on which the rider check parts from the checker; they part on three, and on a closed fence below a fence nobody closed the rider does not read, against line 615's "a fence nobody closed is a malformed file whose lines are read" | `docs/the-evidence-ledger.md:625` | **fixed** `e224390f` | fixed at e224390f; executed: the probe on two added shapes (rider reads and checker skips; checker reads and rider skips); read: `hooks/blocks.py:321`; `overview.md:24` carries the same narrow claim |
| 🟡 3 | the checker's `quoted_lines` and `claim_lines` declare `unknown passed` while the rider check's `quoted_lines` and `anchored_rows` declare `unknown refused` for the same answer on doubt; both `passed` units' own consequence sentences name a refusal | `skills/evidence-check/scripts/evidence_check.py:370` | **fixed** `e224390f` | fixed at e224390f; read: the four `Reads:` lines and their sentences; `docs/the-reader-registry.md` §*The four classes* reads direction at the decision; inventory rows E9 and E58 against S9 |
| ⬜ 4 | one `BY_BIAS` cell (`hidden_lines` on a mid-line comment) is answered by the docstring itself, and its label's reason, "where the walk is unsure", does not hold: the walk is sure of that line | `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:222` | open | executed: the walk returns `live`, `uncertain=False`, on that line; the cell's answer is right; "four cells" also appears in W1, Q4 and phase 1 |
| ⬜ 5 | `overview.md`'s first `Not verified` row can be answered from the code: the walk cannot return `fence` and uncertain together, so the surviving mutation is equivalent | `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/overview.md:31` | open | read: `hooks/blocks.py:321`, `:340` to `:368`, `:424` to `:428`; executed: fuzz, 0 lines in 200,000 texts |
| 🟢 | the seven census lines are gone, and each of the seven units carries one `Reads:` line in the grammar and one consequence sentence | `tests/undeclared_readers.txt` | confirmed | read: the diff, all seven lines; the census test is the orchestrator's executed run at `f8c96c3b` |
| 🟢 | `mixed` for `live_lines`, `hidden_lines` and `readable` holds when read through each unit's callers | `skills/verify/scripts/unverified_check.py:744` | confirmed | read: `live_lines` callers in settle, fold_check, survivor_check, gather_changelog and fold_ledger; `hidden_lines` callers at `hooks/config.py:176` and `broad_gate.py:976`; `readable` callers in chain_check, round_record, release_seal, survivor_check, broad_gate and the review-history guard |
| 🟢 | the corpus grown to eight shapes is what makes the `live_lines` mutation and the two `quoted_lines` visible | `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:79` | confirmed | executed: the two-space fence, checker not read and rider read |
| 🟢 | W1 and W2 reshaped after MALFORMED: W1 holds its two tests alone, and W2 holds the seven units | `seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md` | confirmed | read: the fragment; `evidence-check --strict .` exit 0 is the orchestrator's executed run; W2's direction words follow 🟡 3 |
| 🟢 | no released ledger file changed | `seal/releases` | confirmed | executed: `git diff --stat 321e9de1 f8c96c3b -- seal/releases seal/ledger.md` printed nothing |

## Paste-ready fixes

```markdown
- **A line that EXCUSES or DECLARES something — a fold marker, a
  `seal/config.md` row, a `routing.md` row — is not taken on doubt, except
  where a declaring reader keeps an older reading that took it.**
  `unverified_check.py#live_lines` parks a line inside any fence or comment,
  closed or not, and a line its two span readings disagree about.
  `hooks/config.py#hidden_lines` keeps, wherever its walk is unsure, the
  fence-only reading it gave before #667: a row below a fence nobody closed
  declares nothing, and a row below a comment opener nobody closed still
  declares, because that reading never hid one and work item 1790645290 was
  bound to miss no row the older reading saw. That row is the one place a
  line nobody wrote live declares something; everywhere else, what this
  protects is that nothing is excused or declared by a line nobody wrote
  live. The wrong answer is a fold reported as a deletion at exit 1, a
  fragment the sweep keeps, a hook that says nothing, or a gate that asks.
```
```markdown
  The rider check reads by `hooks/blocks.py#walk` rather than by the
  delimiter rule, and parts from the checker three ways: it reads a fence
  its walk is not sure of, one opened at one to three spaces, which the
  delimiter rule closes, because a rider the walk cannot place is read as it
  was before the walk; it reads a fence inside a line-start comment that
  closes, which a renderer shows as comment text; and it skips a fence that
  closes below a fence nobody closed, which a renderer hides either way.
```
```markdown
| Whether the checker's and the rider check's `quoted_lines` differ | `plan.md` §*Alternatives considered*: "a difference measured at zero rows" / they differ on three shapes: a fence opened at one to three spaces, a fence inside a closed line-start comment, and a closed fence below a fence nobody closed | both, scoped | The zero is about the released ledgers, which carry no fence line (P2-3), and it holds there. On markdown in general they differ, and the table pins the difference |
```
```python
    Reads: guess — a markdown file's lines, a ledger's or any `.md` file an anchor names, by the shared fence rule; unknown refused
```
```python
    Reads: guess — a record's lines, a session's prose in the records' template shape; unknown refused
```
```markdown
`refused` for the checker's two, `anchored_rows` and the rider check's, `mixed` for the other three
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` on `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`, `tests/test_a_folded_statement_names_what_enforces_it.py` and `tests/test_docs_line_wrap.py` with `-q` and `SPECSEAL_CASE_CEILING_S=600`, in the clone at `f8c96c3b` | exit 0, 131 passed |
| `bin/fold-check --root .` in the clone | exit 0: 186 statements in 19 documents, 0 over the 1000-line ceiling; `docs/the-evidence-ledger.md` is 702 lines |
| `git diff --stat 321e9de1 f8c96c3b -- seal/releases seal/ledger.md` | empty |
| one test_tmp probe script, run once with `python3 -I` against the clone's modules, then deleted: four shapes asked of all seven readers and of the walk, and a seeded fuzz of 200,000 texts through `walk` and `walk_text` | inner closed fence below an unclosed `~~~~`: checker read, rider not read, walk `fence` and certain. Fence inside a closed comment: checker not read, rider read. Mid-line comment: walk `live`, `uncertain=False`. Two-space fence: checker not read, rider read. Fuzz: 0 lines both `fence` and uncertain |
| the broad gate: full suite, repository lint, typecheck | not yet. It belongs to the sealer, once the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
