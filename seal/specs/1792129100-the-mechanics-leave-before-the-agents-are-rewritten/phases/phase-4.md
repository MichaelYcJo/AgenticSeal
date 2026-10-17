# 1792129100-the-mechanics-leave-before-the-agents-are-rewritten — phase 4

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 6bceef00 |


## What this phase was asked

The closing word, and then the item's close. `unverified_check.py#CLOSED`
reads `closed` as the first word of a closed row's first cell. It refuses
the old emoji naming the row and the edit, and refuses a bare `closed` the
way a bare mark was refused. Its messages are in words. The template,
`templates/config.md`, `docs/the-record-layout.md` and
`skills/implement/SKILL.md` state the word; the skill change is one
sentence, and its rewrite is #957's. The `## Not verified` rows of the four
0.22.0 work items' overviews are rewritten once by a one-shot script whose
diff is read whole. This item's own overview, whose three-leg CI row was
closed with the old emoji, is rewritten in the same commit and counted in
the script's assertion or edited by hand, as recorded. Then the close:
`overview.md` completed and a `changelog.md` fragment written as the
paragraph a plugin user reads. The fragment covers the census and the
stamps gone, the grammar table with its new refusals of `severity:` and
`answer:`, exit 2 on an unreadable table, and the word `closed`. The round
records and the sealer's files are owed later by the review chain and are
not written here. Every sentence changed in a document, template or skill
is grepped over `tests` and `evals` by a distinctive fragment, and every
module found is run.

## What this phase found

**The rewrite covers 31 overviews, not four, because the hygiene step reads
all of them.** `.github/workflows/hygiene.yml` runs
`unverified_check.py --baseline origin/<base> seal/specs/`. That walks all
112 overviews under `seal/specs/`, released or not. A probe read every
overview at HEAD (d4242aff, before the rewrite) through the new working-tree
reading (executed, run once and deleted). It refused 31 overviews holding
65 rows that open with the old mark. Only three of them are 0.22.0 items
(`1791876666`, `1791876667`, `1791933022`; `1791876665` and `1791940762`
hold no closed row). The fourth is this item. So leaving the other 27 would
turn the hygiene step red on every pull request. Before the rewrite,
`tests/test_unverified_rows_close.py::test_this_repositorys_own_overviews_are_all_readable`
failed on the same 31 files (executed). Narrowing the change leaves two
ways out, and the frame rejects both. The working tree could keep accepting
the emoji, which is `plan.md` Alternative F, rejected by the owner on Q2.
Or the check could skip a list of old directories, which is a list kept
beside the tree. The round records' quoted marks are a different case: #923's
Q10 keeps them because no check refuses a quotation in a record, while an
overview's `## Not verified` row is read by a gate on every pull request.
The directories leave the tree when `settle` retires them, and until then the
gate reads them.

**The rewrite went through the reader itself.** A one-shot script in the
scratch directory loaded `unverified_check.py` and found each closed row
through the base reading, which still reads the old mark as closed. It
replaced only the leading mark (and an emoji selector after it) with
`closed `, then read the file again through the working-tree reading. Per
file, it asserted that the open count, the closed count and every closed
item's text were unchanged, that no error appeared and that no row still
opened with the mark. In total it asserted 31 files, 65 rows before and 65
closed after. It ran once (exit 0) and was deleted. This item's own row was
one of the 65 and was not edited by hand. The diff is 65 lines out and 65
in, each pair differing only in its opening mark, read whole.
`unverified-check seal/specs/ --baseline origin/release/v0.22.1` then gave
exit 0: 112 overviews, 290 open, 65 closed, 0 unreadable, 0 not compared
(executed).

**A base revision still reads the old mark as closed.** Read as a refusal
at the base, every base written before the word would be `not compared`,
and a row deleted against it would pass. That includes this pull request's
own base, where the 31 overviews still carry the mark. So the reading that
already relaxes the heading and the header for a base (`strict_header`
False) also reads the mark as the word. `check_text`'s docstring says so.
The working tree refuses it naming the edit:
`the row opens with U+2705, which no longer closes a row: a closed row opens with the word `closed`, so write `| closed <item> | <what closed it> |``.
The message names the mark by its code point, so the check prints no emoji.

**What the reader refuses, and what it leaves open.** `closing_word`
splits the Item cell, already through `visible`, at the first whitespace.
The word `closed` followed by an item closes the row. A bare `closed`,
including one followed by a zero-width character, is refused as bare.
`Closed`, `CLOSED` and `closed:` are refused naming the spelling, because a
capital or a colon would otherwise turn a closing back into an open row.
`closed-loop …` and `enclosed …` stay open. The mark is spelt
`chr(0x2705)` in the source, so the file carries no emoji. A backslash-u
escape typed into an Edit call arrives as the character itself, which is
how it first landed.

**More texts stated the mark than the frame named.** The frame named the
template, `templates/config.md`, `docs/the-record-layout.md` and one
sentence of `skills/implement/SKILL.md`. The tree also had the sentences
below, and each now states the word (`overview.md`'s divergence row):

- three places in `skills/implement/SKILL.md`: the English-vocabulary list
  (the mark beside `drained`), the example row with its bare-mark sentence, and "beside a check
  mark";
- `skills/verify/SKILL.md`'s closing sentence;
- two sentences of `skills/settle/SKILL.md`;
- `settle.py#RULE_KEPT_HEADING`, which `settle` prints.

Two places still carry the emoji, and both are outside this item.
`skills/audit/SKILL.md:53`'s `Passed` line is an audit report's, which
no check reads (#957's §*Marks and labels*). `publish_release_note.py`'s
release-note headings are output for people (#957's Q9). The plan's
coordinates had moved: `templates/config.md:134`, not `:139`, and the
messages are at `:1654`, `:1771` and `:1778`, not `:1675` and `:1792`.

**The pins, enumerated.** For each sentence changed, `git grep -n -F` over
`tests evals` of: `closed by marking it`, `never by deleting the row`,
`bare check mark`, `ticked checkbox`, `beside a check mark`,
``drained` line and a``, `that closes a row`, `naming where it went`,
`with what closed it`, `also stays in the release branch`, `by marking it`,
`the row keeps the item`, `by being marked`, `Re-add the row`,
`every recorded item carries`, `check mark`, `An unmarked row`,
`Anything unmarked`, `prefix the Item cell`, `Nothing else relaxes`,
`leaves by being closed` (executed). The one pin found is
`test_the_skill_states_the_closing_convention`'s
`closed by marking it, never by deleting it`, which the skill keeps. Three
other modules read `uc.CLOSED` or carry a closed fixture row:
`tests/test_the_pull_request_language_is_the_repositorys.py` derives the
literal and now finds `` `closed` `` in `templates/config.md`, and the
fixtures in `tests/test_a_process_record_drop_passes_the_readers.py` and
`tests/test_settle_reads_before_it_removes.py` open with the word. Then
every test module naming any changed file, `unverified_check`, an
`overview.md` or the settle, verify or implement skill was run: 61 modules
(the `git grep -l` is in the verification below).

**The cases this phase added or changed, and how each was seen red.** In
`tests/test_unverified_rows_close.py` (T4; the plan's
`test_the_unverified_record_is_readable.py` does not exist, and this is the
module that owns the reader):

- `TestClosedRow::test_the_word_closes_and_the_mark_and_the_bare_word_are_refused`,
  over twelve rows;
- `TestClosedRow::test_the_old_marks_refusal_names_the_edit`, the
  refusal pinned whole (§14);
- `TestClosedRow::test_a_base_closed_with_the_old_mark_is_still_compared`;
- `test_no_text_that_states_the_closing_shows_the_old_mark`, over the eight
  texts above;
- `test_the_template_shows_the_word`;
- the existing closing cases moved to the word:
  `test_a_marked_row_counts_closed_and_keeps_its_text`,
  `test_a_bare_closing_word_does_not_close_anything`,
  `test_an_invisible_character_does_not_turn_a_bare_word_into_a_closing`,
  `test_closing_a_row_passes_the_baseline` and the retirement fixture
  `CLOSED_SECTION`.

Against the reader as it stood (unchanged since 401cbb67), 23 ids were red
(executed). They were every
closing and refusal row of the new parametrised case, the edit pin, all
eight text cases, the template case, the two moved closing cases and the
retirement case. The controls (`closed-loop`, `enclosed`) and the base case
passed there, as they should. The base case guards the relaxation this
phase adds, so it was seen red by a break. Then `mutation-check`, one break
at a time, all executed and all `red`:

| Unit | Break | Cases |
|---|---|---|
| `parse_section` | the old mark accepted in the working tree (`and False`) | the edit pin |
| `parse_section` | the base relaxation dropped (`and strict_header` removed) | the base case |
| `parse_section` | a bare word accepted (`if not rest` → `if False`) | the bare cases, six ids |
| `parse_section` | the word read case-insensitively | `[capitalised]` |
| `parse_section` | the near spellings read without `rstrip(NEAR_CLOSED)` | `[with a colon]` |
| `closing_word` | the cell split on a space alone | `[the word, a tab, the item]` |
| `parse_section` | the refusal's suggested row without the item | the edit pin |

**Verification.** On the tree committed as 6bceef00, all executed:
`bin/test` over `tests/test_unverified_rows_close.py`,
`tests/test_settle_reads_before_it_removes.py`,
`tests/test_a_process_record_drop_passes_the_readers.py`,
`tests/test_the_pull_request_language_is_the_repositorys.py` and
`tests/test_docs_line_wrap.py`, exit 0, 431 passed. The 61 modules from
`git grep -l -E "the-record-layout\.md|sdd-overview|skills/settle|settle\.py|skills/verify/SKILL\.md|templates/config\.md|skills/implement/SKILL\.md|unverified_check|overview\.md|…" -- 'tests/test_*.py'`
gave exit 0, 3,188 passed and 9 skipped. `unverified-check seal/specs/
--baseline origin/release/v0.22.1` gave exit 0. `bin/rules --check` gave
exit 0, *all 415 `Enforced by:` targets in 60 rule files resolve*.
`uvx ruff check` and `uvx ruff format --check` over the five changed Python
files gave exit 0.
