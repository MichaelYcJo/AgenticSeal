# The dash shapes become field words (#1000) — overview

## Why this work exists

Every line an agent writes and a check reads now spells its parts with field
words, so a hyphen typed for a dash is refused at its line instead of read as
something else.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| What moves into `unverified_check.py` | `spec.md` Scope 1: "The block's word, field and continuation are spelled once in code". Built: the item line, the field line, the continuation indent and the field checks moved too (`items`, `field_values`), and `rule_changes.py` reads its operations through them | moved | the block is read by the item grammar, so leaving that grammar in `rule_changes.py` would spell the field line and the continuation twice (`phases/phase-1.md`) |
| The near-miss message of `## Rule changes` | `rule_changes.py#NO_CHANGE_WRITTEN` said "a spec that changes no rule writes the block". Built: one message for both sections, "a section that holds nothing writes the block `- nothing` with `  why: <reason>`" | one message | spec silent; one reader of the block cannot word its refusal for one section, and `tests/test_settle_applies_rule_changes_in_place.py#NO_CHANGE` pins the new text |
| Where a `- nothing` after an operation is refused | Before: at the first operation. Built: at the `- nothing` line | its own line | spec silent; the block is what is out of place, so its line is the one to edit |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck over the phases built | the orchestrator's broad run |

## Not done

nothing

## Fed back into the spec

none
