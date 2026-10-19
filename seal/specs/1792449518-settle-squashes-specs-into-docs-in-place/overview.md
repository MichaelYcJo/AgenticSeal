# settle squashes specs into docs/ in place (#953) — overview

## Why this work exists

`settle` applies the rule changes each released spec states to `docs/` in
place, so no session hand-writes policy prose beside a marker.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The section's grammar | `spec.md` *Data & interfaces*: `change · <file> §<heading> › "<text>" · <rule>`. Built: an operation line, then `file:`, `section:`, `from:`, `to:` one per line | the field words | the owner overturned Q1's assumption mid-build (2026-10-20, relayed by the orchestrator): "No unnecessary constants or symbols that break a reader or make it unable to read". `questions.md` Q1 records it. The scenarios S1–S8 keep their meaning; only their spelling in `spec.md` is the old one |
| Where `add` lands in a section with sub-headings | `spec.md`: "at the end of the named section". Built: at the end of the section's own text, before its first sub-heading | before the first sub-heading | spec silent on sub-headings; a rule placed after the last sub-section reads as that sub-section's |
| Two specs added by one commit at one place | `spec.md` *Merge order*: ordered "only where one adding commit is an ancestor of the other". Built: one commit is not its own ancestor, so the pair is a conflict | conflict | the spec's own words; nothing orders two paths inside one commit |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, at the broad gate |

## Not done

nothing

## Fed back into the spec

nothing
