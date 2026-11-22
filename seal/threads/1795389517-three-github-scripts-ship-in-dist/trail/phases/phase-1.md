# Phase 1: 1795389517-three-github-scripts-ship-in-dist

## What this phase found

**The frame held, with three departures.** Each was judged against `frame/design.md` and the tree at `e9d4dc406`.

- **The `MERGED_PR` cases are two assertions, not a class.** *Scope* item 5 and the `## Removes` row name "`Test_keywords_in` and the `MERGED_PR` cases". At `036e7d424` the two `MERGED_PR` assertions stand inside `Test_keywords_in::test_accepts_only_a_keyword_before_a_number`, so the class moved whole and nothing else left `tests/github/test_close_issues_on_release.py`.
- **`docs/releasing/issues-and-milestones.md:320` swaps one file for the other.** *Scope* item 11 says that check line names `tests/lib/test_closing.py` "too". Its rule is the masking of a fence, a span and a comment. Every case holding that rule moved to `tests/lib/test_closing.py`, and no case left in `tests/github/test_close_issues_on_release.py` holds it. So the line now names `tests/lib/test_closing.py tests/github/test_issue_claims_check.py`, judged against `skills/settle/rule-changes.md` *A rule has one shape*: a check line names the case that holds its rule. `docs/releasing/branch-and-release.md:409` adds `tests/lib/test_closing.py` beside the closer's file. Its rule covers reading the `(#N)` of a squash subject, which `MERGED_PR` reads, and the closer's fallback cases, which stay.
- **The `_closer` helper stays in the closer's test file.** `Test_main` still calls it at three cases, so only `Test_keywords_in` left. The new file defines its own `_closer` loader over `lib/closing.py`. The name is kept so each moved case body stands as written (`frame/questions.md` Q1's default).

**Decisions settled while writing the code.**

- `pr_body.py` keeps the name `CLOSER` for the module it now loads from `lib/closing.py`. *Scope* item 2 says "`CLOSER` becomes the new module", and a rename would change six use sites and their docstrings for no reader. `chain_check.py` binds the module as `CLOSING`, after its own convention of naming a loaded module by its stem (`BLOCKS`, `GITCMD`, `OPTIN`).
- `chain_check.py` loads `lib/closing.py` at import, inside the one `try` that loads its other readers. So `tests/skills/test_chain_check.py#copied_tree`, which copies the files the check loads at import, now copies `closing.py` too.
- `publish_release_note.py`'s comment on why a title's trailing `(#N)` goes was moved from the removed `TRAILING_REF_RE` to the one line that strips it.
- Comments and docstrings that placed the readers in the closer were re-pointed to `lib/closing.py`. They stand in `issue_claims_check.py`, `label_merged_on_release_branch.py`, `release_completeness_check.py` (`:100`, which now names the closer's `run` and `gitcmd`), `publish_release_note.py`, `pr_body.py`, `lib/lines.py:41`, `.github/workflows/hygiene.yml:47`, `tests/skills/test_pr_body.py:600`, `tests/github/test_issue_claims_check.py:129` and `docs/releasing/issues-and-milestones.md:214` and `:318`. Each only names where the readers stand, so none is a rule change, as `frame/design.md` *Grounding* reads `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*.
- Two existing cases changed what they hold and were renamed. `test_the_readers_come_from_lib_closing_rather_than_a_second_copy` in `tests/github/test_label_merged_on_release_branch.py` reads `"lib/closing.py"` in the script's source. `test_the_check_imports_the_one_definition_rather_than_restating_it` in `tests/github/test_issue_claims_check.py` reads `sys.modules["closing"]`.

**`frame/questions.md` Q1, answered by the work: refused.** Executed: `bin/seal layout --moved 036e7d424 --from tests/github/test_close_issues_on_release.py --to tests/github/test_close_issues_on_release.py tests/lib/test_closing.py`, exit 1. Last line: `seal layout: moved: 47 old cases, 48 items against 48 at 036e7d424490, 6 failed`. The count and body conditions held for all six moved cases, and each failed on the names condition alone: `name _closer: its definition differs from the base's`. The loader has to name a new path, so no form of the move passes. The mutation table below stands in its place, as `CONTRIBUTING.md` *The test layout* asks.

**`frame/questions.md` Q2, answered by the work: not derived, so the row goes.** Executed: `bin/test tests/behaviour/test_every_entry_point_runs_at_the_floor.py -q -p no:xdist` with the row still in `ruff.toml` failed with ``ruff.toml lints ['.github/scripts/close_issues_on_release.py'] as if a floor-less run reached them``. With the row removed it passed.

**Mutation table for `lib/closing.py`.** Executed at `e9d4dc406`: one `bin/seal mutate lib/closing.py` call, 14 mutants, tests `bin/test tests/lib/test_closing.py -q -x -p no:xdist`. Last line: `seal mutate: 14 mutants, 13 red, 1 SURVIVED, 0 with no verdict (3.6s)`.

| # | Unit | Mutant | New file | Old files |
|---|---|---|---|---|
| 1 | `KEYWORDS` | drop `"closes"` | red | not run |
| 2 | `CLOSING` | `re.IGNORECASE` to `0` | red | not run |
| 3 | `CLOSING` | drop the `\b` after `(\d+)` | SURVIVED | read: an old gap (below) |
| 4 | `MERGED_PR` | drop the `\s*$` anchor | red | not run |
| 5 | `FENCE` | backtick fence only | red | not run |
| 6 | `FENCE` | no leading indent | red | not run |
| 7 | `FENCE` | `\1` to either delimiter | red | not run |
| 8 | `COMMENT` | drop the unclosed-opener arm | red | not run |
| 9 | `COMMENT` | drop the list and quote markers before an opener | red | not run |
| 10 | `COMMENT` | drop the `(?!.*?-->)` lookahead | red | not run |
| 11 | `SPAN` | drop the double-backtick arm | red | not run |
| 12 | `SPAN` | the double arm holds no single backtick | red | not run |
| 13 | `HIDDEN` | drop `COMMENT` from the union | red | not run |
| 14 | `keywords_in` | read the body unmasked | red | not run |

Mutant 3 is an old gap. Read, not run: the six moved cases' bodies are unchanged (the move check's body condition held), and the base closer's `CLOSING` is the same pattern, so the old file misses it too. A body like `Closes #12abc` would tell them apart. `gaps.md` *Not done* records why no case was written for it.

**Mutants of the other units that changed behaviour.** Each executed at `e9d4dc406`:

- `MERGED_PR`'s leading `\s*`, the one change the pattern gained. Removed, `bin/test tests/github/test_publish_release_note.py tests/lib/test_closing.py -q -x -p no:xdist` went red, exit 1. The fixture title `fix(gate): and a second thing (#103)` then keeps a trailing space, and the note's expected line differs. So the `sub` that replaced `TRAILING_REF_RE` is held by a case of its reader.
- `chain_check.py#carried_by`'s subject test, two mutants in one call, `-k Test_carried_by`. Last line: `seal mutate: 2 mutants, 2 red, 0 SURVIVED, 0 with no verdict (5.7s)`.

**Seen red (contract rule 15) for the two cases that changed what they hold.** Each was run with only the guard it names removed:

- `test_the_readers_come_from_lib_closing_rather_than_a_second_copy`: `closing = sibling.load("lib/closing.py")` written as `sibling.load("lib/" "closing.py")`, which loads the same module and drops the literal the case reads. Red, failing line `AssertionError: the closing readers are not imported`.
- `test_the_check_imports_the_one_definition_rather_than_restating_it`: `closing.KEYWORDS` written as `tuple(list(closing.KEYWORDS))`, an equal copy. Red at `assert check.KEYWORDS is closing.KEYWORDS`. A first try with `tuple(closing.KEYWORDS)` survived, because CPython hands back the same tuple object, so that mutant could not tell a copy from the import.

**The definitions search of `frame/design.md` *User scenarios* row 5.** Executed at `e9d4dc406`. It prints `lib/closing.py`'s eight definitions, `lib/blocks.py:97`, `lib/fields.py:70`, `lib/fields.py:99` and `skills/settle/scripts/passages.py:37`, which are the readers the design's *Scope* Out list keeps. The census of old spellings, `git grep -n -E 'close_issues_on_release\.py#|_closer\.|closer\.(KEYWORDS|CLOSING|HIDDEN|FENCE|SPAN|COMMENT|keywords_in|MERGED_PR)|SQUASH_SUBJECT|TRAILING_REF_RE' -- ':!seal/threads'`, prints one line, `tests/behaviour/test_a_declared_label_reaches_the_tracker.py:93`. That line cites the closer's `SPENT_ON_CLOSE`, which stays in the closer.

**For phase 3.** `docs/releasing/branch-and-release.md:168-171` and `tests/behaviour/test_a_cited_section_stands_in_its_file.py#RUN_BY_A_SHIPPED_COMMAND` still say that `pr_body.py` runs the closer. That is false from `e9d4dc406` on. A8 still passes, because it reads only the archive and the document, and the archive still holds the closer. *Rule changes* item 2 rewrites the document's sentence at the settle, and *Scope* item 10 removes A8 and its map.
