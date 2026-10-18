# 1792251842-the-smith-is-written-anew-from-its-job — phase 3

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 7053c184 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Unattended and with no paid run. Give each of `## 문장 규칙` and
`## English prose rules` in `skills/writing-style/SKILL.md` one orientation
line naming `## 먼저`, `## 구성 규칙` and the per-document section, keep every
rule and heading, make the `U+1F534` the word `CRITICAL`, and rewrite the
line that lists *the smith's seal* to the fact after phase 2. Make
`templates/sdd-questions.md`'s `U+2B1C` the word `open` and its *ticked by
whoever answered* sentence *written by whoever answered, as `answered <date>
by <who>`*, and re-point its pin. Make the five marks of `skills/audit/SKILL.md`'s
result block the words `passed`, `warnings`, `violations` (`questions.md` Q3's
default). Plant T6 in place of the four-file emoji case, `legacy-parity`
skipped by name for #970, seen red on the tree first with the marks
recounted. Plant T7, deciding its home. Run `mutation-check` once per
mutation, `-p no:xdist`.

## What this phase found

**The frame's figure held when counted by code point.** The sweep over
`agents/*.md`, `skills/*/SKILL.md` and `templates/*.md` at ffb80d9c found 11
code points in 4 files: `skills/audit/SKILL.md` 5 (`U+2705` at line 53,
`U+26A0 U+FE0F` at 54, `U+274C` at 55 and 58), `skills/writing-style/SKILL.md:260`
`U+1F534`, `templates/sdd-questions.md:10` `U+2B1C`, and
`skills/legacy-parity/SKILL.md:91-94` 4. Outside `legacy-parity` that is 7 code
points in 3 files, on 6 lines, because `U+26A0 U+FE0F` is one mark on one line.
After the docs commit the sweep prints `legacy-parity`'s 4 and nothing else.

**T6 went red on the tree before any doc changed.** It failed on the 6 lines
above and passed the round-record case beside it (`1 failed, 1 passed`).

**Two `Enforced by:` lines named the case T6 replaces.**
`docs/the-review-record.md:19` and `skills/code-review/SKILL.md:132` both cite
`test_the_template_the_format_and_the_two_definitions_carry_no_emoji`, and
`bin/rules --check` reported both as unresolved once it left. Both now name
T6, whose corpus holds every file the old case read: `templates/sdd-round.md`,
`agents/warden.md`, `agents/smith.md`, and `skills/code-review/SKILL.md` whole
rather than its `## The record` section.

**The writing-style seal row now names what exists.** Its good column read
*the smith's seal · the sealer's seal · the warden's review mark*. Phase 2
took the smith's seal away: the smith hands back three labels, and the
sealer's `guarantee.md` is the one seal. The row reads *the sealer's seal ·
the warden's review mark · the smith's labels*, the phrase phase 2 gave the
README. Lines 232-233 (now 237-238) still say `seal` once meant the smith's
proof block, in the past tense, and they stay as history.
`skills/verify/SKILL.md:335`'s *the smith's seal read as though it did* is a
measured account of a past run, in the past tense, and it stays too.

**T7's home is a module of its own,
`tests/test_a_language_section_of_writing_style_opens_alone.py`.** The
payload meter's module tests what `payload_meter.py` computes and builds its
cases around that script. T7 reads no meter output. It reads what an agent
finds when it opens one section of `writing-style` by range, and which
headings an agent's `writing-style` step names.

**T7 checks the headings an agent names, not only the two it was asked
for.** It collects every `` `## …` `` span in an agent's list item or
paragraph that names `writing-style`, and requires each to be a heading of
the file. Today that is `agents/warden.md`'s two and `agents/smith.md`'s two,
the same pair. It also requires the warden to name both, so the collection
cannot pass by finding nothing.

**T6 refuses a stale skip entry.** Beyond the spec's map, the case fails when
the skipped file carries no mark any more, so `legacy-parity`'s entry has to
leave in the commit that repairs #970.

**The white square stands in 72 lines of 35 files outside T6's corpus**,
all of them code comments, docstrings and eval prompts citing a past round's
finding (`round 1's` followed by `U+2B1C` and a number). They are not text an agent reads as instruction,
the frame did not name them, and they stay.

**`.test_durations:5897` still names the replaced case.** The file is
measured on Windows and rewritten by CI, so this phase leaves it.

### The cases, each seen red

T6 was seen red on the tree first, as above. Then each mutation below ran
through `mutation-check` after its case's commit. Each read `red: the cases
failed against the mutation (exit 1)`, exited 0, and left `git status` clean.

| Case | Mutation (the plan's row) | The assertion that went red |
|---|---|---|
| T6 `tests/test_the_record_is_written_in_words.py::test_no_file_an_agent_reads_carries_an_emoji_or_a_proof_block` | `U+2705` planted in `agents/warden.md` step 6 (the `agents` glob) | `agents/warden.md:40: 6. … Before writing the record` |
| T6 | `open` made `U+2B1C` in `templates/sdd-questions.md` (the `templates` glob) | `templates/sdd-questions.md:10` |
| T6 | `U+2705` planted before `passed:` in `skills/audit/SKILL.md` (the `skills` glob) | `skills/audit/SKILL.md:53` |
| T6 | the line `audit applied` planted under `## Output Format` (the `applied` pattern) | `skills/audit/SKILL.md:50: a proof block: audit applied` |
| T6 | a bare `U+FE0F` after `warnings` (the selector in the range) | `skills/audit/SKILL.md:54` |
| T6 | the skip map's `#970` emptied (a skip naming no issue) | *the skip entry for skills/legacy-parity/SKILL.md names no issue* |
| T7 `tests/test_a_language_section_of_writing_style_opens_alone.py::test_each_language_section_of_writing_style_opens_alone` | `## English prose rules` retitled `## English prose` | *lost the heading '## English prose rules'* |
| T7 | `## 문장 규칙`'s first paragraph stops naming `` `## 구성 규칙` `` | *its first paragraph does not name ['`## 구성 규칙`']* |
| T7 | `agents/warden.md` names `## 문장 규칙들` | *agents/warden.md's record step no longer names both language sections* |
| T7 | `## 리뷰 코멘트에만 해당하는 것` retitled | *its first paragraph points at '## 리뷰 코멘트에만 해당하는 것', a heading the file does not have* |

The `applied` mutation first reported line 49, the blank line above the
planted one: the pattern's leading `\W*` crossed a newline under
`MULTILINE`. 7053c184 stops it at the line's start, and the re-run reported
line 50. The last T7 mutation was refused once, because its first `OLD`
occurs three times in the file; the run that counted anchored it with the
newlines around the heading.

### Sizes, recounted from the tree

| File | ffb80d9c | 7053c184 |
|---|---|---|
| `skills/writing-style/SKILL.md` | 21,000 | 21,720 |
| `templates/sdd-questions.md` | 1,934 | 1,967 |
| `skills/audit/SKILL.md` | 1,913 | 1,905 |

`bin/payload-meter --root <checkout> --agent <a>` at 7053c184, totals with
the 13,318 B `CLAUDE.md` pair, estimated at 3.2 B/token:

| Agent | Phase 1 (2fc33333) | Phase 2 (aea8c8e5) | Phase 3 (7053c184) |
|---|---|---|---|
| smith | 104,046 | 39,982 | 39,982 (12,495 tokens) |
| warden | 40,516 | not measured | 40,516 (12,662 tokens) |
| framer | 102,762 | not measured | 99,739 (31,170 tokens) |

The warden opens `writing-style` at its record step rather than preloading
it, so its preload did not move. The framer preloads `implement` and
`writing-style`: its 99,739 holds `implement` at 28,485 after phase 2 and
`writing-style` at 21,720 after this phase.

### Commands, each with its exit code

Read directly with `; echo $?`, never through a pipe. `<mods>` is the modules
`git grep -l -E "writing-style|sdd-questions|audit/SKILL|test_the_record_is_written_in_words" -- tests`
names (7, T7's module among them), plus `test_the_record_is_written_in_words`,
`test_a_question_says_who_can_answer_it`,
`test_no_passage_is_pasted_into_a_second_file`,
`test_the_payload_meter_says_what_it_measured`, `test_docs_line_wrap` and
`test_one_word_one_meaning`: 9 modules once deduplicated.

| Command | Exit |
|---|---|
| the sweep over the three globs, at ffb80d9c | 0: 11 code points in 4 files |
| `bin/test tests/test_the_record_is_written_in_words.py -q -p no:xdist`, T6 on the tree before the docs step | 1: 1 failed, 1 passed |
| `bin/rules --check --root <checkout>`, after T6 replaced the case | 1: 2 of 480 targets unresolved, the two `Enforced by:` lines above |
| `bin/test` T7's module, the words module and the questions module, `-p no:xdist` | 0: 9 passed |
| `mutation-check`, ten runs as tabled above, `-p no:xdist` | 0 each, `red` each |
| `mutation-check` on `## 리뷰 코멘트에만 해당하는 것` unanchored | 2: refused, `OLD` occurs 3 times, nothing written |
| `bin/test <mods> -q` | 0: 245 passed |
| `bin/rules --check --root <checkout>` | 0: all 480 targets in 60 rule files resolve |
| `uvx ruff check` and `uvx ruff format --check` on the 3 changed `.py` files | 0, 0 |
| the sweep over the three globs, at 7053c184 | 0: `skills/legacy-parity/SKILL.md` alone, 4 code points |
| `bin/payload-meter --root <checkout> --agent <a>` for smith, warden, framer | 0 each |
