# Phase 1: 1793588973-pr-body-reads-a-details-tag-as-github-does

## What this phase found

**The frame holds against the tree.** Judged against `frame/design.md` and `frame/plan.md` at `b3e74ca95`, read before the first edit. `CLOSER` is loaded once at import (`skills/code-review/scripts/pr_body.py:94-110`), `.github/scripts/close_issues_on_release.py#SPAN` stands at its line 123, `_composed` held the equality arm against `FOLD` and `FOLD_END`, and `tests/skills/test_pr_body.py#Test_compose::test_refuses_a_record_it_cannot_copy_faithfully` is parametrized over `(rel, text, line, said)`, as `frame/plan.md` *Technical context* states. Nothing in the frame was found wrong about the tree.

**The six new refused cases were seen red before the code changed.** With the cases added and `pr_body.py` as committed at `b3e74ca95`, one run of `bin/test tests/skills/test_pr_body.py -q -p no:xdist -k "copy_faithfully or code_span"` failed six cases, each with `DID NOT RAISE Refused`, and passed the other eight. The six are S1's four lines and S2's two. `b3e74ca95` holds the same `pr_body.py` as `627c47dd9`, the commit S1's cell names, because the frame's commit touched only this work item's records. S3's passing case was green against that code, as expected: the equality test refused no span.

**Each guard of the reading was removed alone, and its own case went red.** Each run is one `bin/seal mutate skills/code-review/scripts/pr_body.py --replace <old> <new> --tests "bin/test tests/skills/test_pr_body.py -q -p no:xdist -k <case>"` at `28a2c63cf`, and each printed `red: the cases failed against the mutation`. The tree was clean after each run.

| Guard removed | Replacement | Case that went red |
|---|---|---|
| the case-insensitive flag | `, re.IGNORECASE)` to `)` | `</DETAILS>` (S1) |
| the search anywhere in the line | `TAG.search(` to `TAG.match(` | `a sentence with </details> inside it` (S1), in its own run |
| the search anywhere in the line | `TAG.search(` to `TAG.match(` | the indented `  </details>` (S1), in its own run |
| the whitespace arm | `[\s/>]` to `[/>]` | `<details open>` (S1) |
| the `/` arm | `[\s/>]` to `[\s>]` | `a <details/> b` (S2) |
| the line-end arm | `(?=[\s/>]\|$)` to `(?=[\s/>])` | `a sentence <details` (S2) |
| the code-span blanking | `CLOSER.SPAN.sub(" ", seen[rel][line - 1])` to `seen[rel][line - 1]` | `test_accepts_a_details_tag_in_a_code_span` (S3) |

The test parameters above are the literal lines the cases copy. In this record they stand in code spans, so `seal pr-body` composes them.

**The pattern names the tag as read, beyond the design's lookahead.** `frame/design.md` *Data & interfaces* gives the constant as `</?details` with `re.IGNORECASE` and a lookahead for whitespace, `/`, `>` or the end of the string. The built constant, `TAG`, adds `[^>]*>?` after the lookahead. It matches whenever the lookahead does, so what is refused is the design's reading unchanged. The suffix lets the cause name the tag up to its `>`, such as `<details open>` rather than `<details`, which the design's "names the matched tag as read" asks for. The new parameters' `said` values hold the tag in backticks, so each case pins the name the sentence gives.

**The refusal sentence reads:** "holds `` `<tag>` ``, a `details` tag GitHub would read as a second fold or as the end of the copy's one `` `<details>` ``; write it in a code span". The two existing parameters keep their `said` values, `<details>` and `</details>`, and pass with it (S4).

**No other text states the equality test.** Judged against contract rule 19. `git grep -n -E` for `FOLD_END`, for "equal to" before a `details` tag and for "equal to" before `HEADING`, outside `seal/threads/`, found only `pr_body.py`'s own lines and two test docstrings about `HEADING` in `Test_split`, which state a different rule. `git grep -i` for `pr-body` beside `details` or `fold` under `docs`, `skills`, `agents`, `templates` and `CONTRIBUTING.md` found `docs/the-review-record.md:270`, *The guarantee*'s sentence, which the design keeps as written. This is a search on wordings, so the list is a sample.

**The new case joined its group.** S1's and S2's six cases are parameters of the existing refusal test. S3's passing case is a new test in `Test_compose`, because the refusal test asserts a refusal. `bin/seal layout --pairs tests` named no pair in `tests/skills/test_pr_body.py`.

**The phase-boundary command and checks exit 0.** The plan's one `bin/test` command over seven modules passed 591 cases. `bin/seal layout --check tests`, `uvx ruff check` and `uvx ruff format --check` on the two changed files each exited 0.
