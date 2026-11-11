# Review round 1: 1794383427-asserts-pin-literal-phrases

```seal
target: f3acf4842 against origin/release/v0.37.4
```

No earlier round exists, so nothing was carried from a round record. The
base is `dbed1d5ff`, the merge base of HEAD and `origin/release/v0.37.4`.
The diff outside `seal/threads/` is 55 files: 53 test modules, one script
docstring and one `check:` line.

What was read whole: the work item's `routing.md`, the three frame files,
`gaps.md`, `changelog.md`, `pr.md` and the five phase records, at the
target; and every hunk of the diff of the 55 files. What was sampled: the
unchanged parts of the changed modules, and the documents each kept literal
stands in. That each kept literal still stands in the text its case cuts
rests on the narrow run, not on a read of each document. The counts at
`18a7e18fb` in *The counts* and the per-phase ledgers were carried from the
phase records, not re-taken; the counts at HEAD were re-taken.

The plan assigns S2 and S3 to this round. S3 holds (see *Confirmations*).
S2 holds for the kept literals read here, with two exceptions of method,
findings 1 and 2. Finding 3 is a class the build's account claims it
handled and handled by sample.

Three gaps are named here and not opened as findings, because each sits
in a case whose assertions hold no fact the frame states
(`skills/code-review/SKILL.md` *The record*):

- `tests/behaviour/test_release_hygiene.py:1093-1094` keeps `.in_use` with
  the comment "The directory the caution tells the person to keep". The
  build removed the `PID` entry and the comment that said why it stood:
  `.in_use` also stands in the repair's `printf` line of
  `skills/update/SKILL.md` step 2b, so the caution sentence can be deleted
  with the case green. The comment now claims the caution, which the
  assert does not hold.
- `tests/behaviour/test_waiver_decided_at_start.py:413` still asserts the
  whole sentence `SHAPE` in `skills/implement/routing-question.md`. Phase 1
  cut the same sentence to `` `manual` `` in
  `tests/text/test_review_axes.py` as wording. The waiver case holds no
  listed assert, so it is *Out* by design, and a rewording of that sentence
  still turns it red.
- Phase 1's record says five literals were mutated and names seven
  (`trail/phases/phase-1.md:229-234`).

## Findings

### 1. The two absence rules overlap, and the build ruled the overlap both ways

```seal
severity: should
location: `seal/threads/1794383427-asserts-pin-literal-phrases/frame/design.md:157-159`, `seal/threads/1794383427-asserts-pin-literal-phrases/frame/design.md:204`, `tests/text/test_a_moved_rule_leaves_its_definition.py:497-539`, `tests/behaviour/test_release_hygiene.py:1305-1320`, `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:1135-1162`, `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:321-345`
evidence: read `frame/design.md:157-159`, `frame/design.md:204`, `trail/phases/phase-2.md:136-149`, `trail/phases/phase-3.md:154-166`, `trail/phases/phase-3.md:60-68`, and the diff of the four modules; executed `git log -S"def split_row" -- skills/code-review/scripts/chain_check.py` and `git log -S` on the close-block values under `agents` and `skills`, each listing the commit that removed the literal
```

Why it matters: design *The criterion* removes an absence assert "where its
literal is text or a design that a shipped release removed", and keeps one
"where a rule in force forbids its literal in that text". It does not say
which paragraph rules an absence that meets both. The build ruled such
absences both ways:

- Kept: phase 2 kept the absence of `lib/fields.py`'s keys from the
  exclusion list of `templates/setup/config.md`
  (`test_the_pull_request_language_is_the_repositorys.py:1157-1158`). It
  cites `skills/core/SKILL.md` *The rule a mechanism is kept against*, "a
  fact has one source". The case's own docstring says the list drifted
  there before, so the literal is also removed text. Phase 3 kept
  `seal stamp --from` absent from `agents/sealer.md`, and its record says
  "the removal clause could rule it too" (`trail/phases/phase-3.md:165-167`).
- Removed: phase 1 removed the loop that held the form's close-block values
  (`THE_FORMS_OWN`) out of the four files a fix pass reads, and the assert
  that `agents/crafter.md` no longer states "A fix pass appends close blocks
  and writes no phase record." Both literals left those files with #1471,
  and the case's comment named the same one-source rule. Phase 3 removed
  `def split_row` absent from `chain_check.py`, which #1211 removed. The
  same case's kept presence asserts cite the same core rule in their new
  comment (`test_release_hygiene.py:1314-1316`).

The four are alike: each literal stood in the text, a shipped release
removed it, and the core's one-source rule forbids it there. Two were kept
and two removed. The rule change at `frame/design.md:204` carries the same
two readings into `docs/running/what-a-script-gates.md` *The checks*: such
an absence "is such a fact", and "so does one" go. After the settle the
proofer and #1489 apply that row with no frame beside it. The list above
is a sample: it is the four absences the phase records name or the diff
shows citing one rule, and the other removed absences were not each read
for a rule that forbids them.

The paste-ready fix states the precedence. The frame is the framer's to
fold, so the orchestrator sends it as a decision. Add after
`frame/design.md:159`:

```markdown
**Where an absence assert meets both paragraphs above, the second rules.** A literal a shipped release removed from that text, which a rule in force forbids there, is kept with the comment the second paragraph asks for, because the rule outlives the release that removed the text. A literal a shipped release removed that no rule in force forbids goes.
```

And rewrite the `to:` line of the first operation at `frame/design.md:204`:

```markdown
  to: a case pins a fact a reader acts on, and the absence of a command, a path or a spelling that a rule in force forbids is such a fact; one that pins wording goes, and so does one that pins the absence of text or a design that a shipped release removed and no rule in force forbids
```

The snippet does not reach the instances. Under it, the fix pass owes a
ruling on each absence above that the build removed: restore it with a
comment citing the rule, or state in `answer:` why that rule does not
forbid the literal there. The three-fix sentence absent from
`agents/crafter.md` went with its case and its `check:` line in
`skills/implement/SKILL.md`, so restoring it brings both back. Were the
framer to fold the other way, the two kept absences go instead.
`changelog.md:3` ("An absence assert stays only where a rule in force
forbids its literal") reads true under either fold.

```seal
verdict: fixed 4864f032d
answer: The finding holds, and the framer's fold at `d664a9194` decided the overlap differently from the record's paste: where an absence meets both paragraphs, the keep paragraph rules, but only for a rule of that text itself; a rule binding every text alike, such as the core's one-source rule, keeps no absence (plan A14). So `seal stamp --from` stays, the `copied` block-key absence goes (its case renamed `test_the_exclusion_list_points_at_the_block_grammar`), and the close-block values and `def split_row` stay removed. Reading all 141 removed `not in` lines against that rule brought back two whose own texts forbid the literal: `/tmp/run.txt` (`skills/verify/SKILL.md` *Capture once, filter locally.*) and `` `.git/seal/` `` in the Bootstrap section (`skills/implement/bootstrap.md` *Orchestrator: Bootstrap*), each red under its mutant. The `rm -rf` removal stays, since contract rule 17 forbids the act and not the command; that call is for the next round. Records at `e1375088c`.
```

### 2. Seven listed asserts on a workflow's text were left unruled under a reading the frame does not state

```seal
severity: should
location: `seal/threads/1794383427-asserts-pin-literal-phrases/frame/design.md:134-142`, `tests/behaviour/test_the_release_check_watches_what_ships.py:193-323`, `seal/threads/1794383427-asserts-pin-literal-phrases/trail/phases/phase-4.md:85-95`
evidence: read `tests/behaviour/test_the_release_check_watches_what_ships.py:174-190`, `frame/design.md:134-142`, `trail/phases/phase-4.md:85-95`; executed `grep -n -i "print\|rule 14" frame/*.md` in the work item, which finds no sentence placing a printed line
```

Why it matters: the claim is that the seven asserts read "the lines the step
prints to a person", so they fall with a program's output and are not
ruled (`trail/phases/phase-4.md:85-95`). The case runs nothing.
`release_step()` and `refusal()` at
`test_the_release_check_watches_what_ships.py:174-190` read the `run:`
text of `.github/workflows/hygiene.yml` through the YAML parser. Design
*What an assert reads* defines a program's behaviour as "What code the case
ran printed", and puts "a workflow or a config file ... read from its
file" among a file's text, which *The criterion* rules. So the frame
places these seven as a file's text, and the phase took another reading.
The reading has grounds in contract rule 14, which asks a case to pin a
line a person reads. It was named for this round and never folded: the
fold after phase 4 and the fold after phase 5 left *What an assert reads*
as it was. The frame therefore says the tree should rule these seven, and
the tree does not. One of them, `'moves' not in skip[0]` at `:323`, sits
beside the presence assert at `:320`, the shape *The criterion*'s last
paragraph removes, were the asserts ruled.

The paste-ready fix states the reading the build took, so the frame says
what the tree holds. Add a fourth bullet to *What an assert reads*, after
`frame/design.md:140`:

```markdown
- **A line a program prints, read from the file that holds it.** A workflow step's `::error::` or skip line, or a script's message constant, read as text because the case does not run the program. Contract rule 14 asks a case to pin a line a person reads, so these asserts are not ruled and are not changed.
```

The snippet does not reach the policy root. The settle carries only
`## Rule changes`, so if #1489 is to read printed lines this way, the
`to:` of the first operation owes the same clause. That is the framer's
call. The other route is for a phase to rule the seven by *The criterion*.
Then the skip line's absence goes, and each kept assert takes the comment
*Scope* item 1 asks for.

```seal
verdict: fixed 3368a3111
answer: The finding holds. The fold at `d664a9194` states in design *What an assert reads* that a printed line read from its file without running it is a file's text, and rejected a separate kind for it (plan A15). The seven asserts were ruled by *The criterion*: `release/vX.Y.Z`, `plugin.json` and `CONTRIBUTING.md` in the `::error::` line stay with a comment each, red under three mutants of `hygiene.yml`; the base wording, the skip sentence and its `moves` absence go, with the order assert and the skip line's count. Two cases left with no assert went and two were renamed for what they still read.
```

### 3. Seven cases keep a name or a comment stating what a removed assert pinned

```seal
severity: should
location: `tests/text/test_the_settings_have_a_front_door.py:89`, `tests/text/test_a_segment_feeds_the_flow_log.py:223`, `tests/text/test_a_rider_reaches_its_file.py:56`, `tests/text/test_edits_go_through_the_edit_tool.py:78-86`, `tests/behaviour/test_the_sealer_guarantees.py:189`, `tests/behaviour/test_first_setup_asks_once.py:269`, `tests/behaviour/test_release_hygiene.py:1305`, `seal/threads/1794383427-asserts-pin-literal-phrases/changelog.md:18`
evidence: executed a script under the round's scratch directory that lists each `test_*` function present by name at `dbed1d5ff` and at HEAD whose body lost a string constant, 59 cases, each read with its name and docstring; read `tests/behaviour/test_first_setup_asks_once.py:269-290`
```

Why it matters: design *Scope* item 7 rewrites "each docstring or comment
that states what a removed assert pinned". The phase records claim the
case names too: "A case whose name stated what a removed assert read is
renamed for what it still reads" (`trail/phases/phase-1.md:127-136`, and
the same bullet in phases 2 to 4). `changelog.md:18` ships that claim: "Cases
that kept a fact and lost a sentence are renamed for what they still
read." Seven did not change:

- `test_the_skill_says_how_a_value_carrying_a_pipe_is_written`
  (`test_the_settings_have_a_front_door.py:89`). Both pipe asserts went;
  the case holds the quote and backslash escapes alone.
- `test_the_tokens_are_counted_rather_than_estimated`
  (`test_a_segment_feeds_the_flow_log.py:223`). "counted, not estimated"
  went; the case holds the `usage` fields.
- `test_the_header_says_what_belongs_and_what_does_not`
  (`test_a_rider_reaches_its_file.py:56`). Both sentences went; the case
  holds the `grep -rn "RIDER:"` command.
- `test_the_reviewer_keeps_the_half_that_makes_the_rule_its_own` and its
  docstring (`test_edits_go_through_the_edit_tool.py:78-86`). The docstring
  says the case holds the paragraph that "names what its own edits are";
  the `scratch fixture` assert went, and the case holds `rule 9`.
- `test_the_sealer_checks_the_copy_and_reads_only_the_orchestrators_part`
  (`test_the_sealer_guarantees.py:189`). Its docstring now says the
  orchestrator's part "is the proofer's to read"; the name still claims it.
- The section comment `# --- Q1: the sentence a session reads, once in each
  place` (`test_first_setup_asks_once.py:269`). The `count(...) == 1`
  assert became a presence assert, so "once" is no longer held.
- `test_the_chain_check_reuses_the_reader_rather_than_writing_a_second`
  (`test_release_hygiene.py:1305`). The absence of a second reader went.
  This name holds again if finding 1's fix restores that absence.

The list is whole for cases that kept their name, by the script. It is a
sample for comments outside a function: the section comment was found by
reading the diff. A wrong name sends the next editor after a guard the
case does not hold, and the changelog line tells the release note's reader
the class was handled. No other file names these cases (executed: `git
grep` on each name outside `seal/threads/`).

```python
# tests/text/test_the_settings_have_a_front_door.py:89
def test_the_skill_says_how_a_quote_or_a_backslash_is_written():

# tests/text/test_a_segment_feeds_the_flow_log.py:223
def test_the_section_names_the_token_fields_the_count_reads():

# tests/text/test_a_rider_reaches_its_file.py:56
def test_the_header_gives_the_command_that_lists_the_riders():

# tests/text/test_edits_go_through_the_edit_tool.py:78
def test_the_reviewer_points_at_the_edit_rule():
    """What stayed in `agents/proofer.md` when contract rule 9 took the rest:
    the rule's number, which the proofer resolves. Which of its own acts the
    paragraph names as edits is the proofer's to read."""

# tests/behaviour/test_the_sealer_guarantees.py:189
    def test_the_sealer_checks_the_copy_with_the_command_and_its_exit(

# tests/behaviour/test_first_setup_asks_once.py:269
# --- Q1: the sentence a session reads, in each place ----------------------

# tests/behaviour/test_release_hygiene.py:1305, only where finding 1 leaves
# the absence removed
def test_the_chain_check_loads_the_one_reader():
```

```seal
verdict: fixed e94c791e9
answer: The finding holds. The six cases and the first-setup section comment take the record's names; the last case is `test_the_chain_check_loads_the_one_reader`, since the `split_row` absence stays removed under the fold of finding 1. No file outside `seal/threads/` cites an old name, and `changelog.md:18`'s claim that such cases are renamed now holds.
```

## Confirmations

What matched: S1's totals. The phase tables sum to 315 kept, 237 removed
and 113 not ruled, and with the one assert #1483's merge took they make the
666 of *The groups*, as `changelog.md:3` says (read, the five phase
records). The counts at HEAD are 289, 14, 436 asserts and 20 absence asserts,
as `changelog.md:11-14` gives (executed, design *The listing* and the two
`git grep -E` forms at HEAD).

What matched: S3. No changed or removed assert read a program's output in
a case that stands. Each of the 59 same-named cases that lost a string
constant lost only asserts on a file's text. The asserts on
`missing_row`, `base_spellings`, the panel and the subprocess outputs are
unchanged (executed, the same script; read, each case's hunk).

What matched: *Scope* item 1's comment. Of the listed asserts at HEAD in the
changed modules, 81 have no comment line directly above them. Each of
those reads a program's output or a built text, stands in the *Out* case,
carries #1233's comment, or follows a comment that covers the asserts
under it (executed, a script under the round's scratch directory; read,
each of the 81).

What matched: the kept absence asserts at HEAD, `disable-model-invocation:
true`, `seal stamp --from`, `continue-on-error` and `persist-credentials`,
and the three outside the listing (`AskUserQuestion`, the `Planning` box,
the copied keys). Each comment cites a rule by path and heading or bold
lead, as *The criterion* asks (read).

What matched: the worked examples of design *Worked examples* are ruled as
the table says, in `test_the_broad_gate_row_is_asked_for_and_runs_as_written.py`,
`test_a_segment_feeds_the_flow_log.py` and
`test_the_seal_is_taken_once_by_the_sealer.py` (read).

What matched: *Scope* item 5 and S6. The old-roots module holds `tracked`,
`lines_naming_the_second_root` and #1059's three cases, and its docstring
says what it holds (read).

What matched: *Scope* items 7 and 8 at the coordinates the phases name. The
docstrings of `.github/scripts/release_completeness_check.py` and
`tests/github/test_release_completeness_check.py`, the comment at
`test_both_editions_carry_the_same_folds.py:94` and at
`test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py:57`, and
the `check:` line removed from `skills/implement/SKILL.md` are as the records
say (read). The `check:` line at `skills/implement/fix-pass.md:70` keeps a
reader: the fix-pass case still reads the two citations of the form in
that paragraph (read).

What matched: S4, S5 and S8. `bin/seal rules --check` prints "all 177 check
lines in 69 rule files hold." None of the 85 test names gone at HEAD, nor
the removed helpers the phase records name, is named outside
`seal/threads/` except by an unrelated case of the same name in another
module. `rule_changes.parse` returns six operations with no error and
nothing unread, and each `from` stands once in its section (executed).

What matched: S9 for the changed modules, and the lint over them. `bin/test`
over the 53 changed test modules passed, 913 cases, and `uvx ruff check`
and `uvx ruff format --check` over `tests/text`, `tests/behaviour`,
`tests/github` and `.github/scripts` exit 0 (executed). No module-level name
of a changed module was left unused by this diff. `ORCH` in the broad gate
row module is unused, as it was at the base (executed).

What matched: `pr.md`'s four quotes stand word for word at
`frame/design.md:159` and `frame/plan.md:72`, `:74` and `:75` (read). No row
left `gaps.md` without `closed` across the branch (executed,
`git log -p` on the file). `gaps.md` labels the suite beyond each phase's
set `unverified` with the orchestrator's broad gate as its answerer, which
is honest: no phase claims the full suite. Design G13 holds: the diff
changes none of the files `docs/layout/the-record-layout.md:52` says owe
a `### Process changes` table (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite beyond the 53 changed modules, the repository-wide lint and the typecheck | the whole tree at HEAD | the orchestrator's broad gate |
| Stale statements the phases found outside their ranges and that no row routes: the module docstring of `tests/text/test_the_chain_section_has_one_shape.py` (phase 1), and `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py:12` with the A10 comment, and `skills/verify/scripts/broad_gate.py:612` (phase 3). Each predates this work. | `trail/phases/phase-1.md:205-211`, `trail/phases/phase-3.md:227-233`, `gaps.md:22-25` | the orchestrator: a home for them, or none |
| The removed absence asserts outside finding 1's four, each read for whether a rule in force forbids its literal | the removed `not in` asserts of the diff | the fix pass, under the precedence finding 1's fold states |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the 53 changed test modules, `-q`, in a `git clone --no-local` at `f3acf4842` | exit 0, 913 passed |
| `uvx ruff check` and `uvx ruff format --check` over `tests/text tests/behaviour tests/github .github/scripts` | exit 0 and exit 0 |
| `bin/seal rules --check` | "all 177 check lines in 69 rule files hold." |
| design *The listing* at HEAD | comparisons 457, asserts 436, absence asserts 20, cases 265, modules 66 |
| `git grep -E` the two forms of *The counts* at HEAD | 289 and 14 |
| `rule_changes.parse(design, "docs")` at HEAD | six operations, no error, nothing unread |
| the same-named cases that lost a string constant, `dbed1d5ff` against HEAD | 59 cases |
| listed asserts in changed modules with no comment directly above | 81 rows, each read |
| test names at `dbed1d5ff` absent at HEAD, each searched with `git grep -w` outside `seal/threads/` | 85 names, one found, in an unrelated case of the same name |
