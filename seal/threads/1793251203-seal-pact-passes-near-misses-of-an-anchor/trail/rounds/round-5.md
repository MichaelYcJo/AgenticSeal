# Review round 5: 1793251203-seal-pact-passes-near-misses-of-an-anchor

target: 9160cff4a against fa7109701

## Findings

### 1. The proofer's stage 1 text judges only anchors of a pact the `Pact` row declares, so the near-miss remote the frame hands it reads as out of scope

severity: should
location: `skills/code-review/SKILL.md:35-42`
evidence: read `skills/code-review/SKILL.md:35-42`, `seal/threads/1793251203-seal-pact-passes-near-misses-of-an-anchor/frame/design.md:150-159`, `seal/threads/1793251203-seal-pact-passes-near-misses-of-an-anchor/frame/design.md:175-179`
verdict: fixed 12fb615c

The frame gives the proofer every line that reads as meant for a pact
anchor and that `seal pact` does not read (`frame/design.md` *Scope* item
7). It also routes #1132's third *Done when* bullet there: a near-miss
remote under a header outside the normalisation "is met only by the
proofer's judgment" (`frame/design.md:178-179`). The built text narrows
this. It makes a finding of "a line written as an anchor of a pact that row
declares, and outside that shape".

A row naming `git@example.com:org/ordres-api.git`, one letter off the pact,
under `| Pact | Clause | Hashes |` names a pact the `Pact` row does not
declare. Probe P5 ran that frame: exit 0, `READ ... 0 pact anchors`, nothing
refused. Read by its letter, the sentence does not cover that row, so a
proofer reading it so passes the row. That row is the double miss the
seal could not decide in `guarantee.md`, now under a plural header. The other
reading, "meant as an anchor of a declared pact", covers it. Two readings of
one instruction break `CLAUDE.md` *Repo rule: text an agent or a check reads
has one reading*.

The crafter's account (`trail/phases/phase-4.md`, *The condition is the
`Pact` row*) gives grounds for the opening condition. It gives none for the
qualifier "of a pact that row declares", and *Scope* item 7 holds no such
qualifier. A row under a header outside the normalisation that names a pact
the signer forgot to declare falls out the same way.

```markdown
Where `seal/config.md` has a `Pact` row, the proofer reads the work item's
`frame/design.md` at stage 1 against the shape
`skills/verify/scripts/pact_check.py` states under *What each frame is read
for*, which is all `seal pact` reads. A line written as a pact anchor and
outside that shape is a finding, whatever remote its `Pact` cell names:
`seal pact` reads it as no anchor and reports the signer as citing nothing.
Examples are a table under a plural or other wording of the anchor header,
a row with no header, a row outside the anchor table, and any of these
naming a remote one letter off a pact that row declares.
```

answer: The finding holds: *Scope* item 7 has no "of a pact that row declares" qualifier, and phase 4 gave no grounds for it. `12fb615c` puts the record's text in word for word at `skills/code-review/SKILL.md:35-43`, so a line written as a pact anchor outside the read shape is a finding whatever remote it names, P5's near-miss remote among the examples. Contract rule 12: `git grep` for "anchor of a pact", "pact that row declares" and "written as an anchor" finds the qualifier in no other live text. `changelog.md:7` names the shapes without it and stands. `trail/phases/phase-4.md:28-35` quotes what phase 4 built at `6303f97f`, a past-state record, and is not rewritten. The skill's readers (`test_review_axes`, every module `git grep -l "code-review/SKILL.md" tests/` lists, `test_chain_hooks_hardening`, `test_a_cited_section_stands_in_its_file`, `test_censuses`) passed in one command, exit 0 (executed).

### 2. The closing memo cites a `CLAUDE.md` section that no revision holds

severity: should
location: `seal/threads/1793251203-seal-pact-passes-near-misses-of-an-anchor/gaps.md:33-36`
evidence: executed `git grep -n "first value" origin/release/v0.24.2 9160cff4a -- CLAUDE.md`
verdict: fixed b10fa44b

`gaps.md` *Not done* grounds the run-of-four limit on "`CLAUDE.md` *The
first value: efficient development through the workflow*". Neither the
branch's `CLAUDE.md` nor the one on `origin/release/v0.24.2` (`10942072`)
holds a heading or a phrase "first value". The search printed nothing,
exit 1. The words the memo quotes, "judgment spent where meaning is the
question", are from *The rules steer judgment, and a few invariants hold
the chain*. That section stands on `origin/release/v0.24.2` alone, since the
branch's base `8d8d6390` predates #1168.

The sealer re-runs a memo's claims from their coordinates (`guarantee.md`
*Claims re-run* did so at the last seal). A cited section that exists
nowhere is a claim it cannot open, and the limit then rests on no source.

```markdown
writes, and a run of four is written by nobody. Source: `CLAUDE.md` *The
rules steer judgment, and a few invariants hold the chain*, on
`origin/release/v0.24.2` (`10942072`), "Judgment is spent where meaning is
the question"; the proofer's sentence covers such a header as a shape the
normalisation leaves out.
```

answer: The finding holds; the record's paste-ready text is not taken. It cites *The rules steer judgment, and a few invariants hold the chain*, a section on `origin/release/v0.24.2` alone, which #1169 may reword before this merges. On the orchestrator's direction, `b10fa44b` names the section by its subject with no italic heading: "`CLAUDE.md`, its section on where judgment is spent, which spends it where meaning is the question". Contract rule 12: the work item's other `CLAUDE.md` citations, *The rule a mechanism is kept against* at `gaps.md:17`, `frame/design.md:28` and `trail/phases/phase-3.md:41`, resolve on the branch and on `origin/release/v0.24.2` (executed, `git show <rev>:CLAUDE.md | grep "^## "`), and stand.

### 3. S10's search prints a line, and the frame still says it prints nothing

severity: should
location: `seal/threads/1793251203-seal-pact-passes-near-misses-of-an-anchor/frame/design.md:216`, `seal/threads/1793251203-seal-pact-passes-near-misses-of-an-anchor/gaps.md:14-18`
evidence: executed `git grep -n -i "no anchor table holds\|misses twice\|four columns" 9160cff4a -- skills/verify/scripts/ tests/skills/`, `git grep -n -i "no anchor table holds\|misses twice\|four columns" 9160cff4a -- skills/verify/scripts/pact_check.py tests/skills/test_pact_check.py`
verdict: fixed b10fa44b

S10's *Verifiable how* cell names a search over `skills/verify/scripts/`
and `tests/skills/` that prints nothing. Run at `9160cff4a`, it prints
`skills/verify/scripts/unverified_check.py:413`, exit 0. Phase 3 found this
(`trail/phases/phase-3.md:20-27`). The line describes another script's
reading, so the phase left it standing, and that holds. The same search
narrowed to `pact_check.py` and its test module prints nothing, exit 1.

The frame's cell was not corrected, and `gaps.md` *Where spec and
implementation diverged* has no row for it. A sealer that runs S10 as the
frame writes it gets a hit and a scenario that reads as unmet. Phase 3
recorded the correction, so the fix is the record, not the code.

```markdown
| S10, the words a person reads | Every sentence `seal pact` prints is pinned by its case (contract rule 14) and passes `tests/behaviour/test_one_word_one_meaning.py`; no sentence names a refusal it no longer makes | that module, and `git grep -n -i "no anchor table holds\|misses twice\|four columns"` over `skills/verify/scripts/pact_check.py` and `tests/skills/test_pact_check.py` printing nothing |
```

Or, where the frame stays as written, one row in `gaps.md`:

```markdown
| S10's search | `frame/design.md` S10: the search over `skills/verify/scripts/` and `tests/skills/` prints nothing / it prints `skills/verify/scripts/unverified_check.py:413` | the line stands | `trail/phases/phase-3.md` *The frame holds, with one correction found against the tree*: the line states a fact about `unverified_check.py`, not the removed scan |
```

answer: The finding holds. On the orchestrator's direction the frame stays as written, and `b10fa44b` adds the record's second form as a row of `gaps.md` *Where spec and implementation diverged*, now `gaps.md:19`. Its grounds also say the line predates this work. `seal unverified` over the memo exited 0, and `test_censuses` and `test_unverified_rows_close` passed in the boundary command (executed).

## Confirmations

confirms: none
The normalisation is closed and holds two members, as *Scope* item 2
states. `header_key` (`skills/verify/scripts/pact_check.py:300-317`) removes
one `EMPHASIS_RUN` (`:211`) where it matches the whole cell, then case
folds. The crafter claimed that removing the three guards changes no
decision. Reading the pattern confirms it. A key equals `pact`, `clause` or
`hash` only where the wrapped text is the word. None of the three words
holds a space, a `*`, a `_` or a backslash, so a space just inside a run, a
nested run or an escaped delimiter always leaves a character in the key.
`table_cells` reduces only `\|` (`hooks/lib/config.py:119-134`), so
`\*Pact\*` reaches the key with its backslashes. Probe P2 ran that header:
`READ ... 0 pact anchors`, exit 0. Executed and read.

confirms: none
Each member is the same meaning. Lower and upper case are the same word, by
the precedent the frame cites (`skills/settle/scripts/rule_changes.py:84-87`,
`casefold`). One `*` or `_` run of one to three renders as emphasis of the
same word. `str.casefold` also folds U+017F, the long s, to `s`. Probe P3
wrote `Clause` and `Hash` with U+017F in place of each `s`, and
`seal pact` read that header as the anchor table and graded its row `OK`. That is the same word in older
typography. It errs toward reading, not toward the owner's worst outcome.
Executed.

confirms: none
`first_table` with a key finds the line `gfm_table` walks. Both read
`config.unfenced(lines, text)`, and `gfm_table` takes the first shown line
whose cells equal the cells it is given (`hooks/lib/config.py:1159-1165`).
Any earlier line with those exact cells would key the same and be first in
`keyed`, so the handed cells name the same line. Without a key, `heads`
compares exactly, so the map is read as before. Probe P6 showed a walk
refusal quoting the header as written: "has a `| pact | clause | hash |`
header directly under `x`". Probe P7 showed a keyed header inside an HTML
comment below the anchor table counted as no second header. Probes P1 and P8
showed a new behaviour the design implies: a keyed line with no delimiter
row, or with a line above it, standing before the exact anchor table, is
refused at exit 2. At the base, the exact table below it would have been
graded instead. The refusal is loud, it names the line as written, and the
same held at the base for an exact header written so. Executed.

confirms: none
The row scan is gone. `git grep` for `stray_rows`, `row_cells` and
`OUTSIDE_TABLE` outside `seal/threads/` prints nothing at `9160cff4a`. The
guarded call in `check` and the docstring paragraph went in `d0351fd6`. The
module docstring's *What each frame is read for* and *Exit codes* are
rewritten in place (`pact_check.py:25-50`, `:102-107`). Rounds 3 and 4 left
a question on whether `row_cells` passes a row four columns in under the
anchor table. With `row_cells` removed it has nothing to ask of; the
walker's own handling of that line is the `gaps.md` *Not done* limit.
Executed.

confirms: none
The red-first claim holds. The phase 3 record claimed 12 cases red against
`a5533a3d`. This round ran HEAD's test module over the `pact_check.py` of
`a5533a3d` with `-k Test_check`: 12 failed, 51 passed. The 12 are S3's nine
ids, S4, the S5 id `a second table in lower case` and the passes case.
Executed.

confirms: none
The run-of-four claim holds. `trail/phases/phase-3.md` says, read and not
run, that widening `{1,3}` to `{1,4}` passes every case. This round ran that
mutant over the whole test module: 108 passed. The bound is unwatched by any
case. `gaps.md` *Not done* states it as the orchestrator's judged limit, and
the `add` to `docs/the-pact.md` in `## Rule changes` writes "one to three
long". A mutation score licenses *tested*, never *safe*. Executed.

confirms: none
Each new test was read against its group. S3,
`test_accepts_an_anchor_table_whose_header_differs_only_by_case_or_emphasis`,
is a group of its own, and no other case grades a non-exact header. S4,
`test_refuses_an_undeclared_remote_under_a_lower_case_anchor_header`, varies
the header, which the `UNDECLARED` ids of
`test_refuses_a_row_it_cannot_grade_at_its_line` do not reach. S5 is one id
of `test_refuses_an_anchor_row_nobody_reads`. S6's seven headers are each
outside the normalisation, and `| *Pact_ | Clause | Hash |` covers the
same-run condition no other shape does. `seal layout --pairs` names no pair
in this module. Executed and read.

confirms: none
The proofer's text gives the judgment a place without restating the shape.
It names the docstring section by path and heading. Its examples are only
shapes the docstring states as not read. It stands under stage 1, inside the
rule whose `check:` line names
`evals/behaviour/proofer/rule-proofer-one-finding/`. The crafter claimed
three sentences where the plan said one. It is three, and the split follows
`skills/writing-style/SKILL.md` *English prose rules*. S11 holds for a
header outside the normalisation over a declared remote. Finding 1 is the
undeclared remote. Read.

confirms: none
`changelog.md` matches the code. A header cell is compared case folded
after one wrapping emphasis run is removed, a plural or a code span is
another table, an undeclared remote is refused at its line, and the token is
refused in any case. `gaps.md`'s divergence row on the emphasis guards
matches the first confirmation above. Its row on the proofer's text matches
`trail/phases/phase-4.md`. Read.

confirms: none
The handoff's label is honest. `gaps.md` *Not verified* names the full
suite, the repository-wide ruff runs and the typecheck, with the
orchestrator answering through `seal gate`. This round ran none of the
three (contract rule 2). The narrow command below ran five modules: 322
passed. `uvx ruff check` and `uvx ruff format --check` over the two changed
Python files exited 0. `bin/seal rules --check` exited 0. Executed.

Carried, not re-established: the frame's d01 to d26 reprobe at `28edee12`;
the four-revision measurements of the case-folded token; the claim that
`5287dd42` and `28edee12` hold the same pact code, which the sealer re-ran;
and the phase 1 and phase 2 red runs and mutants, which rounds 1 to 3 and
the sealer re-ran. The fix diff changes no code that phases 1 and 2 built
except the scan it removes.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck, which stay `unverified`; this round ran none of them (contract rule 2) | the branch at `9160cff4a` | the orchestrator, by the broad gate |
| Phase 3's seven `seal mutate` mutants and the phase boundary counts of 1009 and 988 passed; this round re-ran the red-first run and one mutant outside the seven, not those | `trail/phases/phase-3.md`, `trail/phases/phase-4.md` | the sealer, by its sample |
| Whether the issue `gaps.md` *Not done* and the design's *Out* row assign for the walker's over-refusal exists; carried from rounds 3 and 4 | `hooks/lib/config.py#gfm_table` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_pact_check.py tests/behaviour/test_one_word_one_meaning.py tests/behaviour/test_a_signer_declares_its_pact.py tests/text/test_review_axes.py tests/test_censuses.py -q` in a `git clone --no-local` at `9160cff4a`, unmodified | 322 passed, exit 0 |
| `bin/test tests/skills/test_tmp_r5_probe.py -p no:xdist -q -s` in the same clone, eight frames under the default signer | P1, a lone `\| pact \| clause \| hash \|` line before the exact table: exit 2, "has a `\| pact \| clause \| hash \|` header with no delimiter row under it". P2, `\| \*Pact\* \| ...`: exit 0, 0 anchors. P3, U+017F in `Clause` and `Hash`: exit 0, 1 anchor, 1 ok. P4, `\| ****Pact**** \| ...`: exit 0, 0 anchors. P5, `\| Pact \| Clause \| Hashes \|` over `ordres-api`: exit 0, 0 anchors, nothing refused. P6, a lower-case header under `x`: exit 2, the walk's sentence quoting `\| pact \| clause \| hash \|`. P7, a keyed header in an HTML comment below the anchor table: exit 0, 1 anchor. P8, a bold header under `note` before the exact table: exit 2, "directly under `note`" |
| `bin/test tests/skills/test_pact_check.py -q -p no:xdist -k Test_check`, HEAD's tests over the `pact_check.py` of `a5533a3d` | 12 failed, 51 passed, exit 1: S3's nine ids, S4, `a second table in lower case`, and the passes case |
| `bin/test tests/skills/test_pact_check.py -q -p no:xdist` with `EMPHASIS_RUN` widened to `{1,4}` | 108 passed, exit 0: the mutant survives |
| `bin/seal layout --pairs` | exit 0; no pair in `tests/skills/test_pact_check.py` |
| `uvx ruff check` and `uvx ruff format --check` over `skills/verify/scripts/pact_check.py` and `tests/skills/test_pact_check.py` | exit 0 each |
| `bin/seal rules --check` | exit 0, 17 excused in 268 check lines of 55 rule files |
| `git grep -n "stray_rows\|row_cells\|OUTSIDE_TABLE" -- . ':!seal/threads'` at `9160cff4a` | nothing printed |

Each edit was made with the Edit tool in the clone and reverted with
`git checkout` before the next run. The probe file was deleted, and the
clone was removed before hand-back.
