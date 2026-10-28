# Overview: 1793171931-checks-that-read-text-pass-what-they-cannot-read

## Why this work exists

Issue #956 asks which checks that read written text pass what they cannot read; this audit answers it per reader with a probe, so the fixes it files are each built on a measured direction.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| R2, a grammar table cut short | The frame quotes the tree: "a table it cannot read stops it at exit 2, never a pass" (`docs/the-review-record.md:63-86`). A blank line inside the old-spellings table loads the grammar with the row after it dropped | The probe | executed, `trail/phases/phase-1.md` R2 |
| R3, a finding in a closed fence | The frame quotes the tree: "a line the check cannot read is refused whatever the verdict" (`docs/the-review-record.md:104`). A whole finding at `verdict: open` inside a fence that closes is skipped, and `records()` names no problem | The probe | executed, `trail/phases/phase-1.md` R3 |
| R5, the unit's name | The frame names `seal_stamp.py#sealed_names`. That function composes a label and reads no verdict; the reader at the frame's coordinate `:1103-1104` is `#sealed_before` | The code: the row audits `#sealed_before` | read, `skills/verify/scripts/seal_stamp.py:703-727` and `:1083-1110` |
| R10, the question gate's direction | `hooks/question-gate.py`'s docstring says "Failure direction: it blocks more". An `Automation` row reading `Yes` lets the question through | The probe | executed, `trail/phases/phase-1.md` R10 |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck over this branch; no tree file outside this directory changed, and none was run | the orchestrator, through `seal gate` |
| R13's base-side relaxations (a legacy header, the old `none` line, U+2705) were read and not probed; they apply only to the base revision's side of `--baseline` | the proofer of this work item, by a probe of `--baseline` over a base holding each shape |

## Not done

No `changelog.md`: the audit changes no shipped file, so no release note would state anything; its result is the comment on #956 and the issues it files.

## Fed back into the spec

none
