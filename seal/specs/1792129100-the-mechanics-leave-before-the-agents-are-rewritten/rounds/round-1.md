# 1792129100-the-mechanics-leave-before-the-agents-are-rewritten — review round 1

target: b8956d56 against origin/release/v0.22.1

A finding round over the whole branch, 19 commits from the merge base
d426fbdb, read in a `git clone --no-local` of the checkout at b8956d56.
This is round 1 of a default cap of three, counted from the plan approved
at 361c63b. No earlier round exists, so every confirmation below reads
`none`.

Finding 8 is the one `must`: the handoff committed after the last green CI
run writes a real e-mail address, and `tests/test_no_real_identifiers.py`
is red at the target on it, so the suite fails at the pull request.

The other seven fall into three groups. Findings 1 and 2 are places
where a check now reads a record the wrong way without refusing it: an open
`## Not verified` item whose text begins with the closing word, and a
grammar table loosened by a `docs/` edit. Findings 3 and 4 are claims in
the changelog fragment that are not true of the tree, and one of them
tells a plugin user to do less than their hygiene step needs. Findings 5
to 7 answer the owner's question about `chain_check.py`: what can go.

The narrow modules named in the probes were run. The full suite was not
run. It is `unverified`, and the sealer answers it.

## Findings

### 1. A Not verified item whose text begins with the word closed is counted closed, and nothing refuses it

severity: should
location: `skills/verify/scripts/unverified_check.py:49-51`, `skills/verify/scripts/unverified_check.py:818-848`, `templates/sdd-overview.md:36-42`, `skills/implement/SKILL.md:455-463`, `tests/test_unverified_rows_close.py:98-140`
verdict: fixed bbdd408c

Executed (probe P2). `check_text` on a section whose one row is
`| closed issues are not re-read after the release | the owner |` returns
no open row, one closed row with the item `issues are not re-read after the
release`, and no error. The row was written as an open claim. It is now
counted closed, so `settle` reads its directory as having nothing open and
`--baseline` lets a later deletion of it pass as the deletion of a closed
row.

Read. Before this branch the closing mark was a character no English
sentence begins with, so the docstring at
`skills/verify/scripts/unverified_check.py:50-51` and
`skills/implement/SKILL.md:462` could say that the silent direction is
always "still open". With the word, that sentence is no longer true for one
class of row: an English item whose first word is `closed`. The phase-4
cases cover `closed-loop` and `enclosed`, which stay open, and do not cover
the plain word followed by a space and more prose, because that row is
indistinguishable from a closing. The word is the owner's decision (Q2), so
the repair is to say so where a person writes the row and to pin the
behaviour, not to change the convention.

```markdown
templates/sdd-overview.md, the paragraph at :36-39:

An item is closed by marking it, never by deleting the row: the Item cell
opens with the word `closed`, lower case, then the item. So an open item
never opens with that word. `| closed issues are not re-read | the owner |`
reads as closed, and nothing refuses it.

skills/implement/SKILL.md:462 and
skills/verify/scripts/unverified_check.py:50-51, the sentence that ends
"the silent direction is always "still open"":

An unmarked row counts open, so the silent direction is "still open",
except for an open item whose own text begins with the word `closed`,
which reads as closed and which only a reader catches.
```

```python
# tests/test_unverified_rows_close.py, a case of CLOSED_ROW_CASES (:98):
    "an open item whose text begins with the word": (
        "| closed issues are not re-read after the release | the owner |",
        ("closed", "issues are not re-read after the release"),
    ),
```

answer: the convention stays (Q2); the overview template now says an open item whose own text begins with the word `closed` reads as closed and nothing refuses it, with that row as its example and the edit to make, and the implement skill's and the reader docstring's "the silent direction is always "still open"" both name that one exception. The CLOSED_ROW_CASES entry the paste asked for was not added: `closed issues are not re-read` takes exactly the reader path of the existing "the word and the item" case, so no break of the reader turns one red without the other. In its place `test_a_text_saying_a_row_counts_open_names_the_open_item_that_reads_closed` pins the sentence in the three texts beside the reader's reading of that row. Executed: red at the docstring before its edit (1 failed, 2 passed; the template and skill texts at eb568983 carry the sentence 0 times each), then `mutation-check` red for a break of each of the three texts and of the reader's closing branch; `bin/test tests/test_unverified_rows_close.py -q` 222 passed, exit 0. The fragment (finding 4's paragraph) tells a plugin user the same.

### 2. A grammar table that lets a finding hold two verdict lines loads, and the later verdict hides an open one

severity: should
location: `skills/code-review/scripts/chain_check.py:319-329`, `skills/code-review/scripts/chain_check.py:1026-1041`, `docs/the-review-record.md:56-68`, `tests/test_chain_check.py:540-574`
verdict: fixed 046dee6e

Executed (probe P3). A copy of `docs/the-review-record.md` whose verdict
row reads `| a finding | any |` instead of `| a finding | one |` loads
through `grammar()` with no error. With that table in place, `findings`
reads a finding holding a verdict line at `open` and then one at
`deferred #5` as one finding at `deferred #5`, with no refusal. A ready
pull request would pass with that finding open.

Read. `finding_of` keeps one match per row (`read[row.line] = i`), so a
row whose `How many` is `any` is read as its last line. The loader refuses
a row the check reads that is missing or lacks a named part, and the
document at `:62-66` says so, but it accepts any count word for a row the
check reads one line of. The document's own rule is that a table the check
cannot honour stops it at exit 2, and #941 is a planned rewrite of `docs/`,
which is the edit that would make this happen. The verdict guard at
`:1052-1056` does not catch it, because the verdict did read.

```python
# chain_check.py, after READ_ROWS (:136): the rows the check keeps one
# match of, and the counts it can honour for each.
ONE_LINE_ROWS = {
    TARGET_ROW: (ONE,),
    LOCATION_ROW: (ONE,),
    VERDICT_ROW: (ONE,),
    REGRESSION_ROW: (ONE, AT_MOST_ONE),
    REOPENS_ROW: (ONE, AT_MOST_ONE),
}

# grammar(), inside `for key, parts in READ_ROWS.items():`, after the
# `lacking` refusal:
        if key in ONE_LINE_ROWS and row.many not in ONE_LINE_ROWS[key]:
            raise refuse(
                f"the `{key}` row allows `{row.many}`, and the check reads one "
                f"`{key}` line"
            )

# tests/test_chain_check.py, a case of the broken-document parametrize list
# (:540-574):
            (
                "| a finding | one | a verdict is",
                "| a finding | any | a verdict is",
                "reads one `verdict:` line",
            ),
```

```markdown
docs/the-review-record.md:63-66, the sentence listing a row it cannot read,
gains one clause:

... a row the check reads a meaning from that is missing, one whose shape
lacks the named part, such as `(?P<commit>…)`, the check reads out of it,
or one the check reads a single line of whose `How many` allows more.
```

answer: `grammar()` now refuses a row whose `How many` its reader cannot keep, named by `HONOURED`: `target:`, `location:` and `verdict:` only `one`, `regression:` and `reopens:` `one` or `at most one`, as the paste had, and two more of the class the enumeration found: `## Confirmations` only `at most one` and `confirms:` not `one`, because `confirmations` counts nothing in an absent section, so a table giving either `one` passed a record with none. The refusal reads "the `<key>` row's `How many` is `<word>`, and the check can honour only …", and `docs/the-review-record.md` §*The round record* names the rule. With `verdict:` and `location:` held at `one`, `finding_of`'s guard for a finding with no verdict or location read could no longer fire, so it left, and the case that reached it through an `at most one` table became one of eight new rows of `test_a_document_the_check_cannot_read_is_exit_2_naming_it`. Executed: the eight rows red before the fix (8 failed, DID NOT RAISE GrammarError), then green, `bin/test tests/test_chain_check.py -q` 75 passed; `mutation-check` of the new refusal red. Not closed: a new label placed in `## Confirmations` that the check reads nothing from would still pass at `one` with the section absent; no such row exists.

### 3. The changelog says a trailing word is newly refused, and the base already refused it

severity: should
location: `seal/specs/1792129100-the-mechanics-leave-before-the-agents-are-rewritten/changelog.md:17-22`
verdict: fixed bbdd408c

Executed (probe P1). The check at the base, d426fbdb, loaded from
`git show d426fbdb:skills/code-review/scripts/chain_check.py`, reads
`fixed abc1234 and more` as no verdict (`FIXED_VALUE` is anchored with
`$`), `abc1234 against main and more` as no target, `` `a.py` and more ``
as no location, and `round-1#2 x` as no reference. Each of the four was
already refused. The fragment says "A value with a word after it, such
as `verdict: fixed abc1234 and more`, is refused as well", under "Two things
are now refused that passed before". A plugin user reads that as a third
change in what the check accepts, and there is none.

Read. The same paragraph says `templates/sdd-round.md` points at the
table "instead of listing the labels". The template's comment at
`templates/sdd-round.md:31-60` still lists every finding label with what it
means and the verdict's four values. That is a defensible line, meaning
kept and shape moved to the table, but the sentence describes a different
template. The plan's §*Operational impact* carries the trailing-word claim
too; it is the frame and nobody acts on it after the merge, so only the
fragment needs the edit.

```markdown
  else for the grammar. `templates/config.md` points at the table instead
  of listing the labels, and `templates/sdd-round.md` keeps what each label
  means and leaves its shape to the table. Two things are now refused that
  passed before: a finding with no `severity:` line, or one whose value is
  not `must` or `should`, and a finding with no `answer:` line or with two.
  A round record in flight that lacks either line adds it before it meets
  this release's check. Where the table itself cannot be
```

answer: the trailing-word sentence is gone; the paragraph says `templates/config.md` points at the table and `templates/sdd-round.md` keeps what each label means and leaves its shape to the table; and "two things now refused" is recounted against the base, which counted neither `severity:` nor `answer:` (its `chain_check.py` holds the two labels in `FINDING_LABELS` and reads no line of either), so a second `severity:` line is new as well and is named. The exit-2 sentence gains the third cause round 1's finding 2 added, a `How many` the check cannot read. `plan.md` §*Operational impact* still carries the trailing-word claim; it is the frame, nobody acts on it after the merge, and it is left as the round said.

### 4. The changelog tells a plugin user that only an overview in flight needs the word, and the hygiene step reads every overview

severity: should
location: `seal/specs/1792129100-the-mechanics-leave-before-the-agents-are-rewritten/changelog.md:34-35`
verdict: fixed bbdd408c

Read. The user's hygiene workflow runs
`unverified_check.py --baseline "origin/<base>" seal/specs/`
(`templates/hygiene.yml:77-78`), which reads every `overview.md` under the
root, released or not, until `settle` retires its directory. This
repository met exactly that: phase 4 found that the new working-tree
reading refused 31 overviews, of which only three are 0.22.0 items and one
is this item, and rewrote all 31 so the hygiene step stays green
(`overview.md`'s divergence row, `phases/phase-4.md`). A user's repository
holding unretired overviews from earlier releases is in the same position.
The fragment tells them "An overview in flight rewrites its closed rows",
so a user who follows it rewrites one file and meets a red hygiene step on
the next pull request, naming files they were told to leave alone.

Executed. Recounted from the tree: 6bceef00 changes 31 overview files,
65 lines out and 65 in, every added line opening `| closed `; no
`overview.md` under `seal/specs/` still holds U+2705; 112 overviews in all.

```markdown
  otherwise read as open. The hygiene step reads every `overview.md` under
  `seal/specs/`, released or in flight, so before you move your
  `hygiene.yml` pin to this release, rewrite every closed row that still
  opens with the old mark to open with the word, in each of them. A base
  revision still reads the old mark as closed, so `--baseline` keeps
```

answer: the paragraph now says the hygiene step reads every `overview.md` under `seal/specs/`, released or in flight, until `settle` retires its directory, and tells a plugin user to rewrite every closed row still opening with the old mark, in each of them, before moving the `hygiene.yml` pin; it also tells them what round 1's finding 1 found, that an open item whose own text begins with `closed` reads as closed and is to be worded otherwise. Read: `templates/hygiene.yml:77-78` reads `seal/specs/` whole.

### 5. round_of reads one record twice and matches its target line twice to get a commit it already had

severity: should
location: `skills/code-review/scripts/chain_check.py:1171-1190`, `skills/code-review/scripts/chain_check.py:1234-1248`, `tests/test_chain_check.py`
verdict: fixed eb568983

Executed (probe P4). One `round_of` call on
`seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/rounds/round-1.md`
calls `reader.readable` 2 times, `finding_spans` 4 times and
`record_lines` 2 times. `record_findings` already reads every row outside
every finding through `record_lines`, keeps only the errors and drops the
match. `round_of` then calls `record_target`, which runs `record_lines` on
the same lines again for the `target:` match, and discards its errors
because `record_findings` reported them. So `record_target` exists only to
recover a value the line before it threw away.

Read. The same pattern sits one level down: `finding_of` matches every
labelled line against its row whole and keeps only the index, then
`verdict_of`, `location_of`, `reference_of` and `reopened_of` rebuild
`"<label> <value>"` through `value_of` and `as_row` and match it again.
Those four stay as seams the fixed cases T33 and T35 read, so this record
does not ask for their removal; keeping the match in `finding_of` is the
same repair as the one below if the owner wants it.

What can go: `record_target` (`:1171-1175`) and one of the two readings.
The tests that call `record_target` read `round_of(...).target` instead.

```python
def read_whole(reader, text, rel):
    """`(lines, findings, errors, outside)` for one record, read once:
    `readable`'s lines, `findings` over them with `unclosed`'s refusals
    first and `record_lines`' after, and `{key: match or None}` for every
    row the table places outside every finding."""
    lines = reader.readable(text or "")
    found, errors = findings(reader, lines, rel)
    outside, said = {}, []
    for key, row in GRAMMAR.items():
        if row.where == OUTSIDE_FINDINGS:
            outside[key], refused = record_lines(reader, lines, rel, key)
            said += refused
    return lines, found, unclosed(reader, text, rel) + errors + said, outside


def record_findings(reader, text, rel):
    # docstring as it stands
    _lines, found, errors, _outside = read_whole(reader, text, rel)
    return found, errors


def round_of(reader, text, rel, number):
    # docstring as it stands, `record_target` taken out of it
    lines, found, errors, outside = read_whole(reader, text, rel)
    target = outside[TARGET_ROW]["commit"] if outside[TARGET_ROW] else None
    confirmed, said = confirmations(reader, lines, rel)
    _section, spans, _error = finding_spans(reader, lines)
    held = {finding_number(lines[first].strip()) for first, _stop in spans}
    held.discard(None)
    errors = sorted(errors + said, key=lambda error: error[1])
    return Round(rel, number, found, held, confirmed, target), errors
```

answer: `read_whole` reads a record once and keeps the `record_lines` match of every row outside the findings; `record_findings` and `round_of` both read through it, and `record_target` is gone. `TestRecordTarget` keeps its name and its cases, which `docs/the-review-record.md`'s two `Enforced by:` lines name, and reads `round_of(...).target` through a `target_of` helper; the template case asserts the target `round_of` reads. The second-level re-match (`verdict_of` and the three like it) stays, as the round left it. Executed: `bin/test tests/test_chain_check.py -q` 75 passed; `mutation-check` red for `round_of`'s target set to None and for `read_whole` dropping the outside rows' refusals.

### 6. The grammar loader and the finding reader each re-implement a helper the file already has

severity: should
location: `skills/code-review/scripts/chain_check.py:283-291`, `skills/code-review/scripts/chain_check.py:742-750`, `skills/code-review/scripts/chain_check.py:1006-1025`, `skills/code-review/scripts/chain_check.py:1120-1132`
verdict: fixed eb568983

Read. Two copies, both added in phase 3.

- `grammar()` finds the end of its section with an inline loop
  (`:284-291`): the first heading of the section's level or shallower.
  That is `section_end` (`:742-750`) line for line. The loader runs at
  import, before `section_end` is defined, which is why it was copied;
  moving `section_end` above `grammar` lets the loader call it.
- `finding_of`'s first loop (`:1006-1025`) refuses a row with no line where
  it needs one and a second line where it allows one. That is `counted`
  (`:1120-1132`) with the finding's heading in front and "a finding" for
  the scope. The two sentences differ only in the words after "at the
  start of a line", so one helper says both, and the pins on each sentence
  move with it.

What can go: about 25 lines, the inline loop and the copied count.

```python
# Moved above `grammar`, unchanged:
def section_end(reader, lines, start):
    ...

# grammar(), in place of the inline `level` and `end`:
    start = starts[0]
    end = section_end(reader, lines, start)

# PLACED gains the finding's place, so one sentence serves every scope:
PLACED = {
    OUTSIDE_FINDINGS: "outside every finding",
    IN_FINDING: "in its finding, with no emphasis",
    IN_CONFIRMATIONS: f"in `{CONFIRMATIONS_HEADING}`",
}


def no_record_line(key, scope="a round record"):
    """The refusal of a `scope` holding no `key` line, which it needs one of."""
    return (
        f"no `{key}` line: {scope} carries one, at the start of a line "
        f"{PLACED[GRAMMAR[key].where]}; {GRAMMAR[key].refused}"
    )


def counted(rel, key, said, scope, first=-1, heading=None):
    """The refusal of `said`, the indexes of `key`'s lines in one `scope`,
    where its row's `How many` does not allow that many, or None: at the
    heading at index `first`, and led by it, where one is given."""
    row = GRAMMAR[key]
    lead = f"{heading} {DASH} " if heading else ""
    if not said and row.many == ONE:
        return (rel, first + 1, lead + no_record_line(key, scope))
    if len(said) > 1 and row.many in HOW_MANY:
        return (
            rel,
            said[1] + 1,
            f"{lead}{len(said)} `{key}` lines; {scope} carries {HOW_MANY[row.many]}",
        )
    return None


# finding_of, in place of its first `for row in rows:` loop:
    for row in rows:
        refused = counted(rel, row.line, at[row.line], "a finding", first, heading)
        if refused:
            errors.append(refused)
```

answer: `section_end` moved above `grammar`, which calls it in place of the inline loop; `counted` takes the heading and its index and `finding_of`'s count loop calls it, with `PLACED` gaining the finding's place as "and with no emphasis", so every refusal a finding's count makes reads byte for byte as before and no pin moved. Executed: `bin/test tests/test_chain_check.py -q` 75 passed; `mutation-check` red for `counted` placing a finding's refusal at line 0 and for dropping its heading lead.

### 7. The shared reader is loaded three times, and main keeps a refusal the import already made

severity: should
location: `skills/code-review/scripts/chain_check.py:392-398`, `skills/code-review/scripts/chain_check.py:1751-1756`, `evals/scripts/replay_targets.py:130-140`, `skills/verify/scripts/broad_gate.py:2589-2593`, `.github/scripts/release_seal.py:287-295`
verdict: fixed eb568983

Read, and executed for the identity (probe P5). Importing
`chain_check.py` loads `unverified_check.py` as `_GRAMMAR_READER` and
stops at exit 2 where it will not load (`:392-398`). `main` then loads the
same file again as `reader` (`:1752`) with its own `try` and the same
sentence, which can only fail if the file changed between the two lines.
`replay_targets.py#record_reader` imports the check, which loads the
reader, and then loads it a third time (`:140`). Probe P5 shows
`chain.READER` and the import-time reader are the same file.

What can go: `main`'s second load of the reader, and the third load in
`replay_targets.py`. The module-level reader becomes a public name so an
importer may use it.

```python
# chain_check.py:393 and every use of the name:
    SHARED_READER = load(READER, "specseal_unverified_reader_for_grammar")
...
    GRAMMAR = grammar(GRAMMAR_DOC, SHARED_READER)

# main(), in place of :1751-1756:
    reader = SHARED_READER
    try:
        routing = load(ROUTING, "specseal_routing")
    except (OSError, SyntaxError, ImportError, SystemExit) as exc:
        print(f"chain-check: the shared reader would not load ({exc})", file=sys.stderr)
        return 2

# evals/scripts/replay_targets.py:140:
    return check, check.SHARED_READER
```

answer: the import-time reader is `SHARED_READER`; `main` uses it and loads only `hooks/routing.py` in its `try`, with the message unchanged; `replay_targets.py#record_reader` returns it. Two more importers of the class loaded the reader again after importing the check, and read it the same way now, the coordinates appended to `location:`: `broad_gate.py#rounds_rows` and `release_seal.py#readers`. `tests/test_a_script_copied_alone_exits_2.py`'s docstring, which said the check loads its readers after argument parsing, is corrected at ef27f327. Executed: `bin/test` of the chain, copied-alone, broad-gate rule, release-seal, non-inferiority and evals-layout modules, 212 passed, 1 skipped, then the 57 modules reading what this pass changed, 2886 passed, 8 skipped, exit 0.

### 8. The handoff writes a real e-mail address, and the no-real-identifiers module is red at the target

severity: must
location: `seal/specs/1792129100-the-mechanics-leave-before-the-agents-are-rewritten/handoff.md:66-68`
verdict: fixed cfd687b7

Executed. In the clone at b8956d56, with nothing of this round added,
`bin/test tests/test_no_real_identifiers.py -q` gives 1 failed, 5 passed:
`test_only_neutral_domains` names
`seal/specs/1792129100-the-mechanics-leave-before-the-agents-are-rewritten/handoff.md:67`
and the domain of the author address written there. The module reads every
tracked file, so the broad gate and every CI leg fail on it.

Read. The handoff was added at 1676d155 and edited at b8956d56, both after
d1ff02a5, the commit of run 38867411967. So the overview's closed row
saying the whole suite ran green on all three legs is true of d1ff02a5 and
not of the target, and no run has read this file. The sentence is an
instruction to the next session: the address is the one
`git config user.email` already reads in this clone, so it can be named by
where it comes from rather than written out. `CONTRIBUTING.md`
§*House rules* forbids a real identifier in a tracked file, and a personal
address in a public repository is the case that rule exists for.

```markdown
  heredoc of any kind, no `git stash`, no `bash -c`, never `cd`; the
  repository by its literal path in every git command; author the address
  the clone pins repo-local (`git config user.email`), never another;
  `Co-Authored-By` with the model; no push (the orchestrator pushes);
```

answer: the handoff names the author address as the one the clone pins repo-local (`git config user.email`), never its value. Executed: `bin/test tests/test_no_real_identifiers.py -q` 6 passed, exit 0. Searched the branch's added lines (`git diff origin/release/v0.22.1...HEAD`) for addresses, user paths, domains and personal names: the address was the one real identifier; three overview rows name the repository's own GitHub path, rewritten by 6bceef00 from lines the base already held, and the base and HEAD hold that name in 26 files each. `overview.md` gains an open `## Not verified` row for the whole suite on three legs at the fix pass's HEAD, the orchestrator to answer; the closed d1ff02a5 row stays as the record of that run.

## Confirmations

confirms: none
The 31-overview divergence holds on its grounds. Executed: 6bceef00 changes
31 `overview.md` files, 65 lines out and 65 in, each added line opening
`| closed `; `seal/specs/` holds 112 overviews and none still carries
U+2705; `unverified_check.py --baseline d426fbdb seal/specs/` in the clone
exits 0 (112 overviews, 289 open, 67 closed, 0 unreadable). Read:
`templates/hygiene.yml:77-78` and this repository's hygiene step read all
of `seal/specs/`, so leaving the 27 released overviews on the old mark
would have turned the step red on every pull request.

confirms: none
The severity and answer divergence holds on its grounds. Executed: the
only records in the tree in the 0.22.0 shape are the ten of
`1791933022-every-agent-skill-and-doc-states-the-current-rule-only`, and
each holds as many `severity:` and `answer:` lines as `### ` headings; the
narrow run of `tests/test_chain_check.py` passed with them. Read: the
issue body asks that a line be accepted only where it matches its row
whole, and `spec.md` §*Data & interfaces* asks each row to say how many a
finding may hold. What the grounds leave out is the warden's side: the
check now refuses a finding with no `answer:` line before any fix pass has
run, and the warden's own definition does not name that line. That is a
`Not judged` row below, for #957.

confirms: none
`chain_check.py`'s line counts, recounted with
`git show <sha>:skills/code-review/scripts/chain_check.py | wc -l`: 1,707
at the base d426fbdb, 1,597 after phase 2 at 17b6e581, 1,850 after phase 3
at 4ffad1ec, and 1,854 at the target. Most of phase 3's growth is the
loader, `grammar`, `grammar_row`, `code_span`, `meant_by` and the load at
import (`:221-408`), and the readers it derives from the table
(`:410-466`), which the chosen design needs. Findings 5 to 7 are what can
go, about 40 lines between them.

confirms: none
Phase 2's removals left no reader of a removed file. Executed:
`git grep` for `rider_check`, `reader_registry`, `undeclared_readers`,
`test_a_reader_declares_its_input_class`, `--reverify` and `Reads: ` outside
`seal/specs/`, `changelog/` and `.test_durations` finds two lines, both
deliberate: the header pin in `tests/test_a_rider_reaches_its_file.py:78`
and a command string that a `family` case classifies in
`tests/test_session_cost.py:1572`. The 87 entries of removed cases still
in `.test_durations` are tolerated by design: the comment at
`.github/workflows/test.yml:69-74` gives an unknown case the average and a
stale file only unbalances the shards, and every Windows shard stores the
file again.

confirms: none
The sentence pins moved with the sentences. Executed: `git grep -n -F`
over `tests`, `evals`, `agents`, `skills`, `docs` and `templates` for
fragments of every removed sentence of `docs/the-review-record.md`,
`templates/sdd-round.md`, `docs/branch-and-release.md`,
`docs/the-record-layout.md` and the closing-word texts found one live pin,
`tests/test_the_rules_claude_md_names_have_one_home.py:54`, which already
quotes the rewritten sentence; the modules found and the modules that
read the changed documents passed (probes T1 and T2).

confirms: none
The Windows fix in `evals/scripts/noninferiority.py` keeps the POSIX
behaviour. Read: on POSIX `os.path.normcase` is the identity and the joined
needle is `/.claude/plugins/cache/`, the literal the base used; on Windows
both sides are lower-cased and back-slashed before the comparison.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, repository-wide lint and typecheck at the target: `unverified` | the whole tree | the sealer, through `broad-gate` after the rounds settle |
| Phase 4's cases and the hygiene step on the Linux and Windows legs; this round ran on macOS alone | `tests/test_unverified_rows_close.py`, `.github/workflows/hygiene.yml` | the orchestrator, from CI at the pull request |
| Whether `agents/warden.md` should name the `answer:` line the check now counts in a warden's record, and whether `agents/smith.md`'s "writes the `answer:` line" should read "rewrites" | `agents/warden.md`, `agents/smith.md:193` | #957's agent rewrite; the orchestrator routes it |
| Whether the two skill sentences saying the What-no-row-governs list "is derived from the checkers' own constants" still say what they mean, now that a round record's literals come from the grammar table | `skills/implement/SKILL.md:77`, `skills/commit-pr-convention/SKILL.md:96` | #957's skill rewrite; the orchestrator routes it |
| Whether `replay_targets.py#labelled_round`'s second scan of the `target:` and `location:` values should instead come from `round_of`, which would need `Finding` and `Round` to carry the raw values | `evals/scripts/replay_targets.py:143-187` | the owner; the evaluation is #957's |

## Probes

| Command | Result |
|---|---|
| T1 `bin/test tests/test_chain_check.py tests/test_unverified_rows_close.py tests/test_the_pull_request_language_is_the_repositorys.py tests/test_a_rider_reaches_its_file.py tests/test_the_record_is_written_in_words.py -q`, in the clone | 382 passed, exit 0 |
| T2 `bin/test tests/test_the_rules_claude_md_names_have_one_home.py tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_evals_layout.py tests/test_settle_reads_before_it_removes.py tests/test_a_process_record_drop_passes_the_readers.py tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_the_rules_have_one_owner.py tests/test_a_script_copied_alone_exits_2.py tests/test_release_hygiene.py -q`, in the clone | 319 passed, exit 0 |
| `bin/rules --check`, in the clone | exit 0 |
| `bin/test tests/test_no_real_identifiers.py tests/test_one_word_one_meaning.py -q`, in the clone at b8956d56 with nothing of this round added | 1 failed, 26 passed: `test_only_neutral_domains` names `handoff.md:67` |
| `python3 skills/verify/scripts/unverified_check.py --baseline d426fbdb seal/specs/`, in the clone | exit 0: 112 overviews, 289 open, 67 closed, 0 unreadable |
| P1 to P5, one probe file `<scratchpad>/<item>/round-1/test_tmp_probe.py` run once with `python3` and deleted, loading the clone's `chain_check.py` and `unverified_check.py` and the base's `chain_check.py` from `git show d426fbdb:` | P1: the base reads `fixed abc1234 and more`, `abc1234 against main and more`, a location with a trailing word and `round-1#2 x` as None, each refused. P2: `check_text` counts `closed issues are not re-read after the release` as one closed row, no error. P3: `grammar()` loads a table whose `verdict:` row says `any`, and `findings` reads `verdict: open` then `verdict: deferred #5` as deferred with no error. P4: one `round_of` calls `readable` 2 times, `finding_spans` 4 times, `record_lines` 2 times. P5: the import-time reader and `READER` are the same file |
| `git show <sha>:skills/code-review/scripts/chain_check.py \| wc -l` at d426fbdb, 17b6e581, 4ffad1ec, 3a5351cf, d4242aff, b8956d56 | 1707, 1597, 1850, 1850, 1854, 1854 |
| `git show --stat 6bceef00 -- 'seal/specs/*/overview.md'` and a count of added `\| closed ` lines | 31 files, 65 insertions, 65 deletions; 65 added lines open with the word |
