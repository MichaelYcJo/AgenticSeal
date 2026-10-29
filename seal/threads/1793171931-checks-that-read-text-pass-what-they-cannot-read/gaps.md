# Overview: 1793171931-checks-that-read-text-pass-what-they-cannot-read

## Why this work exists

Issue #956 asks which checks that read written text pass what they cannot read; this audit answers it per reader with a probe, so the fixes it files are each built on a measured direction.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| R2, a grammar table cut short | The frame quotes the tree: "a table it cannot read stops it at exit 2, never a pass" (`docs/the-review-record.md:63-86`). A blank line inside the old-spellings table loads the grammar with the row after it dropped | The probe | executed, `trail/phases/phase-1.md` R2 |
| R3, a finding in a closed fence | The frame quotes the tree: "a line the check cannot read is refused whatever the verdict" (`docs/the-review-record.md:104`). A whole finding at `verdict: open` inside a fence that closes is skipped, and `records()` names no problem | The probe | executed, `trail/phases/phase-1.md` R3 |
| R5, the unit's name | The frame names `seal_stamp.py#sealed_names`. That function composes a label and reads no verdict; the reader at the frame's coordinate `:1103-1104` is `#sealed_before` | The code: the row audits `#sealed_before` | read, `skills/verify/scripts/seal_stamp.py:703-727` and `:1083-1110` |
| R16, a config row under an unclosed comment | The frame quotes `docs/the-record-layout.md:158-162`: "a row below a comment opener nobody closed still declares". `config_table` refuses that table, since GFM renders none inside an HTML block nobody closed | The code; the policy sentence goes to the documents' issue | executed, `trail/phases/phase-2.md` R16 |
| R24, read at the release base | The plan lets phase 4 alone read `origin/release/v0.24.0`, for R36. #913 merged there as `7da1a77e` during the audit and replaced the inline anchor R24 probed with an anchor table | R24 was probed at `5287dd42` to decide its filing; its near misses still pass there, and it is filed as #1132 | executed, `trail/phases/phase-5.md` *R24 at the release base* |
| R10, the question gate's direction | `hooks/question-gate.py`'s docstring says "Failure direction: it blocks more". An `Automation` row reading `Yes` lets the question through | The probe | executed, `trail/phases/phase-1.md` R10 |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck over this branch; no tree file outside this directory changed, and none was run | executed by the orchestrator's broad gate at `441bb9fd` against `5287dd42`, passed (`trail/gate.md`), and this repository declares no typecheck (`seal/config.md` *Broad gate*; #951 would add one) |
| closed R40: how `claude plugin eval` reads a `not_contains` grader whose target file is absent; the harness's reader is not in this tree and no eval was run | re-homed to #1038, whose candidate 3 reads #956's audit row by row; the audit's *Fix* cell for R40 names #1038, and the row is listed in its comment of 2026-10-29 |
| closed R28: whether GitHub itself creates a closing reference from `Closes #18` inside an HTML comment, which all four of this repository's readers read as a claim | re-homed to #1181 |
| closed R37: 131 of the 305 negative asserts matched neither of the probe's word lists, so the count reading a tracked file is between 123 and 264 | re-homed to #1038, whose candidate 3 reads #956's audit row by row; the audit's *Fix* cell for R37 names #1038, and the row is listed in its comment of 2026-10-29 |
| closed R13's base-side relaxations (a legacy header, the old `none` line, U+2705) were read and not probed; they apply only to the base revision's side of `--baseline` | executed by the settle session, 2026-10-29: `check_text` with `strict_header=False` read the row of a table whose legacy header names its second column `Who` as open, the old `none — <why>` line as no rows and a U+2705 row as closed, and with `strict_header=True` refused each, as its docstring says (`skills/verify/scripts/unverified_check.py:860`) |

## Not done

No `changelog.md`: the audit changes no shipped file, so no release note would state anything; its result is the comment on #956 and the issues it files.

## Fed back into the spec

none
