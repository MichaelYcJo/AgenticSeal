# 1792129100-the-mechanics-leave-before-the-agents-are-rewritten — review round 2

target: d59f8a4b, fixes 46bc215c..d59f8a4b

The verifying round on round 1's fix pass: six commits, cfd687b7, 046dee6e,
eb568983, bbdd408c, ef27f327 and d59f8a4b, read in a `git clone --no-local`
of the checkout at d59f8a4b. Round 1's coordinates were carried; every
verdict below was re-derived from the fix diff and the tree.

Seven of the eight closes hold. Finding 1 below reopens round 1's finding 2.
The fix pass refused every table count the check cannot keep for the rows
the check reads a meaning from. It left out one more member of the same
class, and its own answer named it: a label placed in `## Confirmations` at
`one`. The document the fix rewrote now promises exit 2 for that table, and
the check loads it.

The points the fix pass raised for this round are judged in the
confirmations: (a) under round-1#1, (c) under round-1#7, (d) under
round-1#3, (e) under round-1#6. Point (b) is finding 1.

The narrow modules named in the probes were run. The full suite was not run
by this round: it is `unverified` here, and the sealer answers it. Round 1's
three `Not judged` rows for #957 stand as written.

## Findings

### 1. A label placed in `## Confirmations` at `one` still loads, and a record with no such section passes without the line

severity: should
location: `skills/code-review/scripts/chain_check.py:137-148`, `skills/code-review/scripts/chain_check.py:336-353`, `docs/the-review-record.md:63-71`, `seal/specs/1792129100-the-mechanics-leave-before-the-agents-are-rewritten/changelog.md:24-27`, `tests/test_chain_check.py:597-602`
verdict: fixed 6597fe14
reopens: round-1#2

Why the close does not hold. Round 1's finding 2 was a class: a table whose
`How many` the check cannot keep loads, and the record then passes on a
reading the table did not mean. 046dee6e refuses that only for rows in
`READ_ROWS`, because the `HONOURED` test sits inside the
`for key, parts in READ_ROWS.items():` loop (`chain_check.py:336-353`). The
cause it names for `## Confirmations` is that `confirmations` returns
`[], []` for a record with no such section (`chain_check.py:1206-1207`), so
no line placed there is counted. That cause holds for every row whose
`Where` is `## Confirmations`, not only for `confirms:`. A new label placed
there at `one` loads, and a record with the section left out passes with
the line missing. The fix pass's answer says so ("Not closed"), with the
ground that no such row exists. Round 1's finding stood on the same
ground: no `verdict:` row read `any` either. The finding was about the
`docs/` rewrite #941 plans.

The document now promises more than the code does. `docs/the-review-record.md:63-71`,
rewritten by 046dee6e, says a row "whose `How many` the check cannot keep"
stops the check at exit 2. The changelog sentence written for it in
bbdd408c (`changelog.md:24-27`) says the check stops where "a row's
`How many` allows more than the check can read". For both `## Confirmations`
cases the opposite is true. `one` requires more than the check counts, so
the sentence does not describe two of the eight tables 046dee6e refuses.

Executed (probe Q1). A copy of `chain_check.py`, `unverified_check.py` and
`docs/the-review-record.md` laid out as the plugin lays them out, with one
row added after `confirms:`,
`` | `signed:` | `signed: .+` | `## Confirmations` | one | a signature is prose | ``,
imports with no GrammarError. `round_of` on a record with no
`## Confirmations` section and no `signed:` line returns no error. The same
record with the section present and no `signed:` line is refused, "no
`signed:` line: `## Confirmations` carries one". So the reader counts the
row only where the section stands.

Read. Two repairs are open, and they are at different depths. `confirmations`
could count every row against no lines where the section is absent, which
would honour `one` and make the two `## Confirmations` entries of
`HONOURED` unnecessary. Or the loader could refuse the table, which is the
shape 046dee6e and the document chose. The paste follows the second, so the
document's sentence becomes true as written.

```python
# skills/code-review/scripts/chain_check.py, grammar(), after the
# `for key, parts in READ_ROWS.items():` loop and before `return rows`:
    for key, row in rows.items():
        if row.where == IN_CONFIRMATIONS and row.many == ONE:
            raise refuse(
                f"the `{key}` row's `How many` is `{ONE}`, and the check counts "
                f"nothing in a `{CONFIRMATIONS_HEADING}` that is absent"
            )
```

```python
# tests/test_chain_check.py, a row of the parametrize list of
# test_a_document_the_check_cannot_read_is_exit_2_naming_it, after the
# `confirms:` row at :597-602:
            (
                row_of("confirms:"),
                row_of("confirms:")
                + "| `signed:` | `signed: .+` | `## Confirmations` | one | x |\n",
                "`signed:` row's `How many` is `one`",
            ),
```

```markdown
docs/the-review-record.md:69-70, the sentence's end:

counts nothing in a `## Confirmations` that is absent, so that row is
`at most one` and no row placed in it is `one`.

changelog.md:24-27:

  this release's check. Where the table itself cannot be read, because the
  document is missing, a row will not parse or a row's `How many` is one
  the check cannot keep, `chain_check.py` stops with exit 2 naming the
  file, never a pass.
```

answer: fixed for the class, by the first of the two repairs this record names rather than the paste. Enumerated by construction from what `grammar_row` admits: the two sections in `the record` at `one` or `at most one`, the heading in `## Findings` at `each number once`, an old spelling `nowhere` at `none`, and a label in each of three places (outside every finding, a finding, `## Confirmations`) at each of `one`, `at most one` and `any`, 13 combinations. Twelve were kept by their place's reader already: `finding_spans` refuses a missing `## Findings` at `one` and a second at either, `findings` refuses a heading number twice, `misspelt` refuses every line of an old spelling, `record_lines` counts a label outside the findings over the whole record, and `finding_of` counts one per finding. The thirteenth reader was `confirmations`, which counted nothing when the section was absent. It now refuses a missing section the table says is `one` and counts each row placed there against no lines, so every label in `## Confirmations` at `one`, `signed:` among them, is refused where a record leaves the section out. A refusal at load was the other way; it would have forbidden `one` for every row there whatever a later table means. The refusal at load stays only for the rows the check reads a meaning from, where the reader is the limit and not the place: `READ_ROWS` now gives each its place and the counts kept (`target:` outside every finding at `one`; `location:` and `verdict:` in a finding at `one`; `regression:` and `reopens:` in a finding at `one` or `at most one`, since one line's value is read; `confirms:` in `## Confirmations` at any count; the sections and heading as `grammar_row` already holds them), `HONOURED` leaves, and a read row moved elsewhere is refused too. That was the same class at the place axis: probed once at 8de484b4, a table with `verdict:` outside every finding loaded and left `finding_of` no verdict, and one with `target:` in a finding loaded and raised `KeyError` in `round_of`. `docs/the-review-record.md` and the changelog fragment say both rules in the same commit. Executed: five new cases red at 8de484b4 (5 failed: three DID NOT RAISE GrammarError for the moved rows, the section at `one` refused at load by `HONOURED`, the `signed:` row at `one` passing with no error), then `bin/test tests/test_chain_check.py -q` 78 passed, exit 0; `mutation-check` red for each of the place refusal, the count refusal, the absent section's refusal and the absent section's row count; 52 modules reading the check or the document, 2831 passed, 8 skipped, exit 0; `bin/rules --check` exit 0, 416 targets.

## Confirmations

confirms: round-1#1
Point (a) holds. Round 1 asked that the convention stay and the exception
be stated where a person writes the row, and bbdd408c does that.
`templates/sdd-overview.md:41-46`, `skills/implement/SKILL.md:462-465` and
the docstring at `skills/verify/scripts/unverified_check.py:50-53` each name
an open item whose own text begins with `closed`, and none still says
"always". The template keeps it inside the section's comment, beside the
existing indented example, so a copied overview reads no new row. The
paste's `CLOSED_ROW_CASES` row was rightly left out. Read: "the word and the
item" (`tests/test_unverified_rows_close.py:100-103`) takes the same reader
path. The new test asserts the reader's reading of
`| closed issues are not re-read | the owner |` next to the three texts,
which pins the behaviour as well. Executed:
`tests/test_unverified_rows_close.py` passed in probe T1.
`git grep` for `always "still open"` over `tests`, `evals`, `skills`,
`docs` and `templates` finds only the new test's negative assertion.

confirms: round-1#3
The trailing-word sentence is gone from the fragment. Its "two things now
refused" is true of the base. Read: at d426fbdb `chain_check.py:98-108`
names `severity:` and `answer:` among `FINDING_LABELS`. The docstring at
`:722` says "Nothing of a `severity:` or an `answer:` value is read", and
nothing there counts either line. So no line, two lines and a value
outside `must` or `should` are all new. Point (d) is no defect. The exit-2
clause landed in bbdd408c with the rest of this paragraph, which is the
commit this finding's verdict names. Neither the grammar nor the fix pass's
rule asks for a changelog line in the commit of the fix it describes. What
that clause says is wrong for two cases, and finding 1 above carries it.

confirms: round-1#4
The paragraph tells a plugin user that the hygiene step reads every
`overview.md` under `seal/specs/` until `settle` retires it. It also tells
them to rewrite every closed row still on the old mark before moving the
pin. Read: `templates/hygiene.yml:77-78` runs `unverified_check.py` with
`--baseline` over `seal/specs/` whole. Executed:
`unverified_check.py --baseline d426fbdb seal/specs/` in the clone exits 0.

confirms: round-1#5
`record_target` is gone, and no name in `tests`, `evals`, `skills`, `docs`,
`templates`, `agents`, `.github`, `hooks` or `bin` still calls it.
`read_whole` (`chain_check.py:1166-1178`) runs `readable` once and keeps the
`record_lines` match of every row outside the findings. `round_of`
(`:1232-1246`) takes the target from that match instead of matching the line
again. The order of errors is the old one, `unclosed`'s, then `findings`',
then the outside rows'. Read: `TestRecordTarget` now reads the target
through `round_of`, so each of its cases also asserts that the rest of the
fixture record is clean. That is stricter than before, not looser.
Executed: `tests/test_chain_check.py` passed in probe T1.

confirms: round-1#6
`section_end` has one definition (`chain_check.py:234-242`), and `grammar`
calls it. Read: the old inline loop took the level without `or 1`. The
heading it starts from is the one `reader.headings` found, so the level is
never None there. `finding_of`'s count now goes through `counted`. The
heading lead, the line (`first + 1`) and both sentences match the removed
copy byte for byte, with `PLACED[IN_FINDING]` supplying "and with no
emphasis". There is one side effect. `no_record_line` now takes the scope,
so a missing line of a row placed in `## Confirmations` reads
"`## Confirmations` carries one" where it read "a round record carries
one". Only a `## Confirmations` row at `one` reaches it, which finding 1's
fix makes unreachable. Point (e), recounted with
`git show <sha>:skills/code-review/scripts/chain_check.py | wc -l`: 1,854 at
46bc215c, 1,869 at 046dee6e and 1,852 at eb568983 and at d59f8a4b. So
finding 2's refusal added 15 lines and findings 5 to 7 removed 17. Round
1's "about 40 lines" was an estimate, and the tree is 2 lines shorter than
the target round 1 read. That number backs no claim in any record of this
item: the handoff's 1,597 and 1,850 are phase 3's and still true.

confirms: round-1#7
`SHARED_READER` is the one reader `main` (`chain_check.py:1749`),
`replay_targets.py#record_reader`, `broad_gate.py#rounds_rows` and
`release_seal.py#readers` use. Read: no other file loads `chain_check.py`.
The other loaders of `unverified_check.py`, `gather_changelog.py`,
`issue_claims_check.py`, `settle.py`, `fold_check.py`, `coordinates.py` and
`payload_meter.py`, do not import the check, so they are outside the class.
In `rounds_rows` a reader missing beside the check is still a `Refused`: the
check's import raises `OSError`, and `broad_gate.py#load` turns any
`Exception` into one. Point (c) is no finding. The message at `:1753` now
fires only for `hooks/routing.py`, and it fired for it at the base as well
(d426fbdb `chain_check.py:1597-1600`). `hooks/routing.py`'s docstring opens
"Shared reader:". Executed (probe Q2): a copy with its reader and table and
no `hooks/` exits 2 with that sentence, and the `OSError` it quotes names
`hooks/routing.py`. So the reader learns which file is missing.

confirms: round-1#8
The handoff names the author address by where the clone pins it.
`tests/test_no_real_identifiers.py` passed in probe T1. Read, not
executed: `gh run view 38984051602` reports the tests workflow `completed`,
`success`, at d59f8a4b. That is the run the overview's open row at
`overview.md:54` waits on, and closing that row is the orchestrator's.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, repository-wide lint and typecheck at d59f8a4b: `unverified` in this round | the whole tree | the sealer, through `broad-gate` after the rounds settle |
| Whether run 38984051602 closes the overview's open row for the whole suite on three legs at the fix pass's HEAD; this round read its status and not its legs | `seal/specs/1792129100-the-mechanics-leave-before-the-agents-are-rewritten/overview.md:54` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| T1 `bin/test tests/test_chain_check.py tests/test_unverified_rows_close.py tests/test_a_script_copied_alone_exits_2.py tests/test_the_changelog_is_gathered_at_release.py tests/test_no_real_identifiers.py tests/test_the_record_is_written_in_words.py -q`, in the clone | 368 passed, exit 0 |
| `python3 skills/verify/scripts/unverified_check.py --baseline d426fbdb seal/specs/`, in the clone | exit 0 |
| Q1 to Q3, one probe file `<scratchpad>/<item>/round-2/test_tmp_probe.py` run once with `python3 -I` and deleted, copying the clone's `chain_check.py`, `unverified_check.py` and `docs/the-review-record.md` into scratch trees | Q1: a table with a `signed:` row in `## Confirmations` at `one` imports; `round_of` on a record with no section returns `[]`, and with the section present refuses "no `signed:` line". Q2: a copy with no `hooks/routing.py` exits 2, "chain-check: the shared reader would not load", quoting the missing `hooks/routing.py`. Q3: `confirms:` at `at most one` refuses a record with two lines, "2 `confirms:` lines" |
| `git show <sha>:skills/code-review/scripts/chain_check.py \| wc -l` at 46bc215c, 046dee6e, eb568983, d59f8a4b | 1854, 1869, 1852, 1852 |
| `git grep -n -F` over `tests`, `evals`, `skills`, `docs`, `templates`, `agents`, `.github`, `hooks` and `bin` for fragments of every sentence the fix diff changed, and for `record_target`, `_GRAMMAR_READER` and `specseal_unverified_reader` | the live pins found are in the modules of T1; `record_target` and `_GRAMMAR_READER` have no reader left |

## Files opened

`seal/specs/1792129100-the-mechanics-leave-before-the-agents-are-rewritten/rounds/round-1.md`,
`skills/code-review/scripts/chain_check.py` (at d59f8a4b, and at d426fbdb
through `git show`), `docs/the-review-record.md`,
`templates/sdd-overview.md`, `templates/sdd-round.md`,
`templates/hygiene.yml`, `skills/implement/SKILL.md`,
`skills/verify/scripts/broad_gate.py`, `.github/scripts/release_seal.py`,
`hooks/routing.py`, `tests/test_chain_check.py`,
`tests/test_unverified_rows_close.py`,
`tests/test_a_script_copied_alone_exits_2.py`,
`tests/test_the_changelog_is_gathered_at_release.py`, and the fix diff of
`changelog.md`, `handoff.md` and `overview.md` in the work item's directory.
