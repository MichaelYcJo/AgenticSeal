# settle squashes specs into docs/ in place (#953) — overview

## Why this work exists

`settle` applies the rule changes each released spec states to `docs/` in
place, so no session hand-writes policy prose beside a marker.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The section's grammar | `spec.md` *Data & interfaces*: `change · <file> §<heading> › "<text>" · <rule>`. Built: an operation line, then `file:`, `section:`, `from:`, `to:` one per line | the field words | the owner overturned Q1's assumption mid-build (2026-10-20, relayed by the orchestrator): "No unnecessary constants or symbols that break a reader or make it unable to read". `questions.md` Q1 records it. The scenarios S1–S8 keep their meaning; only their spelling in `spec.md` is the old one |
| Where `add` lands in a section with sub-headings | `spec.md`: "at the end of the named section". Built: at the end of the section's own text, before its first sub-heading | before the first sub-heading | spec silent on sub-headings; a rule placed after the last sub-section reads as that sub-section's |
| A spec with no `## Rule changes` | `spec.md` is silent on what `--apply` does with one. Built: named and kept, and not a refusal (exit 0) | kept, exit 0 | `--apply` would otherwise exit 1 on every run in this repository until #941 settles the backlog, and the cheaper mistake is keeping a directory |
| A case `## Removes` did not name | `tests/test_unverified_rows_close.py#test_the_shipped_skill_copied_into_docs_records_no_fold` was retired in phase 2 | retired | its premise was that `skills/settle/SKILL.md` shows a marker; the rewritten skill tells nobody to write one (S15) |
| How the settled predicate compares | `spec.md` *The settled predicate*: "Every text the replay leaves in place must be present at HEAD, and every text it took out must be absent there", with "A text the base already held twice is a limit". Built: each text an applied operation names occurs as often across `docs/` at HEAD as in the replay | the count | the same rule with its limit gone, and it also refuses a change whose old text was left beside the new; `docs/the-record-layout.md` states it |
| `tests/conftest.py#cutoff_item_is_traceable` | `spec.md` Scope 4: it asks the predicate. Built: removed | removed | it had no caller since #923 (`git log -S`), so Q5 had nothing to answer |
| A removal `## Removes` did not name | `unverified_check.py#work_item_of` | removed | its one caller was the marker arm; `seal.py` keeps its own |
| A document past the ceiling | `spec.md` S12: "it names the document and exits 1"; *The one-read row*: this repository declares 37,178 until #941. Built: named as one to split, exit 0, and this repository declares 25000 | the report | the owner's answer of 2026-10-20, relayed by the orchestrator after the spawn: "a report, not a gate". The estimate is a guess from bytes, 25,000 is one tool's per-call cap, and a section past it cannot be split along headings. The framer updates `spec.md` |
| The index's line shape | `spec.md` Scope 6: "Each line names one topic and its file". Built: each table row after a header | table rows | the record-layout table it replaces is a table; prose lines in the index stay prose |
| A removal `## Removes` did not name | `docs/the-record-layout.md` §*The fold, and what tells it from a deletion*'s line-ceiling statement and its two markers | removed with the statement | its rule was the freeze; §*The size a reader takes whole* holds the one-read rule |
| Two specs added by one commit at one place | `spec.md` *Merge order*: ordered "only where one adding commit is an ancestor of the other". Built: one commit is not its own ancestor, so the pair is a conflict | conflict | the spec's own words; nothing orders two paths inside one commit |
| Where the model is stated | `spec.md` S15: "each states the model". Built: the implement skill's lifetime row states it; the framer and both READMEs point to it | one home | `CLAUDE.md` "A fact has one source", and `tests/test_no_passage_is_pasted_into_a_second_file.py` refused the copies |
| The dated sections of `docs/one-root-by-lifetime.md` | the document: "The text above is a record of 2026-09-02 and is not rewritten". Built: the rows `## Removes` names, and the rest of their class, rewritten in place in both editions | rewritten | `spec.md` Grounding: "Both editions are rewritten in place where they state the old split" |
| Removals `## Removes` did not name | "a work item that finds it wrong corrects it" in `docs/measuring-a-run.md`, `docs/the-agent-set.md`, `docs/the-broad-gate.md`, `docs/the-pact.md`; the implement skill's §6 *Needs a decision* row | each points to `docs/README.md`, or names `## Rule changes` | the same class as `docs/the-record-layout.md:278`, which `## Removes` names |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, at the broad gate |
| Q4: whether bytes halved is a safe estimate for dense Hangul or symbol-heavy text | a measurement, now a report and not a gate, so a wrong estimate names a document or misses one and refuses nothing |

## Not done

- `questions.md` carries no row for the owner's 2026-10-20 answer on the ceiling, and Q5's Status is not written; the smith's definition names no write to that file. The orchestrator writes both.
- `spec.md` S12 and *The one-read row* still say exit 1 and 37,178; the framer updates them.
- `docs/worktree-guard-spec.md` and `docs/one-root-by-lifetime.ko.md` are past the ceiling and reported; #941 splits them.

## Fed back into the spec

*Inferred during implementation*; a planner may overturn each.

- The settled predicate counts each text an operation names, the `from`, the `to` and the section heading, across the policy root (`docs/the-record-layout.md`).
- An index row is a table row after a header, naming documents as backticked paths (`skills/settle/SKILL.md` §*The index*).
- A `Policy root` value that is empty, absolute or holds a `..` part reads as `docs` (`templates/config.md` §*The fold's values*).
