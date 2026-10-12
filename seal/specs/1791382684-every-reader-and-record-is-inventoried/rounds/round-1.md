# 1791382684-every-reader-and-record-is-inventoried — review round 1

| Field | Value |
|---|---|
| Target SHA | 8938af5baa786798b60c8bc05db59856433b9926 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #901 |
| Broad gate | not yet |
| Fixes checked by | round-2 |
| Fix range | `a6b0ac200865f1b12662c2a6b5f1f448338d529c..bf1e425a01f0a5f2f5a2afe2378fcf13357c1e14`, 1 commit |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (32 `Reads:` lines or paragraphs that describe another unit), 🟡 2 (five class words and two direction words the code contradicts), 🟡 3 (three wrong line references) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 1 of #834's build (phases 1–3 of `plan.md`; phase 4, `hooks/worktree-guard.py`, not yet built), target 8938af5b against `origin/release/v0.21.0` at dae101ab; the build is `7608d82c..8938af5b`. The reviewer was asked to judge the frame's three recorded divergences, and above all to sample the 189 transcribed `Reads:` lines against the code they describe, class and unknown-input direction, and to say how often a transcribed line is wrong.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | 32 `Reads:` lines or their paragraphs describe a sibling unit's input, mostly a helper given its row's lead description; four carry the inventory's own shorthand | `hooks/commitgate.py:144` | **fixed** `bf1e425a` | fixed at bf1e425a — the 32 units the report lists, each read against its own code before its line or paragraph was replaced; the four shorthand words went with them; `overview.md` carries the divergence row for spec acceptance row 4; the eleven places `survivor-check` names over the fix range are lead units whose lines still describe them and the inventory's own rows, recorded in `survivors.md`; read all 189 units against their code; 97 of 180 matched lines came from multi-unit rows, 65 as a non-lead unit (probe) |
| 🟡 2 | five class words and two direction words the unit's code contradicts, one an identical body declared two ways | `skills/evidence-check/scripts/correction_check.py:746` | **fixed** `bf1e425a` | fixed at bf1e425a — both `parse_range` bodies now declare `observed … mixed` in one line and paragraph; `tree_at`, `lease_dirs` and `other_ci_files` declare `observed`, `agents_in` `guess`; `tree_at`'s direction is `passed`, and `short_commit`'s, in finding 1, `passed`; `survivor_check.py:458` is the same body declared `observed … mixed`; `tree_at`, `lease_dirs`, `other_ci_files`, `agents_in` read in code |
| 🟡 3 | three new paragraphs cite line numbers that were wrong at the commit that wrote them | `hooks/cmdline.py:339` | **fixed** `bf1e425a` | fixed at bf1e425a — `drop_heredoc_bodies` and `heredoc_bodies` name `_heredoc_split`'s comment on an unbalanced `${` instead of its line numbers, and `origin` names `check` as the unit that refuses an empty name; the cited comment is at 457 (was 443), the cited refusal at 541 (was 518); found by a search of every added line, three hits |
| ⬜ 4 | one shape (does a marker this plugin wrote exist) is declared `owned` twice and `observed` twice | `hooks/commit-review-gate.py:686` | answered | corrected at `bf1e425a`: the registry's table decides it. `owned` is a format this repository's writer produces or a vocabulary its checker defines, and a presence test reads no format; `observed` is a fact asked of the system, and K1 lists existence tests in its process-boundary family. All four now declare `observed`; `overview.md` records it; the registry's class table does not settle it; the registry's owner answers |
| ⬜ 5 | Q4 still ⬜ though phase 2 applied its answer | `seal/specs/1791382684-every-reader-and-record-is-inventoried/questions.md` | answered | corrected at `bf1e425a`: `questions.md` Q4 closed ✅ with phase 2's answer; correction to the run's paperwork |
| ⬜ 6 | the plan's mapping rule gives a helper its lead's line, and phase 4 reruns it | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md` | answered | corrected at `bf1e425a`: `plan.md` §*Technical context*'s `Unit → units` bullet now gives the row's prose only to the unit whose body does the reading, reads every other named unit on its own code, and leaves on the census one that cannot be read so; phase 4 and any later rerun apply it; correction to the run's paperwork; it is what keeps 🟡 1 from recurring on the guard |
| ⬜ 7 | the plan's approval line misses the form the chain check reads, so it reports the line absent | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md` | answered | corrected at `bf1e425a`: `plan.md`'s approval line now ends with the words when smith was spawned, in the form `APPROVED_RE` matches (checked against the regex); the Q1 (c) answer is a sentence of its own under it; correction to the run's paperwork; the notice printed when the generator ran in the scratch clone |
| 🟢 | the build changes no reader's behaviour | the 44 changed `.py` files | confirmed | syntax trees equal at both ends with docstrings removed (probe) |
| 🟢 | the census lost exactly the written units' 189 lines | `tests/undeclared_readers.txt` | confirmed | numstat 0 added, 189 removed; registry test green |

## Paste-ready fixes

```
hooks/answer-clear.py:15  (one-line docstring)
    """Reads: observed — payload `tool_name`, `tool_input.command`, `tool_use_id`, `session_id`; unknown passed"""

hooks/cmdline.py:2183  _expands, the paragraph
    Refused: a first word holding an `EXPANDS` character counts as expanding, so the commit gate stops.

hooks/cmdline.py:2559  _dedup, the line and the two-line paragraph under it
    Reads: guess — the (directory, previous) states the walk built from the segments; unknown refused

    Refused: an `Unresolved` state is kept apart from a readable one that spells the same path.

hooks/cmdline.py:2579  _directories, the line and the two-line paragraph under it
    Reads: guess — the (directory, previous) states the walk built from the segments; unknown refused

    Refused: an `Unresolved` directory is kept apart from a readable one that spells the same path.

hooks/cmdline.py:2653  _step
    Reads: guess — a `cd` operand and the directory the shell stood in; unknown refused

hooks/commitgate.py:95  pressed
    Reads: guess — the transcript's routing answer, through `automation_answered`; unknown refused

hooks/commitgate.py:144  _process — and delete the two-line `What it reads, continued:` paragraph
    Reads: observed — `ps -o ppid=,comm=` of one process; unknown refused

hooks/dispatch.py:453  flat, the `Passed:` paragraph
    Passed: a value that is not a string gives "".

hooks/evidence-advisor.py:88  commits_in
    Reads: guess — the command split on `&&`, `||`, `;`, `|` and newlines, quotes ignored; unknown passed

hooks/sealer-stamp.py:97  load_stamp — and replace the two-line `What it reads, continued:` paragraph
    Reads: owned — `seal_stamp.py` beside this hook, loaded by path; unknown passed

    Passed: any exception, `SystemExit` included, gives None, so nothing is drawn.

hooks/tokens.py:160  _empties_the_environment, the `Refused:` paragraph
    Refused: `-i` anywhere in a short option cluster counts as emptying the environment.

hooks/version-check.py:91  due
    Reads: observed — the marker's mtime; unknown passed

hooks/worktree_consent.py:146  granted, the `What it reads, continued:` paragraph
    What it reads, continued: the path `consent_path` builds under the common git directory.

hooks/worktree_consent.py:269  _content — and delete the two-line `What it reads, continued:` paragraph
    Reads: guess — one transcript entry's `message.content` list; unknown refused

    Refused: an entry whose message holds no content list gives [].

hooks/worktree_consent.py:284  _clone_of — and delete the two-line `What it reads, continued:` paragraph
    Reads: guess — a transcript entry's `cwd`, resolved by git to its clone's common dir; unknown refused

    Refused: a `cwd` that is not a string, or sits in no clone, gives "".

skills/code-review/scripts/chain_check.py:1634  is_ancestor: delete the `What it reads, continued:` paragraph

skills/code-review/scripts/chain_check.py:1705  carried_by_a_pull_head — and delete the `What it reads, continued:` paragraph
    Reads: observed — `for-each-ref --contains <sha> refs/remotes/pull/`, exit and first line; unknown refused

skills/code-review/scripts/chain_check.py:2603  nobody_reason
    Reads: owned — one `Fixes checked by` cell: `nobody`, then a separator or nothing; unknown refused

skills/code-review/scripts/chain_check.py:4946  range_ends
    Reads: owned — the `Fix range` cell through `FIX_RANGE_RE`, both ends resolved; unknown passed

skills/code-review/scripts/round_record.py:3616  under_tests  (one-line docstring)
    """Reads: guess — a path's directories, for one named `tests`; unknown passed"""

skills/evidence-check/scripts/evidence_check.py:3438  calendar_date, the line and its `Passed:` paragraph
    Reads: owned — a `CHECKED_RE` match, asked of `datetime.date.fromisoformat`; unknown passed

    Passed: False, and the caller sorts that reading as "", oldest.

skills/evidence-check/scripts/evidence_check.py:5790  github_slug, the line and its `Passed:` paragraph
    Reads: guess — one heading's text from a `.md` file; unknown passed

    Passed: every character outside the kept set is dropped, never refused.

skills/evidence-check/scripts/pact_check.py:267  git
    Reads: observed — git's stdout and exit code; unknown passed

skills/evidence-check/scripts/pact_check.py:287  read
    Reads: observed — a file's text, decoded as strict UTF-8; unknown passed

skills/implement/scripts/seal.py:670  no_root  (one-line docstring)
    """Reads: observed — whether `optin.SCRATCH` is a file under `optin.git_common_dir`; unknown refused"""

skills/implement/scripts/seal.py:1809  plugin_workflow
    Reads: observed — `templates/hygiene.yml` and its `PLACEHOLDER`, with `plugin_version`; unknown refused

skills/verify/scripts/broad_gate.py:700  short_commit — and delete the `What it reads, continued:` paragraph
    Reads: observed — `rev-parse --short <rev>^{commit}`; unknown passed

    Passed: a failed git and a rev naming no commit both give None, and `resolve_base` tries its next step.

skills/verify/scripts/broad_gate.py:2410  unquote
    Reads: guess — one YAML scalar from a `hygiene.yml` step's `- name:` line; unknown passed

skills/verify/scripts/unverified_check.py:235  visible
    Reads: owned — a cell's text, with the `INVISIBLE` characters taken off; unknown refused

skills/verify/scripts/unverified_check.py:882  sections
    Reads: owned — a file's headings: the exact `## Not verified` first, else the matcher given; unknown refused

tests/conftest.py:105  _indent  (one-line docstring)
    """Reads: guess — one workflow line's leading spaces, by which `workflow_steps` splits steps; unknown passed"""

tests/conftest.py:113  _unquote
    Reads: guess — a step's `name:` scalar, its matching quotes taken off; unknown passed

overview.md, a row in "Where spec and implementation diverged":
| `Reads:` prose of 32 units named beside a reader in one row | `spec.md` acceptance row 4: the line carries the row's `What it reads` | each line says what its own unit reads; class and direction kept, `short_commit`'s direction `passed` | `docs/the-reader-registry.md`: the prose is what the unit reads, and a false one is limit 1; round 1 🟡 1 |

Verify: bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_a_rider_reaches_its_file.py
        bin/evidence-check .   (no unit above is cited; it should stay exit 0)
```
```
skills/evidence-check/scripts/correction_check.py:746  parse_range, the line, and a paragraph under it
    Reads: observed — `A..B` / `A...B` from the CLI, each end resolved by git; unknown mixed

    Mixed: no separator, or an end that does not resolve, is refused; a failing `merge-base` keeps the
    left end for `...`.

skills/verify/scripts/unverified_check.py:1401  tree_at, the line, and a paragraph under it
    Reads: observed — `os.walk` of the disk, or `git ls-tree -r --name-only <ref>` without `-z`; unknown passed

    Passed: a failed `ls-tree` gives [], the same answer as an empty directory.

hooks/hooksession.py:150  lease_dirs, the line; replace the `What it reads, continued:` paragraph
    Reads: observed — the `specseal-leases` directories under the common dir and `worktrees/*/`; unknown passed

    Passed: a `worktrees` directory that will not list reads as none.

skills/verify/scripts/deferral_check.py:156  other_ci_files
    Reads: observed — whether six fixed CI paths are files, and `.buildkite/*.yml`; unknown passed

skills/verify/scripts/payload_meter.py:375  agents_in  (one-line docstring)
    """Reads: guess — `agents/*.md`, each `name` through `frontmatter`, else the filename; unknown passed"""

Verify: the same two commands as 🟡 1, and `grep -rn "Reads: guess" skills/verify/scripts/deferral_check.py`
names `other_ci_files` no more.
```
```
hooks/cmdline.py:339-340  drop_heredoc_bodies, and hooks/cmdline.py:387-388  heredoc_bodies — the `Mixed:` paragraph in each
    Mixed: an unterminated body runs to the end of the input; an unbalanced `${` hides a
    `((` region (fails open, as `_heredoc_split`'s comment on an unbalanced `${` says)

skills/evidence-check/scripts/pact_check.py:303  origin, the `Passed:` paragraph
    Passed: "" gives no name, which `main` then refuses.
```

## Executed probes

| What was run | Result |
|---|---|
| clone at 8938af5b; list every unit whose docstring gained a `Reads:` line between 7608d82c and HEAD, with its source | 189 units, 4,268 lines of source, all read |
| match each line to its inventory row by unit name and prose | 180 matched: 83 from single-unit rows, 97 from multi-unit rows (32 as the lead, 65 not); 9 unmatched |
| each changed `.py` file's syntax tree with docstrings removed, 7608d82c against HEAD | 44 files, 0 differ |
| `wc -l` and `git diff --numstat` on `tests/undeclared_readers.txt` | 1,395 lines; 0 added, 189 removed |
| `bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_a_rider_reaches_its_file.py` | 126 passed |
| search of every added `.py` line for a line-number shape | 3 hits, all wrong (🟡 3) |
| search of every added `.py` line for the inventory's shorthand | `same` ×2, `wc`, `outside this part` (🟡 1) |
| `round_record.py new` on this report, in the scratch clone only, to see that the tables parse | wrote the clone's `round-1.md` with seven verdict rows and both lines; exit 1 from the chain check over the clone, whose other work items' targets it cannot reach, and the ⬜ 7 notice |
| the broad gate: full suite, lint, typecheck | not yet — the sealer's, after the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
