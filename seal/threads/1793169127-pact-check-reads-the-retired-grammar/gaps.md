# Overview: 1793169127-pact-check-reads-the-retired-grammar

## Why this work exists

`seal pact` read two tables with grammars of its own, so a map line the
walk did not read vanished silently and a mistyped pact anchor needed a
second grammar to be named; both are now read by the one table walker, or
refused.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| A second map header the walk already refuses | `design.md` *Scope* item 1: "a second `\| Remote \| Path \|` header in the file, named at its line". The code names it in its own sentence only where the walk refused nothing; where the walk refused, its stray-row sentence names that line | The code | The walk's sentence already says "it and every row below it would go unread", so a second sentence would print one fault twice. `hooks/lib/config.py#read_table` takes the same course for the old pact header: it is "not added where the walk's stray-row refusal already names the old header" |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, through `seal gate` after the review rounds settle |

## Not done

nothing

## Fed back into the spec

none
