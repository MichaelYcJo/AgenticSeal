# Feature Specification: the mechanics leave before the agents are rewritten (#964)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

This frame is #957's, split. The owner answered #957's Q1 on 2026-10-16: two
work items, this one first. What is here is #957's phases 0, 1, 2 and 8 as
they were framed (commits 50520644 and e81e7017 on
`chore/957-every-agent-is-written-anew-from-its-job`), moved and renumbered,
with nothing redesigned. #957 keeps the agents, the contract, the skills and
the paid proof at
`seal/specs/1792126889-every-agent-is-written-anew-from-its-job/`.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The rule a mechanism is kept against — subtract before you add* | The census and the stamps are lists kept beside the tree to stay in step with it, and they leave. The round record's grammar is stated once, where the check reads it. A change rewrites in place and removes what stood on the old fact in the same commit, which is every phase's closing check |
| `CLAUDE.md` §*The goal a design is chosen against* | No step of this item asks a person mid-run. Every phase is verified by CI alone; no paid run is spawned |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The item removes two gates (the census, the rider check) and changes two (the chain check's grammar reading, the unverified check's closing mark): each names what it caught against its cost, its failure direction, a prompt budget of zero and its `## Removes` rows. Its own bullet *A `Reads:` line on every unit* leaves with the census |
| `docs/the-review-record.md` §*The round record* | The record's grammar, stated here in prose over five paragraphs, becomes one table this document holds and the check reads. Its other sections are #957's |
| `docs/the-reader-registry.md` | Its census rules leave with the census. §*A frame names what its work removes* stays and is this file's `## Removes` |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | The changelog is this item's `changelog.md` fragment. The document's sentence on the closing mark is rewritten to the word |
| `skills/implement/SKILL.md` §*3. The SDD file set* | The item changes a gate's verdict and the word a smith writes into `overview.md`, so it sits on the top rung and this frame exists |
| #964's body (the owner, 2026-10-16) | The one source for what was decided: four numbered items, what is out of scope and how it is checked. Where this file and that body differ, the body holds |
| #957's body, items 3 and 5 (the owner, 2026-10-13 to 2026-10-16) | The census and the grammar table were decided there and now point here. #957's frame is where the rest of that body is read |

## Scope

**In.** The red case on Windows on `main` at the release and the two stale
sentences of the evaluation harness (§*The tree as it stands, measured*),
because every pull request of this item runs the suite they are in. The
`Reads:` census and the rider stamps. The round record's grammar as one
table the check reads whole. The closing mark of `## Not verified` as the
word `closed`, with the four 0.22.0 items' overviews rewritten once. The
test modules this item writes, re-points or deletes, and the changelog
fragment.

**Out, and whose.** The five definitions under `agents/`, the contract, the
four skills the `skills:` lists inject, the baseline and the per-phase paid
proof, the proof block, the batching numbers, the `U+2B1C` question status
and the parity verdict emoji — #957, which builds on the tree this item
leaves. The `Enforced by:` label keeps its spelling in every file this item
writes, because its rename is #941's with `rules.py` as its reader. The test
suite's layout beyond the modules this item writes — #942. The audit of
every reader of written text — #956; the `Reads:` lines were a
self-declaration and not that audit's input, so removing them takes nothing
from it. The emoji in output a script prints for a person and no agent or
check reads — the release note's headings, the seal stamp's drawing, the
hooks' terminal messages — stay where they are, by the owner's answer to
#957's Q9 (2026-10-16). The quotations of old marks inside test fixtures and
inside the four 0.22.0 items' round records stay as the history they quote
(#923's Q10). The other red case of run 38852872472, in the sealer tests, is
#963's and already fixed.

## What the referenced issues already decided

What each referenced issue decided is one table, #957's `spec.md`
§*What the referenced issues already decided*: it holds all eight issues
because #957 acts on all eight and this item on six. Until #957 merges it is
on #957's branch
(`git show chore/957-every-agent-is-written-anew-from-its-job:seal/specs/1792126889-every-agent-is-written-anew-from-its-job/spec.md`).
This table holds only what this frame does with each.

| Issue | What this frame does with it |
|---|---|
| #923 (closed, 0.22.0) | The grammar table restates the shape #923 chose in one place and changes no label or value; the three shapes that leaked in its rounds stay as fixed cases; its Q10 (old quotations stay) holds here |
| #929 (closed, 0.22.0) | No generated-variant or mutation case is written for the grammar (`plan.md` Alternative E, the owner's decision); the `mutation-check` runs in `plan.md`'s Verified-by cells are the smith's own narrow runs at its phase, never a CI job |
| #931 (closed, 0.22.0) | Nothing here refreshes `.test_durations` by hand. Where phase 2's deletions leave entries of cases the suite no longer collects and the durations case fails, the smith prunes to the collected ids by the method #923's phase 5a used, and nothing is re-measured |
| #941 (open, 0.22.2) | The grammar table goes into `docs/the-review-record.md` under §*The round record*, which `chain_check.py#grammar` finds by that heading; a #941 split that moves the heading meets exit 2 in CI and moves the loader's path with it. `Enforced by:` keeps its spelling |
| #944 (closed, 0.22.0) | Nothing kept beside the tree comes back: the census and the stamps are the class #944 removed and leave. `rider_check.py` is one importer of the coordinate kernel and leaves; the kernel at `skills/verify/scripts/coordinates.py` stays for its other readers |
| #956 (open, 0.22.4) | The grammar loader and the `closed` reader fail closed as #923's record does; the `Reads:` lines this item removes were a self-declaration, not the audit's input, which is the code |

## Marks and labels

The owner's rule (2026-10-16, #964's body item 4 and #957's body): a mark or
label an agent writes or a check reads has a reader that decides something,
or it leaves; what stays is one lowercase plain-English word at the start of
a line, exact spelling only, anything else refused; no emoji anywhere an
agent writes or a check reads. The marks this item disposes of, with their
readers (`executed` where a count is given; an emoji is named by its code
point so that this file carries none). Every other mark in the tree is a
row of #957's `spec.md` §*Marks and labels*.

| Mark | Written by | Read by, and what it decides | Disposition |
|---|---|---|---|
| `U+2705` closing a `## Not verified` row of `overview.md` (`templates/sdd-overview.md:38`) | the smith or the session, on closing an item | `skills/verify/scripts/unverified_check.py#CLOSED`, a gate in `hygiene.yml` that fails a pull request whose rows left unclosed | becomes the word `closed` as the first word of the row's first cell, read fail-closed; the rows of the four 0.22.0 items' overviews are rewritten once by a one-shot script in the same commit (`questions.md` Q2, answered) |
| The `Reads:` docstring line (364 lines in `.py` files, 31,055 bytes, `executed`) | every unit of shipped Python | `tests/test_a_reader_declares_its_input_class.py`, which leaves (§*The census and the stamps leave*) | leaves with its reader, by a one-shot script, in the same commit |
| The rider stamp `Verified <date> against <anchor>@<hash>` on 55 `RIDER:` comments in 20 files (`executed`) | whoever runs `rider_check.py --reverify` | `.github/scripts/rider_check.py`, exit 2 in CI on a drifted hash | leaves; the `RIDER:` comment stays as a comment with no stamp and no checker, and `seal/follow-up.md`'s header says so |

## The census and the stamps leave

`tests/undeclared_readers.txt` (994 lines, 49,722 bytes) keys every unit
undeclared at the rule's landing by a hash of its source, so a comment edit
asks for a new declaration; `.github/scripts/rider_check.py` (889 lines)
stores a hash and a date per rider and asks for `--reverify` whenever the
unit moves. Both are a list kept beside the tree to stay in step with it,
and both leave with what stood on them: `tests/test_a_reader_declares_its_input_class.py`
(866 lines, 38.4 s of the suite's 3,371 s at d4552372, `executed` from
`.test_durations`), `tests/reader_registry.py` (536), the stamp cases of
`tests/test_a_rider_reaches_its_file.py` (798 lines; its cases over
`seal/follow-up.md`'s rows stay), `CONTRIBUTING.md`'s census bullet,
`docs/the-reader-registry.md`'s three census sections and its *What neither
check can read* list, `seal/follow-up.md`'s four stamp paragraphs, the
`Reads:` lines, the 55 stamps, and `test.yml`'s *Not shallow* comment where
the rider test was its reason. The question the census was built to answer,
which way a reader fails on an input it cannot read, is #956's audit, which
reads the code and not a self-declaration.

Both were gates: the census failed a pull request whose changed unit did not
declare, and the rider check exited 2 on a drifted hash. What each caught:
the census caught a declaration missing, never a reader failing the wrong
way (the four misses of #923's check all carried a `Reads:` line); the rider
check caught drift on one fix pass of #923 (the smith's own account, `read`),
and the drift it reported was a comment edit.

## The record's grammar is one table

`docs/the-review-record.md` §*The round record* states the grammar in prose
over five paragraphs, `templates/sdd-round.md` restates every label and
value in its comment, `templates/config.md` §*What no row governs* lists the
literals a third time, and `chain_check.py` holds the regular expressions a
fourth (`SEVERITY` … `RECORD_TARGET`, `EXACT_LABEL`, `MISSPELT_LABEL`,
`TARGET_VALUE`, `LOCATION_VALUE`, `REFERENCE`, `FIXED_VALUE`,
`DEFERRED_VALUE`, lines 93–191 at d4552372). Three refusals of #923 were
added one at a time after a review found each shape leak, because the labels
were strict while parts of the value and heading reading were lenient.

**The grammar is one table in `docs/the-review-record.md`, and the check
reads it.** One row per line kind: the label, the exact shape of the value
as a regular expression that must match the whole line, where the line may
stand, how many a finding or a record may hold, and what the refusal says.
`chain_check.py` loads that table from the document at its own relative
path, as it already locates `hooks/routing.py`, and matches each line
against the row whole; a table it cannot read, or a document it cannot find,
is exit 2 naming the file, never a pass. In a user's repository the hygiene
template clones this repository into `$RUNNER_TEMP/specseal` and runs the
check from there (`templates/hygiene.yml:59, 92`, `read`), so the document is
beside the script wherever the script runs. The template's comment and
`templates/config.md` point at the table and restate nothing; the language
test derives its literal list from the table. The shapes that leaked —
a `path#unit` coordinate, a heading with no number or a repeated one, a
relation label with no value — stay as fixed example cases (T32, T33, T35,
T36 of #923, re-pointed at the table), and no generated-variant or mutation
case is written for the grammar (#929's finding, the owner's decision).

## The tree as it stands, measured

Read at d4552372, the 0.22.0 release; `executed` where a command produced
the number, `read` where a document or a CI log did. #957's frame measured
the tree once, and the readings are split by the phase that acts on each:
the definitions, their preloads, the test pins on them, the `§N` citations,
the `Enforced by:` lines, the emoji by directory and the evaluation's case
counts stay in #957's `spec.md` §*The tree as it stands, measured*. The
suite's size and CI cost are here, because this is the item that changes
them and it merges first, so #957 reads them from the tree.

- **Marks** (`executed`): `Reads:` lines 364 (31,055 B).
  `undeclared_readers.txt` 994 lines. `RIDER:` comments 55 in 20 files.
  `U+2705` is read by one gate, `unverified_check.py#CLOSED` (line 75),
  called at `:823` and in two messages at `:1675` and `:1792`.
- **Suite and CI** (`executed` from `.test_durations` and the job list of
  run 38850511000, the last green `tests` run, 2026-10-16): 7,329 cases
  priced at 3,371 s; one run is ubuntu 5.0 min, three macOS shards 13.1 min,
  four Windows shards 35.5 min, lint and durations 1.5 min — 55 runner
  minutes, wall under 11 minutes, and 208 billable minutes a run if the
  repository went private (Linux 1×, Windows 2×, macOS 10×). The census
  module is 38.4 s of that and the rider module 3.5 s.
- **The release tree is red on one case this item owns** (`read`, the log of
  run 38852872472 on `main` at d4552372):
  `tests/test_a_rewritten_definition_proved_non_inferior.py::test_a_side_runs_the_tree_it_measures_and_no_installed_plugin`
  fails on Windows on path separators. Every pull request of this item runs
  it, so it is phase 1. The same run's other red case,
  `tests/test_the_sealer_guarantees.py::test_a_verdict_other_than_sound_fails_a_ready_pull_request`,
  is fixed outside this item by #963 (no work item, into
  `release/v0.22.1`): under `GITHUB_ACTIONS` the check prints `::error`
  annotations and the case searched for the plain `<rel>:` line, so the
  fixture now clears the variable. This frame does not touch it.
- **The evaluation harness** (`executed`): `evals/README.md` names a
  `--list` flag `rule_cases.py` does not have (unrecognized arguments), and
  #923's `overview.md` says `replay_targets.py` reads a paragraph new
  records do not carry (`read`). The cases, their counts and their cost are
  #957's.
- **The check** (`executed`, `wc`): `chain_check.py` 1,707 lines;
  `docs/the-review-record.md` 350.

Every figure above is a reading at d4552372, and `plan.md`'s rows that quote
one say so. A phase that acts on a figure re-reads it at its own commit, and
nothing recounts a figure by hand into the changelog.

## User scenarios & acceptance *(mandatory)*

Each row says what it protects: the defect it would catch, and why no other
case does.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The tree is green first | Given the Windows-red case of run 38852872472, when phase 1 closes, then it passes on all three legs and `replay_targets.py` reads the new record's shape | CI green on the phase-1 commit; `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_evals_layout.py -q` exit 0. Protects: #957's baseline run and every later pull request red on a defect that predates them |
| S2 The census is gone | Given the tree, when `git grep -n "Reads: "` runs over `*.py`, then nothing matches, and `tests/undeclared_readers.txt`, `tests/reader_registry.py`, `tests/test_a_reader_declares_its_input_class.py` are not tracked | the grep in the phase record, `git ls-files` for the three paths, `bin/rules --check` exit 0 with the census paragraphs gone. Protects: a stored list coming back beside the tree |
| S3 The stamps are gone | Given the tree, when `git grep -n "Verified .* against"` runs over the 55 riders, then nothing matches; `rider_check.py` is untracked; `tests/test_a_rider_reaches_its_file.py` keeps its follow-up cases and no stamp case | the grep, `git ls-files`, the module's collection. Protects: a hash kept beside the tree |
| S4 One grammar, read whole | Given the table in `docs/the-review-record.md` §*The round record*, when `chain_check.py` loads, then it reads the table into its line readers and refuses a line that does not match a row whole; a table it cannot read is exit 2 naming the file | `tests/test_chain_check.py::TestGrammar` (new): the table loads; a row's regex matches the template's example lines whole; `verdict: fixed abc1234 and more` is refused; a document with a broken row exits 2; the module's constants equal the table's rows. Protects: a fourth statement of the grammar drifting, and a partial match letting a shape through, which #923 met three times |
| S5 The leaked shapes stay as cases | Given the grammar reader, when the three shapes that leaked in #923 are read, then each is refused by name | T32, T33, T35 and T36 of #923 re-pointed at the table, unchanged in what they refuse. Protects: the known leaks reopening under the new reader |
| S6 The closing word | Given an `overview.md` with a closed `## Not verified` row, when `unverified-check` reads it, then a row opening `closed` with what closed it is closed, a bare `closed` is refused, and `U+2705` is refused naming the row | the success and the failure case of `unverified_check.py`'s row reader, rewritten in its test module; the four 0.22.0 items' overviews pass the check after the one-shot rewrite. Protects: the emoji mark read by a gate, which is the class #923 found four times |
| S7 Every case is seen red and says what it protects | Given a test this item writes or changes, when read, then its docstring names the defect it would catch and why no other case does, and the phase record says how it was seen red | the warden's reading of the diff and of the phase record; `Enforced by: nothing — a reading from words is a report`. Protects: a case that passes against the very defect it was written for, which contract §15 records three times |
| S8 Rewritten in place | Given a fact this item removes, when the commit lands, then every sentence, pin, comment and copy standing on it leaves in the same commit, enumerated by the `git grep` the phase record names | `bin/rules --check` exit 0; `tests/test_no_passage_is_pasted_into_a_second_file.py` green; the greps in the phase record finding nothing outside `seal/specs/` and `changelog/`. Protects: the stale half of a file misleading the next agent, which is #957's root problem and the reason this item goes first |
| S9 Nothing asks a person | Given this item's run, when any phase executes, then no step stops for an answer; the two `questions.md` rows are answered before the first edit | `plan.md`'s rows read by the orchestrator; the sealer's step 4 reads the parties. Protects: a run that stops at minute thirty |

## Data & interfaces

- **The grammar table** in `docs/the-review-record.md` §*The round record*:
  `| Line | Shape | Where | How many | Refused as |`, one row per `target:`,
  `severity:`, `location:`, `verdict:`, `regression:`, `reopens:`, `answer:`,
  `confirms:` and the finding heading. `chain_check.py#grammar(path)` returns
  `{line: (compiled shape, where, how many, refusal)}` from the table and is
  called once at load; `records` reads through it; every former constant from
  `SEVERITY` to `DEFERRED_VALUE` leaves. Exit 2 names the document where the
  table is missing or a row does not parse.
- **The closing word**: a `## Not verified` row whose first cell opens
  `closed ` is closed; `unverified_check.py#CLOSED = "closed"`, the bare word
  refused as the bare mark was.
- **The harness**: `evals/scripts/replay_targets.py` reads the asked
  paragraph the new record carries, or none; `evals/README.md` states the
  generators' usage as it is, with no `--list`.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| `U+2705` as the closing mark | `skills/verify/scripts/unverified_check.py#CLOSED`, `templates/sdd-overview.md:38`, `templates/config.md:139`, `docs/the-record-layout.md` and `skills/implement/SKILL.md` §4's sentences, the four 0.22.0 items' `overview.md` rows | the word `closed`, read fail-closed; the old rows rewritten once by a script |
| The `Reads:` docstring lines | 364 lines in `.py` files under `hooks/`, `skills/`, `evals/`, `.github/scripts/`, `tests/` | nothing reads them once the census leaves |
| The census and its reader | `tests/undeclared_readers.txt`, `tests/reader_registry.py`, `tests/test_a_reader_declares_its_input_class.py` | #956 audits readers from the code |
| The census rules | `docs/the-reader-registry.md` §*The four classes*, §*Who declares*, §*The census*, §*What neither check can read*, §*The counts at landing*; `CONTRIBUTING.md:247-251` | §*A frame names what its work removes* stays as the document's one rule |
| The rider stamps and their checker | `.github/scripts/rider_check.py`, the stamp cases of `tests/test_a_rider_reaches_its_file.py`, the `Verified … against …@…` line of 55 riders, `seal/follow-up.md:27-47`, `.github/workflows/test.yml:110-112`'s comment | the `RIDER:` comment stays, unstamped; a rider outliving its fix is the reader's finding |
| The grammar's three restatements and the check's constants | `templates/sdd-round.md:3-14, 32-60`, `templates/config.md` §*What no row governs*' label list, `chain_check.py:93-191` | the one table in `docs/the-review-record.md`, which the check loads |
| The sealer case model note and the `--list` sentence | `evals/README.md:34-35` | the generators' usage as it is |

## Open questions → questions.md

Every decision the tree could make is made above with its grounds. The two
rows of `questions.md` were the owner's and are answered; nothing in this
item waits on a person.

Framed 2026-10-16 by framer, before the build.
