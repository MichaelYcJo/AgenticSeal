# Overview: 1792926874-the-records-carry-no-comment-and-the-readers-drop-it

## Why this work exists

The records under `seal/specs/` lose the template comments they carried, and the readers of a record lose the comment state that produced three reader defects in 0.22.3; a record line that begins with `<!--` is refused at its line by the reader that reads it.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| How many record files the strip changes | `spec.md` *Scope* item 1 and *Removes*: "273 of them outside every fence, in 208 files". The strip changed 173 files | 173, the reader's count | The frame's awk count included `routing.md`, which *Scope* item 5 keeps: 35 `routing.md` files hold a comment, and 208 less 35 is 173. The shared reader at the phase base, skipping fenced lines, finds comments in 173 files that are not `routing.md` (executed, `phases/phase-1.md`) |
| How many specs the strip changes | `spec.md` S11 and `plan.md` row 1: "the 41 `spec.md` files the strip changes". The strip changed 40 | 40 parsed for S11, and all 42 parsed besides | 41 is the count of work items the backlog settle left. Of their specs, `1792627930-the-section-sign-is-still-syntax/spec.md` quotes `<!--` only in code spans, so the strip leaves it as it is (executed) |
| How many inline comments the strip removes | `spec.md` *Scope* item 1: "Five are bare inline comments, `<!-- NAME NOT IN TREE -->`". The strip removed 11 | 11, every one the reader found | The marker stands on 11 lines of `seal/specs/1791384158-the-broad-gate-reads-its-counts-from-the-recorder/`, 10 in `spec.md` and 1 in `plan.md` (executed: the strip's own list of removals that start after a line's first character) |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and format check, at the branch head | the orchestrator, through `broad-gate` after the review rounds settle |

## Not done

A strip command for a consuming repository's records was not built: `questions.md` Q1 is the owner's, and its default (a) ships none.

## Fed back into the spec

none
