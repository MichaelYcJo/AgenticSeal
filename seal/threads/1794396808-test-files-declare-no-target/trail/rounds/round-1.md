# Review round 1: 1794396808-test-files-declare-no-target

```seal
target: 926e1da4b against origin/release/v0.37.4
```

This is the first round, so no earlier record carries a coordinate, and
every fact below was established here. The diff was read from the merge
base `38123f839` to `926e1da4b`, 140 files. `routing.md`, the three frame
files, `gaps.md`, `changelog.md` and `pr.md` were read whole at
`926e1da4b`, and so were the eight phase records. No `pr.<lang>.md`
stands, and none is owed: `seal/config.json` names English for both
language keys. No `seal/parity.json` is declared. The runs below were made
in a `git clone --no-local` of the worktree under the round's scratch
directory.

The round weighed the work where a sample buys the most. It read whole
the reader's change and its cases, `CONTRIBUTING.md` *The test layout*, the
four binding-alignment commits, every reason line against the paths its
file reads, every class that holds a printed pair, and a sample of the
criterion's rulings. It re-ran two of the five move checks, and it listed
every moved case and grepped each name.

## Findings

### 1. `tests/lib/test_blocks.py` says the readers-hide file keeps the oracle's own cases, which phase 7 moved out

```seal
severity: should
location: `tests/lib/test_blocks.py:13-15`, `seal/threads/1794396808-test-files-declare-no-target/trail/phases/phase-7.md:216-228`
evidence: executed `git grep -n "test_the_readers_hide_what_a_renderer_hides" -- . ':!seal/threads' ':!CHANGELOG.md'`, `git grep -n -i "oracle's own cases\|keeps the oracle" -- tests`, `git log 38123f839..HEAD -- tests/lib/test_blocks.py`; read `tests/lib/test_blocks.py:1-18`, `tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py:1-60`, `tests/test_commonmark_oracle.py:1-20`
```

Why it matters: the docstring tells the next reader that the oracle's own
cases stand in `tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py`.
A reader who goes there finds one case, the import case, and the six
oracle cases are in `tests/test_commonmark_oracle.py`. Design *Scope*
item 10 asks that each docstring of a file a phase changes say what the
file now holds, and that a sentence naming where moved cases stood be
rewritten in place.

The sentence was true when phase 3 wrote it at `7a2c58b2c`: phase 3's
record says "The two oracle files keep the oracle's own cases: 3 and 7."
Phase 7 moved six of the seven to `tests/test_commonmark_oracle.py` at
`d97c66c38`. `git log` shows no later commit to `tests/lib/test_blocks.py`.

Claimed in `trail/phases/phase-7.md:216-228`: "Six lines in five files cited
the deleted file or said the old file keeps the oracle's own cases", and
"`tests/lib/test_blocks.py:3,7` ... still hold". Found: the stem's grep
lists five lines, and the one at `tests/lib/test_blocks.py:3` opens a
docstring whose sentence at `:13-15` says the old file "keeps the oracle's
own cases". The account read the lines the grep printed and not the
sentence each stood in, so it handed back a sample as the whole list. The
same sentence was rewritten in `tests/lib/test_routing.py:12-16` and
`tests/lib/test_tables.py:21-25`, which shows the class phase 7 was
working through.

The class, listed by taking apart every line the readers-hide file's stem
is written on (five lines, all read in their sentences) and by a grep for
the phrase: `tests/commonmark_oracle.py:10` still holds, since the import
case reads the oracle's imports; `tests/lib/test_routing.py:15`,
`tests/lib/test_tables.py:57` and `tests/test_commonmark_oracle.py:11`
hold; `tests/lib/test_blocks.py:13-15` is the one that does not. The
snippet below reaches it whole.

```python
`Test_walk` and `Test_walk_text` hold the walk to a CommonMark oracle,
`tests/commonmark_oracle.py`, over the corpus this file builds: on every line
the walk does not call uncertain, the walk and the oracle agree. #1489's
phase 3 moved those two cases and the corpus here from the first file. The
oracle's own cases stand in `tests/test_commonmark_oracle.py`, and the first
file keeps the case that holds the oracle imports nothing of this
repository's. `tests/lib/test_tables.py` and `tests/lib/test_routing.py`
import the corpus from here and hold their readers to the oracle over it.
```

### 2. `CONTRIBUTING.md` *The test layout* places a file with no `TARGET` by whether it runs shipped code, and five such files stand the other way

```seal
severity: should
location: `CONTRIBUTING.md:289-290`
evidence: executed `git grep -n -E 'load_module|load_lib_module|subprocess|import_module|spec_from_file' -- tests/text`, a loop over the 67 files `git grep -l '^# No TARGET: ' -- tests` lists under `tests/behaviour/` with `grep -E` for a loader, a subprocess or an import of a test file, `git grep -n -i -e 'only read text' -e 'load or run shipped code' -- . ':!seal/threads'`, `git show 38123f839:CONTRIBUTING.md | grep -n 'where its cases load or run shipped code'`; read `tests/text/test_no_passage_is_pasted_into_a_second_file.py:56-66`, `tests/text/test_a_moved_rule_leaves_its_definition.py:85-95`, the imports of `tests/behaviour/test_a_commit_names_its_repository.py:17`, `tests/behaviour/test_a_probe_that_commits_says_so.py:17` and `tests/behaviour/test_the_set_a_work_item_always_has.py:30`
```

Why it matters: the paragraph is the rule this work rewrote (design *Scope*
item 3), and a contributor or a crafter acts on it to place a new file. It
says: "Such a file stands in `tests/behaviour/` where its cases load or
run shipped code, and in `tests/text/` where they only read text." The
tree holds the opposite in both directions:

- `tests/text/test_no_passage_is_pasted_into_a_second_file.py:60-65` loads
  `skills/settle/scripts/passages.py` and runs its `in_corpus`, `words` and
  `windows`. `tests/text/test_a_moved_rule_leaves_its_definition.py:90`
  loads the same module for `WINDOW`.
- `tests/behaviour/test_a_commit_names_its_repository.py`,
  `tests/behaviour/test_a_probe_that_commits_says_so.py` and
  `tests/behaviour/test_the_set_a_work_item_always_has.py` import only
  `read` from `tests/conftest.py`, and their cases only read documents.

The sentence stood at the base too (`CONTRIBUTING.md:260` at `38123f839`),
so the work did not make the contradiction. Phase 1 rewrote the paragraph
around it and phases 2, 6 and 7 filed all five files in place, so the
released paragraph keeps a placement rule the tree it describes does not
follow. The five files were found by a pattern search for a loader, a
subprocess or a test-file import, so they are a sample; a file that runs
shipped code through another spelling is outside it. One statement of the
rule stands in the tree (the grep above), and the snippet reaches it.

The fix states where the files stand. The alternative, moving the five
files to the directory the sentence names, re-points three `check:` lines
and any importer, and the fix pass owes that choice an answer.

```markdown
reads that line. Such a file stands in `tests/behaviour/` or in
`tests/text/`, which together hold every file that declares none.
```

## Confirmations

What matched: the pair reader, design *Scope* item 1 and *The pair
reader*. `skills/verify/scripts/test_layout.py:457-492` leaves out a call
whose every positional and keyword argument is `[]`, `()`, `{}` or `None`,
and keeps a call with no argument out as before, since `all()` over no
argument is true. A starred argument or a `**` spread is not a display, so
such a call is still compared. The two docstrings say the same. Executed:
`bin/test tests/skills/test_test_layout.py -q` gave `83 passed`, and
`bin/seal layout --pairs` names no pair of `tests/github/test_run_tests.py`.
Read: phase 1's mutant table shows each guard red, the `not any` mutant on
the case that holds *every* apart from *any*.

What matched: `--all` is gone, design *Scope* item 2 and S2. Executed:
`bin/seal layout --check --all` exits 2. Read: the `every` parameter, its
two refusals and its docstring lines left together, and the twin refusal
now turns on a declared file alone, as design `## Removes` row 1 says.

What matched: the counts of `changelog.md` and phase 8. Executed at
`926e1da4b`: `bin/seal layout --check` ends `141 files read, 0 refused, 67
declare no TARGET` and exits 0; `bin/seal layout --pairs` ends `141 files
read, 43 pairs`; `bin/seal rules --check` holds all 176 check lines; 67
files carry a reason line, each one line, and they are the 67 files the
report names. An `ast` count gives 590 cases in 82 files at `926e1da4b`
and 692 in 86 at `b9ca37404`.

What matched: S3, the place of the reason line. An `ast` script over the
67 files found each reason line after the last import and before the first
other statement.

What matched: the moves, design *Scope* items 5 and 9 and S4, S6. A script
set each case name of `tests/text/` and `tests/behaviour/` at `38123f839`
against every test file at HEAD: 65 names left those directories, 23 for
`tests/lib/`, 27 for `tests/skills/`, 5 for `tests/github/`, 1 for
`tests/test_conftest.py`, 6 for `tests/test_commonmark_oracle.py` and 3 for
`tests/test_gfm_table_oracle.py`, which are the changelog's numbers. A
`git grep -w` of each of the 65 names outside `seal/threads/` finds it only
in its new file. Executed again: phase 7's oracle move check at
`d97c66c38` (`44 old cases, 160 items against 160 at edc9ba6e0d56, 0
failed`) and phase 5's at `21dbe042e` (`120 old cases, 200 items against
200 at 81ec9ed53ce0, 0 failed`), each exit 0. The four deleted files'
stems appear nowhere outside `seal/threads/`.

What matched: the four binding-alignment commits, `20a9460fa`,
`6adfab9cc`, `81ec9ed53` and `edc9ba6e0`, read line by line. Each rewrite
is a rename to a name bound to the same object (`ITEM_NAME` for the alias
`STAMPED`, `PR` for `PR_BODY`, `UC` for `UNVERIFIED` and the rest), or a
helper of the same body (`said` in `tests/skills/test_seal.py:201-204`
equals the one removed), or `git_out` for `git`, which runs the same
`git(...)` with `check=True` (`tests/conftest.py:1002-1015`); the cases
discard both results. `chain.FIELDS` is `lib/fields.py` loaded by
`chain_check.py:298`, which the sealer file now loads directly. No assert
changed.

What matched: the seven S3 cases under `tests/skills/test_chain_check.py`'s
`@pytest.mark.rule("routing-read-first")`, which phase 4 left to this
round. Each runs `chain_check.py#main` where the declaration stands under
`agentic-seal/`, so each holds where the check reads the declaration, the
rule `docs/running/the-review-and-parity-arms.md:32-44` states. They belong
under it.

What matched: the reason lines, S3 and design *The kinds*. A script printed
each of the 67 lines beside the paths its file names; each ground names
what its cases read or walk, and none names a ground the file's paths
contradict. The D files were read the same way: each case reads its
`TARGET` alone. `tests/behaviour/test_update_reads_the_config_directory_in_use.py`
runs the skill's own bash fences, which are the document's text, so D
holds for it. The three phase 5 cases that read a document to build a
call's input (`tests/github/test_issue_claims_check.py:291`,
`tests/github/test_rules.py:743`, `tests/github/test_publish_release_note.py:1198`)
assert on what the call returned, which *The kinds* makes M.

What matched: S8, every class holding a printed pair. All 18 classes were
read with their cases. Each docstring names the input its cases differ by,
and `tests/skills/test_session_cost.py::Test_main` names `run_with_segments`
and the two facts its one-input pair holds (`:1532-1541`, against
`test_the_reading_names_the_release_it_is_comparable_from` and
`test_the_reading_says_its_family_rows_moved_at_642`). The pair
`tests/skills/test_test_layout.py::Test_main` that phase 1 made differs by
the monkeypatched `_toplevel` (`:1125-1160`), as its docstring says.

What matched: `CONTRIBUTING.md` *The test layout*, its kinds paragraph,
pair sentence and threshold sentence (`:236-253`, `:265-293`, `:306-313`),
against design *The kinds* and *Scope* item 11. Each kind, the module under
`tests/`, the source case, the read-through case and the one-input pair
are stated as the design states them; finding 2 is the one sentence the
tree contradicts. `CONTRIBUTING.md:43` says the two directories hold the
tree-wide files, which holds, since all 67 stand there.

What matched: the criterion's rulings, a sample against #1488's *What an
assert reads* and *The criterion*:
`tests/text/test_edits_go_through_the_edit_tool.py` (two absence cases of
text a release removed), the deleted
`tests/text/test_the_verifying_round_is_bounded_not_cheapest.py` (wording
and its absences), `tests/text/test_every_agent_reads_the_contract.py`
(`BOUNDS`, phrases of wording, and the one-sentence equality across
definitions), and rule 3 of `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`,
cut from whole sentences to the spellings the gate prints, the flag and
variables a person keeps, and the files a reader opens, each with its
comment. Each removal is a kind *The criterion* removes, and each kept
literal a kind it keeps.

What matched: `pr.md`. Each of its 35 quotes stands word for word, with
whitespace collapsed, in `frame/plan.md` at the row its coordinate names.

What matched: design G1 to G14, *Scope* and *The files* as dated, and
`frame/plan.md`, `frame/questions.md`, `gaps.md` and `changelog.md` at
`926e1da4b`. Every row of *The files* that a phase found otherwise carries
the phase's ruling in its last cell, and the target contradicts no sentence
of them that states what the work does.

Two things are named here and are no finding. The comments
`tests/skills/test_chain_check.py:4886` ("left where they stand, for #923")
and `tests/skills/test_pact_check.py:1259` ("For #923") stand in files
phase 4 changed and still say their cases wait for #923; design *Scope*
item 10 and `## Removes` reach docstrings, not comments, so the fix pass
may take them where it is cheap. `trail/phases/phase-7.md:188-194` says a
pair stood in the readers-hide file before the move; phase 8 corrected
that account (`trail/phases/phase-8.md:184-193`), and the record is
history.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite beyond `tests/skills/test_test_layout.py` and the two move checks this round ran; frame Q3, which modules outside each phase's narrow run turn red. Phases 6 and 7 ran a set that left out tree-wide files such as `tests/text/test_review_axes.py` | each phase record's boundary command | the orchestrator's broad gate |
| The criterion's rulings this round did not sample: the kept and removed asserts of the other files phases 2, 6 and 7 ruled | `trail/phases/phase-2.md`, `phase-6.md`, `phase-7.md`, the ruling tables | the orchestrator, who decides whether a later round samples further |
| The move checks of phases 3 and 4, which this round read and did not re-run | `trail/phases/phase-3.md:130-141`, `trail/phases/phase-4.md:154-169` | the orchestrator's broad gate, for the cases they moved |

## Probes

| Command | Result |
|---|---|
| `bin/seal layout --check` at `926e1da4b` | exit 0; `141 files read, 0 refused, 67 declare no TARGET` |
| `bin/seal layout --pairs` at `926e1da4b` | exit 0; 43 pairs in 18 classes, none of `tests/github/test_run_tests.py` |
| `bin/seal rules --check` at `926e1da4b` | exit 0; `all 176 check lines in 69 rule files hold.` |
| `bin/seal layout --check --all` at `926e1da4b` | exit 2 |
| `bin/test tests/skills/test_test_layout.py -q` at `926e1da4b` | `83 passed`, exit 0 |
| phase 7's second `bin/seal layout --moved edc9ba6e0 ...` at `d97c66c38` | exit 0; `44 old cases, 160 items against 160 at edc9ba6e0d56, 0 failed` |
| phase 5's `bin/seal layout --moved 81ec9ed53 ...` at `21dbe042e` | exit 0; `120 old cases, 200 items against 200 at 81ec9ed53ce0, 0 failed` |
| an `ast` script setting the case names of `tests/text/` and `tests/behaviour/` at `38123f839` against every test file at HEAD, then `git grep -n -w` of each moved name | 65 moved names; each cited only in its new file |
| an `ast` count of the cases of `tests/text/` and `tests/behaviour/` at `926e1da4b` and at `b9ca37404` | 590 in 82 files; 692 in 86 files |
| an `ast` script locating each reason line against the file's imports | every line after the last import and before the first other statement |
| a script printing each class docstring that holds a printed pair | 18 classes, each with a docstring |
| a script setting each `pr.md` quote, whitespace collapsed, against `frame/plan.md` | 35 of 35 found |
| `python3 skills/code-review/scripts/chain_check.py --baseline 38123f839 --root <the branch worktree> --worktree` | exit 0 before this record; it named no round record yet, the gate record and the guarantee, and printed no notice on `frame/design.md` |
